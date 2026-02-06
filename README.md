# Codex Skills Catalog

Versioned skill repository for Codex, packaged in repo-scoped format under `.codex/skills`.

## Goals

- Preserve and version high-value skills in git.
- Keep skills deterministic, validated, and portable.
- Make installation and distribution straightforward.

## Repository Layout

```text
.codex/skills/
  cognitive-collaboration/
  dev-browser/
  frontend-design/
  interview/
  mermaid/
  playground/
  prompt-craft/
  securing-ai/
  systematic-debugging/
  .system/skill-creator/
  .system/skill-installer/
skills-manifest.yaml
scripts/validate_skills.sh
scripts/build_manifest.py
scripts/bump_manifest_version.py
```

## Install Options

### 1. Repo-scoped (recommended for development)

Clone this repo and run Codex from this repository root so `.codex/skills` is discovered automatically.

### 2. Install individual skills from GitHub

Use the installer script from `skill-installer`:

```bash
python .codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo <owner>/<repo> \
  --path .codex/skills/<skill-name>
```

## Validation

Run:

```bash
./scripts/validate_skills.sh
```

This runs:
- strict frontmatter validation for non-system skills
- cross-skill lint checks (broken links, hardcoded paths, missing contracts)

Regenerate/check manifest:

```bash
./scripts/build_manifest.py
```

## Versioning

- Repository uses SemVer tags (example: `v1.0.0`).
- Each skill version is tracked in `skills-manifest.yaml`.
- Bump skill versions when behavior or contracts change.
- Use `scripts/bump_manifest_version.py` for controlled version bumps.

## Included Skills

See `skills-manifest.yaml` for versions and checksums.

## Best-Practice Basis

This repo follows:
- Codex docs guidance for repository-scoped `.codex/skills` usage.
- OpenAI Agent Skills spec for skill metadata (`agents/openai.yaml`).
- OpenAI skills repository conventions for distribution and validation workflows.

See `docs/best-practices.md` for implementation details.
