#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_ROOT="$ROOT/.codex/skills"
VALIDATOR="$SKILLS_ROOT/.system/skill-creator/scripts/quick_validate.py"
LINTER="$SKILLS_ROOT/.system/skill-creator/scripts/lint_skills.py"

NON_SYSTEM_SKILLS=(
  cognitive-collaboration
  dev-browser
  evals
  frontend-design
  interview
  mermaid
  playground
  prompt-craft
  securing-ai
  systematic-debugging
)

echo "[1/2] strict frontmatter validation"
for skill in "${NON_SYSTEM_SKILLS[@]}"; do
  "$VALIDATOR" --strict-frontmatter "$SKILLS_ROOT/$skill" >/dev/null
  echo "  - $skill: ok"
done

echo "[2/2] cross-skill lint"
"$LINTER" --root "$SKILLS_ROOT" --strict

echo "Validation complete."
