---
name: <skill-name>
description: <what this skill does and when to use it>
---

# <Skill Title>

## Prereqs

- Required tools/runtime:
- Optional capabilities and fallback behavior:

## Deterministic Workflow

1. Route request to mode/task.
2. Gather required context.
3. Execute one bounded step.
4. Validate state/output.
5. Continue or terminate based on explicit exit criteria.

## Failure Recovery

- Failure mode 1:
  - Signal:
  - Recovery:
- Failure mode 2:
  - Signal:
  - Recovery:

## Output Contract

- Human-readable output fields:
- Optional machine-readable block (when requested):

```json
{
  "mode": "",
  "status": "",
  "results": []
}
```

## Validation

- Command 1:
- Command 2:

## References

- `references/...` (load condition)
- `scripts/...` (run condition)
