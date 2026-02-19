# Claude Subagents Inventory

Generated from these roots:
- `/Users/andremachon/.claude/agents`
- `/Users/andremachon/.claude/plugins`
- `/Users/andremachon/.claude-work/plugins`

## Inventory Summary
- Total unique markdown agent definition paths discovered: 57
- Duplicate-heavy families are repeated across plugin cache and marketplace mirrors.
- Primary high-level families detected:
  - PAI role agents (`Architect`, `Engineer`, `QATester`, research variants)
  - AJBM development agents (`docs-research-specialist`, `clean-code-reviewer`)
  - Official feature-dev and PR-review agents (`code-architect`, `code-explorer`, `code-reviewer`, `silent-failure-hunter`, `pr-test-analyzer`, etc.)

## Dedupe Notes
- `.claude-work/plugins/marketplaces/*` duplicates many `.claude/plugins/marketplaces/*` definitions.
- `.claude/plugins/cache/*` and `.claude-work/plugins/cache/*` are cache mirrors and were not treated as canonical sources.
- Canonical source preference used for migration:
  1. `/Users/andremachon/.claude/agents`
  2. `/Users/andremachon/.claude/plugins/marketplaces/*`
  3. `/Users/andremachon/.claude-work/plugins/marketplaces/*` (fallback only)

## Selected for Migration
- architect
- engineer
- qa_tester
- docs_research_specialist
- clean_code_reviewer
- code_architect
- code_explorer
- code_reviewer
- silent_failure_hunter
- pr_test_analyzer

## Excluded from This Curated Pack
Examples of excluded definitions:
- Persona-heavy PAI roles not central to core implementation flow (`Artist`, `Intern`, model-specific researchers)
- Plugin authoring roles (`agent-creator`, `plugin-validator`, `skill-reviewer`)
- Narrow analyzers not required in the first high-value pack (`type-design-analyzer`, `comment-analyzer`, `code-simplifier`, etc.)
