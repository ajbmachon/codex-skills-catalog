#!/usr/bin/env python3
"""Bump version fields in skills-manifest.yaml.

Usage:
  scripts/bump_manifest_version.py --repo-version 1.0.1
  scripts/bump_manifest_version.py --skill prompt-craft --skill-version 1.1.0
"""

from __future__ import annotations

import argparse
from pathlib import Path

MANIFEST = Path(__file__).resolve().parents[1] / "skills-manifest.yaml"


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--repo-version")
    p.add_argument("--skill")
    p.add_argument("--skill-version")
    return p.parse_args()


def main():
    args = parse_args()
    text = MANIFEST.read_text().splitlines()

    if args.repo_version:
        for i, line in enumerate(text):
            if line.startswith("repository_version:"):
                text[i] = f"repository_version: {args.repo_version}"
                break

    if args.skill and args.skill_version:
        target = args.skill
        for i, line in enumerate(text):
            if line.strip() == f"path: .codex/skills/{target}":
                # next version line
                for j in range(i + 1, min(i + 5, len(text))):
                    if text[j].strip().startswith("version:"):
                        indent = text[j].split("version:", 1)[0]
                        text[j] = f"{indent}version: {args.skill_version}"
                        break
                break

    MANIFEST.write_text("\n".join(text) + "\n")
    print(f"updated {MANIFEST}")


if __name__ == "__main__":
    main()
