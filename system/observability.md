# Observability

This workspace provides local auditability by default, not full runtime tracing.

## What Exists By Default

- `logs/activity.md` records visible actions.
- `logs/memory-changes.md` records material memory updates.
- `memory/index.md` helps users inspect what the agent believes it knows.
- `sources/` preserves original evidence separately from interpreted memory.

These files are useful for human review, portability, and lightweight debugging.

## What Is Not Included By Default

This starter does not include:

- model-call traces
- token or cost tracking
- latency dashboards
- prompt and completion capture
- tool-call span trees
- hosted eval datasets
- Langfuse, OpenTelemetry, Braintrust, Helicone, or similar integrations

Add those only when there is an actual runner, service, or app layer making model calls.

## If You Add Hosted Observability

Prefer an optional integration over a mandatory dependency.

Recommended shape:

```yaml
observability:
  enabled: false
  provider: langfuse
  capture_prompts: false
  capture_completions: false
  capture_tool_inputs: false
  redact_sources: true
```

Use environment variables for secrets:

```text
LANGFUSE_PUBLIC_KEY
LANGFUSE_SECRET_KEY
LANGFUSE_HOST
```

## Privacy Rules

Before sending traces to an external service:

1. Treat `sources/` as private evidence by default.
2. Redact secrets, credentials, personal identifiers, and sensitive business material.
3. Avoid capturing full prompts or completions unless the user explicitly opts in.
4. Log trace IDs locally when useful, but do not make hosted tracing required for normal workspace use.

## Implementation Notes

If a future runtime wrapper is added, instrument the boundary where model calls and tool calls happen:

- create one trace per user task
- create spans for model calls, tool calls, file edits, and memory writes
- attach provider, model, duration, token counts, and status when available
- store only the trace ID in `logs/activity.md` unless richer local logging is explicitly desired

The filesystem should remain understandable even when observability is disabled.
