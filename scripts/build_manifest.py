#!/usr/bin/env python3
from __future__ import annotations
import hashlib
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / ".codex" / "skills"
MANIFEST = ROOT / "skills-manifest.yaml"

skills = [
    "cognitive-collaboration",
    "dev-browser",
    "evals",
    "frontend-design",
    "interview",
    "mermaid",
    "playground",
    "prompt-craft",
    "securing-ai",
    "systematic-debugging",
    ".system/skill-creator",
    ".system/skill-installer",
]

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def repository_version() -> str:
    if not MANIFEST.exists():
        return "1.1.0"
    for line in MANIFEST.read_text().splitlines():
        if line.startswith("repository_version:"):
            return line.split(":", 1)[1].strip()
    return "1.1.0"


def existing_skill_versions() -> dict[str, str]:
    if not MANIFEST.exists():
        return {}
    versions: dict[str, str] = {}
    lines = MANIFEST.read_text().splitlines()
    for i, line in enumerate(lines):
        line = line.strip()
        if not line.startswith("path: .codex/skills/"):
            continue
        skill = line.split("path: .codex/skills/", 1)[1]
        for j in range(i + 1, min(i + 6, len(lines))):
            candidate = lines[j].strip()
            if candidate.startswith("version:"):
                versions[skill] = candidate.split(":", 1)[1].strip()
                break
    return versions

lines = []
lines.append(f"manifest_version: 1")
lines.append(f"generated_on: {date.today().isoformat()}")
lines.append(f"repository_version: {repository_version()}")
lines.append("skills:")
versions = existing_skill_versions()

for skill in skills:
    skill_dir = SKILLS_ROOT / skill
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        raise SystemExit(f"Missing SKILL.md: {skill_md}")
    lines.append(f"  - id: {skill.replace('/', '__')}")
    lines.append(f"    path: .codex/skills/{skill}")
    lines.append(f"    version: {versions.get(skill, '1.0.0')}")
    lines.append(f"    skill_md_sha256: {sha256(skill_md)}")

MANIFEST.write_text("\n".join(lines) + "\n")
print(f"wrote {MANIFEST}")
