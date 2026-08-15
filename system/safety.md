# Safety And Privacy

This workspace may contain personal data.

Do not commit secrets, API keys, tokens, passwords, or private credentials.

Treat `memory/` and `sources/` as potentially private.

Run the agent with workspace-scoped filesystem permissions when the runtime supports it.

Do not inspect broad local paths outside this workspace unless the user explicitly approves the specific scope.

Before sending source content to an external provider, consider whether the user understands that the provider may receive that content.

Local model providers such as Ollama may keep more work local, but may also have fewer capabilities.
