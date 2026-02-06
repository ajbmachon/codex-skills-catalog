# Code Map Template

Use this template for architecture visualization: modules, services, data flow, boundaries, and integration paths.

## Codex intent

Give the user a visual model of the system and a structured way to annotate what should change, then emit a precise implementation prompt.

## Recommended layout

```
+----------------------------+--------------------------------+
| Controls                   | Diagram canvas (SVG preferred) |
| - view presets             | - nodes + typed edges          |
| - layer filters            | - zoom + pan                   |
| - relation filters         | - selection highlights         |
| - comment list             |                                |
+----------------------------+--------------------------------+
| Prompt Output + actions                                      |
| [Copy] [Send to Codex]                                       |
+--------------------------------------------------------------+
```

## Model design

Nodes should include:

- stable id
- display label
- optional file path/subtitle
- layer classification
- position data

Edges should include:

- source + target
- relation type
- optional label
- visibility state

## Interaction expectations

- Toggle visibility by layer and relation type.
- Click node to add change comments.
- Keep comment list editable and tied to node ids.
- Support presets (full view, backend only, data path, etc.).

## Prompt output strategy

Prompt should summarize selected scope and concrete requested changes.

Example style:

> In the backend and data layers, update retry behavior for `queue-worker` and `event-dispatcher`. Add idempotency checks between `api-handler -> command-service -> postgres` and preserve current public API contracts.

## Creative latitude

- Diagram can be clean enterprise, editorial map, or sketch-like style if readable.
- Relation taxonomy should be customizable per project domain.
- Presets should guide exploration, not lock users into one interpretation.

## Output contract

- Single-file HTML with inline CSS/JS.
- Live prompt regeneration from current selections/comments.
- Include Copy and Send-to-Codex actions (`prompt-output`, `send-btn`).
