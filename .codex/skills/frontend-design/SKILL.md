---
name: frontend-design
description: Design and implement production-ready frontend interfaces with a clear visual direction and high UX quality, then validate responsive and accessible behavior. Use when the user asks for UI page/component/app implementation, redesigns, landing pages, dashboards, or design-system work, especially when they ask for polished, premium, or distinctive visuals.
---

# Frontend Design Skill (GPT-5.3-Codex)

Build production-ready frontend code with a strong visual point of view, not generic UI output.

## Trigger cases

- user asks for a page, component, app shell, redesign, landing page, dashboard, or design system work
- user asks for "beautiful", "premium", "bold", "distinctive", or "high quality" frontend

## Codex execution workflow

1. Read local project constraints first: framework/runtime, existing design system/tokens, CSS/Tailwind strategy, routing/build/component conventions.
2. If existing system exists, preserve it.
3. If greenfield, choose one clear visual direction and commit.
4. Implement code directly in project files (do not stop at concepts).
5. Validate by running build/type/lint/tests when available, checking desktop/mobile behavior, and confirming no broken initial state.

## Design direction checklist

- Purpose: what the interface must help user do.
- Audience tone: refined, playful, editorial, industrial, etc.
- Signature move: one memorable design choice.
- Interaction profile: subtle, expressive, or dramatic motion.

## Visual quality rules

- Typography: avoid default/system-heavy stacks when a stronger choice is appropriate, and pair display/body fonts intentionally.
- Color and theming: define tokens/CSS variables up front and use deliberate contrast hierarchy.
- Layout: avoid boilerplate symmetry unless intentionally minimal; use consistent rhythm in spacing and scale.
- Motion: prefer meaningful transitions and staged reveals; motion should improve comprehension.
- Surfaces/background: add depth (gradient, texture, layering, shape) when it supports the concept.

## Hard constraints

- No generic "AI template" look.
- No purple-on-white default gradient style unless explicitly requested.
- No placeholder-only deliverables; always provide working implementation.
- Accessibility is mandatory (focus states, semantic structure, contrast).
- Responsive behavior is mandatory.

## Output expectations

- Return implemented files, not just recommendations.
- Keep code maintainable and idiomatic for the target stack.
- Briefly explain key design choices and tradeoffs after implementation.

## Deterministic acceptance checklist

- Capture the selected visual direction in 2-4 bullets before coding.
- Verify responsive behavior at mobile and desktop breakpoints.
- Run the strongest available local checks (`build`, `typecheck`, `lint`, `test`) and report which commands ran.
- Validate keyboard focus visibility, semantic landmarks, and contrast for primary text/actions.
- Confirm no dead controls and no broken initial render state.
