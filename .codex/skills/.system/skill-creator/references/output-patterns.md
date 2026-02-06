# Output Patterns

Use explicit output contracts to improve reliability.

## Human-readable contract
- Summary
- Key findings/steps
- Next actions

## Structured contract (optional)
Provide a machine-readable block when requested, for example:

```json
{
  "mode": "example",
  "status": "ok",
  "actions": ["..."],
  "risks": ["..."]
}
```

## Quality footer
Add a short quality footer with:
- Confidence
- Coverage
- Assumptions
