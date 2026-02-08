# Question Guidelines

Ask fewer, sharper questions that materially change implementation decisions.

## Brevity sweet spot

- Keep most questions to 1 sentence.
- Add 1 short context line only when the question could be interpreted multiple ways.
- Do not force options/tradeoffs into every question.
- Do not ask bare questions with no decision context when the answer changes implementation.
- For framework/architecture choices, default to slightly richer framing (short option baselines).

## Question quality test

Ask only if at least one is true:
- research cannot answer it reliably
- it resolves a non-obvious risk/ambiguity
- the answer changes architecture, scope, or success criteria

## Good question behaviors

- challenge assumptions directly
- cite specific user text or codebase findings
- ask failure-mode questions, not only happy path
- surface your own assumptions explicitly
- drive toward decisions, not conversation volume

## Avoid

- generic filler questions
- questions answerable through repo/docs checks
- agreement-seeking questions
- repeating broad discovery late in the interview

## Question depth ladder (use the lightest level that works)

### Level 1: Clarification (default)

Use for simple missing facts.

Format:
- One direct question only.

Example:
- "Should retry happen on 429 only, or also on 5xx?"

### Level 2: Choice framing (when multiple plausible directions exist)

Use when answer selects between 2-3 valid implementation paths.

Format:
- One direct question
- One short "why this matters" line
- 2-3 options with terse labels

Example:
- "For tenant data, do you want shared DB with row isolation or separate DB per tenant?"
- "Why this matters: it changes migration and ops complexity."
- "Options: shared+RLS (simpler ops), separate DBs (stronger isolation)."

### Level 3: Tradeoff callout (only for material architecture/scope decisions)

Use only when the user must explicitly pick a tradeoff.

Format:
- One direct question
- 2-3 options (include a short baseline per option when unfamiliar)
- One short tradeoff line (cost vs benefit)
- Optional: one recommendation line with condition ("if X, choose A; if Y, choose B")

Example:
- "Should we optimize for fastest launch or lowest long-term infra cost?"
- "Options: managed queue now, or self-hosted queue now."
- "Tradeoff: managed is faster to ship; self-hosted reduces recurring cost later."

## Framework/architecture default (richer, still practical)

When asking users to choose between frameworks or architectures they may not know:
- Start at Level 2 minimum (often Level 3 for architecture).
- Provide a one-line baseline for each option:
  - plain-language description
  - biggest upside
  - biggest cost/risk
- Keep it tight: 2 options by default, 3 max when required.
- End with a decision aid line when possible: "If X matters most, choose A; if Y, choose B."

Example:
- "For the API layer, should we use tRPC or REST?"
- "tRPC: type-safe end to end, fast internal iteration, tighter frontend coupling."
- "REST: broad interoperability, easier public integrations, more boilerplate."
- "Decision aid: if v1 is internal-only, tRPC; if external clients are expected soon, REST."

## Round structure

- Early (challenger): up to 4 focused questions
- Mid (partner): 2-4 focused questions
- Late (convergence): 1-3 precision questions

Question count should decrease over time.

## Theme coverage

Cover these themes with project-specific wording:
- alternatives and tradeoffs
- failure modes and edge cases
- integration with existing systems
- measurable success criteria
- scope boundaries and out-of-scope

## Example rewrites

- Weak: "What are your requirements?"
- Strong: "You asked for tenant isolation; does that mean separate repos, separate DBs, or both?"

- Weak: "Should we use React?"
- Strong: "Given your existing Vue stack in `apps/admin`, what benefit justifies adding React here?"

- Weak: "Which option do you want?"
- Strong: "Do you want batch writes every minute or near-real-time writes per event? Why this matters: this sets load profile and cost."
