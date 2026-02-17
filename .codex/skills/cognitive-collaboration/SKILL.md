---
name: cognitive-collaboration
description: Twelve structured thinking modes for decision stress-testing, blind-spot discovery, and option generation (for example red-team, pre-mortem, assumptions, scenarios, values, synthesis). Use when the user asks to poke holes, challenge a plan, pressure-test tradeoffs, explore alternatives, or asks what they are missing in a decision.
---

# Cognitive Collaboration

Use this skill to stress-test decisions and expand options with targeted, mode-specific analysis.

## Mode Router

Route directly when intent is clear. Show menu only when ambiguous or user asks `*help`.

| # | Mode | File | Core Question |
|---|------|------|---------------|
| 1 | Red Team | [red-team.md](reference/red-team.md) | How would critics destroy this? |
| 2 | Steelman | [steelman.md](reference/steelman.md) | What is the strongest case against me? |
| 3 | Pre-Mortem | [pre-mortem.md](reference/pre-mortem.md) | Why did this fail from the future? |
| 4 | Assumptions | [assumptions.md](reference/assumptions.md) | What am I taking for granted? |
| 5 | Biases | [biases.md](reference/biases.md) | Where am I fooling myself? |
| 6 | First Principles | [first-principles.md](reference/first-principles.md) | If I restart from zero, what changes? |
| 7 | Analogist | [analogist.md](reference/analogist.md) | What outside patterns apply here? |
| 8 | Scenario Weaver | [scenario-weaver.md](reference/scenario-weaver.md) | Which futures should I prepare for? |
| 9 | Perspective Shifter | [perspective-shifter.md](reference/perspective-shifter.md) | How do stakeholders see this differently? |
| 10 | Synthesizer | [synthesizer.md](reference/synthesizer.md) | What throughline connects the signals? |
| 11 | Option Generator | [option-generator.md](reference/option-generator.md) | What alternatives are missing? |
| 12 | Values Clarifier | [values-clarifier.md](reference/values-clarifier.md) | What values are actually driving this? |

Always load the selected reference file before execution.

## Commands

- `1-12`: run a mode
- `*chain a,b,c`: run a sequence (example: `*chain 4,1,3`)
- `*quick`: one fast critical question
- `*skip`: skip context questions
- `*single`: force single-variant response
- `*help`: show menu

## Execution Contract

1. Route mode:
   If user intent maps clearly, pick mode and proceed.
   If ambiguous, show menu and suggest 1-2 likely modes.
2. Gather context:
   Default to one short round (2-3 questions).
   Critique modes: subject + stakes + mode-specific field.
   Expansion modes: subject + constraints + mode-specific field.
   If user uses `*skip` or asks for speed, proceed with explicit caveats.
   Use [context-gathering.md](reference/context-gathering.md) for mode-specific prompts.
3. Execute selected mode:
   Follow the selected reference file process exactly.
4. Decide synthesis:
   For chained or complex requests, provide cross-mode synthesis.
5. Close with output contract below.

## Quick Mode

When user asks for speed, ask:
"What is the one assumption that, if wrong, breaks this entire plan?"

Then return one concise analysis and offer full-mode expansion.

## Chaining

Recommended presets:
- Full stress test: `4,1,3`
- Opposition analysis: `2,1`
- Launch prep: `3,1`
- Expansion sprint: `11,7,10`
- Values check: `12,4,6`

Chain output must include:
- Top 3 risks
- Key blind spots
- Recommended actions

## Verbalized Sampling (Conditional)

Use multi-variant output only when one is true:
- user requests alternatives or breadth
- stakes are high and uncertainty is material
- mode naturally benefits from divergent exploration

Default variants: 2-3. Include one tail insight when useful.
Skip VS when user uses `*single` or request is straightforward.

## Output Contract

Every response ends with:

```
QUALITY SUMMARY
• Depth: [Deep / Standard / Quick]
• Confidence: [High / Medium / Low]
• Specificity: [Tailored / Generic]
• Follow-up: [Mode or action]
```

Optional structured block when requested:

```json
{
  "mode": "assumptions",
  "depth": "standard",
  "confidence": "medium",
  "top_risks": ["..."],
  "actions": ["..."]
}
```

## Tone Rules

- Match directness to stakes and sensitivity.
- Stay clear, concrete, and non-theatrical.
- If unsure, start measured.
- Never hide uncertainty in the quality summary.

## Activation Guardrails

Activate when user asks to challenge, stress-test, or broaden a decision.
Do not activate for pure factual lookup, pure encouragement, or early unconstrained brainstorming.

## Checklist

- [ ] Routed to a clear mode or asked one routing question
- [ ] Loaded selected mode reference file
- [ ] Gathered minimum required context (or documented caveat)
- [ ] Executed mode process, not generic advice
- [ ] Used VS only when justified
- [ ] Ended with quality summary
