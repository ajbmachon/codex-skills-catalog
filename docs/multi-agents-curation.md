# Multi-Agents Curation Rationale

## Goal
Create a high-leverage first pack for software delivery with minimal overlap.

## Selection Criteria
1. Direct impact on day-to-day build, design, validation, and review loops.
2. Strong complementarity between roles (planning, implementation, QA, review, research).
3. Low redundancy with other selected agents.
4. Deterministic, actionable behavior after normalization.

## Selected Roles and Value
- `architect`: turns ambiguous requirements into implementation-ready architecture.
- `engineer`: executes features with disciplined verification.
- `qa_tester`: blocks false completion by validating behavior.
- `docs_research_specialist`: supplies current API/library facts.
- `clean_code_reviewer`: enforces maintainability and readability quality.
- `code_architect`: deep file-level architecture mapping for large changes.
- `code_explorer`: traces existing features for safe extension.
- `code_reviewer`: high-signal correctness and risk review.
- `silent_failure_hunter`: hardens error handling and fallback behavior.
- `pr_test_analyzer`: catches critical test coverage gaps before merge.

## Why Not Everything
- Full import would add duplicate and overlapping roles with diminishing value.
- Curated scope improves reliability, discoverability, and maintenance cost.
- Additional roles can be added in future packs once usage data identifies gaps.
