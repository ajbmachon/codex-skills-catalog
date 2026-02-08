/**
 * Binary Tests Grader
 * Run actual test files and check pass/fail
 */

import { BaseGrader, registerGrader, type GraderContext } from '../Base.ts';
import type { GraderConfig, GraderResult, BinaryTestsParams } from '../../Types/index.ts';

interface CommandResult {
  exitCode: number;
  stdout: string;
  stderr: string;
  timedOut: boolean;
}

export class BinaryTestsGrader extends BaseGrader {
  type = 'binary_tests' as const;
  category = 'code_based' as const;

  async grade(context: GraderContext): Promise<GraderResult> {
    const start = performance.now();
    const params = this.config.params as BinaryTestsParams;

    if (!params?.test_files?.length) {
      return this.createResult(0, false, performance.now() - start, {
        reasoning: 'No test files configured',
      });
    }

    const workingDir = context.working_dir ?? process.cwd();
    const timeout = params.timeout_ms ?? 60000;
    const results: { file: string; passed: boolean; output: string; error?: string }[] = [];

    for (const testFile of params.test_files) {
      try {
        const command = params.test_command
          ? `${params.test_command} ${this.shellEscape(testFile)}`
          : this.detectTestCommand(testFile);

        const result = await this.runShellCommand(command, workingDir, timeout);
        const passed = result.exitCode === 0 && !result.timedOut;
        results.push({
          file: testFile,
          passed,
          output: result.stdout.slice(-500),
          error: passed
            ? undefined
            : result.timedOut
              ? `Timed out after ${timeout}ms`
              : result.stderr.slice(-500),
        });
      } catch (e) {
        results.push({
          file: testFile,
          passed: false,
          output: '',
          error: String(e),
        });
      }
    }

    const passCount = results.filter(r => r.passed).length;
    const score = passCount / params.test_files.length;
    const passed = passCount === params.test_files.length;

    return this.createResult(score, passed, performance.now() - start, {
      reasoning: `${passCount}/${params.test_files.length} tests passed`,
      details: {
        results,
        working_dir: workingDir,
      },
    });
  }

  private detectTestCommand(file: string): string {
    const testPath = this.shellEscape(file);
    if (file.endsWith('.py')) return `python -m pytest ${testPath}`;
    if (file.endsWith('.ts')) return `bun test ${testPath}`;
    if (file.endsWith('.js')) return `node --test ${testPath}`;
    if (file.endsWith('.go')) return `go test ${testPath}`;
    if (file.endsWith('.rs')) return `cargo test -- ${testPath}`;
    return `bun test ${testPath}`;
  }

  private shellEscape(value: string): string {
    return `'${value.replace(/'/g, `'\\''`)}'`;
  }

  private async runShellCommand(command: string, cwd: string, timeoutMs: number): Promise<CommandResult> {
    const proc = Bun.spawn({
      cmd: ['sh', '-lc', command],
      cwd,
      stdout: 'pipe',
      stderr: 'pipe',
    });

    let timedOut = false;
    const timeoutId = setTimeout(() => {
      timedOut = true;
      proc.kill();
    }, timeoutMs);

    try {
      const [exitCode, stdout, stderr] = await Promise.all([
        proc.exited,
        new Response(proc.stdout).text(),
        new Response(proc.stderr).text(),
      ]);
      return { exitCode, stdout, stderr, timedOut };
    } finally {
      clearTimeout(timeoutId);
    }
  }
}

registerGrader('binary_tests', BinaryTestsGrader);
