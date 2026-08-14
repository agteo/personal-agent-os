# Ollama Adapter

## How Ollama Discovers Instructions

Ollama by itself is a local model server, not a full coding agent. A user or lightweight runner may need to paste or inject relevant files such as `AGENTS.md`, `memory/index.md`, and selected memory files.

## File Access

Plain Ollama models do not automatically read or edit files. File access depends on the client wrapped around Ollama.

## Skills

Skills are still readable Markdown. For simple local-model usage, paste the relevant skill and memory context into the prompt.

## Capabilities

```yaml
filesystem: partial
shell: false
web: false
mcp: false
structured_tools: false
```

## Start

```bash
ollama serve
ollama run qwen3
```

## Limitations

Local models may keep data local, but they may require more manual context selection and may not use tools.

