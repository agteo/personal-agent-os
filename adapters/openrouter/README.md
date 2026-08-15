# OpenRouter Adapter

OpenRouter gives this workspace access to a hosted model catalog through an OpenAI-compatible API.

## Instruction Discovery

Tell the runtime or tool using OpenRouter:

```text
Read AGENTS.md and follow it as the canonical workspace instructions.
```

## Credentials

Set an OpenRouter API key in your shell or local environment:

```bash
export OPENROUTER_API_KEY=sk-or-v1-...
```

Use this API base URL in tools that support custom OpenAI-compatible endpoints:

```text
https://openrouter.ai/api/v1
```

## Choosing A Model

For first setup, use `openrouter/auto`. It lets OpenRouter route requests without forcing the user to understand every model family.

Other simple choices:

- `openrouter/free`: try the workspace with free models.
- `~openai/gpt-latest`: use OpenAI's latest flagship alias.
- `~anthropic/claude-sonnet-latest`: use the latest Claude Sonnet family alias.
- Any explicit OpenRouter model slug from the model catalog.

OpenRouter model slugs usually use `provider/model` format. Latest aliases can start with `~`.

## Capabilities

```yaml
filesystem: partial
shell: false
web: false
mcp: false
structured_tools: true
```
