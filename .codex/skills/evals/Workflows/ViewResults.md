# ViewResults Workflow (Codex)

1. Open run artifact:
- `~/.codex/skills/evals/Results/<suite-name>/<run-id>/run.json`

2. Review in this order:
- overall pass rate / score
- per-trial pass/fail
- grader-level failures
- transcript and tool-call evidence

3. Decision:
- Keep as capability suite if still exploratory
- Graduate to regression if consistently high and stable
