# CreateJudge Workflow (Codex)

Use this workflow when deterministic graders are not enough.

1. Choose one model-based grader:
- `llm_rubric`
- `natural_language_assert`
- `pairwise_comparison`

2. Configure strict prompts:
- short rubric/assertions
- explicit scoring format
- avoid ambiguous criteria

3. Set `judge_model` (optional):
- default uses GPT-5 model mapping from `JudgeProvider.ts`
- override with an explicit model string if needed

4. Ensure `OPENAI_API_KEY` is set before running model-based graders.
