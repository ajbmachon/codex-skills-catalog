# Document Critique Template

Use this template for reviewing text artifacts: specs, READMEs, proposals, policies, docs, and prompt drafts.

## Codex intent

Provide structured review controls (approve/reject/comment) that produce a clean, actionable revision prompt.

## Recommended layout

```
+------------------------------+-----------------------+
| Document viewer              | Suggestions panel     |
| - line numbers               | - filter by status    |
| - inline highlighting        | - approve/reject      |
| - click to focus suggestion  | - add user comment    |
+------------------------------+-----------------------+
| Prompt Output + actions                              |
| [Copy] [Send to Codex]                               |
+------------------------------------------------------+
```

## State model

Each suggestion should track:

- `status`: pending/approved/rejected
- `lineRef` or `range`
- `suggestion` text
- optional user comment
- optional category tag

## UX expectations

- Fast filtering: All, Pending, Approved, Rejected.
- Clear visual statuses in both panel and document.
- Jump from suggestion card to document location.
- Preserve comments when switching filters.

## Prompt output strategy

Generate prompt from approved items + user comments, while optionally preserving rejected notes for context.

Example style:

> Revise the document with these approved changes: tighten the objective statement on lines 12-18, add measurable success criteria, and replace ambiguous language in section "Rollout". Keep tone direct and implementation-focused.

## Creative latitude

- Critique workflows can be strict editorial, collaborative workshop, or lightweight pass.
- You may support custom statuses if they improve the review process.
- Do not force one scoring system; adapt to document type.

## Output contract

- Single-file HTML, no external dependencies.
- Live prompt regeneration on every decision change.
- Include Copy and Send-to-Codex actions (`prompt-output`, `send-btn`).
