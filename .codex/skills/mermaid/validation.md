# Mermaid Validation Guide

Verify diagrams are syntactically correct before use.

## Prerequisites

**mermaid-cli** must be installed:
```bash
npm install -g @mermaid-js/mermaid-cli
```

Verify installation:
```bash
mmdc --version
```

## Validation Workflow

### Method 1: Text Validation (Default, Recommended)

```bash
# Create diagram text
DIAGRAM="graph TD
    A --> B"

# Validate (stdin is default)
echo "$DIAGRAM" | ~/.claude/skills/mermaid/scripts/validate.py
```

**Output:**
```
✅ Diagram is valid
```

Or:
```
❌ Validation failed: Parse error on line 5
💡 Suggestion: Check for unescaped quotes or special characters
```

### Method 2: File Validation

```bash
# If diagram already written to file
~/.claude/skills/mermaid/scripts/validate.py --file diagram.mmd
```

**Use file mode when:**
- Diagram already exists in a file
- Working with existing .mmd files
- Need to validate multiple files in a script

## Common Validation Errors

### Parse Error
**Cause:** Syntax issue - unquoted labels, wrong brackets, unbalanced parentheses

**Fix:**
1. Quote all labels with special chars: `A["Label: text"]`
2. Check bracket balance
3. Verify arrow syntax for diagram type

### Invalid Direction
**Cause:** Missing or wrong direction declaration

**Fix:** Add `graph TD` or `graph LR` at the start

### Unexpected Token
**Cause:** Special character not escaped

**Fix:** Wrap label in quotes or remove special char

### Render Timeout
**Cause:** Diagram too complex or infinite loop

**Fix:** Simplify diagram or check for circular references

## Standard Workflow

### Creating Diagrams (ALWAYS Use This)

1. **Create complete diagram** following SKILL.md pitfall guidelines
2. **ALWAYS validate before writing to file:**
   ```bash
   DIAGRAM="graph TD..."
   echo "$DIAGRAM" | ~/.claude/skills/mermaid/scripts/validate.py
   ```
3. **If valid:** Write to file or store in Graphiti ✅
4. **If invalid:** Follow debugging workflow below

### Debugging Workflow (Only When Validation Fails)

If validation fails, debug incrementally:

```bash
# 1. Isolate the error by testing sections
# Create test.mmd with just first section
mmdc -i test.mmd -o /tmp/test.png

# 2. Add sections one at a time until error appears
# 3. Fix the problematic section
# 4. Re-validate complete diagram
```

**Key principle:** Don't validate during creation - only validate the final result.

## Integration Tips

### In Scripts

```bash
#!/bin/bash
if mmdc -i "$1" -o /tmp/test.png --quiet 2>/dev/null; then
    echo "✅ Diagram valid"
    # Proceed with using diagram
else
    echo "❌ Diagram invalid"
    exit 1
fi
```

### Pre-commit Hook

```bash
# .git/hooks/pre-commit
for file in $(git diff --cached --name-only | grep '\.mmd$'); do
    if ! mmdc -i "$file" -o /tmp/test.png --quiet 2>/dev/null; then
        echo "❌ Invalid Mermaid diagram: $file"
        exit 1
    fi
done
```

## Troubleshooting Validation

### mmdc Not Found
**Solution:** Install mermaid-cli: `npm install -g @mermaid-js/mermaid-cli`

### Permission Denied
**Solution:** Check file permissions: `chmod +x validate.sh`

### Validation Passes But Renders Wrong
**Cause:** Syntax is valid but logic is wrong (e.g., circular flow)
**Solution:** Visual inspection of rendered output

## Alternative: Online Validation

Use Mermaid Live Editor for quick checks:
```
https://mermaid.live
```

Paste diagram, see immediate rendering + errors.

**Note:** Online validation requires internet and doesn't integrate into automated workflows.
