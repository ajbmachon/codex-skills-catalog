#!/usr/bin/env python3
"""
Mermaid Diagram Validator

Usage:
    echo "graph TD..." | validate.py         # Validate text (DEFAULT)
    validate.py --file diagram.mmd           # Validate file
"""

import sys
import subprocess
import tempfile
import os
import argparse
from pathlib import Path

# Colors
RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
NC = '\033[0m'  # No Color


def check_mmdc():
    """Check if mermaid-cli is installed."""
    try:
        subprocess.run(['mmdc', '--version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def suggest_fix(error_text):
    """Provide helpful suggestions based on error."""
    error_lower = error_text.lower()

    if 'parse error' in error_lower:
        return [
            "Check for:",
            "  - Unquoted labels with special chars → Use A[\"text\"]",
            "  - Wrong brackets → Check shape syntax",
            "  - Unbalanced parentheses/brackets"
        ]
    elif 'direction' in error_lower:
        return ["Add direction at start: graph TD or graph LR"]
    elif 'unexpected token' in error_lower:
        return [
            "Special character issue:",
            "  - Wrap labels in quotes",
            "  - Avoid special chars in node IDs"
        ]
    else:
        return ["Check SKILL.md common pitfalls section"]


def validate_diagram(diagram_text):
    """Validate diagram by attempting to render with mmdc."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.mmd', delete=False) as diagram_file:
        diagram_file.write(diagram_text)
        diagram_path = diagram_file.name

    output_path = f"/tmp/mermaid-validation-{os.getpid()}.png"

    try:
        result = subprocess.run(
            ['mmdc', '-i', diagram_path, '-o', output_path, '--quiet'],
            capture_output=True,
            text=True,
            timeout=30
        )

        # Cleanup
        if os.path.exists(output_path):
            os.unlink(output_path)
        os.unlink(diagram_path)

        if result.returncode == 0:
            print(f"{GREEN}✅ Diagram is valid{NC}")
            return True
        else:
            print(f"{RED}❌ Validation failed{NC}\n")

            # Show error details
            error_text = result.stderr + result.stdout
            if error_text.strip():
                print("Error details:")
                lines = [l for l in error_text.split('\n') if 'error' in l.lower()]
                for line in lines[:5]:
                    print(line)
                if not lines:
                    print(error_text[:500])
                print()

            # Provide suggestions
            suggestions = suggest_fix(error_text)
            print(f"{YELLOW}💡 Suggestion: {suggestions[0]}{NC}")
            for suggestion in suggestions[1:]:
                print(suggestion)

            return False

    except subprocess.TimeoutExpired:
        print(f"{RED}❌ Validation timed out{NC}")
        print(f"{YELLOW}💡 Suggestion: Diagram may be too complex{NC}")
        if os.path.exists(output_path):
            os.unlink(output_path)
        os.unlink(diagram_path)
        return False


def main():
    parser = argparse.ArgumentParser(description='Validate Mermaid diagrams')
    parser.add_argument('--file', '-f', type=str, help='Validate diagram from file')
    args = parser.parse_args()

    # Check mmdc is installed
    if not check_mmdc():
        print(f"{RED}❌ mermaid-cli not installed{NC}")
        print(f"{YELLOW}💡 Install: npm install -g @mermaid-js/mermaid-cli{NC}")
        sys.exit(1)

    # Get diagram text
    if args.file:
        # Read from file
        file_path = Path(args.file)
        if not file_path.exists():
            print(f"{RED}❌ File not found: {args.file}{NC}")
            sys.exit(1)

        with open(file_path) as f:
            diagram_text = f.read()
        print(f"🔍 Validating: {args.file}\n")
    else:
        # Read from stdin
        if sys.stdin.isatty():
            print(f"{RED}❌ Usage: echo 'diagram' | validate.py OR validate.py --file diagram.mmd{NC}")
            sys.exit(1)

        diagram_text = sys.stdin.read()
        print("🔍 Validating diagram\n")

    # Validate
    is_valid = validate_diagram(diagram_text)
    sys.exit(0 if is_valid else 1)


if __name__ == '__main__':
    main()
