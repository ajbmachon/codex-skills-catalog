# Data Explorer Template

Use this template for structured exploration: SQL/API queries, pipeline composition, regex building, schedules, or transformation logic.

## Codex intent

Let users shape structured output visually, then generate an implementation-ready prompt that includes context, constraints, and desired behavior.

## Recommended layout

```
+-------------------------+---------------------------+
| Controls                | Generated Output          |
| - Source/schema         | - formatted query/config  |
| - Fields                | - optional visual flow    |
| - Filters/conditions    |                           |
| - Aggregation/sort      +---------------------------+
| - Limits + options      | Prompt Output + actions   |
| - Presets               | [Copy] [Send to Codex]    |
+-------------------------+---------------------------+
```

## Control design

| Decision | Good controls |
|---|---|
| Select entities/fields | Searchable chips or checklist |
| Add conditions | Dynamic rule rows (field/operator/value) |
| Composition mode | Cards (strict, balanced, permissive) |
| Limits and thresholds | Numeric input/slider |
| Ordering/grouping | Sort selectors + drag reorder |

## Preview strategy

- Render readable output with lightweight syntax highlighting.
- Keep generated output deterministic for the same state.
- If using pipeline mode, show a simple step graph with arrows.
- Highlight invalid combinations inline, not in a separate error wall.

## Prompt output strategy

Generated prompt should include:

- Desired outcome (what to produce)
- Data context (schema/fields/endpoints)
- Rules and constraints (filters, ordering, limits)
- Edge handling (empty results, nulls, malformed input)

Example style:

> Write a SQL query for Postgres that joins `orders` to `users` on `user_id`, filters to paid orders after 2025-01-01, groups by user, and returns top 20 users by order count. Exclude null emails and keep deterministic ordering.

## Creative latitude

- Support multiple "output personalities" (strict SQL, explainable SQL, compact SQL).
- Allow domain-specific presets without hard-coding one workflow.
- Encourage exploratory controls (what-if toggles) while preserving valid output.

## Output contract

- Single-file HTML with inline CSS/JS.
- Live updates on every control change.
- Prompt includes enough context to execute without opening the playground.
- Include Copy and Send-to-Codex actions (`prompt-output`, `send-btn`).
