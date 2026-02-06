#!/usr/bin/env python3
"""Cross-skill linter.

Checks:
- SKILL.md frontmatter shape
- broken local markdown links
- hardcoded ~/.claude paths
- unresolved required sub-skill references
- stale NEW <year> markers
"""

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path


FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
CODE_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
REQUIRED_SUPERPOWER_RE = re.compile(r"superpowers:([a-z0-9-]+)")
NEW_YEAR_RE = re.compile(r"\bNEW\s+(20\d{2})\b")
ALLOWED_FRONTMATTER_KEYS = {"name", "description", "metadata", "license", "allowed-tools"}


@dataclass
class Finding:
    level: str  # ERROR | WARN
    path: Path
    message: str


def parse_frontmatter(content: str):
    match = FRONTMATTER_RE.match(content)
    if not match:
        return None

    fm = {}
    for raw in match.group(1).splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw.startswith(" "):
            continue
        if ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        fm[key.strip()] = value.strip()
    return fm


def strip_code_fences(content: str) -> str:
    return CODE_FENCE_RE.sub("", content)


def iter_local_links(text: str):
    for raw in LINK_RE.findall(text):
        link = raw.strip()
        if not link or link.startswith(("http://", "https://", "mailto:")):
            continue
        if link.startswith("#"):
            continue
        yield link.split("#", 1)[0]


def lint_skill(skill_md: Path, root: Path):
    findings = []
    content = skill_md.read_text()
    body = strip_code_fences(content)

    # Frontmatter checks
    fm = parse_frontmatter(content)
    if fm is None:
        findings.append(Finding("ERROR", skill_md, "Missing or invalid YAML frontmatter block"))
    else:
        missing = [k for k in ("name", "description") if k not in fm]
        for key in missing:
            findings.append(Finding("ERROR", skill_md, f"Missing required frontmatter key: {key}"))
        unexpected = sorted(set(fm.keys()) - ALLOWED_FRONTMATTER_KEYS)
        if unexpected:
            findings.append(
                Finding(
                    "ERROR",
                    skill_md,
                    f"Unexpected frontmatter keys: {', '.join(unexpected)}",
                )
            )

    # Hardcoded path checks
    if "~/.claude/skills" in content:
        findings.append(
            Finding("ERROR", skill_md, "Uses hardcoded ~/.claude/skills path; use $CODEX_HOME/$HOME portable path")
        )

    # Broken markdown links (outside fenced code)
    skill_dir = skill_md.parent
    for link in sorted(set(iter_local_links(body))):
        target = (skill_dir / link).resolve() if not link.startswith("/") else Path(link)
        if not target.exists():
            findings.append(Finding("ERROR", skill_md, f"Broken local markdown link: {link}"))

    # Unresolved superpowers references
    for match in REQUIRED_SUPERPOWER_RE.findall(content):
        if not (root / match).exists():
            findings.append(
                Finding("ERROR", skill_md, f"References unavailable required sub-skill: superpowers:{match}")
            )

    # Stale year marker warnings
    current_year = date.today().year
    for year_str in NEW_YEAR_RE.findall(content):
        year = int(year_str)
        if year < current_year:
            findings.append(
                Finding(
                    "WARN",
                    skill_md,
                    f"Stale freshness marker: 'NEW {year}' (current year is {current_year})",
                )
            )

    return findings


def discover_skills(root: Path):
    skill_files = sorted(root.rglob("SKILL.md"))
    return [path for path in skill_files if path.is_file()]


def parse_args():
    parser = argparse.ArgumentParser(description="Lint Codex skills")
    parser.add_argument(
        "--root",
        default=str(Path.home() / ".codex" / "skills"),
        help="Skills root directory (default: ~/.codex/skills)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as errors",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    root = Path(args.root).expanduser().resolve()

    if not root.exists():
        print(f"ERROR: root does not exist: {root}")
        return 2

    skill_files = discover_skills(root)
    if not skill_files:
        print(f"ERROR: no SKILL.md files found under {root}")
        return 2

    findings = []
    for skill_md in skill_files:
        findings.extend(lint_skill(skill_md, root))

    errors = [f for f in findings if f.level == "ERROR"]
    warnings = [f for f in findings if f.level == "WARN"]

    for finding in findings:
        rel = finding.path.relative_to(root)
        print(f"{finding.level:5} {rel}: {finding.message}")

    print("\nSummary")
    print(f"- Skills scanned: {len(skill_files)}")
    print(f"- Errors: {len(errors)}")
    print(f"- Warnings: {len(warnings)}")

    if errors:
        return 1
    if args.strict and warnings:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
