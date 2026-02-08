#!/usr/bin/env bun
/**
 * Codex Bridge
 * Run suites in this skill without Claude-specific dependencies.
 */

import type { EvalRun, Task } from '../Types/index.ts';
import { loadSuite, checkSaturation } from './SuiteManager.ts';
import { TrialRunner } from './TrialRunner.ts';
import { createTranscript, parseClaudeCodeTranscript } from './TranscriptCapture.ts';
import { existsSync, mkdirSync, writeFileSync, readFileSync } from 'fs';
import { join } from 'path';
import { parse as parseYaml } from 'yaml';
import { parseArgs } from 'util';

const EVALS_DIR = join(import.meta.dir, '..');
const RESULTS_DIR = join(EVALS_DIR, 'Results');

interface CodexRunRequest {
  suite: string;
  trials?: number;
  outputFile?: string;
  transcriptFile?: string;
}

interface CodexRunResult {
  suite: string;
  passed: boolean;
  score: number;
  summary: string;
  run_ids: string[];
}

function findTaskFile(taskId: string): string | null {
  const useCasesDir = join(EVALS_DIR, 'UseCases');
  const possiblePaths = [
    join(useCasesDir, `${taskId}.yaml`),
    join(useCasesDir, 'Regression', `${taskId}.yaml`),
    join(useCasesDir, 'Capability', `${taskId}.yaml`),
  ];

  for (const path of possiblePaths) {
    if (existsSync(path)) return path;
  }

  return null;
}

function saveRunResults(suiteName: string, run: EvalRun): void {
  const suiteResultsDir = join(RESULTS_DIR, suiteName);
  if (!existsSync(suiteResultsDir)) mkdirSync(suiteResultsDir, { recursive: true });

  const runDir = join(suiteResultsDir, run.id);
  if (!existsSync(runDir)) mkdirSync(runDir);

  writeFileSync(join(runDir, 'run.json'), JSON.stringify(run, null, 2));
}

function loadSharedOutput(outputFile?: string): string {
  if (!outputFile) return 'No output file provided to CodexBridge.';
  if (!existsSync(outputFile)) return `Output file not found: ${outputFile}`;
  return readFileSync(outputFile, 'utf-8');
}

function loadSharedTranscript(taskId: string, trialId: string, transcriptFile?: string) {
  if (!transcriptFile) {
    return createTranscript(taskId, trialId, {
      turns: [
        { role: 'system', content: 'No transcript file provided.' },
        { role: 'assistant', content: 'CodexBridge executed with synthetic transcript.' },
      ],
      toolCalls: [],
    });
  }

  if (!existsSync(transcriptFile)) {
    return createTranscript(taskId, trialId, {
      turns: [
        { role: 'system', content: `Transcript file not found: ${transcriptFile}` },
        { role: 'assistant', content: 'CodexBridge executed with synthetic transcript.' },
      ],
      toolCalls: [],
    });
  }

  const content = readFileSync(transcriptFile, 'utf-8');
  const trimmed = content.trim();

  if (trimmed.startsWith('{')) {
    try {
      return JSON.parse(trimmed);
    } catch {
      // Fall through to JSONL parsing.
    }
  }

  return parseClaudeCodeTranscript(content, taskId, trialId);
}

export async function runSuiteForCodex(request: CodexRunRequest): Promise<CodexRunResult> {
  const suite = loadSuite(request.suite);
  if (!suite) {
    return {
      suite: request.suite,
      passed: false,
      score: 0,
      summary: `Suite not found: ${request.suite}`,
      run_ids: [],
    };
  }

  const tasks: Task[] = [];
  for (const taskId of suite.tasks) {
    const taskPath = findTaskFile(taskId);
    if (taskPath && existsSync(taskPath)) {
      const task = parseYaml(readFileSync(taskPath, 'utf-8')) as Task;
      tasks.push(task);
    }
  }

  if (tasks.length === 0) {
    return {
      suite: request.suite,
      passed: false,
      score: 0,
      summary: `No tasks found in suite: ${request.suite}`,
      run_ids: [],
    };
  }

  const sharedOutput = loadSharedOutput(request.outputFile);
  const runIds: string[] = [];
  let totalScore = 0;
  let passedTasks = 0;

  for (const baseTask of tasks) {
    const task: Task = {
      ...baseTask,
      trials: request.trials ?? baseTask.trials ?? 1,
    };

    const runner = new TrialRunner({
      task,
      executor: async (_task, trialNum) => {
        const trialId = `trial_${trialNum}`;
        const transcript = loadSharedTranscript(task.id, trialId, request.transcriptFile);
        return {
          output: sharedOutput,
          transcript,
        };
      },
    });

    const run = await runner.run();
    saveRunResults(request.suite, run);
    runIds.push(run.id);
    totalScore += run.mean_score;

    if (run.pass_rate >= (task.pass_threshold ?? 0.75)) {
      passedTasks += 1;
    }
  }

  const score = totalScore / tasks.length;
  const passed = passedTasks === tasks.length || score >= (suite.pass_threshold ?? 0.75);

  return {
    suite: request.suite,
    passed,
    score,
    summary: `${passedTasks}/${tasks.length} tasks passed, score: ${(score * 100).toFixed(1)}%`,
    run_ids: runIds,
  };
}

if (import.meta.main) {
  const { values } = parseArgs({
    args: Bun.argv.slice(2),
    options: {
      suite: { type: 'string', short: 's' },
      trials: { type: 'string', short: 'n' },
      'output-file': { type: 'string' },
      'transcript-file': { type: 'string' },
      'show-saturation': { type: 'boolean' },
      json: { type: 'boolean' },
      help: { type: 'boolean', short: 'h' },
    },
    allowPositionals: true,
  });

  if (values.help || !values.suite) {
    console.log(`
CodexBridge - Run eval suites in Codex environments

Usage:
  bun run Tools/CodexBridge.ts -s <suite> [options]

Options:
  -s, --suite              Eval suite to run
  -n, --trials             Override trials per task
  --output-file            Text file used as grader output
  --transcript-file        Transcript file (.json or JSONL) used by tool-call graders
  --show-saturation        Print saturation status for the suite
  --json                   Print machine-readable JSON result
  -h, --help               Show this help
`);
    process.exit(0);
  }

  if (values['show-saturation']) {
    const status = checkSaturation(values.suite!);
    console.log(JSON.stringify(status, null, 2));
    process.exit(0);
  }

  const result = await runSuiteForCodex({
    suite: values.suite!,
    trials: values.trials ? parseInt(values.trials, 10) : undefined,
    outputFile: values['output-file'],
    transcriptFile: values['transcript-file'],
  });

  if (values.json) {
    console.log(JSON.stringify(result, null, 2));
  } else {
    console.log(`Suite: ${result.suite}`);
    console.log(`Passed: ${result.passed ? 'yes' : 'no'}`);
    console.log(`Score: ${(result.score * 100).toFixed(1)}%`);
    console.log(`Summary: ${result.summary}`);
    console.log(`Run IDs: ${result.run_ids.join(', ') || 'none'}`);
  }

  process.exit(result.passed ? 0 : 1);
}
