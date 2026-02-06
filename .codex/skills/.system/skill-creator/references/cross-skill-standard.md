# Cross-Skill Standard

Use this standard for all skills to improve determinism, reliability, ergonomics, clarity, and value.

## Required Sections
- `Prereqs`: runtime assumptions, tools, and capability checks.
- `Deterministic Workflow`: numbered sequence with explicit routing and exit criteria.
- `Failure Recovery`: known failure modes and fallback behavior.
- `Output Contract`: expected output shape and optional machine-readable format.
- `Validation`: concrete commands to verify success.

## Authoring Rules
- Keep frontmatter minimal (`name`, `description`) unless extra fields are explicitly required.
- Use environment-portable paths (`$CODEX_HOME` / `$HOME`) instead of hardcoded home directories.
- Avoid references to tools/skills that are not guaranteed to exist; provide fallback behavior.
- Use one canonical command example per critical operation.
- Prefer deterministic checks over subjective completion criteria.

## Validation Rules
- `SKILL.md` exists and has valid frontmatter.
- All local markdown links resolve.
- No hardcoded `~/.claude/skills` paths.
- No unresolved required-skill references.
- Mentioned scripts/templates/references exist.

## Maintenance Rules
- Version assumptions with explicit dates when time-sensitive.
- Re-run lint after changes.
- Keep `SKILL.md` concise; move deep content to references.
