# Attack Evasions: Encoding & Transformation

Character encoding and transformation evasions
Total entries: 10

## Table of Contents

1. [Base64](#base64)
2. [Hex](#hex)
3. [Cipher](#cipher)
4. [Morse](#morse)
5. [Reverse](#reverse)
6. [Case Changing](#case-changing)
7. [Phonetic Substitution](#phonetic-substitution)
8. [Alternative Language](#alternative-language)
9. [Fictional Language](#fictional-language)
10. [Emoji](#emoji)

---

<a id="base64"></a>

<!-- Source: base64.md -->

# Base64

## Description
Using Base64 encoding to obfuscate malicious content

## Attack Examples
- Encoding entire prompts in Base64
- Splitting Base64 content across multiple inputs
- Mixing Base64 with plaintext
- Double-encoding content
- Using custom Base64 alphabets
- Padding manipulation
- Combining Base64 with other encodings


---


---

<a id="hex"></a>

<!-- Source: hex.md -->

# Hex

## Description
Using hexadecimal encoding to obfuscate malicious content

## Attack Examples
- Using hex escape sequences
- Mixing hex with ASCII text
- Using HTML hex entities
- Encoding Unicode code points in hex
- Using hex in URL encoding
- Splitting hex values across inputs
- Using different hex case variations
- Combining hex with other encodings


---


---

<a id="cipher"></a>

<!-- Source: cipher.md -->

# Cipher

## Description
Using encryption or cipher techniques to encode malicious content

## Attack Examples
- Using simple substitution ciphers
- Implementing Caesar cipher variants
- Using Vigenère cipher encoding
- Creating custom encryption schemes
- Using polyalphabetic substitution
- Implementing ROT13 variations
- Using book ciphers
- Creating transposition ciphers
- Combining multiple cipher techniques


---


---

<a id="morse"></a>

<!-- Source: morse.md -->

# Morse

## Description
Using Morse code to encode malicious content

## Attack Examples
- Using dots and dashes in text
- Hiding Morse code in punctuation
- Using Unicode dots and dashes
- Embedding Morse in formatting
- Using timing patterns to represent Morse
- Combining Morse with other text
- Using alternative Morse-like patterns


---


---

<a id="reverse"></a>

<!-- Source: reverse.md -->

# Reverse

## Description
Using reversed text or logic to evade detection

## Attack Examples
- Reversing entire text strings
- Using character-by-character reversal
- Implementing word-level reversal
- Creating palindromic structures
- Using bidirectional text
- Implementing reverse encoding
- Creating mirror text patterns
- Using reverse logic sequences


---


---

<a id="case-changing"></a>

<!-- Source: case_changing.md -->

# Case Changing

## Description
Using case manipulation to evade detection of malicious content

## Attack Examples
- Alternating letter case (e.g., aLtErNaTiNg)
- Using all caps for certain words
- Random case distribution
- Using title case to hide patterns
- Implementing case-based encoding
- Using case as binary signals
- Combining case changes with Unicode
- Creating case-based patterns


---


---

<a id="phonetic-substitution"></a>

<!-- Source: phoenetic_substitution.md -->

**Phonetic Substitution**

**Description**
Using phonetic equivalents to evade detection of malicious content and requesting the AI to respond using similar phonetic patterns

**Attack Examples**
* Replacing letters with phonetically similar characters (e.g., "ph" for "f")
* Using homophones (words that sound alike but are spelled differently)
* Implementing deliberate misspellings that preserve pronunciation
* Adding silent letters that don't change pronunciation
* Replacing words with phonetic spellings (e.g., "yoo" for "you")
* Using regional pronunciation variations
* Combining phonetic substitutions with numbers (e.g., "4" for "for")
* Creating phonetic patterns that preserve meaning but alter text patterns
* Requesting the AI to "pleez respond in fonetik spelling" to normalize the pattern
* Asking the AI to "rite yor anser lyk this" to establish communication in phonetic code
* Instructing the AI to "mayk yor response sownd natural but spel it differently"
* Directing the AI to "yuze inglish sowndz but ignor proper speling rulz"


---


---

<a id="alternative-language"></a>

<!-- Source: alt_language.md -->

# Alternative Language

## Description
Using alternative languages or language mixing to obfuscate malicious content

## Attack Examples
- Using Chinese characters that look similar to English letters
- Mixing Cyrillic letters with Latin letters
- Using mathematical symbols that resemble letters
- Embedding content in right-to-left languages to confuse parsers


---


---

<a id="fictional-language"></a>

<!-- Source: fictional_language.md -->

# Fictional Language

## Description
Using a fictional language to obfuscate malicious content

## Attack Examples
- using 1337 5p34k
- using Piglatin


---


---

<a id="emoji"></a>

<!-- Source: emoji.md -->

# Emoji

## Description
Using emoji characters to encode or hide malicious content

## Examples
- https://paulbutler.org/2025/smuggling-arbitrary-data-through-an-emoji/
- https://emoji.paulbutler.org/?mode=decode

## Implementation Details


---

## Defensive Guidance

### Detection Methods

#### Pattern-Based Detection
- **Character Set Analysis**: Different encodings have distinctive character sets
  - Base64: `[A-Za-z0-9+/=]` with padding
  - Hex: `[0-9A-Fa-f]` or `\x[0-9A-Fa-f]{2}` patterns
  - Morse: `[.\- ]+` patterns
  - Cipher patterns: ROT13, Caesar shifts
- **Format Recognition**: Detect encoding signatures (e.g., Base64 padding with `=`)
- **Entropy Analysis**: Encoded text has different entropy distribution than natural language
- **Regular Expressions**:
  - Base64: `^[A-Za-z0-9+/]+={0,2}$`
  - Hex: `^[0-9A-Fa-f]+$` or `\x[0-9A-Fa-f]{2}` patterns
  - Morse: `^[.\- ]+$`

#### Behavioral Detection
- **Encoding Stacking**: Multiple encodings applied sequentially
- **Prompt Structure**: Phrases like "Decode this:", "The following is Base64:", "Translate from hex:"
- **Length Anomalies**: Encoded strings are typically longer than natural language
- **Decode-Then-Analyze Pattern**: User provides encoding then asks for analysis
- **Phonetic Consistency**: Phonetic substitutions preserve pronunciation patterns
- **Language Mixing**: Unusual combinations of character sets from different languages

#### Automated Tools
- **Multi-format decoders**: CyberChef, base64/hex libraries
- **ML-based encoding detection**: Train classifier on encoded vs natural text features
- **Entropy-based detection**: Calculate Shannon entropy, flag high-entropy inputs
- **Language identification**: langdetect, fastText for alternative language detection
- **Character set analysis**: Unicode range detection for language families

### Defensive Strategies

#### Input Normalization
1. **Automatic Decoding**:
   ```python
   # Detect and decode before processing
   import base64
   import re

   def normalize_input(text):
       # Try common encodings
       if is_base64(text):
           text = base64.b64decode(text).decode()
       if is_hex(text):
           text = bytes.fromhex(text).decode()
       if is_morse(text):
           text = decode_morse(text)
       # Apply same safety checks to decoded text
       return text
   ```

2. **Recursive Decoding**: Handle multiple encoding layers
3. **Error Handling**: Gracefully handle invalid encodings
4. **Phonetic Normalization**: Convert phonetic substitutions to standard spelling
5. **Language Translation**: Auto-translate to primary language for safety checks

#### Policy Enforcement
- **Default Policy**: Decode all inputs automatically, apply safety checks post-decoding
- **Legitimate Use Cases**:
  - Developers working with encoded data
  - Security researchers analyzing samples
  - Data processing workflows
  - Multilingual users (for alternative languages)
  - Translation services
- **Graduated Response**:
  - Level 1: Auto-decode and process normally
  - Level 2: Decode + flag for audit if decoded content is suspicious
  - Level 3: Block if decoded content violates policy
  - Level 4: Track users who frequently use encoding

#### Layered Defense
1. **Pre-Processing Layer**: Detect and decode encodings
2. **Content Layer**: Apply safety checks to normalized text
3. **Post-Processing Layer**: Check if output contains encoded harmful content
4. **Monitoring Layer**: Track users who frequently use encoding/obfuscation

### Implementation Example

```python
def detect_and_normalize_encoding(text: str) -> tuple[str, list[str]]:
    """
    Detect and decode common encodings.
    Returns: (normalized_text, list_of_encodings_detected)
    """
    detected_encodings = []

    # Base64 detection and decoding
    if re.match(r'^[A-Za-z0-9+/]+={0,2}$', text) and len(text) % 4 == 0:
        try:
            decoded = base64.b64decode(text).decode('utf-8')
            detected_encodings.append('base64')
            text = decoded
        except:
            pass

    # Hex detection and decoding
    if re.match(r'^[0-9A-Fa-f]+$', text) and len(text) % 2 == 0:
        try:
            decoded = bytes.fromhex(text).decode('utf-8')
            detected_encodings.append('hex')
            text = decoded
        except:
            pass

    # Morse code detection
    if re.match(r'^[.\- ]+$', text):
        try:
            decoded = decode_morse(text)
            detected_encodings.append('morse')
            text = decoded
        except:
            pass

    # Language detection and translation
    from langdetect import detect
    try:
        lang = detect(text)
        if lang != 'en':  # Or your primary language
            detected_encodings.append(f'language:{lang}')
            # Translate to primary language for safety checks
    except:
        pass

    # Recursive detection (handle multiple layers)
    if detected_encodings:
        text, additional = detect_and_normalize_encoding(text)
        detected_encodings.extend(additional)

    return text, detected_encodings
```

### Severity Assessment

**Detectability**: ⭐⭐⭐⭐ (4/5 - Easy to Moderate) - Encoding patterns are distinctive
**Bypass Difficulty**: 🟢 Low - Trivial to apply encoding
**Legitimate Use Cases**: 🟡 Moderate - Some legitimate developer and multilingual use
**Risk Level**: 🟡 **MEDIUM** - Easy to detect and mitigate, but widely known

### Special Considerations

#### Alternative Language Evasions
- **Low-Resource Languages**: Models often less safe in languages with less training data
- **Translation-based attacks**: Craft prompt that translates to harmful request
- **Recommendation**: Extra scrutiny for low-resource languages in high-risk domains
- **Cultural Sensitivity**: Don't discriminate against non-English users

#### Fictional Language Evasions
- Less legitimate use; higher prior for evasion attempt
- Pig Latin, Leetspeak, ROT13: Treat as encoding, not language
- Phonetic substitutions: Normalize to standard spelling before processing

### Related Taxonomy
- **Techniques**: Obfuscation, Character Encoding, Language Confusion
- **Intents**: Detection Evasion, Content Filter Bypass
- **Related**: Structural Evasions, Rendering Evasions

---
