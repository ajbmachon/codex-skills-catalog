# RunEval Workflow (Codex)

1. Confirm suite exists:
```bash
bun run ~/.codex/skills/evals/Tools/SuiteManager.ts show <suite-name>
```

2. Run suite:
```bash
bun run ~/.codex/skills/evals/Tools/CodexBridge.ts \
  -s <suite-name> \
  --output-file <path/to/output.txt> \
  --transcript-file <path/to/transcript.jsonl> \
  --json
```

3. Inspect run artifacts:
- `~/.codex/skills/evals/Results/<suite-name>/<run-id>/run.json`

4. Report:
- pass/fail
- score/pass rate
- failed graders and why
- proposed task/grader changes
