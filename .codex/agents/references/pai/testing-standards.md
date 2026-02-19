# Testing Standards (Normalized)

## Principles
- Test behavior and contracts, not incidental implementation details.
- Prioritize high-impact paths: correctness, failures, and regressions.
- Prefer integration-realistic validation for user-facing behavior.

## Test Priorities
1. Contract and interface expectations
2. Critical workflows
3. Error handling and edge cases
4. Regression guards for previously broken behavior

## Review Expectations
- If tests are missing for critical behavior, treat as a blocking gap.
- Distinguish must-fix test gaps from optional improvements.
