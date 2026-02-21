# Multi-Agents Usage Guide

This guide explains how to use the curated 10-agent pack migrated into this repository, how each role is intended to be used, how Codex should orchestrate them, and what was changed during migration.

## Scope
- Config location: `.codex/config.toml`
- Role configs: `.codex/agents/*.toml`
- Bundled references: `.codex/agents/references/pai/*.md`
- Curated role count: 10

## Prerequisites
- Use a Codex runtime that supports role-based multi-agent config in TOML (`[agents.<id>]` with `config_file`).
- Open Codex from this repo root so `.codex/` is in scope.
- Restart session after changing `.codex/config.toml` or role TOMLs.

## Quick Start
1. Confirm roles are registered in `.codex/config.toml`.
2. Ask explicitly for a role when needed, for example:
   - `Use architect to produce a file-level implementation plan for this feature.`
   - `Use code_reviewer to review my unstaged changes.`
3. Let Codex auto-select when intent is obvious from role descriptions.
4. For complex work, run a multi-stage loop:
   - `architect` -> `engineer` -> `qa_tester` -> review agents.

## Role Intent and Outputs

| Role | Primary Intent | Typical Input | Expected Output |
|---|---|---|---|
| `architect` | Convert goals/constraints into implementation-ready architecture | feature brief, constraints, non-goals | architecture decision, file map, phases, risks |
| `engineer` | Implement with disciplined validation | approved plan/spec, codebase context | focused code changes, tests/checks, validation notes |
| `qa_tester` | Validate behavior and block false completion | feature branch/build, test target URL/workflow | PASS/FAIL with evidence and repro details |
| `docs_research_specialist` | Retrieve current official API/library facts | tool/library question | source-backed findings, recommendation |
| `clean_code_reviewer` | Enforce maintainability and clarity | changed files/diff | tiered findings (green/yellow/red) + remediation |
| `code_architect` | Map architecture from existing code patterns | subsystem/topic | deep file-level blueprint and integration map |
| `code_explorer` | Trace how a feature currently works | endpoint/component/command | end-to-end execution and dependency map |
| `code_reviewer` | High-signal correctness/risk review | diff/PR scope | severity-ranked findings + suggested fixes |
| `silent_failure_hunter` | Find hidden error handling and fallback risks | changed error paths | critical silent-failure findings + fix priorities |
| `pr_test_analyzer` | Analyze test coverage quality and gaps | PR/diff + tests | must-fix and should-fix test coverage gaps |

## How Codex Should Use These Agents

## 1) Auto-selection behavior
Codex should use role descriptions as routing hints. If user intent is explicit (for example “review this diff for regressions”), select the matching reviewer directly.

## 2) Explicit invocation behavior
For critical tasks, prefer explicit role calls in prompts to avoid ambiguous routing.

Recommended explicit patterns:
- `Use architect for planning` when requirements are still fluid.
- `Use engineer for implementation` after scope is fixed.
- `Use qa_tester for final validation` before declaring done.
- Add reviewer/analyzer roles only where their specialization is needed.

## 3) Orchestration patterns

### Feature delivery
1. `architect` for boundaries and implementation phases.
2. `engineer` for code + tests.
3. `qa_tester` for realistic validation.
4. `code_reviewer` and `pr_test_analyzer` for merge readiness.

### Legacy feature understanding
1. `code_explorer` to map current behavior.
2. `code_architect` to propose target structure.
3. `engineer` to implement safely.

### Hardening loop
1. `silent_failure_hunter` for error-path audit.
2. `clean_code_reviewer` for maintainability cleanup.
3. `pr_test_analyzer` for regression guard coverage.

## Configuration Defaults (as migrated)

| Role | Model | Reasoning Effort | Reasoning Summary | Sandbox |
|---|---|---|---|---|
| `architect` | `gpt-5.3-codex` | `high` | `detailed` | `workspace-write` |
| `engineer` | `gpt-5.3-codex` | `high` | `detailed` | `workspace-write` |
| `qa_tester` | `gpt-5.3-codex` | `high` | `concise` | `workspace-write` |
| `docs_research_specialist` | `gpt-5.3-codex` | `medium` | inherited | `read-only` |
| `clean_code_reviewer` | `gpt-5.3-codex` | `medium` | inherited | `read-only` |
| `code_architect` | `gpt-5.3-codex` | `high` | inherited | `read-only` |
| `code_explorer` | `gpt-5.3-codex` | `medium` | inherited | `read-only` |
| `code_reviewer` | `gpt-5.3-codex` | `medium` | inherited | `read-only` |
| `silent_failure_hunter` | `gpt-5.3-codex` | `medium` | inherited | `read-only` |
| `pr_test_analyzer` | `gpt-5.3-codex` | `medium` | inherited | `read-only` |

## Important Implementation Detail
Each role TOML instructs the agent to load local bundled references first. This keeps role behavior deterministic and self-contained without relying on external `~/.claude/skills/...` paths.

## Migration Changes and Why

### Removed
- Voice notification hooks and `localhost` notifier calls.
- Placeholder voice IDs and persona theater.
- Mandatory emoji-heavy output templates.

### Kept
- Core role purpose.
- Useful quality constraints (planning discipline, evidence-based QA, reviewer focus).
- High-value workflows and task boundaries.

### Why these changes
- Reduce noise and brittle environment coupling.
- Improve portability and repeatability across machines.
- Keep agent behavior task-focused and operational.

## Recommended Prompting Patterns
- Be explicit about scope: files, branch, and success criteria.
- Ask for artifacts, not essays: file maps, checklists, findings, repro steps.
- For reviewers, provide exact diff scope.
- For QA, provide runnable target and expected behavior.

Examples:
- `Use code_explorer to map how billing retries currently work. Include key files and failure paths.`
- `Use architect to produce a phased implementation plan for adding idempotency keys.`
- `Use silent_failure_hunter on this diff and list only high-confidence failure risks.`
- `Use pr_test_analyzer to identify must-fix test gaps before merge.`

## Troubleshooting
- Agent not picked automatically: invoke explicitly by role name in the prompt.
- Behavior drift: verify role TOML references and restart session.
- Missing files: validate `.codex/config.toml` `config_file` links.
- Runtime mismatch: if using older Codex versions, role config fields may not be honored.

## Related Docs
- `docs/claude-subagents-inventory.md`
- `docs/multi-agents-curation.md`
- `docs/multi-agents-migration-notes.md`
