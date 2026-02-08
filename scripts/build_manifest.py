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

lines = []
lines.append(f"manifest_version: 1")
lines.append(f"generated_on: {date.today().isoformat()}")
lines.append("repository_version: 1.1.0")
lines.append("skills:")

for skill in skills:
    skill_dir = SKILLS_ROOT / skill
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        raise SystemExit(f"Missing SKILL.md: {skill_md}")
    lines.append(f"  - id: {skill.replace('/', '__')}")
    lines.append(f"    path: .codex/skills/{skill}")
    lines.append(f"    version: 1.0.0")
    lines.append(f"    skill_md_sha256: {sha256(skill_md)}")

MANIFEST.write_text("\n".join(lines) + "\n")
print(f"wrote {MANIFEST}")
