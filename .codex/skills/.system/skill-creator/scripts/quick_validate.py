#!/usr/bin/env python3
"""
Quick validation script for skills.

Validates:
- SKILL.md exists
- YAML frontmatter is parseable
- Required frontmatter keys are present
- Skill name format and length
- Description basic constraints
"""

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except ModuleNotFoundError:  # pragma: no cover - exercised in minimal envs
    yaml = None

MAX_SKILL_NAME_LENGTH = 64
DEFAULT_ALLOWED_PROPERTIES = {"name", "description", "license", "allowed-tools", "metadata"}


def _strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def _parse_frontmatter_fallback(frontmatter_text: str):
    """
    Minimal YAML subset parser used only when PyYAML is unavailable.

    Supports top-level key/value pairs and one-level nested maps:

    key: value
    metadata:
      nested: value
    """
    result = {}
    current_parent = None

    for raw in frontmatter_text.splitlines():
        line = raw.rstrip("\n")
        if not line.strip() or line.lstrip().startswith("#"):
            continue

        # top-level key
        if not line.startswith(" ") and ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if not value:
                result[key] = {}
                current_parent = key
            else:
                result[key] = _strip_quotes(value)
                current_parent = None
            continue

        # one-level nested key under a top-level map
        if line.startswith("  ") and current_parent and ":" in line:
            nested_key, nested_value = line.strip().split(":", 1)
            if not isinstance(result.get(current_parent), dict):
                result[current_parent] = {}
            result[current_parent][nested_key.strip()] = _strip_quotes(nested_value)
            continue

        raise ValueError(f"Unsupported YAML structure in fallback parser: {line}")

    if not isinstance(result, dict):
        raise ValueError("Frontmatter must be a mapping")
    return result


def _load_frontmatter(frontmatter_text: str):
    if yaml is not None:
        try:
            loaded = yaml.safe_load(frontmatter_text)
        except yaml.YAMLError as exc:
            raise ValueError(f"Invalid YAML in frontmatter: {exc}") from exc
        if not isinstance(loaded, dict):
            raise ValueError("Frontmatter must be a YAML dictionary")
        return loaded

    try:
        return _parse_frontmatter_fallback(frontmatter_text)
    except ValueError as exc:
        raise ValueError(
            "Invalid YAML in frontmatter (fallback parser). "
            "Install PyYAML for full YAML support. "
            f"Details: {exc}"
        ) from exc


def validate_skill(skill_path, strict_frontmatter=False):
    """Basic validation of a skill."""
    skill_path = Path(skill_path)

    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return False, "SKILL.md not found"

    content = skill_md.read_text()
    if not content.startswith("---"):
        return False, "No YAML frontmatter found"

    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return False, "Invalid frontmatter format"

    frontmatter_text = match.group(1)

    try:
        frontmatter = _load_frontmatter(frontmatter_text)
    except ValueError as exc:
        return False, str(exc)

    allowed_properties = {"name", "description"} if strict_frontmatter else DEFAULT_ALLOWED_PROPERTIES

    unexpected_keys = set(frontmatter.keys()) - allowed_properties
    if unexpected_keys:
        allowed = ", ".join(sorted(allowed_properties))
        unexpected = ", ".join(sorted(unexpected_keys))
        return (
            False,
            f"Unexpected key(s) in SKILL.md frontmatter: {unexpected}. Allowed properties are: {allowed}",
        )

    if "name" not in frontmatter:
        return False, "Missing 'name' in frontmatter"
    if "description" not in frontmatter:
        return False, "Missing 'description' in frontmatter"

    name = frontmatter.get("name", "")
    if not isinstance(name, str):
        return False, f"Name must be a string, got {type(name).__name__}"
    name = name.strip()
    if name:
        if not re.match(r"^[a-z0-9-]+$", name):
            return (
                False,
                f"Name '{name}' should be hyphen-case (lowercase letters, digits, and hyphens only)",
            )
        if name.startswith("-") or name.endswith("-") or "--" in name:
            return (
                False,
                f"Name '{name}' cannot start/end with hyphen or contain consecutive hyphens",
            )
        if len(name) > MAX_SKILL_NAME_LENGTH:
            return (
                False,
                f"Name is too long ({len(name)} characters). "
                f"Maximum is {MAX_SKILL_NAME_LENGTH} characters.",
            )

    description = frontmatter.get("description", "")
    if not isinstance(description, str):
        return False, f"Description must be a string, got {type(description).__name__}"
    description = description.strip()
    if description:
        if "<" in description or ">" in description:
            return False, "Description cannot contain angle brackets (< or >)"
        if len(description) > 1024:
            return (
                False,
                f"Description is too long ({len(description)} characters). Maximum is 1024 characters.",
            )

    if yaml is None:
        return True, "Skill is valid! (validated with fallback parser; install PyYAML for full YAML validation)"
    return True, "Skill is valid!"


def parse_args():
    parser = argparse.ArgumentParser(description="Validate a skill directory")
    parser.add_argument("skill_directory", help="Path to skill directory")
    parser.add_argument(
        "--strict-frontmatter",
        action="store_true",
        help="Allow only name+description in frontmatter",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    valid, message = validate_skill(args.skill_directory, strict_frontmatter=args.strict_frontmatter)
    print(message)
    sys.exit(0 if valid else 1)
