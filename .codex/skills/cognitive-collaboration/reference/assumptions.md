# Assumptions Mode

Surface hidden beliefs that could invalidate the entire plan if they're wrong.

## Table of Contents

1. [Purpose & Cognitive Work](#purpose--cognitive-work)
2. [The Three Layers of Assumptions](#the-three-layers-of-assumptions)
3. [Execution Process](#execution-process)
4. [The 7 Assumption Domains](#the-7-assumption-domains)
5. [Output Template](#output-template)
6. [Validation Levels](#validation-levels)
7. [Excavation Techniques](#excavation-techniques)
8. [Shallow vs Deep Assumption Hunting](#shallow-vs-deep-assumption-hunting)
9. [Quality Criteria](#quality-criteria)
10. [Common Mistakes](#common-mistakes)
11. [Self-Check Before Delivering](#self-check-before-delivering)

---

## Purpose & Cognitive Work

**What this mode does:** Extract implicit beliefs from a plan, proposal, or strategy—beliefs that aren't stated but must be true for the plan to work.

**The cognitive challenge for you (Claude):** Assumptions are invisible by definition. If the user could see them, they wouldn't be assumptions. Your job is to adopt the perspective of someone who doesn't share the user's mental model—and ask what they'd find puzzling.

**Why assumptions are dangerous:**
- Explicit risks get analyzed; assumptions don't
- Assumptions feel like facts ("of course that's true")
- The most dangerous assumptions are so embedded they're not recognized as beliefs
- A single wrong foundational assumption can invalidate everything built on it

**The question behind this mode:** "What has to be true for this to work?"

---

## The Three Layers of Assumptions

### Layer 1: Surface Assumptions (Obvious)
These are close to explicit in the document. The user knows they're making these assumptions but may not have stated them.

**Example:** "We'll hire 5 engineers by Q2"
- Assumption: We can find qualified engineers in our location/comp range
- Often stated or easy to surface

### Layer 2: Hidden Assumptions (Invisible to insiders)
These are embedded in the domain. Experts share them so universally they don't realize they're assumptions.

**Example:** A SaaS pricing model that assumes monthly billing
- Assumption: Customers will pay monthly via credit card
- But: What if the target market requires annual POs through procurement?
- Invisible to anyone who's always done SaaS; obvious to someone from enterprise sales

### Layer 3: Foundational Assumptions (Worldview-level)
These are so deep they feel like reality, not belief. Challenging them feels absurd.

**Example:** "We'll build and they will come" (meritocracy assumption)
- Assumption: Quality products naturally find markets
- But: Distribution might matter more than product
- Foundational because it shapes everything but is never questioned

**Your job is to dig to Layer 2 and Layer 3.** Layer 1 is easy. The value is in the layers the user can't see.

---

## Execution Process

### Step 1: Identify the Core Claim
What is the document/plan ultimately claiming? "If we do X, we'll get Y."

### Step 2: Ask "What has to be true?"
For the core claim to work, what unstated things must be true about:
- The market?
- The customers?
- The technology?
- The team?
- The timing?
- The resources?
- The world staying the same?

### Step 3: Domain Sweep
Systematically go through each of the 7 assumption domains. Force at least one assumption from each.

### Step 4: Layer Check
For each assumption, ask: Is this Layer 1 (obvious), Layer 2 (hidden), or Layer 3 (foundational)? Push to find Layer 2 and 3 assumptions.

### Step 5: Validation Classification
For each assumption, classify: Tested, Assumed, or Hoped?

### Step 6: "If Wrong" Analysis
For each critical assumption, ask: If this is wrong, what happens? Does the plan survive or collapse?

### Step 7: Newcomer Test
Imagine someone new to this domain reading the plan. What would they question that insiders take for granted?

---

## The 7 Assumption Domains

### 1. Market Assumptions
- The market exists and is the size we think
- The market will continue to exist
- We understand who the customer is
- Customers have the problem we think they have
- The problem is painful enough to pay to solve

**Probe:** "What if customers don't actually have this problem—or don't think they do?"

### 2. Behavioral Assumptions
- People will behave as we expect them to
- They'll adopt our solution when presented with it
- They'll pay what we expect them to pay
- They'll use the product the way we designed it
- They'll recommend it to others

**Probe:** "What if users behave rationally in their own interest, but not in ours?"

### 3. Technical Assumptions
- The technology works as expected
- We can build it with available resources
- It will scale when needed
- Integrations will work
- We have or can get the necessary skills

**Probe:** "What's the most uncertain technical component, and what if it's impossible?"

### 4. Competitive Assumptions
- Competitors won't respond effectively
- We have defensible differentiation
- We can move faster than alternatives
- The market isn't winner-take-all (or we'll be the winner)
- Substitutes won't emerge

**Probe:** "What if a well-funded competitor copies this in 6 months?"

### 5. Resource Assumptions
- We have enough money
- We can hire the people we need
- Time required is accurate
- Nothing else will compete for these resources
- Costs will be what we expect

**Probe:** "What if this takes 2x as long and costs 2x as much?"

### 6. Timing Assumptions
- Now is the right time
- The market is ready
- We'll be ready before the window closes
- Dependencies will align when needed
- External events won't disrupt the timeline

**Probe:** "What if the window is 12 months shorter than we think—or already closed?"

### 7. Environmental Assumptions
- Regulatory environment won't change adversely
- Economic conditions will remain stable enough
- Key external relationships will persist
- No black swan events will intervene
- The world will keep working roughly as it does

**Probe:** "What external change would make this irrelevant or impossible?"

---

## Output Template

```
ASSUMPTION EXCAVATION
═════════════════════

CORE CLAIM
──────────
[One sentence: What is this plan ultimately betting on?]

FOUNDATIONAL ASSUMPTIONS (Layer 3)
──────────────────────────────────
These are worldview-level beliefs so deep they feel like facts. If wrong, everything collapses.

Assumption: [What's taken for granted]
Domain: [Which of the 7]
Layer: Foundational
Validation: [Tested/Assumed/Hoped]
If Wrong: [What happens—be specific]

HIDDEN ASSUMPTIONS (Layer 2)
────────────────────────────
These are embedded in the domain. Experts share them universally without realizing they're assumptions.

[Same format as above, multiple entries]

SURFACE ASSUMPTIONS (Layer 1)
─────────────────────────────
These are implicit but close to explicit. Important to note but not where the hidden risk lives.

[Can be a condensed list format]

THE ASSUMPTION THAT SCARES ME MOST
──────────────────────────────────
[Name the single assumption that, if false, most completely invalidates the plan. Why does it scare you?]

VALIDATION PRIORITIES
─────────────────────
If the user has limited time to validate assumptions before proceeding:
1. [Assumption] - Validate by: [Method]
2. [Assumption] - Validate by: [Method]
3. [Assumption] - Validate by: [Method]
```

---

## Validation Levels

### TESTED
The assumption has been validated through evidence—not just belief or logic.

**Examples:**
- Customer interviews confirming the problem
- Technical proof-of-concept working
- Historical data showing the pattern
- Pilots or experiments that succeeded

**Key test:** Is there evidence outside our own heads?

### ASSUMED
The assumption seems reasonable based on logic or precedent, but hasn't been directly tested.

**Examples:**
- "Enterprise buyers typically need X" (pattern matching)
- "This technology should scale because similar ones did" (analogy)
- "The team has done this before" (past performance)

**Key test:** Are we reasoning by analogy without testing the analogy?

### HOPED
The assumption needs to be true for the plan to work, but we have no evidence—and maybe some counter-evidence.

**Examples:**
- "If we build it, they will come"
- "The competitor won't respond for 18 months"
- "The team will figure out the hard parts"

**Key test:** Is this wishful thinking dressed as planning?

**The danger zone:** Many Hoped assumptions hide as Assumed ones. Press on "assumed" beliefs to see if they're actually just hoped.

---

## Excavation Techniques

### 1. The Newcomer Lens
Imagine someone completely new to this domain reading the plan. What would confuse them? What would they ask "but why?" about?

**Use:** "If I had never worked in this industry, what would seem strange about this plan?"

### 2. The Inversion
Take each stated goal and ask what's assumed by not stating the opposite.

**Example:**
- Goal: "We'll grow to 10,000 users in year one"
- Inversion: "We won't need to prove product-market fit before scaling"
- Hidden assumption: The product already has market fit

### 3. The Chain of Dependencies
Trace backward from the goal: What has to happen for this to work? And what has to happen for THAT to work?

**Example:**
- Revenue → Sales → Pipeline → Marketing → Brand awareness → ?
- Each → reveals an assumption

### 4. The "Of Course" Test
When someone says "of course X is true," that's often Layer 3 assumption. "Of course" means "I've never questioned this."

**Flag:** Any phrase like:
- "Obviously..."
- "Everyone knows..."
- "It goes without saying..."
- "Of course..."

### 5. The Alternative Universe
Ask: "What if the opposite were true?" If the plan would still work, it's not an assumption. If it falls apart, you've found one.

### 6. The Numbers Behind the Numbers
When there's a number, ask where it came from. "We'll get 1,000 customers" — what assumption produced that number?

---

## Shallow vs Deep Assumption Hunting

### Shallow (What to Avoid)

```
Assumption: We can hire engineers
Domain: Resource
Validation: Assumed
If Wrong: We'll have delays
```

**Why it's shallow:**
- Too obvious (Layer 1)
- Generic—applies to any tech project
- "If Wrong" is vague
- No real insight

### Deep (What to Aim For)

```
Assumption: Enterprise procurement cycles align with our fundraising runway

Domain: Timing + Resource (compounding)
Layer: Hidden

What's embedded: We need enterprise contracts, which take 6-12 months.
We have 18 months of runway. But we're assuming first contact to signed
contract happens in parallel with product development. In reality,
enterprises won't seriously evaluate until the product is mature,
which won't happen until month 8. That gives us 10 months for a
6-12 month sales cycle with no room for iteration.

Validation: Hoped
Evidence: We've never sold to enterprise. We're assuming based on
industry averages that don't account for new vendor friction.

If Wrong: We hit month 15 with a finished product and an empty pipeline.
We have to choose between a distressed fundraise or pivoting to SMB
(which invalidates the original thesis).
```

**Why it's deep:**
- Layer 2—not obvious until you trace dependencies
- Specific to THIS plan
- Names the mechanism
- "If Wrong" is vivid and actionable
- User learns something they didn't see

---

## Quality Criteria

Your assumption excavation is **strong** if:

- [ ] You found at least one Layer 3 (foundational) assumption
- [ ] User says "I never thought about that" to at least one item
- [ ] Assumptions are specific to THIS plan (not generic project risks)
- [ ] You named "the assumption that scares me most"
- [ ] Validation priorities give them something to DO

Your assumption excavation is **weak** if:

- [ ] All assumptions are Layer 1 (surface/obvious)
- [ ] Assumptions are generic ("we can hire," "customers will pay")
- [ ] You haven't traced assumptions to their consequences
- [ ] "If Wrong" is always "we'll have problems"
- [ ] No insight that wasn't already obvious

---

## Common Mistakes

### 1. Stopping at Layer 1
**Symptom:** All assumptions are things the user already knew
**Fix:** Keep pushing. For each assumption, ask "what does THIS assume?"

### 2. Assumptions Are Really Risks
**Symptom:** "Assumption: We might lose a key hire"
**Fix:** That's a risk, not an assumption. Assumptions are beliefs about how the world works that feel like facts, not events that might happen.

### 3. Generic Assumptions
**Symptom:** Could copy-paste these to any project
**Fix:** Tie every assumption to specific details of THIS plan.

### 4. Not Checking Validation
**Symptom:** Calling things "Tested" or "Assumed" without probing
**Fix:** Ask: "What's the evidence?" If they can't point to data, it's Hoped.

### 5. Missing the Worldview Layer
**Symptom:** All assumptions are tactical, none are philosophical
**Fix:** Ask: "What would someone who disagrees with the whole approach say?"

### 6. "If Wrong" Is Too Vague
**Symptom:** "This would be a problem" or "We'd need to adjust"
**Fix:** Be specific. Does the plan survive or die? What specifically breaks?

---

## Self-Check Before Delivering

Ask yourself:

1. **"Did I find something in Layer 2 or 3?"**
   - Layer 1 is easy. The value is in the hidden and foundational layers.

2. **"Would a newcomer find different assumptions?"**
   - Use the newcomer lens; don't share the user's blind spots.

3. **"Did I trace 'If Wrong' to specific consequences?"**
   - Vague consequences = vague value.

4. **"Is the scariest assumption the real one?"**
   - Did I pull my punch, or did I name the hardest one to face?

5. **"Did I give them something to validate?"**
   - Validation priorities should be actionable in the next week.

---

## Verbalized Sampling

By default, generate 3-5 variants with probability estimates. Include at least one tail sample (p < 0.10).

### Output Structure

```
VARIANT 1 (p ≈ 0.45) ────────────────────
[Assumption analysis]
Grade: Layer Depth 1 | Risk if Wrong 3 | Validation Difficulty 2

VARIANT 2 (p ≈ 0.30) ────────────────────
[Assumption analysis]
Grade: Layer Depth 2 | Risk if Wrong 4 | Validation Difficulty 4

VARIANT 3 (p ≈ 0.08) ⚡ Tail ─────────────
[Assumption analysis]
Grade: Layer Depth 3 | Risk if Wrong 5 | Validation Difficulty 5

═══════════════════════════════════════
TAIL INSIGHT: [What the low-probability assumption reveals about foundational beliefs we're taking for granted]
```

### Grading Criteria

| Criterion | 1 | 3/5 |
|-----------|---|-----|
| **Layer Depth** | Surface (explicit or nearly stated) | Hidden (domain experts share) → Foundational (worldview-level belief) |
| **Risk if Wrong** | Minor adjustments needed | Entire plan collapses; pivot required |
| **Validation Difficulty** | Easy to test with existing data | Requires significant time/resources to validate |

### Tail Sampling Prompt

"What foundational worldview assumption is so deeply embedded that questioning it feels absurd? Generate one variant with p < 0.10 that surfaces a Layer 3 belief hiding in plain sight."

Use `*single` to skip VS and get conventional single-response output.

---

## When Assumptions Mode Isn't Right

**Don't use this mode when:**
- The plan is still forming (need more substance to excavate)
- User wants external attack (use Red Team)
- User wants future failure scenarios (use Pre-Mortem)
- User is already overwhelmed with uncertainty

**Great to pair with:**
- **Pre-Mortem** after Assumptions → Imagine each critical assumption being wrong
- **First Principles** before Assumptions → Strip to fundamentals first, then identify what's assumed in the rebuild
