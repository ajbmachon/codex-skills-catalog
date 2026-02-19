# Multi-Agents Migration Notes

## Target
- Repo: `/Users/andremachon/Projects/codex-skills-catalog`
- Format: 0.102+ role configuration (`[agents.<id>]` + `config_file = "agents/<role>.toml"`)
- Scope: 10 curated roles

## Source-to-Destination Mapping
- `/Users/andremachon/.claude/agents/Architect.md` -> `.codex/agents/architect.toml`
- `/Users/andremachon/.claude/agents/Engineer.md` -> `.codex/agents/engineer.toml`
- `/Users/andremachon/.claude/agents/QATester.md` -> `.codex/agents/qa_tester.toml`
- `/Users/andremachon/.claude/plugins/marketplaces/ajbm/plugins/development-skills/agents/docs-research-specialist.md` -> `.codex/agents/docs_research_specialist.toml`
- `/Users/andremachon/.claude/plugins/marketplaces/ajbm/plugins/development-skills/agents/clean-code-reviewer.md` -> `.codex/agents/clean_code_reviewer.toml`
- `/Users/andremachon/.claude/plugins/marketplaces/claude-plugins-official/plugins/feature-dev/agents/code-architect.md` -> `.codex/agents/code_architect.toml`
- `/Users/andremachon/.claude/plugins/marketplaces/claude-plugins-official/plugins/feature-dev/agents/code-explorer.md` -> `.codex/agents/code_explorer.toml`
- `/Users/andremachon/.claude/plugins/marketplaces/claude-plugins-official/plugins/feature-dev/agents/code-reviewer.md` -> `.codex/agents/code_reviewer.toml`
- `/Users/andremachon/.claude/plugins/marketplaces/claude-plugins-official/plugins/pr-review-toolkit/agents/silent-failure-hunter.md` -> `.codex/agents/silent_failure_hunter.toml`
- `/Users/andremachon/.claude/plugins/marketplaces/claude-plugins-official/plugins/pr-review-toolkit/agents/pr-test-analyzer.md` -> `.codex/agents/pr_test_analyzer.toml`

## Intentional Normalizations
- Removed voice notification hooks and placeholder voice IDs.
- Removed mandatory emoji output templates and theatrical persona narrative blocks.
- Kept core role purpose, triggers, workflows, and quality constraints.
- Replaced external PAI path dependencies with local bundled references under `.codex/agents/references/pai/`.
- Enforced conservative sandbox defaults for review/analyzer roles.

## Compatibility Note
- Local runtime currently reports `codex-cli 0.98.0`, while these files target the requested 0.102+ multi-agent schema.
- Static validation is included (TOML parse, linkage, normalization guards).
- Runtime behavior should be validated in a 0.102+ environment.
