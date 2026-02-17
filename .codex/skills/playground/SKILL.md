---
name: playground
description: Build single-file interactive HTML playgrounds with live preview, state-driven controls, generated prompt output, presets, and Codex sync hooks. Use when the user needs a visual sandbox or interactive explorer to iterate on design, data, mapping, or critique decisions that are cumbersome in plain text.
---

# Playground Skill (GPT-5.3-Codex)

Use this skill when the user needs an interactive HTML tool to explore choices visually and send structured prompts back to Codex.

## Trigger cases

- "build a playground", "explorer", "interactive dashboard/tool"
- visual decisions are hard to communicate in plain text
- rapid iteration on layout, color, spacing, filters, mappings, or critiques

## Codex workflow

1. Identify the closest template in `templates/`.
2. Inspect project styling first (`rg` for CSS variables, tokens, Tailwind config, theme files, UI primitives).
3. Build one self-contained `.html` file with inline CSS/JS.
4. Open it using platform-appropriate command (`open` on macOS, `xdg-open` on Linux, `start` on Windows, or `python -m webbrowser <file>.html`).
5. Check MCP availability before watch mode (for example, list MCP resources/templates and confirm `playground-sync` is present).
6. If `playground-sync` MCP is available, enter a watch loop: call `playground_watch`, execute the returned prompt, call `playground_clear`, then return to `playground_watch`.
7. If MCP is unavailable, keep copy/paste fallback and continue.

## Template map

- `templates/design-playground.md`: components, visual style, typography, spacing, motion
- `templates/data-explorer.md`: queries, filters, transforms, structured configs
- `templates/concept-map.md`: concepts, dependencies, understanding gaps
- `templates/document-critique.md`: review workflow with approve/reject/comment
- `templates/diff-review.md`: code diff review with line comments
- `templates/code-map.md`: architecture and data/tool flow mapping

## Required output contract

- Single file HTML only, no external deps.
- Immediate live preview on every control change.
- Prompt output in natural language, only non-default decisions.
- Copy button with clear feedback state.
- "Send to Codex" button posting to `http://localhost:4242/prompt`.
- 3-5 presets with sensible defaults.
- Works on desktop and mobile.

## Implementation rules

- Keep one canonical `state` object.
- Every input writes to `state`, then one `updateAll()` refreshes preview and prompt.
- Prefer simple, inspectable DOM updates over complex abstractions.
- Keep control count focused; move advanced controls into collapsible section.
- Ensure generated prompt is actionable without opening the playground.

## Codex sync snippet (required)

```html
<button id="send-btn" onclick="sendToCodex()">Send to Codex</button>
```

```javascript
const SYNC_URL = "http://localhost:4242";

async function sendToCodex() {
  const prompt = document.getElementById("prompt-output").textContent || "";
  const btn = document.getElementById("send-btn");
  btn.textContent = "Sending...";
  try {
    await fetch(`${SYNC_URL}/prompt`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt, url: location.href, pathname: location.pathname }),
    });
    btn.textContent = "Sent";
    setTimeout(() => (btn.textContent = "Send to Codex"), 1500);
  } catch {
    btn.textContent = "No server";
    setTimeout(() => (btn.textContent = "Send to Codex"), 2500);
  }
}

try {
  const es = new EventSource(`${SYNC_URL}/events`);
  es.addEventListener("status", (e) => {
    const d = JSON.parse(e.data);
    const btn = document.getElementById("send-btn");
    if (!btn) return;
    if (d.status === "processing") btn.textContent = "Codex working...";
    if (d.status === "done") {
      btn.textContent = "Done";
      setTimeout(() => (btn.textContent = "Send to Codex"), 1500);
    }
  });
} catch {}
```

## Quality bar

- No broken initial state.
- No dead controls.
- No stale prompt output.
- No inaccessible contrast for core UI text.
- No mismatch between preview and prompt language.
