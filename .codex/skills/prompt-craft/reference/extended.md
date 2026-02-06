# Extended Techniques

Use this file for techniques outside the core 10. Select only what is relevant to the task.

## Decomposition
- Break complex tasks into explicit stages.
- Use when scope is broad or failure modes differ by stage.

## Compression
- Reduce context while preserving constraints and examples.
- Use when prompt length is near model limits.

## Sufficiency
- Add non-inferable context and required assumptions.
- Use when model repeatedly misses hidden requirements.

## Scope
- Explicitly define in-scope vs out-of-scope.
- Use to prevent overreach and unwanted side effects.

## Format-Spec
- Specify exact output contract and validation rules.
- Use for machine-consumed outputs.

## Uncertainty
- Request confidence + evidence quality.
- Use for high-risk or low-trust domains.

## Chaining
- Split work into sequential prompts where outputs feed next stage.
- Use when one-shot prompts become brittle.

## Self-Consistency
- Sample multiple attempts and converge on common answer.
- Use when consistency matters more than latency.

## Tree-of-Thoughts
- Explore multiple reasoning branches before committing.
- Use when strategic alternatives matter.
