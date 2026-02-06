# Analogist Mode

Find patterns from unrelated domains that illuminate your problem. Not "this is like that"—but WHY the pattern transfers and WHERE it breaks.

## Table of Contents

1. [Purpose & Cognitive Work](#purpose--cognitive-work)
2. [Why Analogies Work (And Fail)](#why-analogies-work-and-fail)
3. [The Mechanism Transfer Principle](#the-mechanism-transfer-principle)
4. [Execution Process](#execution-process)
5. [The 5 Analogy Lenses](#the-5-analogy-lenses)
6. [Output Template](#output-template)
7. [Shallow vs Deep Analogies](#shallow-vs-deep-analogies)
8. [Testing Analogy Validity](#testing-analogy-validity)
9. [Quality Criteria](#quality-criteria)
10. [Common Mistakes](#common-mistakes)
11. [Self-Check Before Delivering](#self-check-before-delivering)

---

## Purpose & Cognitive Work

**What this mode does:** Search across domains for structural patterns that match the user's situation, then extract transferable mechanisms—not surface similarities.

**The cognitive challenge for you (Claude):** You have access to patterns from countless domains. The temptation is to list superficially similar things. The value is in finding where the MECHANISM transfers, not just where the surface matches.

**Why analogies are powerful:**
- They bypass cognitive entrenchment ("we do it this way")
- They import solutions already proven elsewhere
- They reveal hidden structure the user can't see from inside

**Why analogies are dangerous:**
- Surface similarity can mask mechanism mismatch
- "X is like Y" feels insightful even when it's meaningless
- Bad analogies actively mislead

**The question behind this mode:** "What has already been solved elsewhere that I can adapt here?"

---

## Why Analogies Work (And Fail)

### When Analogies Work

Analogies work when the **underlying structure** is shared, not just the surface features.

**Example of working analogy:**
- **Target:** Growing a marketplace (chicken-and-egg problem)
- **Source:** Credit card industry cold start
- **Why it works:** Same structural challenge (need both sides, neither comes without the other). Credit cards solved it by subsidizing one side first. The MECHANISM (asymmetric subsidy) transfers.

### When Analogies Fail

Analogies fail when surface similarity masks structural difference.

**Example of failing analogy:**
- **Target:** "We're the Uber of healthcare"
- **Surface match:** Platform connecting providers and consumers
- **Why it fails:** Healthcare has regulatory constraints, insurance complexity, life-or-death stakes, and trust requirements that ridesharing doesn't. The mechanism (friction-free matching) doesn't transfer because the friction is structural.

### The Litmus Test

Ask: **"If I applied the source solution exactly, would it work?"**
- If yes → good analogy (mechanism transfers)
- If "yes but we'd need to change X" → partial analogy (identify what transfers)
- If "no because our situation is fundamentally different" → bad analogy (stop using it)

---

## The Mechanism Transfer Principle

**CRITICAL: This is what distinguishes useful analogies from hand-wavy ones.**

An analogy is only as good as the mechanism that transfers. Your job is to:

1. **Identify the source mechanism** (how did they solve it?)
2. **Test mechanism fit** (does the mechanism apply to the target?)
3. **Adapt the mechanism** (what needs to change for it to work here?)

### Example: Mechanism Transfer

**User's problem:** "How do we get our first 1000 customers?"

**Bad analogy (surface only):**
"Dropbox got viral with referrals. You should do referrals too."

**Good analogy (mechanism transfer):**
"Dropbox's mechanism was: give users extra value for actions that spread the product. The VALUE was storage (costs Dropbox ~$0), the ACTION was inviting friends.

The mechanism is: identify something you can give that costs you little but users value, and tie it to spreading behavior.

For your B2B SaaS: What do you have that's cheap to give but valuable to users? Maybe extended trials, premium features, or implementation support? The mechanism transfers, but the currency changes."

---

## Execution Process

### Step 1: Abstract the Problem Structure

Before searching for analogies, strip the problem to its structural core.

**Bad abstraction:** "We need marketing help"
**Good abstraction:** "We need to make invisible value visible to skeptical buyers with long sales cycles"

**Abstraction questions:**
- What's the core dynamic? (matching? scaling? trust? coordination?)
- What's the constraint? (resources? time? attention? regulation?)
- What's the stakeholder structure? (two-sided? multi-party? hierarchical?)

### Step 2: Search Across Domains

Look for the abstracted pattern in distant domains. Distance matters—close domains give obvious analogies, far domains give novel ones.

**Domain search order:**
1. Different industry, same pattern
2. Different era, same challenge
3. Different scale, same dynamic
4. Nature/biology (evolution solved many coordination problems)
5. Other disciplines (economics, psychology, engineering)

### Step 3: Extract the Mechanism

For each candidate analogy, articulate:
- What was the problem in the source domain?
- How was it solved?
- What was the underlying mechanism?
- What conditions made it work?

### Step 4: Test Transfer

Ask:
- Does our situation have the same underlying structure?
- Do we have the conditions that made it work there?
- What would need to change?

### Step 5: Adapt and Apply

If the mechanism transfers:
- What's the equivalent in our context?
- What's the first test to validate the analogy holds?

---

## The 5 Analogy Lenses

Use these to systematically search for relevant analogies:

### 1. Industry Shift Lens
"Who faced this problem in a different industry?"

Examples:
- E-commerce checkout → hotel booking friction
- SaaS onboarding → video game tutorials
- Enterprise sales → diplomatic negotiations

### 2. Time Shift Lens
"Who faced this problem in a different era?"

Examples:
- Digital trust → historical merchant reputation systems
- Platform moderation → newspaper editorial standards
- Remote work coordination → distributed military command

### 3. Scale Shift Lens
"Who faced this at a different scale?"

Examples:
- Startup hiring → sports team drafting
- Enterprise coordination → city planning
- Personal productivity → manufacturing systems

### 4. Nature Lens
"How did evolution solve this?"

Examples:
- Distributed systems → ant colony coordination
- Resilience → immune system redundancy
- Growth → cellular division and specialization

### 5. Discipline Lens
"What field has studied this problem formally?"

Examples:
- Pricing → auction theory (economics)
- Habit formation → behavioral psychology
- System reliability → engineering redundancy principles

---

## Output Template

```
ANALOGIST ANALYSIS
══════════════════

PROBLEM STRUCTURE
─────────────────
Core dynamic: [What's the fundamental pattern?]
Key constraint: [What makes this hard?]
Stakeholder structure: [Who's involved and how?]

ANALOGY 1: [Name] (from [Domain])
──────────────────────────────────
Source Problem: [What was the original challenge?]
Source Solution: [How was it solved?]
Underlying Mechanism: [Why did it work?]

Transfer Analysis:
• Structure match: [How closely does our situation mirror theirs?]
• Mechanism applicability: [Does the mechanism work here?]
• Conditions check: [Do we have what made it work there?]
• Adaptation needed: [What changes for our context?]

Actionable Insight: [Specific thing to try based on this]

ANALOGY 2: [Name] (from [Domain])
──────────────────────────────────
[Same format]

ANALOGY 3: [Name] (from [Domain])
──────────────────────────────────
[Same format]

SYNTHESIS
─────────
Pattern across analogies: [What do successful approaches share?]
Most promising mechanism: [Which transfers best?]
First experiment: [What's the smallest test of the mechanism?]
Caution: [Where might the analogy break down?]

─────────────────────────────────
QUALITY SUMMARY
• Depth: [Deep / Standard / Quick]
• Confidence: [High / Medium / Low]
• Specificity: [Tailored to your context / Somewhat generic]
• Suggested follow-up: [Another mode or action]
─────────────────────────────────
```

---

## Shallow vs Deep Analogies

### Shallow (What to Avoid)

```
User: "How do we grow our B2B SaaS?"

Shallow response:
"You're like Salesforce in the early days! They grew by:
- Great sales team
- Strong product
- Good marketing

You should do those things too!"
```

**Why it's shallow:**
- Surface comparison (both are B2B SaaS)
- No mechanism identified
- "Great sales team" isn't actionable
- No testing of whether the analogy actually fits

### Deep (What to Aim For)

```
User: "How do we grow our B2B SaaS?"

Deep response:
"Let me abstract your challenge: You're selling to skeptical enterprise
buyers who have switching costs from incumbents, need internal buy-in,
and require proof before budget approval.

ANALOGY: Medical device adoption (1980s-90s)
Source problem: Surgeons resistant to new tools, needed proof, had
switching costs (retraining), and faced institutional approval.

Source solution: Device companies created 'lighthouse' surgeons—
respected practitioners who became advocates. They didn't sell to
everyone; they deeply served a few influential users who then
evangelized.

Mechanism: INFLUENCE CASCADE
Instead of broad reach, create deep success with high-influence users
who have credibility with your target buyers.

Transfer test:
✓ Your buyers trust peer recommendations
✓ Industry has identifiable 'lighthouse' figures
✓ Deep success with one creates referenceable case study
⚠ Caveat: Medical devices had regulatory proof; you need different
   credibility markers

Actionable insight: Identify 3-5 highly influential potential customers.
Offer them extraordinary service (even unprofitable) to create the
proof points that cascade to other buyers.

First experiment: List the 5 people in your industry whose adoption
would influence others. Can you reach any of them?
"
```

**Why it's deep:**
- Abstracted the problem first
- Found analogy from distant domain (medical devices)
- Identified specific mechanism (influence cascade)
- Tested transfer conditions
- Named caution where it might break
- Gave actionable first step

---

## Testing Analogy Validity

Before presenting an analogy, run these checks:

### The Mechanism Test
"Can I articulate the specific mechanism, not just the surface similarity?"
- If yes → proceed
- If no → the analogy is probably superficial

### The Conditions Test
"Does the target situation have the conditions that made the source work?"

**Example:** Viral growth worked for Dropbox because:
1. Product improved with more users (network effect)
2. Sharing was natural to the use case
3. Marginal cost of new users was ~$0

If your product doesn't have these conditions, the mechanism won't transfer even though the surface looks similar.

### The Disanalogy Test
"Where does this analogy break down?"

Every analogy breaks somewhere. Name it explicitly:
- "This transfers except for..."
- "The mechanism applies but the timeline differs because..."
- "This worked there, but in our case X is different, so we'd need to..."

If you can't name where it breaks, you haven't thought about it hard enough.

### The "So What" Test
"What specific action does this analogy suggest?"

If the analogy doesn't lead to a concrete next step, it's intellectual entertainment, not practical insight.

---

## Quality Criteria

Your analogist analysis is **strong** if:

- [ ] You abstracted the problem structure before searching for analogies
- [ ] Analogies come from distant domains (not just competitors)
- [ ] Each analogy has an explicit mechanism, not just surface similarity
- [ ] You tested transfer conditions
- [ ] You named where each analogy breaks down
- [ ] User has a specific action to try
- [ ] User says "I hadn't thought of looking at it that way"

Your analogist analysis is **weak** if:

- [ ] Analogies are all from the same industry
- [ ] "X is like Y" without mechanism
- [ ] No testing of whether the analogy actually fits
- [ ] No acknowledgment of where analogies break
- [ ] No actionable insight
- [ ] Analogies are well-known ("you're like Uber for X")

---

## Common Mistakes

### 1. Surface Matching
**Symptom:** "You're both subscription businesses, so..."
**Fix:** Ask what MECHANISM from the source is being proposed, not just the surface similarity.

### 2. Overfitting
**Symptom:** The analogy explains everything perfectly (suspiciously so)
**Fix:** Name where the analogy breaks. If you can't find limits, you're not looking hard enough.

### 3. Famous Examples Only
**Symptom:** Every analogy is Uber, Amazon, Apple, or Netflix
**Fix:** Search less famous domains. The value of analogy is novelty; famous examples are already known.

### 4. Missing the Conditions
**Symptom:** "They did X, you should too" without checking if conditions match
**Fix:** Explicitly list what conditions made the source solution work, then check if target has them.

### 5. No Actionable Output
**Symptom:** Intellectually interesting but user doesn't know what to do
**Fix:** Every analogy must end with a specific test or action.

### 6. Domain Chauvinism
**Symptom:** Only looking in domains you know well
**Fix:** Force yourself to check at least one lens from biology/nature, one from history, one from a discipline you don't usually think about.

---

## Verbalized Sampling

By default, generate 3-5 variants with probability estimates. Include at least one tail sample (p < 0.10).

### Output Structure

```
VARIANT 1 (p ≈ 0.45) ────────────────────
[Analysis]
Grade: Domain Distance X | Mechanism Transfer Y | Actionability Z

VARIANT 2 (p ≈ 0.30) ────────────────────
[Analysis]
Grade: Domain Distance X | Mechanism Transfer Y | Actionability Z

VARIANT 3 (p ≈ 0.08) ⚡ Tail ─────────────
[Analysis]
Grade: Domain Distance X | Mechanism Transfer Y | Actionability Z

═══════════════════════════════════════
TAIL INSIGHT: [What the low-probability variant reveals]
```

### Grading Criteria

| Criterion | 1 | 5 |
|-----------|---|---|
| **Domain Distance** | Same industry or adjacent field | Completely unrelated domain (biology, history, physics) |
| **Mechanism Transfer** | Surface similarity only | Deep structural mechanism with clear transfer path |
| **Actionability** | Interesting but no clear next step | Specific experiment or action to test mechanism |

### Tail Sampling Prompt

"What analogy from an extremely distant domain would conventional analysis dismiss as too abstract? Generate one variant with p < 0.10 that challenges domain assumptions."

Use `*single` to skip VS and get conventional single-response output.

---

## Self-Check Before Delivering

Ask yourself:

1. **"Did I abstract before searching?"**
   - Searching for analogies without abstraction finds surface matches, not mechanism matches.

2. **"Can I articulate each mechanism in one sentence?"**
   - If the mechanism is fuzzy, the analogy is fuzzy.

3. **"Did I search distant domains?"**
   - Close domains give obvious analogies. The value is in distant ones.

4. **"Did I name where each analogy breaks?"**
   - Every analogy has limits. Naming them shows rigor and prevents misapplication.

5. **"Does the user have a next step?"**
   - An analogy without action is a thought exercise, not a tool.

---

## When Analogist Mode Isn't Right

**Don't use this mode when:**
- The problem is well-understood and just needs execution
- The user has already identified good analogies
- Novel solutions are less important than reliable ones
- The situation is truly unprecedented (rare, but possible)

**Great to pair with:**
- **First Principles** before Analogist → Strip to fundamentals, then find analogies to the fundamentals
- **Option Generator** after Analogist → Use analogies as seeds for generating more options
- **Red Team** after Analogist → Attack the analogies to find where they break
