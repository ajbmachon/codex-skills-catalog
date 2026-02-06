---
name: securing-ai
description: Tests AI systems for security vulnerabilities using red team attacks, blue team defense assessments, and educational deep-dives. Use when red teaming AI, assessing AI defenses, testing prompt injection, auditing LLM security, or learning about AI attack patterns.
---

# Prompt Injection Security Testing

For authorized security testing and defense improvement only.

## Modes And Commands

- `A` Red Team: generate safe test plans for authorized targets
- `B` Blue Team: assess defenses and prioritize mitigations
- `C` Learn: explain attack/defense concepts
- `D` Quick Probe: fast baseline prompt-injection checks
- `*intents`, `*techniques`, `*evasions`, `*help`

## Authorization Gate (Mandatory For Mode A)

Before any offensive testing guidance, confirm:
1. System owner
2. Explicit test scope (systems/environments)
3. Allowed time window
4. Allowed actions and exclusions

If any field is missing, do not provide offensive testing plans. Switch to Mode B or Mode C.

## Mode Router

Route directly when intent is clear:
- "test/attack/try" + target -> Mode A
- "defend/protect/assess" -> Mode B
- "what is/how does" -> Mode C
- "quick prompts" -> Mode D

If ambiguous, ask one routing question.

## Reference Loading (Scenario-Based)

Load only scenario-relevant files:
- Chatbots: `TECHNIQUES_PROMPT_MANIPULATION.md`, `INTENTS_RECONNAISSANCE.md`, `INTENTS_EXPLOITATION.md`
- Agentic systems: `TECHNIQUES_AGENTIC.md`, `INTENTS_ADVANCED.md`, `INTENTS_EXPLOITATION.md`
- MCP-connected systems: `INTENTS_MCP_SECURITY.md`, `TECHNIQUES_AGENTIC.md`, `OWASP_AGENTIC_TOP10.md` (added 2026)
- Business abuse/fraud: `INTENTS_BUSINESS.md`, `TECHNIQUES_PROMPT_MANIPULATION.md`
- Evasions: `EVASIONS_ENCODING.md`, `EVASIONS_STRUCTURAL.md`, `EVASIONS_RENDERING.md`, `EVASIONS_IDENTITY.md`
- Modern defenses: `DEFENSES_2025.md` (added 2025), `OWASP_AGENTIC_TOP10.md`
- Quick baseline prompts: `COMMON_TEST_PROMPTS.md`

## Mode A: Red Team (Authorized Only)

Process:
1. Confirm authorization gate fields.
2. Profile target capabilities, trust boundaries, and likely attacker goals.
3. Select intent + technique references by scenario.
4. Generate safe, non-weaponized test prompts (5-10) with expected failure signals.
5. Capture findings with severity, evidence, and reproduction notes.
6. Provide corresponding mitigations for each finding.

Output contract:
- Target profile
- Test set grouped by intent
- Findings table
- Mitigation plan
- Risk summary

## Mode B: Blue Team

Process:
1. Inventory inputs, tools, data access, and side-effect actions.
2. Map attack surface using relevant intent files.
3. Audit controls: input handling, output filtering, action gating, provenance, monitoring.
4. Identify gaps and prioritize fixes by risk and feasibility.

Output contract:
- Attack surface summary
- Defense audit table
- Prioritized recommendations
- Risk summary with owner assignment

## Mode C: Learn

Process:
1. Confirm one topic (intent, technique, evasion, or framework).
2. Load the relevant reference file.
3. Explain what it is, why it works, examples, and defenses.

Output contract:
- Topic
- Mechanism
- Example patterns
- Defensive countermeasures
- Related references

## Mode D: Quick Probe

Process:
1. Ask target type in one question.
2. Load `COMMON_TEST_PROMPTS.md`.
3. Return 10 baseline prompts spanning leak, override, enumeration, extraction, and boundary tests.

Output contract:
- 10 baseline tests
- What to observe for pass/fail
- Recommendation for deeper Mode A/B follow-up

## Safe Output Rules

- Never provide exploit optimization playbooks.
- Keep examples as defensive test patterns, not weaponized instructions.
- Always pair discovered weakness with mitigations.
- Refuse offensive guidance when authorization is missing.

## Output Summary

End with:

```
QUALITY SUMMARY
• Mode: [A/B/C/D]
• Coverage: [N test intents or control layers]
• Confidence: [High / Medium / Low]
• Highest risk: [critical finding or primary gap]
```

Optional structured block when requested:

```json
{
  "mode": "B",
  "highest_risk": "...",
  "recommendations": ["..."],
  "confidence": "medium"
}
```

## Checklist

- [ ] Routed mode or asked one routing question
- [ ] Enforced authorization gate for Mode A
- [ ] Loaded only relevant references
- [ ] Kept output non-weaponized
- [ ] Included mitigations and quality summary
