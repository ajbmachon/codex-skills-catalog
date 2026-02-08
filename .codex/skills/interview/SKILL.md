---
name: interview
description: Run a structured interview that turns rough ideas into implementation-ready specs through challenge, constraint capture, and verification.
---

# Interview Skill (Codex Operator Mode)

Use this skill to convert ambiguous requests into build-ready specs with explicit constraints, decisions, and verification.

## Trigger

Use when user asks for:
- spec, requirements, planning, architecture direction
- help fleshing out a feature or system
- interview-style discovery before implementation

## Quick Start (first 5 actions)

1. Read `references/role-evolution.md` and `references/quality-criteria.md`.
2. Create working log from `templates/working-log.md`.
3. Run blocking research per `references/research-protocol.md`.
4. Enter Devil's Advocate and challenge viability.
5. Capture and confirm Constraint Registry before partner mode.

## Core mode shifts

- Phase 1-2: Challenger
- Goal: prove the idea should exist and is scoped correctly.

- Transition: Constraint capture
- Goal: lock hard/soft constraints and boundaries with explicit user confirmation.

- Phase 3+: Partner
- Goal: refine implementation details without violating constraints.

## Workflow

### Phase 0: Initialize log

Read `templates/working-log.md`. If file creation is appropriate for the workspace, create `./interview-log-{topic}.md` (or user path); otherwise keep an in-response running log with the same structure. Start logging immediately.

### Phase 1: Blocking research

Read `references/research-protocol.md` and complete blocking research before first interview questions:
- codebase patterns and existing solutions
- current docs for mentioned technologies
- alternatives already available

Log findings in working log.

### Phase 2: Devil's Advocate

Challenge hard:
- should this exist?
- why this approach vs alternatives?
- most likely failure mode?
- scope mismatch risk?

Do not soften challenges. Cite research.

### Transition: Constraint Registry (mandatory gate)

Read `references/constraint-store.md`.
Extract and classify:
- Hard constraints (immutable)
- Soft constraints (preferences)
- Boundaries (out of scope)

Surface registry and get explicit confirmation before moving on.

### Phase 3: Partner interview

Read:
- `references/question-guidelines.md`
- `references/verification-gate.md`
- `references/self-challenge.md`

Ask direct grouped questions (1-4 per round, usually fewer as interview converges).
Keep questions practical: default to one-sentence questions, add brief context/options only when needed for a real decision.
For framework/architecture choices, include short option baselines (what it is, key upside, key downside) before asking for a decision.
Run parallel research between rounds and surface findings as they arrive.

After each exchange, update working log:
- Q&A entry
- new constraints
- decisions
- assumption corrections

**Exit criteria for interview rounds (mandatory):**
- Core constraints are explicit and confirmed
- Success criteria are measurable
- Main implementation approach has no unresolved contradictions
- Remaining open questions are non-blocking or explicitly deferred

### Phase 4: Contradiction protocol

If research contradicts user claims:
1. Stop flow.
2. Surface contradiction with evidence.
3. Request explicit decision.
4. Record correction in log/spec.

Never silently continue.

### Phase 5: Verification loop

Before final output:
- quote user intent back
- re-check all recommendations against constraints
- verify claims and APIs against current docs
- identify gaps/open questions

### Phase 6: Spec output

Before drafting, read required templates:
- `templates/base-block.md`
- `templates/interview-record.md`
- `templates/assumption-corrections.md`
- `templates/constraint-registry.md`

Add conditional templates only when needed:
- `templates/edge-cases.md`
- `templates/tradeoffs.md`
- `templates/open-questions.md`
- `templates/tdd-block.md`
- `templates/code-examples.md`

Spec should be implementation-ready for another Codex run without follow-up clarification.

## Fast Mode (low-stakes)

Use when stakes/complexity are low.

- One short challenge round
- Minimal blocking research
- Constraint capture (still required)
- 1-2 interview rounds
- concise spec with required sections only
- avoid overlong prompts, but do not leave decisions under-explained

Do not skip contradiction handling or constraint verification.

## Output minimum

Always include:
- Problem Statement
- Objective
- Success Criteria
- Constraint Registry
- Interview Record
- Decisions
- Assumption Corrections (if any)

## Execution checklist

- [ ] Read mandatory references
- [ ] Create working log
- [ ] Complete blocking research
- [ ] Challenge viability
- [ ] Capture + confirm constraints
- [ ] Run partner interview with verification gate
- [ ] Handle contradictions explicitly
- [ ] Run final verification loop
- [ ] Build spec from templates
- [ ] Mark log COMPLETE

## Non-negotiables

1. Constraint confirmation is a hard gate.
2. Research before recommendations.
3. No silent assumptions; surface them.
4. Log progressively, not at the end.
5. Keep decisions traceable to evidence.
