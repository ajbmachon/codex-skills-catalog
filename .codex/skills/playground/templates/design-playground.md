# Design Playground Template

Use this template for visual UI decisions: component style, layout structure, typography, spacing, color systems, motion, and responsive behavior.

## Codex intent

Build a playground that helps the user decide visually, then emits an implementation-ready prompt for Codex.

## Recommended layout

```
+-----------------------+---------------------------+
| Controls              | Live Preview              |
| - Layout              | - component/page state    |
| - Spacing             | - interactive states      |
| - Typography          | - light/dark contexts     |
| - Color + effects     |                           |
| - Motion              +---------------------------+
| - Presets             | Prompt Output + actions   |
|                       | [Copy] [Send to Codex]    |
+-----------------------+---------------------------+
```

## Control palette

| Decision | Good controls |
|---|---|
| Size and spacing | Sliders with visible numeric value |
| Style modes | Preset chips/cards |
| Binary features | Toggle switches |
| Palette selection | Color swatches + optional HSL/hex |
| Animation profile | Dropdown + duration slider |
| Responsiveness | Viewport width slider + preset breakpoints |

## Preview behavior

- Update preview instantly on every control change.
- Show at least one interaction state (hover/focus/active) when relevant.
- Include context switching when needed (surface/background, light/dark, dense/airy).
- Use realistic sample content, not lorem-only placeholders.

## Prompt output strategy

Prompt text should read like direction to an implementer, not a raw value dump.

- Mention only non-default choices.
- Combine quantitative and qualitative language.
- Include stack-aware hints when known (Tailwind classes, CSS variables, design tokens, etc.).

Example style:

> Update the dashboard card to feel editorial and crisp: 10px radius, compact 12px vertical rhythm, semibold labels, and a restrained accent border. Keep hover lift subtle and preserve AA contrast.

## Creative latitude (do not over-constrain)

- Offer 3-5 stylistic presets that are intentionally different.
- Allow users to blend presets with manual tuning.
- Do not force one visual language unless user asked for strict branding.
- Keep advanced controls available behind an "Advanced" disclosure, not removed.

## Code pattern

```javascript
const state = { ...DEFAULTS };

function updateAll() {
  renderPreview();
  updatePrompt();
}

function bindControl(id, apply) {
  const el = document.getElementById(id);
  el.addEventListener("input", () => {
    apply(el.value);
    updateAll();
  });
}
```

## Output contract

- Single self-contained HTML file (inline CSS/JS, no external dependencies).
- `id="prompt-output"` present.
- Copy action includes success feedback.
- Send action uses the shared Codex sync snippet from `SKILL.md` (`id="send-btn"`).
- Works on desktop and mobile.
