# Sandboxing

This repository is a workspace convention, not a security boundary by itself.

The agent should not be exposed to the user's entire local device by default. The intended pattern is to run the selected AI runtime with access scoped to this workspace folder and temporary working directories.

## Default Boundary

Use this folder as the default boundary:

```text
personal-agent-os/
```

Within that boundary, the agent may usually:

- read workspace instructions, memory, skills, workflows, and sources
- search workspace text
- create or update Markdown memory
- append activity and memory-change logs
- draft documents or plans inside the workspace

Outside that boundary, the agent should treat files as private unless the user explicitly grants access.

## Practical Guidance

- Do not run this workspace from the root of a home directory.
- Keep the repo in a dedicated project folder.
- Treat `sources/` as the intentional import boundary for private evidence.
- Put only material the agent should use into `sources/`.
- Keep secrets in environment variables or a secret manager, not in `memory/`, `sources/`, or logs.
- Use runtime sandboxing or permission prompts where available.
- Prefer read-only access for external folders when possible.
- Ask before scanning broad paths such as `~/Documents`, `~/Desktop`, downloads, browser profiles, email exports, cloud-sync folders, or company repositories.
- Ask before sending local source content to hosted models, tracing tools, search APIs, or other external services.
- Ask before installing software, changing shell startup files, modifying system settings, or deleting files.

## Runtime Expectations

Different runtimes enforce boundaries differently:

- CLI coding agents may have filesystem permissions, shell access, and approval prompts.
- API-hosted models have no local filesystem access unless a wrapper gives it to them.
- Local models have no local filesystem access unless an agent runtime gives it to them.
- Browser, email, calendar, and cloud-drive connectors can expose external account data and should be treated as separate permission surfaces.

If a runtime cannot enforce sandboxing, compensate with a narrow working directory, explicit file-passing, and conservative approvals.

## Approval Rule

Ask for approval before:

- reading or searching outside the workspace
- writing outside the workspace
- deleting files
- changing core system instructions
- installing dependencies or software
- sending messages externally
- exposing private source files to external providers
- connecting new tools, plugins, or accounts

If the user grants a broader permission, keep the scope as narrow as possible and explain what path, account, or service is being accessed.

## What To Log

Log visible actions in `logs/activity.md`, such as:

- external folders intentionally inspected
- source files imported into the workspace
- new tools or connectors configured
- sandbox or permission assumptions that materially affect future use

Do not log secrets, raw private content, or private reasoning.
