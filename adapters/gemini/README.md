# Gemini CLI Adapter

## How Gemini Discovers Instructions

Gemini CLI users should direct Gemini to read `GEMINI.md`, which points to `AGENTS.md`.

## File Access

Gemini CLI can usually inspect workspace files and may edit them depending on configuration.

## Skills

Skills live in `skills/*/SKILL.md`.

## Capabilities

```yaml
filesystem: true
shell: true
web: true
mcp: false
structured_tools: true
```

Actual availability depends on local setup.

## Start

```bash
gemini
```

## Limitations

Gemini-specific conventions should stay in this adapter.

