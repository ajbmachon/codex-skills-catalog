# Workflow Patterns

Use these when a skill requires a strict execution flow.

## Pattern: Deterministic Router
1. Detect intent from explicit signals.
2. If ambiguous, ask one routing question.
3. Confirm selected mode in one line.
4. Execute only that mode's procedure.

## Pattern: Evidence-First Loop
1. Gather required context and evidence.
2. Run one action.
3. Validate state.
4. Decide next action based on evidence.

## Pattern: Bounded Iteration
- Define max rounds or attempts.
- Define exit criteria.
- Define fallback behavior when criteria are not met.

## Pattern: Safe Degradation
- If optional dependencies are missing, switch to documented fallback path.
- Keep output useful without the optional dependency.
