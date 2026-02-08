# CreateUseCase Workflow (Codex)

1. Create a task YAML in `~/.codex/skills/evals/UseCases/<Capability|Regression>/`.

2. Required fields:
- `id`
- `description`
- `type` (`capability` or `regression`)
- `domain`
- `graders`

3. Prefer code-based graders first (`binary_tests`, `static_analysis`, `tool_calls`, `state_check`).

4. Add the new task to a suite:
```bash
bun run ~/.codex/skills/evals/Tools/SuiteManager.ts add-task <suite-name> <task-id>
```

5. Validate by running one suite execution with `Tools/CodexBridge.ts`.
