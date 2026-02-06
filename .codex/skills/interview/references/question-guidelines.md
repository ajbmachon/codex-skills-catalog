# Question Guidelines

Ask fewer, sharper questions that materially change implementation decisions.

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
