#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_ROOT="$ROOT/.codex/skills"
VALIDATOR="$SKILLS_ROOT/.system/skill-creator/scripts/quick_validate.py"
LINTER="$SKILLS_ROOT/.system/skill-creator/scripts/lint_skills.py"
MANIFEST="$ROOT/skills-manifest.yaml"

if [[ ! -x "$VALIDATOR" ]]; then
  echo "Error: validator script is missing or not executable: $VALIDATOR" >&2
  exit 1
fi

if [[ ! -x "$LINTER" ]]; then
  echo "Error: linter script is missing or not executable: $LINTER" >&2
  exit 1
fi

if [[ ! -f "$MANIFEST" ]]; then
  echo "Error: manifest file is missing: $MANIFEST" >&2
  exit 1
fi

NON_SYSTEM_SKILLS=()
while IFS= read -r skill; do
  NON_SYSTEM_SKILLS+=("$skill")
done < <(awk '$1 == "-" && $2 == "id:" && $3 !~ /^\.system/ { print $3 }' "$MANIFEST")

if [[ ${#NON_SYSTEM_SKILLS[@]} -eq 0 ]]; then
  echo "Error: no non-system skills found in manifest: $MANIFEST" >&2
  exit 1
fi

echo "[1/2] strict frontmatter validation"
for skill in "${NON_SYSTEM_SKILLS[@]}"; do
  "$VALIDATOR" --strict-frontmatter "$SKILLS_ROOT/$skill" >/dev/null
  echo "  - $skill: ok"
done

echo "[2/2] cross-skill lint"
"$LINTER" --root "$SKILLS_ROOT" --strict

echo "Validation complete."
