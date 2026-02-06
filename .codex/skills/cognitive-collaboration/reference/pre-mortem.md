# Pre-Mortem Mode

Assume the project has already failed. Now trace backward to discover why.

## Table of Contents

1. [Purpose & Cognitive Work](#purpose--cognitive-work)
2. [Why Pre-Mortems Work](#why-pre-mortems-work)
3. [Execution Process](#execution-process)
4. [The 6 Failure Domains](#the-6-failure-domains)
5. [Output Template](#output-template)
6. [Likelihood × Impact Scoring](#likelihood--impact-scoring)
7. [Shallow vs Deep Pre-Mortems](#shallow-vs-deep-pre-mortems)
8. [Failure Generation Prompts](#failure-generation-prompts)
9. [Identifying Early Warning Signs](#identifying-early-warning-signs)
10. [Quality Criteria](#quality-criteria)
11. [Common Mistakes](#common-mistakes)
12. [Self-Check Before Delivering](#self-check-before-delivering)

---

## Purpose & Cognitive Work

**What this mode does:** Mentally transport to a future where the initiative has failed, then work backward to identify what caused the failure.

**The cognitive trick:** Instead of asking "what could go wrong?" (which triggers optimistic defense mechanisms), you state "this failed—why?" The failure is a fact; now explain it.

**Why this unlocks different thinking:**
- Optimism bias makes us dismiss future risks as unlikely
- But explaining a fait accompli activates different mental models
- Hindsight bias—usually a cognitive flaw—works in your favor
- People are better at explaining the past than predicting the future

**Your job (Claude):** Guide the user through rigorous failure-imagining. Don't let them off easy with generic risks. Force specificity.

---

## Why Pre-Mortems Work

Gary Klein (research psychologist who pioneered the technique) found that pre-mortems:

1. **Reduce overconfidence** by making failure vivid and concrete
2. **Sensitize to early warnings** by identifying what symptoms would appear
3. **Surface unvoiced concerns** because the "failure is certain" framing makes it safe
4. **Break conformity pressure** because you're not predicting failure, just explaining it

**The paradox:** By deeply imagining failure, you become more likely to succeed—because you've identified and can now prevent the failure modes.

---

## Execution Process

### Step 1: Set the Scene
"It is [6 months / 1 year / project deadline] from now. This project has failed. Not partially—completely. The goal was not achieved, resources were wasted, and there's a post-mortem meeting tomorrow."

Make the failure vivid and total. Partial failure doesn't trigger the same thinking.

### Step 2: Domain Sweep
Go through each of the 6 failure domains (below) and generate at least one failure story per domain. Use the phrase: "It failed because..."

### Step 3: Identify Root Causes
For each failure story, trace backward: What was the root cause? What led to that? Keep asking "why" until you hit something preventable today.

### Step 4: Warning Signs
For each failure mode, identify the early signals that would indicate you're on this path. What would you see in month 1-2 that would predict this failure?

### Step 5: Prevention Actions
What can be done NOW to either prevent this failure mode or create early detection systems?

### Step 6: Prioritize
Score each failure mode by Likelihood × Impact. Focus the user's attention on the high-scoring items.

---

## The 6 Failure Domains

### 1. People Failures
- Key person left and took critical knowledge
- Team conflict paralyzed decision-making
- Wrong person in the wrong role, discovered too late
- The sponsor/champion lost interest or power
- Hiring took 2x as long, execution delayed

### 2. Technical Failures
- The core technology didn't work at scale
- Integration with existing systems was impossible
- Technical debt from shortcuts became unmanageable
- Vendor/dependency failed or changed terms
- Security or compliance issue stopped everything

### 3. Market/External Failures
- Customer need evaporated or shifted
- Competitor launched first/better
- Regulatory change made it impossible
- Economic downturn killed the budget
- Key partner pulled out

### 4. Execution Failures
- Scope creep consumed all resources
- Milestones slipped until deadline was impossible
- Quality was so low that launch was embarrassing
- Communication breakdown between teams
- Decision paralysis at critical moments

### 5. Resource Failures
- Ran out of money before completion
- Key equipment/infrastructure wasn't available
- Budget was cut mid-project
- Competing priorities stole the best people
- Underestimated true cost by 3x

### 6. Political/Organizational Failures
- Stakeholder opposition was underestimated
- Organizational priorities shifted
- The initiative was a threat to powerful people
- No one took ownership of critical decisions
- Success required cooperation that never came

---

## Output Template

```
PRE-MORTEM ANALYSIS
═══════════════════

DATE OF FAILURE: [Future date]
WHAT FAILED: [One sentence summary of the complete failure]

CRITICAL FAILURE MODES (High likelihood × High impact)
──────────────────────────────────────────────────────

FAILURE MODE #1: [Title]
What happened: [Narrative of how this failure unfolded]
Root cause: [What underlying issue caused this]
Warning signs: [What we'd see early that indicates this is happening]
Prevention: [What we can do NOW]
L×I Score: [High/Medium/Low]

FAILURE MODE #2: [Title]
[Same format]

SIGNIFICANT RISKS (Medium L×I)
──────────────────────────────
[Same format, can be more condensed]

KNOWN BUT ACCEPTABLE RISKS (Low L×I)
────────────────────────────────────
[Brief list—these exist but aren't worth major mitigation]

THE FAILURE NOBODY WANTS TO DISCUSS
───────────────────────────────────
[The failure mode that's most likely being actively ignored because it's uncomfortable. Name it directly.]

EARLY WARNING DASHBOARD
───────────────────────
If you see these signals, you're on a failure path:
□ [Warning sign 1] → Indicates [Failure Mode X]
□ [Warning sign 2] → Indicates [Failure Mode Y]
□ [Warning sign 3] → Indicates [Failure Mode Z]
```

---

## Likelihood × Impact Scoring

### Likelihood
- **High:** Has happened before in similar contexts; multiple paths lead here; depends on things we don't control
- **Medium:** Plausible but requires some bad luck or mistakes; we have partial control
- **Low:** Would require multiple things to go wrong simultaneously; we have good controls

### Impact
- **High:** Project-killing; irrecoverable; reputational damage; significant financial loss
- **Medium:** Major setback but recoverable; scope reduction required; deadline slipped
- **Low:** Annoying but manageable; minor delays; workarounds exist

### Priority Matrix
```
              │ Low Impact │ Med Impact │ High Impact
──────────────┼────────────┼────────────┼────────────
High Likely   │  Monitor   │ Must Address│ CRITICAL
Med Likely    │  Accept    │  Monitor    │ Must Address
Low Likely    │  Accept    │  Accept     │  Monitor
```

---

## Shallow vs Deep Pre-Mortems

### Shallow Pre-Mortem (What to Avoid)

```
Failure Mode: The project was delayed.
Root cause: Things took longer than expected.
Prevention: Build in buffer time.
```

**Why it's shallow:**
- Generic—applies to any project
- No specific mechanism identified
- Prevention is vague
- Doesn't illuminate anything new

### Deep Pre-Mortem (What to Aim For)

```
Failure Mode: Integration with SAP Took 4x Longer Than Planned

What happened: We assumed SAP's API would handle our data format natively.
In month 2, we discovered their API requires a specific XML schema that
doesn't map to our data model. We needed a translation layer. The only
engineer who understood SAP left the company. The replacement took 6 weeks
to hire and 4 weeks to get up to speed. By then, we'd burned 3 months
and had to descope the real-time features that were the project's
main value proposition.

Root cause: We didn't do a technical spike on SAP integration before
committing to the architecture. We assumed because SAP is "standard"
that integration would be straightforward.

Warning signs:
- Week 2: No one on the team has actually opened SAP's API documentation
- Week 4: The SAP integration is still "planned for later"
- Month 2: First actual API test reveals major gaps

Prevention:
- Before project kickoff: 2-day technical spike on SAP integration
- Week 1: Identify SAP expert or consultant, have on standby
- Milestone gate: No feature work starts until integration proven

L×I Score: HIGH - This is a project-killer and we've done nothing to validate
```

**Why it's deep:**
- Specific to THIS project
- Names exact mechanisms and sequences
- Warning signs are observable and time-bound
- Prevention is actionable and specific
- Reader understands exactly how this failure unfolds

---

## Failure Generation Prompts

Use these questions to generate specific, non-obvious failures:

**People:**
- "If the most critical person on this project quit tomorrow, what would we not be able to do?"
- "Who is a single point of failure, and what happens when they become unavailable?"
- "Which stakeholder relationship could sour, and how would that kill this?"

**Technical:**
- "What are we assuming 'just works' that we haven't actually tested?"
- "What's the most complex integration, and what if it's 5x harder than planned?"
- "What vendor or dependency could fail or change terms on us?"

**Market:**
- "What if customers don't want this as much as we think?"
- "What if a competitor launches something similar but better next month?"
- "What external event (regulation, economy, pandemic) would kill this?"

**Execution:**
- "What decision have we been avoiding that will eventually be forced on us?"
- "Where is 'we'll figure it out later' hiding in the plan?"
- "What milestone is most likely to slip, and what cascades from that?"

**Resources:**
- "What if the real cost is 2x what we've budgeted?"
- "What if this takes 2x as long as planned—do we survive?"
- "What if we lose access to a critical resource in month 3?"

**Political:**
- "Who would benefit from this project failing, and what could they do?"
- "What happens if our sponsor's attention shifts to something else?"
- "Which organizational priority could rise and kill our staffing?"

---

## Identifying Early Warning Signs

For each failure mode, ask:

1. **What would we see in Week 1-2?**
   - Absence of something expected
   - An early decision that sets a bad trajectory
   - A conversation that didn't happen

2. **What would we see in Month 1-2?**
   - A milestone slipping for the first time
   - A person becoming unavailable
   - A blocker that keeps getting "pushed to next week"

3. **What would make us say "I should have seen this coming"?**
   - The retrospective insight—identify it now

**Good warning signs are:**
- Observable (not "team morale is low" but "two people have updated their LinkedIn")
- Early (provide time to intervene)
- Actionable (trigger a specific response, not general worry)

---

## Quality Criteria

Your pre-mortem is **strong** if:

- [ ] User says "I hadn't thought about that" to at least one failure mode
- [ ] Failure modes are specific to THIS project (not generic project risks)
- [ ] You've identified "the failure nobody wants to discuss"
- [ ] Warning signs are early, observable, and specific
- [ ] Prevention actions are things they can do in the next week/month

Your pre-mortem is **weak** if:

- [ ] All failure modes were already known/obvious
- [ ] Failures are described generically ("scope creep," "delays")
- [ ] Warning signs are just restating the failure
- [ ] Prevention is vague ("communicate better," "plan carefully")
- [ ] You avoided naming uncomfortable political/people failures

---

## Common Mistakes

### 1. Failures Are Too Generic
**Symptom:** "We might run over budget"
**Fix:** HOW would you run over budget? By what mechanism? Which specific costs were underestimated?

### 2. Only External Failures
**Symptom:** Market changes, competitor launches, economy shifts
**Fix:** Those are real, but the INTERNAL failures (people, execution, politics) are often more preventable and ignored.

### 3. Ignoring the Elephant
**Symptom:** The most obvious but uncomfortable failure mode (the weak sponsor, the impossible deadline, the missing skill) isn't mentioned
**Fix:** Explicitly name "the failure nobody wants to discuss."

### 4. Prevention Is Wishful
**Symptom:** "We'll communicate better" or "We'll be more careful"
**Fix:** Prevention must be specific and actionable. WHAT will you communicate, to WHOM, by WHEN?

### 5. Warning Signs Are Just Failures Restated
**Symptom:** "Warning sign that we'll miss deadline: milestones slip"
**Fix:** Warning signs should appear BEFORE the failure is obvious. What's the early signal?

---

## Self-Check Before Delivering

Ask yourself:

1. **"Did I imagine the failure as total and complete?"**
   - Partial failure doesn't trigger the same insights.

2. **"Did I cover all 6 domains?"**
   - People, Technical, Market, Execution, Resources, Political.

3. **"Did I name the uncomfortable one?"**
   - There's always a failure mode no one wants to say out loud. Did you?

4. **"Are the warning signs actionable?"**
   - Can they create a dashboard or checklist from these?

5. **"Would this analysis have predicted real past failures?"**
   - Think of a project you know failed. Would this process have surfaced it?

---

## Verbalized Sampling

By default, generate 3-5 variants with probability estimates. Include at least one tail sample (p < 0.10).

### Output Structure

```
VARIANT 1 (p ≈ 0.45) ────────────────────
[Failure scenario analysis]
Grade: Plausibility 4 | Impact Severity 5 | Preventability 3

VARIANT 2 (p ≈ 0.30) ────────────────────
[Failure scenario analysis]
Grade: Plausibility 3 | Impact Severity 4 | Preventability 4

VARIANT 3 (p ≈ 0.08) ⚡ Tail ─────────────
[Failure scenario analysis]
Grade: Plausibility 2 | Impact Severity 5 | Preventability 2

═══════════════════════════════════════
TAIL INSIGHT: [What the low-probability failure scenario reveals about hidden vulnerabilities]
```

### Grading Criteria

| Criterion | 1 | 5 |
|-----------|---|---|
| **Plausibility** | Requires multiple unlikely events | Has happened before; clear path to this outcome |
| **Impact Severity** | Annoying delay; workarounds exist | Project-killing; irrecoverable damage |
| **Preventability** | Outside our control; unavoidable | Within our control; clear preventive action |

### Tail Sampling Prompt

"What failure mode would a typical pre-mortem miss because it seems too unlikely or uncomfortable to discuss? Generate one variant with p < 0.10 that challenges our implicit trust in key dependencies."

Use `*single` to skip VS and get conventional single-response output.

---

## When Pre-Mortem Isn't Right

**Don't use this mode when:**
- The initiative is in early ideation (need to build enthusiasm first)
- User is already overwhelmed with problems (don't pile on)
- There's no specific plan to analyze (need substance to pre-mortem)
- User needs encouragement, not risk analysis

**Great to pair with:**
- **Red Team** after Pre-Mortem → External attacks on top of internal failures
- **Assumptions** before Pre-Mortem → Surface hidden beliefs, then imagine them being wrong
