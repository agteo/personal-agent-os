# OpenAI Codex Adapter

## How OpenAI/Codex Discovers Instructions

OpenAI-compatible coding agents should be directed to read `AGENTS.md` as the canonical instruction file.

## File Access

Codex-style agents can typically read and edit workspace files and run shell commands depending on configuration.

## Skills

Skills live in `skills/*/SKILL.md`. The agent should read the matching skill before using it.

## Capabilities

```yaml
filesystem: true
shell: true
web: true
mcp: false
structured_tools: true
```

Actual availability depends on the client.

## Start

```bash
codex
```

## Limitations

Some OpenAI-compatible tools may not support MCP or persistent local tool state. Use the Markdown workspace as the portable layer.

