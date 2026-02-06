# Attack Evasions: Identity & Channel

Identity confusion and channel bypass evasions
Total entries: 3

## Table of Contents

1. [Tool Identity Confusables (Lookalike Tools / Unicode / Namespace Tricks)](#tool-identity-confusables-lookalike-tools-unicode-namespace-tricks)
2. [Structured-Channel Bypass](#structured-channel-bypass)
3. [Metacharacter Confusion](#metacharacter-confusion)

---

<a id="tool-identity-confusables-lookalike-tools-unicode-namespace-tricks"></a>

<!-- Source: tool_identity_confusables.md -->

# Tool Identity Confusables (Lookalike Tools / Unicode / Namespace Tricks)

## Description
Evasion where a malicious tool is designed to appear equivalent to a legitimate tool:
- typosquats
- Unicode homoglyphs
- namespace shadowing
- "official-sounding" names

## Defensive notes
- signed identities, allowlists by publisher, pinned versions/hashes
- UI surfacing of provenance and identity
- detection for confusables in tool names


---


---

<a id="structured-channel-bypass"></a>

<!-- Source: structured_channel_bypass.md -->

# Structured-Channel Bypass

## Description
Evasion that exploits scanning gaps by hiding instruction-like content inside
structured fields (JSON, schemas, typed outputs) that are not normalized and scanned
like plain text.

## Defensive notes
- canonicalize + scan all channels uniformly
- schema linting rules (block imperatives in descriptions)
- validate meaning, not just shape


---


---

<a id="metacharacter-confusion"></a>

<!-- Source: metacharacter_confusion.md -->

# Metacharacter Confusion

## Description
Using special characters and metacharacters to confuse content filters

## Attack Examples
- Using escape sequences
- Implementing character encoding tricks
- Using special Unicode characters
- Creating metacharacter sequences
- Using control characters
- Implementing character substitution
- Using alternative representations
- Exploiting parser behavior


---

## Defensive Guidance

### Detection Methods

#### Identity Analysis
- **Homoglyph Detection**: Identify visually similar characters from different Unicode blocks
  - Cyrillic vs Latin lookalikes (е vs e, а vs a, о vs o)
  - Greek characters (ο vs o, ν vs v)
  - Mathematical symbols (∕ vs /)
- **Typosquatting Detection**: Identify tool names similar to legitimate tools
  - Single character substitutions
  - Character omissions
  - Character additions
  - Character transpositions
- **Namespace Confusion**: Detect namespace shadowing or collision attempts
- **Signature Verification**: Check cryptographic signatures on tool identities
- **Provenance Tracking**: Verify tool publisher and version information

#### Behavioral Detection
- **Tool Registration Patterns**: Monitor for tools with "official-sounding" names
- **Version Inconsistencies**: Flag mismatches between claimed and actual versions
- **Publisher Anomalies**: Detect unknown or suspicious publishers
- **Rapid Tool Changes**: Track tools that frequently change identity
- **Confusable Registration**: Alert when tool name is similar to existing tool

#### Automated Tools
- **Unicode Confusable Libraries**: Use confusables.py or similar
- **Fuzzy Matching**: Calculate edit distance for tool names
- **Allowlist Validators**: Check against known-good tool registries
- **Hash Verification**: Verify tool integrity via cryptographic hashes
- **DNS/Registry Lookups**: Validate tool publisher authenticity

### Defensive Strategies

#### Tool Verification

1. **Signed Identities**:
   ```python
   def verify_tool_identity(tool_name, tool_signature, tool_content):
       """Verify cryptographic signature of tool."""
       from cryptography.hazmat.primitives import hashes
       from cryptography.hazmat.primitives.asymmetric import padding

       # Verify signature against known publisher keys
       public_key = get_publisher_key(tool_name)
       try:
           public_key.verify(
               tool_signature,
               tool_content,
               padding.PSS(...),
               hashes.SHA256()
           )
           return True
       except:
           return False
   ```

2. **Confusable Detection**:
   ```python
   from confusables import confusable_characters

   def detect_confusables(tool_name, allowlist):
       """Check if tool name uses confusable characters."""
       normalized = confusable_characters(tool_name)

       # Check against allowlist
       for legitimate_tool in allowlist:
           if normalized == confusable_characters(legitimate_tool):
               if tool_name != legitimate_tool:
                   return True, legitimate_tool
       return False, None
   ```

3. **Provenance Display**:
   ```python
   def display_tool_provenance(tool):
       """Surface tool identity information to users."""
       info = {
           'name': tool.name,
           'publisher': tool.publisher,
           'version': tool.version,
           'hash': tool.content_hash,
           'signature_valid': verify_signature(tool),
           'first_seen': tool.registration_date
       }
       return info
   ```

#### Policy Enforcement

- **Allowlist by Publisher**:
  - Maintain list of trusted publishers
  - Require approval for new publishers
  - Pin specific tool versions/hashes
- **Identity Requirements**:
  - Cryptographic signatures required
  - Publisher verification required
  - Unique namespaces enforced
- **Graduated Access**:
  - Level 1: Only pre-approved tools
  - Level 2: Verified publishers with review
  - Level 3: User-defined tools in sandbox only
- **UI Requirements**:
  - Always display tool provenance
  - Highlight new or unverified tools
  - Show confusable warnings

#### Layered Defense

1. **Registration Layer**: Verify tool identity at registration
2. **Confusable Detection Layer**: Check for lookalike tools
3. **Signature Verification Layer**: Validate cryptographic signatures
4. **Runtime Validation Layer**: Re-verify tools before each use
5. **Audit Layer**: Log all tool usage with full provenance

### Implementation Example

```python
class ToolIdentityValidator:
    def __init__(self, allowlist, publisher_keys):
        self.allowlist = allowlist
        self.publisher_keys = publisher_keys

    def validate_tool(self, tool):
        """Comprehensive tool identity validation."""
        alerts = []

        # Check for confusables
        is_confusable, similar_to = detect_confusables(tool.name, self.allowlist)
        if is_confusable:
            alerts.append(f'CONFUSABLE: {tool.name} looks like {similar_to}')
            return False, alerts

        # Check for typosquatting
        for legitimate_tool in self.allowlist:
            distance = levenshtein_distance(tool.name, legitimate_tool)
            if 0 < distance <= 2:  # Very similar but not exact
                alerts.append(f'TYPOSQUAT: {tool.name} similar to {legitimate_tool}')
                return False, alerts

        # Verify signature
        if not verify_tool_identity(tool.name, tool.signature, tool.content):
            alerts.append('SIGNATURE_INVALID: Tool signature verification failed')
            return False, alerts

        # Check publisher
        if tool.publisher not in self.publisher_keys:
            alerts.append(f'UNKNOWN_PUBLISHER: {tool.publisher}')
            return False, alerts

        # Verify hash
        expected_hash = compute_hash(tool.content)
        if tool.declared_hash != expected_hash:
            alerts.append('HASH_MISMATCH: Tool content hash mismatch')
            return False, alerts

        return True, alerts

# Structured channel bypass detection
def validate_schema_content(schema):
    """Check for instruction-like content in schema fields."""
    dangerous_patterns = [
        r'\bignore\b.*\binstructions\b',
        r'\bexecute\b',
        r'\brun\b.*\bcommand\b',
        r'\bsystem\b.*\bprompt\b'
    ]

    # Check all string fields in schema
    for field in extract_string_fields(schema):
        for pattern in dangerous_patterns:
            if re.search(pattern, field, re.IGNORECASE):
                return False, f'Suspicious content in schema: {field[:50]}...'

    return True, None

# Metacharacter normalization
def normalize_metacharacters(text):
    """Normalize special characters to prevent confusion."""
    # Normalize Unicode lookalikes
    from unicodedata import normalize
    text = normalize('NFKC', text)

    # Remove/replace control characters
    text = ''.join(c for c in text if c.isprintable() or c.isspace())

    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)

    return text
```

### Severity Assessment

**Detectability**: ⭐⭐⭐ (3/5 - Moderate) - Confusables detectable, but new techniques emerge
**Bypass Difficulty**: 🟡 Medium - Requires understanding of Unicode or namespace systems
**Legitimate Use Cases**: ⭐ (1/5 - Rare) - Very few legitimate reasons for confusable tool names
**Risk Level**: 🟠 **MEDIUM-HIGH** - Can completely bypass trust systems

### Special Considerations

#### Tool Identity Confusables
- **Unicode Homoglyphs**: Characters that look identical but have different codes
  - Example: Cyrillic "а" (U+0430) vs Latin "a" (U+0061)
  - Defense: Normalize to NFC/NFKC, use confusables library
- **Typosquatting**: Tool names with small variations
  - Example: "reqeusts" instead of "requests"
  - Defense: Edit distance checking, allowlist matching
- **Namespace Shadowing**: Tools with names that shadow legitimate namespaces
  - Example: "official.google.search" when only "google.search" is legitimate
  - Defense: Strict namespace validation, publisher verification

#### Structured-Channel Bypass
- **Schema Injection**: Instructions hidden in JSON schema descriptions
- **Type Field Abuse**: Malicious content in type definitions
- **Validation Bypass**: Content that passes shape validation but contains instructions
- **Defense**: Scan ALL fields for instruction-like content, not just values

#### Metacharacter Confusion
- **Escape Sequences**: Using `\x41` instead of 'A'
- **Control Characters**: Zero-width spaces, direction controls
- **Alternative Representations**: Unicode variations of same character
- **Defense**: Normalize all inputs to canonical form

### Related Taxonomy
- **Techniques**: Identity Spoofing, Unicode Exploitation, Supply Chain Attack
- **Intents**: Trust Bypass, Privilege Escalation, Tool Impersonation
- **Related**: Encoding Evasions, Structural Evasions, Tool Shadowing

---
