# Codex Skill Packaging Best Practices

This repository applies the following practices for packaging, versioning, and distribution.

## Packaging

- Keep skills in repository-scoped `.codex/skills` for predictable discovery in Codex projects.
- Keep each skill self-contained with required `SKILL.md` and optional `scripts/`, `references/`, `assets/`, `agents/openai.yaml`.
- Exclude runtime artifacts from version control (`node_modules`, browser profiles, temp files, caches).

## Metadata

- Use strict `SKILL.md` frontmatter with `name` and `description` for non-system skills.
- Add `agents/openai.yaml` for UI-facing metadata and better discoverability.

## Versioning

- Track repository release with SemVer tags (`vX.Y.Z`).
- Track per-skill versions in `skills-manifest.yaml`.
- Include content hashes (`skill_md_sha256`) to detect drift.

## Validation

- Validate every non-system skill with strict frontmatter checks.
- Run cross-skill lint to catch broken links, hardcoded paths, and portability issues.
- Enforce validation in CI on push and pull request.

## Distribution

- Distribute as a Git repo with `.codex/skills` path intact.
- Install individual skills via GitHub path using installer script.
- Prefer updating via pull/tag rather than ad-hoc local edits.

## Source References

- Codex docs: https://platform.openai.com/docs/codex/overview
- Codex docs (config): https://platform.openai.com/docs/codex/config
- Agent Skills spec: https://www.agentskills.io/skills
- OpenAI skills repository conventions: https://github.com/openai/skills
