# Generic Adapter

Use this adapter for any future or unsupported AI runtime.

## Instruction Discovery

Tell the runtime:

```text
Read AGENTS.md and follow it as the canonical workspace instructions.
```

## Minimum Workflow

If the runtime cannot read files automatically:

1. Paste `AGENTS.md`.
2. Paste `memory/index.md`.
3. Paste relevant memory files.
4. Paste the relevant skill.
5. Ask the model to produce changes.
6. Apply changes manually if needed.

## Capabilities

```yaml
filesystem: partial
shell: false
web: false
mcp: false
structured_tools: false
```

