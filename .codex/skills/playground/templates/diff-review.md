# Diff Review Template

Use this template for code review workflows over diffs: commits, pull requests, patch files, or before/after refactors.

## Codex intent

Enable line-level feedback and produce a high-signal review prompt that can be applied directly in follow-up implementation.

## Recommended layout

```
+-----------------------------+--------------------------------+
| Meta panel                  | Diff viewer                    |
| - commit/PR info            | - file sections + hunks        |
| - file list + filters       | - line numbers + +/- styling   |
| - summary stats             | - click line to comment        |
+-----------------------------+--------------------------------+
| Prompt Output + actions                                      |
| [Copy] [Send to Codex]                                       |
+--------------------------------------------------------------+
```

## Interaction model

- Click a line to add/edit comment.
- Show indicator for commented lines.
- Support delete/reset comment state.
- Keep comments keyed by stable line identifier.

## Data structure suggestion

```javascript
const comments = {
  "file:hunk:line": "Potential null dereference if payload is missing"
};
```

## Prompt output strategy

Output should be review-ready and implementation-ready.

Include:

- file + line reference
- observed issue/risk
- suggested change intent
- severity/prioritization (optional)

Example style:

> Review and address these findings:
> 1) `src/cache/store.ts:88` possible stale write on concurrent updates; add compare-and-set or lock strategy.
> 2) `src/api/users.ts:143` missing null guard for optional profile field.

## Creative latitude

- You can use strict "findings" mode or collaborative "improvements" mode.
- Allow severity labels only if they help this review context.
- Keep visual style adaptable to project branding or neutral Git-style.

## Output contract

- Single self-contained HTML file.
- Supports both light and dark reading contexts when practical.
- Includes `prompt-output` and `send-btn` wiring for Codex sync.
