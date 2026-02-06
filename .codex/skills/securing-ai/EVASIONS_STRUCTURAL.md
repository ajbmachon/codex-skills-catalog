# Attack Evasions: Structural Formats

Structured data format evasions
Total entries: 6

## Table of Contents

1. [Graph Nodes](#graph-nodes)
2. [JSON](#json)
3. [Markdown](#markdown)
4. [Spaces](#spaces)
5. [Splats](#splats)
6. [XML](#xml)

---

<a id="graph-nodes"></a>

<!-- Source: graph_nodes.md -->

# Graph Nodes

## Description
Using graph-based data structures to hide malicious content

## Attack Examples
- Encoding messages in node relationships
- Using graph traversal patterns to hide data
- Storing content in node attributes
- Creating steganographic graph layouts
- Using edge weights to encode information
- Hiding data in graph metadata
- Creating special graph patterns
- Using subgraph structures to segment content


---


---

<a id="json"></a>

<!-- Source: json.md -->

# JSON

## Description
Using JSON structure and formatting to hide malicious content

## Attack Examples
- Using Unicode escapes in JSON strings
- Nesting objects deeply to hide content
- Using JSON comments (non-standard)
- Exploiting whitespace in JSON
- Using JSON pointer syntax
- Embedding content in property names
- Using array indices to encode information
- Exploiting JSON parsing quirks


---


---

<a id="markdown"></a>

<!-- Source: markdown.md -->

# Markdown

## Description
Using markdown formatting to hide or obfuscate malicious content

## Attack Examples
- Using markdown comments to hide content
- Exploiting markdown table formatting
- Using markdown link references to split content
- Hiding content in markdown code blocks
- Using HTML within markdown
- Exploiting markdown escaping mechanisms
- Using markdown footnotes to store partial content


---


---

<a id="spaces"></a>

<!-- Source: spaces.md -->

# Spaces

## Description
Using whitespace manipulation to hide malicious content

## Attack Examples
- Using zero-width spaces to hide content
- Embedding messages in trailing spaces
- Using different types of spaces (em space, en space, etc.)
- Tab character substitution
- Using line breaks and carriage returns to split content


---


---

<a id="splats"></a>

<!-- Source: splats.md -->

# Splats

## Description
Using splat-based techniques to obfuscate malicious content

## Attack Examples
- Using asterisk patterns to encode messages
- Creating visual patterns with special characters
- Using splat characters in variable names
- Hiding content in comment decorations
- Creating ASCII art with splats
- Using splats for text alignment
- Combining splats with other special characters


---


---

<a id="xml"></a>

<!-- Source: xml.md -->

# XML

## Description
Using XML formatting and structure to hide malicious content

## Attack Examples
- Using XML CDATA sections to hide content
- Exploiting XML comments
- Using XML entity references
- Embedding content in XML attributes
- Using XML namespaces to obfuscate
- Exploiting XML processing instructions
- Using XML DTD for content hiding


---

## Defensive Guidance

### Detection Methods

#### Structural Analysis
- **Format Detection**: Use JSON parsers, XML parsers, Markdown processors to identify structure
- **Nesting Depth**: Flag deeply nested structures (>10 levels) as potential evasion
- **Whitespace Analysis**: Detect unusual whitespace patterns (steganography, hidden text)
  - Zero-width spaces (U+200B, U+200C, U+200D)
  - Different space types (em space, en space, etc.)
  - Trailing spaces, excessive line breaks
- **Markup Abuse**: HTML/Markdown hiding text in comments, styles, or attributes
- **Graph Complexity**: Unusual graph structures, excessive node/edge counts

#### Behavioral Detection
- **Structure-Payload Mismatch**: Simple question wrapped in complex structure
- **Hidden Content Indicators**: Comments, style tags, Unicode whitespace
- **Nested Instruction Patterns**: Instructions buried deep in structure
- **Format-Specific Exploits**:
  - JSON injection (property names containing instructions)
  - XML entity expansion attacks
  - Markdown XSS vectors
  - Graph steganography (encoding in relationships)

#### Automated Tools
- **JSON/XML Validators**: Check for malformed or malicious structures
- **Markdown Sanitizers**: Strip potentially harmful markdown (e.g., bleach, DOMPurify)
- **Whitespace Normalizers**: Remove excess/unusual whitespace
- **AST Analysis**: Parse structure and analyze semantic tree
- **Graph Analysis Tools**: Detect anomalous graph patterns

### Defensive Strategies

#### Input Normalization

1. **Structure Flattening**:
   ```python
   def flatten_json(data, depth=0, max_depth=5):
       """Limit nesting depth to prevent exploit."""
       if isinstance(data, dict) and depth < max_depth:
           return {k: flatten_json(v, depth+1, max_depth) for k, v in data.items()}
       elif isinstance(data, list) and depth < max_depth:
           return [flatten_json(item, depth+1, max_depth) for item in data]
       else:
           return str(data)  # Flatten to string at max depth
   ```

2. **Whitespace Normalization**:
   ```python
   import re

   def normalize_whitespace(text):
       # Remove zero-width characters
       text = re.sub(r'[\u200B-\u200D\uFEFF]', '', text)
       # Collapse multiple spaces to single space
       text = re.sub(r'\s+', ' ', text)
       # Remove trailing whitespace
       text = text.strip()
       return text
   ```

3. **Comment Stripping**: Remove HTML/XML comments, Markdown comments
4. **Markup Sanitization**: Strip or escape HTML/Markdown before processing
5. **Graph Flattening**: Extract text content from node/edge attributes

#### Policy Enforcement

- **Structure Limits**:
  - Max nesting depth: 10 levels
  - Max structure size: 100KB
  - Max array length: 1000 elements
  - Max graph nodes: 500
  - Max graph edges: 1000
- **Legitimate Use Cases**:
  - API requests (JSON/XML)
  - Document processing (Markdown)
  - Code formatting (spaces)
  - Data visualization (graphs)
- **Risk-Based Response**:
  - Simple structures: Process normally
  - Complex structures: Flatten or request simplification
  - Malicious structures: Block and log

#### Layered Defense

1. **Parse Layer**: Validate and sanitize structure
2. **Flatten Layer**: Reduce to semantic content
3. **Content Layer**: Apply safety checks to extracted text
4. **Monitor Layer**: Track users exploiting structure

### Implementation Example

```python
import json
import re
import xml.etree.ElementTree as ET

def sanitize_structured_input(text: str) -> str:
    """
    Detect and sanitize structured formats.
    """
    # Whitespace normalization (do first)
    text = normalize_whitespace(text)

    # Try JSON
    try:
        data = json.loads(text)
        # Flatten deeply nested structures
        flattened = flatten_json(data, max_depth=5)
        # Extract all string values
        text = extract_strings(flattened)
    except json.JSONDecodeError:
        pass

    # Try XML
    if text.strip().startswith('<'):
        try:
            root = ET.fromstring(text)
            # Extract text content, ignore structure
            text = ''.join(root.itertext())
        except ET.ParseError:
            pass

    # Markdown sanitization
    if has_markdown(text):
        # Strip code blocks, comments, HTML
        text = strip_markdown_artifacts(text)

    return text

def extract_strings(obj):
    """Extract all string values from nested structure."""
    if isinstance(obj, str):
        return obj
    elif isinstance(obj, dict):
        return ' '.join(extract_strings(v) for v in obj.values())
    elif isinstance(obj, list):
        return ' '.join(extract_strings(item) for item in obj)
    else:
        return str(obj)
```

### Severity Assessment

**Detectability**: ⭐⭐⭐⭐ (4/5 - Easy to Moderate) - Structure is analyzable
**Bypass Difficulty**: 🟢 Low - Easy to create complex structures
**Legitimate Use Cases**: ⭐⭐⭐⭐⭐ (5/5 - Very Common) - APIs, documents, code all use structure
**Risk Level**: 🟢 **LOW to MEDIUM** - Depends on system's exposure to structured inputs

### Special Considerations

#### JSON/XML Specific
- **Property Name Injection**: Instructions hidden in JSON property names
- **Entity Expansion**: XML billion laughs attack
- **Comment Abuse**: Non-standard JSON comments containing instructions
- **Unicode Escapes**: `\u0048\u0065\u006c\u006c\u006f` bypassing detection

#### Whitespace Specific
- **Zero-Width Characters**: Invisible to users but readable by models
- **Bidirectional Text**: Unicode direction control characters
- **Steganography**: Information encoded in spacing patterns
- **Line Break Abuse**: Splitting keywords across lines

#### Graph-Based Specific
- **Relationship Encoding**: Messages hidden in edge relationships
- **Traversal Patterns**: Instructions revealed through specific graph traversal
- **Metadata Hiding**: Content in node/edge attributes not displayed
- **Subgraph Segmentation**: Splitting malicious content across disconnected subgraphs

### Related Taxonomy
- **Techniques**: Format Abuse, Steganography, Obfuscation
- **Intents**: Detection Evasion, Content Hiding
- **Related**: Encoding Evasions, Rendering Evasions, Metadata-Only Visibility

---
