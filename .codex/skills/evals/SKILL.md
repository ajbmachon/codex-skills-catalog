---
name: evals
description: Build and run agent evaluations for coding/research/chat workflows. Use when user asks to evaluate quality, run regressions, benchmark prompts/models, compare outputs, or convert failures into repeatable tasks.
---

# Evals

Run structured evals for GPT-5 Codex workflows using local suites, task YAML, and grader pipelines.

## Prereqs

- Bun installed (`bun --version`)
- Optional for model-based graders: `OPENAI_API_KEY`
- Skill root: `~/.codex/skills/evals`

## When To Use

- "run evals", "benchmark this agent", "regression test this workflow"
- "compare prompt versions" or "compare model outputs"
- "turn these failures into tests"
- "check whether quality regressed after a code change"

## Deterministic Workflow

1. Select eval mode
- Existing suite run: use `Tools/CodexBridge.ts`
- New suite/task authoring: use `Tools/SuiteManager.ts` + `UseCases/`
- Failure-driven test generation: use `Tools/FailureToTask.ts`

2. Prepare inputs
- Ensure suite exists under `Suites/Capability` or `Suites/Regression`
- Ensure suite task IDs map to YAML files under `UseCases/`
- If scoring real trajectories, provide transcript JSON or JSONL via `--transcript-file`
- If scoring final text output, provide it via `--output-file`

3. Execute
```bash
# Run suite and print JSON
bun run ~/.codex/skills/evals/Tools/CodexBridge.ts \
  -s <suite-name> \
  --output-file <path/to/output.txt> \
  --transcript-file <path/to/transcript.jsonl> \
  --json
```

4. Inspect results
- Per-run artifacts are written to `~/.codex/skills/evals/Results/<suite>/<run_id>/run.json`
- Check pass rate, failed graders, and trial-level details

5. Tighten and repeat
- Add/adjust graders in task YAML
- Re-run same suite to track deltas over time

## Core Commands

```bash
# Suite management
bun run ~/.codex/skills/evals/Tools/SuiteManager.ts create <name> -t capability -d "description"
bun run ~/.codex/skills/evals/Tools/SuiteManager.ts list
bun run ~/.codex/skills/evals/Tools/SuiteManager.ts show <name>
bun run ~/.codex/skills/evals/Tools/SuiteManager.ts check-saturation <name>

# Convert real failures to regression tasks
bun run ~/.codex/skills/evals/Tools/FailureToTask.ts log "description" -c <category> -s <severity>
bun run ~/.codex/skills/evals/Tools/FailureToTask.ts convert-all --suite <suite-name>

# Execute suite
bun run ~/.codex/skills/evals/Tools/CodexBridge.ts -s <suite-name>
```

## Grader Strategy

- Start with code-based graders (`binary_tests`, `static_analysis`, `tool_calls`, `state_check`)
- Add model-based graders (`llm_rubric`, `natural_language_assert`, `pairwise_comparison`) only when deterministic checks are insufficient
- Use `required: true` for hard gates
- Keep grading weights simple and explicit

## Failure Recovery

- Missing suite: create/list with `SuiteManager.ts`
- Missing tasks in suite: verify IDs exist in `UseCases/`
- Model-based grader fails: confirm `OPENAI_API_KEY`, or temporarily rely on code-based graders
- Inconsistent scores: run multiple trials (`-n`) and inspect transcripts/tool calls

## Output Contract

When this skill is invoked for an eval task, return:

1. Eval setup summary
- Suite name
- Task count
- Graders used
- Inputs used (`output-file`, `transcript-file`, trials)

2. Result summary
- Overall pass/fail
- Score/pass rate
- Top failing grader categories

3. Actionable next steps
- Exact task/grader edits to improve signal quality
- Whether to keep as capability suite or graduate to regression

## Validation Commands

Run before relying on new changes to the skill code:

```bash
bun run ~/.codex/skills/evals/Tools/SuiteManager.ts -h
bun run ~/.codex/skills/evals/Tools/FailureToTask.ts -h
bun run ~/.codex/skills/evals/Tools/CodexBridge.ts -h
```

## References

- Type definitions: `Types/index.ts`
- Domain defaults: `Data/DomainPatterns.yaml`
- Example regression tasks: `UseCases/Regression/`
