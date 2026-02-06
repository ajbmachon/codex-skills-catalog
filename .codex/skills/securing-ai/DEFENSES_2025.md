# Defense Mechanisms: 2025-2026

Modern defense strategies against prompt injection and AI attacks
Total entries: 8

## Table of Contents

1. [Defense-in-Depth Architecture](#defense-in-depth-architecture)
2. [LLM Salting](#llm-salting)
3. [ARGUS Defense](#argus-defense)
4. [Microsoft Prompt Shields](#microsoft-prompt-shields)
5. [Spotlighting Techniques](#spotlighting-techniques)
6. [Guardrail Solutions](#guardrail-solutions)
7. [Action Gating](#action-gating)
8. [Provenance Tracking](#provenance-tracking)

---

<a id="defense-in-depth-architecture"></a>

# Defense-in-Depth Architecture

## Description
Layered security approach combining prevention, detection, and impact mitigation. No single defense is sufficient against sophisticated prompt injection attacks.

## Architecture layers

### Prevention Layer
- Hardened system prompts with clear boundaries
- Input validation and sanitization
- Constrained model behavior via fine-tuning
- Spotlighting untrusted input

### Detection Layer
- Real-time injection detection (Prompt Shields)
- Content classification (Meta Prompt Guard)
- AI-assisted anomaly detection
- Behavioral analysis and monitoring

### Impact Mitigation Layer
- Data governance and access controls
- Principle of least privilege
- Output sanitization
- Human-in-the-loop for sensitive actions

## Implementation guidance
1. Never rely solely on prompt-based defenses
2. Implement security at architectural/API level
3. Treat LLM-accessible APIs as public endpoints
4. Enforce authentication and rate limiting
5. Limit sensitive data exposure to AI context

## Effectiveness
Research shows layered defenses reduce attack success rates by 60-80% compared to single-layer approaches.

---

<a id="llm-salting"></a>

# LLM Salting

## Description
Lightweight fine-tuning technique inspired by cryptography that applies targeted rotation to the model's "refusal direction," invalidating precomputed jailbreak prompts.

## Origin
Developed by Sophos (October 2025)

## Why it works
- Jailbreaks are optimized against specific model weights
- Salting changes the model's internal representation of refusal
- Attackers must recompute attacks for each deployment
- Minimal impact on model utility

## Implementation
1. Identify the model's "refusal direction" in activation space
2. Apply controlled rotation to this direction
3. Fine-tune on safety dataset to maintain alignment
4. Deploy salted model variant

## Benefits
- Forces attackers to recompute for each deployment
- Can be rotated periodically
- Minimal overhead compared to full fine-tuning
- Complementary to other defenses

## Limitations
- Requires access to model weights (not for API-only use)
- May need periodic re-salting
- Does not prevent all attack types

---

<a id="argus-defense"></a>

# ARGUS Defense

## Description
Defense mechanism against multi-modal indirect prompt injection that steers the model's instruction-following behavior in activation space by exploiting the "safety subspace" in model internals.

## Origin
Academic research (2025)

## How it works
1. Identifies activation patterns associated with instruction-following
2. Locates "safety subspace" where legitimate vs. malicious instructions differ
3. Projects activations onto safety subspace during inference
4. Suppresses activations that indicate malicious instruction-following

## Target attacks
- Image-based prompt injection
- Audio-based prompt injection
- Document-embedded instructions
- Multi-modal adversarial inputs

## Implementation requirements
- Access to model internals (activations)
- Pre-computed safety subspace vectors
- Inference-time intervention capability

## Effectiveness
Reduces multi-modal injection success rates by 70-85% in research benchmarks.

---

<a id="microsoft-prompt-shields"></a>

# Microsoft Prompt Shields

## Description
Real-time prompt injection detection service from Microsoft Azure AI Content Safety, providing both user prompt and document attack detection.

## Components

### User Prompt Attack Detection
Analyzes user inputs for direct injection attempts targeting:
- System prompt extraction
- Jailbreaking attempts
- Role manipulation
- Instruction override

### Document Attack Detection
Scans documents and retrieved content for:
- Embedded malicious instructions
- Hidden commands in PDFs, images, HTML
- Indirect prompt injection in RAG pipelines

## Integration
```
Azure AI Content Safety API
POST /contentsafety/text:shieldPrompt
{
  "userPrompt": "...",
  "documents": ["..."]
}
```

## Response
Returns attack likelihood scores and specific attack type classification.

## Deployment
- Available as Azure service
- Can be integrated into pre-processing pipeline
- Supports multiple languages

---

<a id="spotlighting-techniques"></a>

# Spotlighting Techniques

## Description
Methods to clearly delimit untrusted input from system instructions, making it harder for injected content to be interpreted as commands.

## Technique variants

### Datamarking
Insert special markers around untrusted content:
```
<UNTRUSTED_DATA>
{user_input}
</UNTRUSTED_DATA>
```

### Delimiting
Use consistent delimiters that the model learns to recognize:
```
###USER_INPUT_START###
{content}
###USER_INPUT_END###
```

### Encoding
Transform untrusted content to reduce instruction-following:
```
Base64 encode user input
Instruct model to decode before processing
```

### Sandboxing
Isolate untrusted content in separate context:
```
Process untrusted content with restricted model
Pass only extracted data to main model
```

## Best practices
1. Use unique, uncommon delimiters
2. Reinforce boundaries in system prompt
3. Validate delimiter integrity before processing
4. Combine with other defenses

## Limitations
- Sophisticated attacks can escape delimiters
- Not effective against all injection types
- Requires consistent implementation

---

<a id="guardrail-solutions"></a>

# Guardrail Solutions

## Description
Dedicated tools and services that provide input/output validation, content filtering, and safety enforcement for LLM applications.

## Solution comparison

| Solution | Provider | Key Features | Cost |
|----------|----------|--------------|------|
| Azure AI Content Safety | Microsoft | Prompt shields, content filters | Pay-per-use |
| Amazon Bedrock Guardrails | AWS | Denied topics, PII detection, word filters | Included |
| Checks Guardrails API | Google | Safety policy scoring | Pay-per-use |
| LLM Guard | Open Source | Input/output validation, extensive checks | Free |
| NeMo Guardrails | NVIDIA | Programmable safety rails, dialog management | Free/Enterprise |
| Lakera Guard | Lakera | Real-time protection, low latency | SaaS pricing |
| Prompt Armor | Third Party | Injection detection | SaaS pricing |

## Selection criteria
1. Latency requirements (real-time vs. batch)
2. Deployment model (cloud vs. self-hosted)
3. Customization needs
4. Integration complexity
5. Cost at scale

## Implementation pattern
```
User Input → Guardrail Check → LLM → Guardrail Check → Output
```

---

<a id="action-gating"></a>

# Action Gating

## Description
Independent authorization check for each tool or action the AI attempts to execute, preventing unauthorized operations even if the model is compromised.

## Implementation

### Per-action authorization
```python
def execute_tool(tool_name, params, user_context):
    if not authorize(user_context, tool_name, params):
        raise UnauthorizedAction()
    return tool.execute(params)
```

### Capability-based access
```python
capabilities = get_user_capabilities(user_id)
allowed_tools = filter_tools_by_capabilities(all_tools, capabilities)
```

### Risk-based gating
```python
risk_score = assess_action_risk(tool_name, params)
if risk_score > threshold:
    require_human_approval()
```

## Best practices
1. Default deny for all actions
2. Explicit allow-list per user/role
3. Log all action attempts
4. Separate authorization from execution
5. Rate limit sensitive actions

## Effectiveness
Reduces impact of successful prompt injection by 90%+ by limiting what compromised models can do.

---

<a id="provenance-tracking"></a>

# Provenance Tracking

## Description
Marking and tracking the origin of all content in the AI context to distinguish trusted system instructions from untrusted external data.

## Implementation approaches

### Content tagging
```json
{
  "content": "user message",
  "provenance": {
    "source": "user_input",
    "trust_level": "untrusted",
    "timestamp": "2025-01-21T08:00:00Z"
  }
}
```

### Separate context windows
```
System context: [trusted instructions only]
User context: [user input, tool outputs]
```

### Tool output labeling
```
<TOOL_OUTPUT source="web_search" trust="low">
{search_results}
</TOOL_OUTPUT>
```

## Trust levels
- **Trusted**: System prompts, verified internal data
- **Semi-trusted**: Authenticated user input
- **Untrusted**: External data, tool outputs, retrieved content

## Best practices
1. Label all content at ingestion
2. Propagate provenance through processing
3. Apply different policies based on trust level
4. Audit provenance for anomalies

## Integration with other defenses
Provenance tracking enables:
- Risk-aware action gating
- Targeted spotlighting
- Audit trail for incident response

---

## Defense Selection Guide

### For chatbots (no tools)
- Spotlighting + Guardrails + Content filtering

### For agentic systems (with tools)
- Action Gating + Provenance Tracking + Guardrails + Human-in-the-loop

### For RAG applications
- Document scanning + Spotlighting + Output validation

### For high-security environments
- All layers + LLM Salting (if possible) + ARGUS (for multi-modal)

---

## Sources

- Microsoft MSRC: Indirect Prompt Injection Defenses (July 2025)
- Sophos: LLM Salting Defense (October 2025)
- OWASP Prompt Injection Prevention Cheat Sheet
- Academic research on ARGUS (2025)
- Vendor documentation for guardrail solutions

---
