# Attack Evasions: Rendering & Preprocessing

Rendering layer and preprocessing evasions
Total entries: 6

## Table of Contents

1. [Render-Layer Smuggling (Rich Text / Hidden Links / Invisible Instructions)](#render-layer-smuggling-rich-text-hidden-links-invisible-instructions)
2. [Link Smuggling](#link-smuggling)
3. [Metadata-Only Visibility](#metadata-only-visibility)
4. [Preprocessing-Triggered Payloads](#preprocessing-triggered-payloads)
5. [Steganography](#steganography)
6. [Waveforms/Frequencies](#waveformsfrequencies)

---

<a id="render-layer-smuggling-rich-text-hidden-links-invisible-instructions"></a>

<!-- Source: render_layer_smuggling.md -->

# Render-Layer Smuggling (Rich Text / Hidden Links / Invisible Instructions)

## Description
Evasion where malicious instructions hide in rendering layers:
- invisible text (CSS, font size, color match)
- hidden hyperlinks / misleading anchor text
- markup tricks that change what user sees vs what model ingests

## Defensive notes
- flatten rich text to canonical representation before scanning
- strip or proxy external links/resources
- safe rendering defaults (treat output as hostile)


---


---

<a id="link-smuggling"></a>

<!-- Source: link_smuggling.md -->

# Link Smuggling

## Description
Using URL or link manipulation to hide malicious content

## Examples
- https://x.com/mbrg0/status/1838217987104665985

## Implementation Details


---


---

<a id="metadata-only-visibility"></a>

<!-- Source: metadata_only_visibility.md -->

# Metadata-Only Visibility

## Description
Evasion where malicious instructions are placed in content that is visible to the
model but not to the end user or reviewer, such as:
- tool descriptions not displayed in UI
- hidden schema fields
- truncated metadata panes

## Defensive notes
- ensure reviewers can view the same content the model sees
- diff and audit metadata changes
- treat metadata as untrusted and sanitize/validate it


---


---

<a id="preprocessing-triggered-payloads"></a>

<!-- Source: preprocessing_triggered_payloads.md -->

# Preprocessing-Triggered Payloads

## Description
Evasion where content becomes malicious only after transformations:
- image scaling/resampling
- compression artifacts
- OCR pipelines
- formatting flattening

## Defensive notes
- log and display the exact post-processed input
- standardize transforms and test them
- require confirmation before sensitive tool calls from transformed inputs


---


---

<a id="steganography"></a>

<!-- Source: stego.md -->

# Steganography

## Description
Using steganographic techniques to hide malicious content within seemingly innocent data

## Attack Examples
- Hiding prompts in image LSB (Least Significant Bit)
- Using invisible watermarks in images
- Embedding text in audio frequency ranges
- Using color variations to encode messages
- Hiding data in file metadata
- Using timing or spacing between elements to encode information


---


---

<a id="waveformsfrequencies"></a>

<!-- Source: waveforms.md -->

# Waveforms/Frequencies

## Description
Using audio or signal-based techniques to encode malicious content

## Attack Examples
- Encoding text in audio frequencies
- Using ultrasonic carriers for data
- Hiding data in audio spectrograms
- Manipulating wave phase to encode information
- Using frequency modulation techniques
- Embedding data in audio harmonics
- Creating visual waveform patterns
- Using audio watermarking techniques


---

## Defensive Guidance

### Detection Methods

#### Rendering Analysis
- **Rich Text Inspection**: Detect CSS/style-based hiding (font-size:0, color match, visibility:hidden)
- **Link Analysis**:
  - Check for anchor text vs URL mismatch
  - Detect misleading link descriptions
  - Identify shortened/obfuscated URLs
- **Metadata Extraction**: Compare visible content vs metadata content
- **Preprocessing Pipeline Monitoring**: Track transformations applied to inputs
  - Image scaling/resampling
  - Compression artifacts
  - OCR pipeline outputs
  - Format conversions

#### Behavioral Detection
- **User-Model Content Divergence**: Content shown to user differs from content sent to model
- **Preprocessing Anomalies**: Input changes significantly after preprocessing
- **Hidden Layer Indicators**:
  - Invisible text spans
  - Zero-size elements
  - Color-matched text/background
  - CSS display:none or visibility:hidden
- **Steganographic Patterns**:
  - LSB (Least Significant Bit) patterns in images
  - Frequency-domain hiding in audio
  - Timing patterns in waveforms
  - Metadata container anomalies

#### Automated Tools
- **Rich Text Sanitizers**: Strip styling, flatten to plain text
- **Link Validators**: Expand and verify URLs
- **Image Analysis**: LSB extraction, visual similarity checks
- **Audio Analysis**: Spectrogram analysis, frequency decomposition
- **OCR Testing**: Test OCR pipeline with adversarial samples
- **Metadata Viewers**: Display ALL metadata visible to model

### Defensive Strategies

#### Content Sanitization

1. **Rich Text Flattening**:
   ```python
   from bs4 import BeautifulSoup

   def flatten_rich_text(html_content):
       """Strip all formatting, extract only visible text."""
       soup = BeautifulSoup(html_content, 'html.parser')

       # Remove invisible elements
       for tag in soup.find_all(style=re.compile(r'display:\s*none|visibility:\s*hidden')):
           tag.decompose()

       # Extract text only
       return soup.get_text(separator=' ', strip=True)
   ```

2. **Link Sanitization**:
   ```python
   def sanitize_links(content):
       """Expand and verify all links, proxy external resources."""
       # Expand shortened URLs
       # Check for anchor text vs URL mismatch
       # Replace with safe proxy links
       # Log suspicious link patterns
       return sanitized_content
   ```

3. **Preprocessing Consistency**:
   ```python
   def log_preprocessing_transforms(original, processed):
       """Log exact transformations applied during preprocessing."""
       # Track image resampling
       # Log OCR conversions
       # Monitor compression changes
       # Alert on significant divergence
       return processed
   ```

#### Policy Enforcement

- **Safe Rendering Defaults**:
  - Treat all output as potentially hostile
  - Strip HTML/CSS by default
  - Display plain text unless explicitly rich format needed
  - Sandbox any rendered content
- **Link Handling**:
  - Proxy all external links through safety checker
  - Display full URL alongside anchor text
  - Warn users before following external links
- **Metadata Visibility**:
  - Display ALL metadata to reviewers
  - Audit metadata changes
  - Treat metadata as untrusted input
- **Preprocessing Requirements**:
  - Display post-processed input to users
  - Require confirmation for sensitive actions after transformations
  - Standardize and test all preprocessing pipelines

#### Layered Defense

1. **Canonicalization Layer**: Convert all inputs to canonical plain text representation
2. **Content Extraction Layer**: Extract text from images, audio, rich formats
3. **Validation Layer**: Apply safety checks to extracted content
4. **Display Layer**: Show users the SAME content the model sees
5. **Monitoring Layer**: Track rendering/preprocessing anomalies

### Implementation Example

```python
def normalize_rendering_evasions(content, content_type='text/html'):
    """
    Detect and neutralize rendering-based evasions.
    """
    normalized = content
    alerts = []

    # Rich text handling
    if content_type in ['text/html', 'text/markdown']:
        # Flatten to plain text
        normalized = flatten_rich_text(content)
        alerts.append('rich_text_flattened')

    # Link sanitization
    if contains_links(content):
        normalized = sanitize_links(normalized)
        alerts.append('links_sanitized')

    # Metadata extraction
    metadata = extract_metadata(content)
    if metadata and differs_from_content(normalized, metadata):
        alerts.append('metadata_divergence')
        # Include metadata in safety checks
        normalized = f"{normalized} [METADATA: {metadata}]"

    # Steganography detection
    if is_image(content):
        extracted = analyze_image_steganography(content)
        if extracted:
            alerts.append('steganography_detected')
            normalized = f"{normalized} [HIDDEN: {extracted}]"

    return normalized, alerts

def ensure_preprocessing_transparency(input_data):
    """
    Log and display preprocessing transformations.
    """
    original = input_data

    # Apply preprocessing (OCR, scaling, etc.)
    processed = apply_preprocessing(input_data)

    # Log the transformation
    log_transform(original, processed)

    # Display post-processed version to user
    display_to_user(processed, label="Content after preprocessing")

    return processed
```

### Severity Assessment

**Detectability**: ⭐⭐⭐ (3/5 - Moderate to Hard) - Requires multi-modal analysis
**Bypass Difficulty**: 🟡 Medium - Requires formatting knowledge or steganography tools
**Legitimate Use Cases**: ⭐⭐⭐⭐ (4/5 - Common) - Rich text, links, and images are standard
**Risk Level**: 🟠 **MEDIUM-HIGH** - Hard to detect, significant user-model divergence

### Special Considerations

#### Render-Layer Smuggling
- **Invisible Text**: CSS tricks making text invisible to users but visible to models
- **Font-Size Zero**: Text with font-size:0 or very small sizes
- **Color Matching**: Text color matches background color
- **Defense**: Always flatten rich text to canonical representation

#### Metadata-Only Visibility
- **Tool Descriptions**: Malicious instructions in tool metadata not shown to users
- **Hidden Schema Fields**: Content in fields not displayed in UI
- **Truncated Panes**: Metadata truncated in display but fully sent to model
- **Defense**: Ensure reviewers see SAME content as model

#### Preprocessing-Triggered Payloads
- **Image Resampling Attacks**: Content appears after image scaling
- **OCR Vulnerabilities**: Text extracted differently than displayed
- **Compression Artifacts**: Malicious patterns emerge after compression
- **Defense**: Display post-processed content, standardize transforms

#### Steganography
- **LSB Image Hiding**: Instructions in image least significant bits
- **Audio Frequency Hiding**: Content in specific frequency ranges
- **Waveform Patterns**: Visual patterns in spectrograms
- **Defense**: Multi-modal extraction and analysis of hidden channels

### Related Taxonomy
- **Techniques**: Content Hiding, Steganography, Format Abuse, Preprocessing Exploitation
- **Intents**: Detection Evasion, User Deception
- **Related**: Structural Evasions, Metadata-Only Visibility, Link Smuggling

---
