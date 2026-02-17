---
name: prompt-craft
description: Improve prompt quality through deterministic modes: analyze existing prompts, craft new prompts from requirements, teach prompting techniques, or apply fast high-impact prompt edits with model-aware adjustments. Use when the user asks to write, refine, critique, or explain prompts for LLM tasks or subagents.
---

# Prompt Craft

Use this skill to build better prompts with deterministic routing, concise execution, and model-aware adjustments.

## Modes And Commands

- `A` Analyze: critique an existing prompt
- `B` Craft: build a new prompt from requirements
- `C` Teach: explain one technique deeply
- `D` Quick Fix: fast 3-change improvement pass
- `*model <name>`: apply model-specific guidance from `reference/models.md`
- `*help`: show mode menu

## Mode Router

Route directly when intent is clear:
- User provides a prompt to improve -> Mode A
- User asks to create a prompt -> Mode B
- User asks how a technique works -> Mode C
- User asks for a fast cleanup -> Mode D

If ambiguous, show the menu and ask one routing question.

## Required Context (Minimal)

Use one short question round before Mode B (and optionally Mode A):
- Task goal
- Target model (or "general")
- Required output format
- Hard constraints

If user asks for speed, proceed with caveats.

## Technique Reference Map

Load technique files only when needed:
- `reference/chain-of-thought.md`
- `reference/structured-output.md`
- `reference/few-shot.md`
- `reference/placement.md`
- `reference/salience.md`
- `reference/roles.md`
- `reference/positive-framing.md`
- `reference/reasoning-first.md`
- `reference/verbalized-sampling.md`
- `reference/self-reflection.md`
- Extended techniques: `reference/extended.md`
- Model-specific guidance: `reference/models.md`

## Mode A: Analyze

Process:
1. Read the prompt exactly as written.
2. Score core techniques as `present`, `partial`, `missing`, or `n/a`.
3. Pick top 3 highest-impact improvements.
4. Provide before/after snippets for each.
5. Output optimized full prompt.

Output contract:
- Prompt snapshot
- Technique scorecard
- Top 3 improvements
- Optimized prompt
- Quality summary

## Mode B: Craft

Process:
1. Gather minimal requirements (one question round).
2. Select techniques based on task type.
3. Draft prompt with explicit output contract.
4. Run self-check for ambiguity and missing constraints.
5. Output final prompt + brief rationale.

Output contract:
- Requirements understood
- Techniques applied
- Final prompt
- Short rationale
- Quality summary

## Mode C: Teach

Process:
1. Confirm one technique.
2. Load its reference file.
3. Explain mechanism, when to use, pitfalls, and examples.
4. End with one practical exercise.

Output contract:
- Technique
- Mechanism
- Use / avoid cases
- Common mistakes
- Practice exercise

## Mode D: Quick Fix

Process:
1. Read prompt.
2. Apply top 3 high-impact edits.
3. Return improved prompt with one-line change notes.

Prioritize speed over depth.

Output contract:
- 3 changes made
- Improved prompt
- Optional suggestion to run Mode A for deeper pass

## Model-Specific Adjustments

When a target model is specified, load `reference/models.md` and apply only relevant adjustments.
If no model is specified, keep guidance model-agnostic.

## Output Summary

End every mode with:

```
QUALITY SUMMARY
• Mode: [A/B/C/D]
• Confidence: [High / Medium / Low]
• Main gain: [clarity / compliance / reasoning / robustness]
• Next step: [optional]
```

Optional JSON block when requested:

```json
{
  "mode": "A",
  "confidence": "medium",
  "changes": ["..."],
  "next_step": "..."
}
```

## Checklist

- [ ] Routed to correct mode (or asked one routing question)
- [ ] Loaded only necessary references
- [ ] Gathered minimal required context for Mode B
- [ ] Produced deterministic output contract
- [ ] Applied model-specific guidance only when model is known
