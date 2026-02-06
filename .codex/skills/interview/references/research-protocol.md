# Research Protocol

Research is mandatory. The only variable is timing.

## Stage 1: Blocking research (before first challenge question)

Do this before Devil's Advocate starts:
- inspect codebase structure and conventions
- find existing implementation patterns
- verify mentioned technologies against current docs
- identify viable off-the-shelf alternatives

Outcome: you can challenge with evidence, not guesses.

## Stage 2: Parallel research (during partner phase)

While user answers:
- run targeted doc/code lookups in parallel
- verify claims about APIs/libraries
- test feasibility of candidate approaches
- surface findings immediately when relevant

Pattern:
- "While you answered, I verified X and found Y."

## Stage 3: Pre-output verification

Before writing final spec, verify:
- technical claims are current
- APIs and signatures are valid
- dependencies are available and maintained
- recommendations are implementable in this codebase

## Contradiction protocol (hard rule)

If research contradicts a claim:
1. Stop the current interview flow.
2. Surface contradiction with source evidence.
3. Ask user to choose direction.
4. Record in Assumption Corrections.

Never ignore contradictions.

## Scope guide

| Topic | Timing | Method |
|---|---|---|
| Codebase architecture | Blocking | Local repo inspection |
| Existing implementations | Blocking | Local repo inspection |
| Current docs/API behavior | Blocking + Parallel | Web/docs lookup |
| Alternative libraries | Blocking + Parallel | Web/docs lookup |
| Final claim verification | Pre-output | Targeted checks |

## Failure modes

- asking user what research could answer
- relying on stale model memory for APIs
- recommending without checking constraints
- delaying critical findings until the end
