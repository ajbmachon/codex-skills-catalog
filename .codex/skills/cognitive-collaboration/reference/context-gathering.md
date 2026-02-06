# Context Gathering Protocol

Mandatory context collection before any cognitive mode execution.

## Table of Contents

1. [Why This Matters](#why-this-matters)
2. [Form-Based Gathering](#form-based-gathering)
3. [Text-Based Fallback](#text-based-fallback)
4. [Required Context by Mode](#required-context-by-mode)
5. [Question Templates](#question-templates)
6. [Skip Conditions](#skip-conditions)
7. [Multi-Round Protocol](#multi-round-protocol)

---

## Why This Matters

**The Assumption Problem:** Claude's helpful instinct is to proceed with "reasonable inferences" when context is incomplete. In cognitive analysis, this backfires catastrophically:

- Generic insights replace targeted analysis
- Claude's assumptions may be completely wrong for YOUR situation
- The most valuable insights come from understanding YOUR specific context
- Assumptions about stakes, constraints, and stakeholders lead to irrelevant output

**The Solution:** Gather context BEFORE analysis. Every time. No exceptions unless explicitly skipped.

---

## Form-Based Gathering

**When:** Claude Code environment with AskUserQuestion tool available.

**How it works:**
1. Claude presents 2-4 targeted questions as an interactive form
2. User sees all questions at once
3. User answers efficiently in one interaction
4. If critical fields remain empty, Claude asks follow-up round
5. Process continues until required context is complete

**Benefits:**
- User sees the full scope upfront
- Faster than back-and-forth text
- Clear structure reduces ambiguity
- Multiple rounds feel natural, not nagging

---

## Text-Based Fallback

**When:** Outside Claude Code (API, other interfaces) where forms aren't available.

**How it works:**
1. Claude presents numbered questions in text
2. User replies with answers (by number or inline)
3. Claude acknowledges answers and asks follow-ups if needed
4. Same thoroughness, different format

**Template:**
```
Before I proceed with [MODE], I need to understand your specific situation:

1. **Subject**: [Mode-specific question about what to analyze]
2. **Stakes**: What's riding on this? Why does it matter?
3. **[Mode-specific]**: [Additional required question]
4. **Constraints**: Anything off the table or must be preserved?

Please answer these—or say "*skip" to proceed with my best guesses.
```

---

## Required Context by Mode

### CRITIQUE MODES

| Mode | Required | Optional |
|------|----------|----------|
| **1. Red Team** | Subject, Stakes, Critics/Audience | Timeline, Resources |
| **2. Steelman** | Subject, Opposition, Stakes | Your constraints |
| **3. Pre-Mortem** | Subject, Timeline, Success criteria | Resources, Dependencies |
| **4. Assumptions** | Subject (plan/proposal), Stakes | Decision timeline |
| **5. Biases** | Subject, Decision context, Stakes | Past similar decisions |

### EXPANSION MODES

| Mode | Required | Optional |
|------|----------|----------|
| **6. First Principles** | Subject, Core goal, Constraints | Current approach |
| **7. Analogist** | Subject, Core challenge | Domains to explore |
| **8. Scenario Weaver** | Subject, Time horizon, Stakes | Key uncertainties |
| **9. Perspective Shifter** | Subject, Stakeholders, Stakes | Decision timeline |
| **10. Synthesizer** | Multiple inputs, Goal | Constraints |
| **11. Option Generator** | Subject, Constraints, Criteria | Resources |
| **12. Values Clarifier** | Decision/situation, Stakes | Time pressure |

---

## Question Templates

### Mode 1: Red Team

**Form questions:**
```
Question 1: "What specifically should I attack?"
Options: [Product/service, Strategy/plan, Pitch/proposal, Argument/position]

Question 2: "Who are the critics I should channel?"
Options: [Investors/board, Competitors, Skeptical customers, Internal team, Regulators]

Question 3: "What's at stake if weaknesses go unaddressed?"
Options: [Major launch/decision, Funding round, Strategic pivot, Public announcement]

Question 4: "What areas are absolutely off-limits for criticism?"
[Free text]
```

**Text fallback:**
```
Before I Red Team this, I need to know:

1. **Target**: What specifically should I attack? (product, strategy, pitch, argument?)
2. **Critics**: Who should I channel? (investors, competitors, customers, regulators?)
3. **Stakes**: What happens if I find major weaknesses? What decision does this inform?
4. **Boundaries**: Anything off-limits for criticism?
```

### Mode 4: Assumptions

**Form questions:**
```
Question 1: "What plan/proposal should I excavate assumptions from?"
[Free text - or reference to prior context]

Question 2: "What decision does this inform?"
Options: [Go/no-go decision, Investment, Strategic direction, Resource allocation]

Question 3: "What's the timeline for this decision?"
Options: [This week, This month, This quarter, Exploring/no deadline]

Question 4: "What would make this analysis most valuable for you?"
[Free text]
```

**Text fallback:**
```
Before excavating assumptions, I need:

1. **The Plan**: What specifically should I analyze? (Paste or describe the plan/proposal)
2. **Decision**: What does this analysis inform? (go/no-go, investment, direction?)
3. **Timeline**: When must this decision be made?
4. **Value**: What would make this most useful? (Focus areas, concerns?)
```

### Mode 9: Perspective Shifter

**Form questions:**
```
Question 1: "What situation/decision should I examine from multiple perspectives?"
[Free text]

Question 2: "Who are the key stakeholders whose perspectives matter?"
Options: [Customers, Employees, Investors, Partners, Regulators, Community]
[Multi-select enabled]

Question 3: "What's the core tension or decision point?"
[Free text]

Question 4: "Are there any perspectives you've already deeply considered?"
[Free text - so Claude doesn't repeat]
```

### Mode 11: Option Generator

**Form questions:**
```
Question 1: "What problem or opportunity needs options?"
[Free text]

Question 2: "What constraints must all options respect?"
[Free text - critical for useful generation]

Question 3: "What criteria will you use to evaluate options?"
Options: [Cost, Speed, Risk, Innovation, Simplicity, Scalability]
[Multi-select enabled]

Question 4: "How many options would be useful?"
Options: [3-5 focused options, 5-10 diverse options, Exhaustive exploration]
```

---

## Skip Conditions

**Explicit skip commands:**
- `*skip` - Proceed immediately with available context
- `*quick` - Fast mode, single question only
- "just proceed" / "skip the questions" - Natural language skip

**Implicit skip (Claude judges):**
- User provided comprehensive context unprompted (2+ paragraphs with clear subject and stakes)
- Continuation of previous analysis in same session
- User explicitly shared a document/plan that contains necessary context

**When in doubt:** Ask. The cost of one question round is tiny compared to irrelevant analysis.

---

## Multi-Round Protocol

**Round 1: Core Requirements**
Ask for the required fields for this mode. 2-4 questions max.

**Round 2: Clarification (if needed)**
If answers are vague or missing:
- Acknowledge what you understood
- Ask for specific clarification on gaps
- Offer concrete examples if user seems stuck

**Round 3: Confirmation (rare)**
Only if still unclear after Round 2:
- Summarize your understanding
- Ask user to confirm or correct
- Then proceed regardless (avoid infinite loops)

**Maximum rounds:** 3 (then proceed with best understanding and caveat gaps)

---

## Context Quality Indicators

**Strong context (proceed confidently):**
- Specific subject clearly defined
- Stakes articulated (what's riding on this)
- Relevant constraints mentioned
- Mode-specific requirements met

**Weak context (need more):**
- Subject is vague ("my business")
- Stakes unclear ("it matters")
- No constraints or criteria mentioned
- Mode-specific gaps

**Proceed with caveats when:**
- User explicitly skipped
- 3 rounds completed
- User seems frustrated with questions
- Context is "good enough" for useful output (but always note what was assumed)
