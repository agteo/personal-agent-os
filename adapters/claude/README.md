# Claude Code Adapter

## How Claude Discovers Instructions

Claude Code commonly reads `CLAUDE.md`. This repository keeps `AGENTS.md` canonical, so the root `CLAUDE.md` only points Claude to `AGENTS.md`.

## File Access

Claude Code can typically read and edit workspace files.

## Skills

Skills live in `skills/*/SKILL.md`. Ask Claude to read the relevant skill before using it.

## Capabilities

```yaml
filesystem: true
shell: true
web: true
mcp: true
structured_tools: true
```

Actual availability depends on local settings.

## Start

```bash
claude
```

## Limitations

Claude-specific features should not be required by core memory, sources, or skills.

