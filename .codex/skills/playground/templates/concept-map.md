# Concept Map Template

Use this template for learning and systems understanding: concept maps, dependency maps, knowledge-gap mapping, decomposition, and relationship reasoning.

## Codex intent

Turn a fuzzy topic into a navigable concept graph that captures what the user knows, what they do not know, and what relationships need explanation.

## Recommended layout

```
+----------------------------------------------+
| Interactive canvas (nodes + relationships)   |
+-----------------------------+----------------+
| Sidebar                     | Prompt Output  |
| - Knowledge levels          | + actions      |
| - Relationship type         | [Copy] [Send]  |
| - Visibility filters        |                |
| - Presets + auto-layout     |                |
+-----------------------------+----------------+
```

## Interaction model

- Drag nodes to reflect mental model.
- Connect nodes with typed edges (depends on, calls, owns, reads, etc.).
- Let each node carry knowledge state (known/fuzzy/unknown/custom).
- Support quick reset and auto-layout.

## Rendering guidance

- Use `<canvas>` or `<svg>` depending on interaction complexity.
- Draw edges first, nodes second for clarity.
- Show labels clearly at normal zoom.
- Include simple legend and keyboard-accessible alternatives where possible.

## Prompt output strategy

Prompt should ask for targeted explanation, not generic teaching.

Include:

- Topic and scope
- What user already understands
- What remains fuzzy/unknown
- Relationships user wants explained
- Preferred depth and format

Example style:

> Explain this architecture map with emphasis on unknown nodes (`event bus`, `retry worker`) and fuzzy relationships (`api-gateway -> auth-service`, `worker -> redis`). Build from known components first and include concrete code-level examples.

## Creative latitude

- Node visuals can be playful or formal as long as readability stays high.
- Relationship vocabulary should be editable for domain fit.
- Allow custom tags beyond known/fuzzy/unknown when useful.

## Output contract

- Self-contained HTML with live updates.
- Prompt reflects only current visible/selected state.
- Include Copy and Send-to-Codex actions (`prompt-output`, `send-btn`).
