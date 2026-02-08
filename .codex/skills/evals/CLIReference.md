# Evals CLI Reference (Codex)

## Skill Root

`~/.codex/skills/evals`

## Suite Management

```bash
bun run ~/.codex/skills/evals/Tools/SuiteManager.ts create <name> -t capability -d "description"
bun run ~/.codex/skills/evals/Tools/SuiteManager.ts list
bun run ~/.codex/skills/evals/Tools/SuiteManager.ts show <name>
bun run ~/.codex/skills/evals/Tools/SuiteManager.ts add-task <suite> <task-id>
bun run ~/.codex/skills/evals/Tools/SuiteManager.ts check-saturation <name>
bun run ~/.codex/skills/evals/Tools/SuiteManager.ts graduate <name>
```

## Failure To Task

```bash
bun run ~/.codex/skills/evals/Tools/FailureToTask.ts log "description" -c <category> -s <severity>
bun run ~/.codex/skills/evals/Tools/FailureToTask.ts list
bun run ~/.codex/skills/evals/Tools/FailureToTask.ts convert-all --suite <suite-name>
```

## Run Suites

```bash
bun run ~/.codex/skills/evals/Tools/CodexBridge.ts -s <suite-name>

bun run ~/.codex/skills/evals/Tools/CodexBridge.ts \
  -s <suite-name> \
  -n 3 \
  --output-file <path/to/output.txt> \
  --transcript-file <path/to/transcript.jsonl> \
  --json
```

## Results

Runs are saved to:

`~/.codex/skills/evals/Results/<suite-name>/<run-id>/run.json`
