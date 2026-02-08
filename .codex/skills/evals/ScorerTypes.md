# Scorer Types

## Code-based

- `string_match`: exact substring checks
- `regex_match`: pattern checks
- `binary_tests`: run tests
- `static_analysis`: run linters/type/security checks
- `state_check`: verify files/env/final state
- `tool_calls`: verify required/forbidden/sequence

Use for deterministic gating and fast iteration.

## Model-based

- `llm_rubric`: rubric-scored judgment
- `natural_language_assert`: assertion truth checks
- `pairwise_comparison`: output-vs-reference comparison

Use when deterministic checks cannot capture nuanced quality.
Requires `OPENAI_API_KEY`.

## Recommended Mix

- Regression suites: 70-90% code-based, 10-30% model-based
- Capability suites: 50-80% code-based, 20-50% model-based
