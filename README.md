# Your Personal Agent OS

Most AI chats forget what happened before.

This project gives your AI a home.

Inside this folder, your assistant can gradually learn:

- who you are
- what you are working on
- how you like to work
- what decisions you have made
- what tools and workflows it can use

You own the files.

The knowledge lives in this workspace, not inside one AI provider. You can use the same memory with Claude Code, OpenAI Codex, Gemini CLI, Ollama, OpenRouter-backed tools, Cursor-style coding agents, or future tools that can read and edit files.

## The Big Idea

```text
PERSONAL AGENT OS

User
  |
  v
Agent Runtime
  |
  |-- Rules
  |-- Memory
  |-- Skills
  |-- Sources
  `-- Tools
```

The core loop is:

```text
Observe -> Understand -> Act -> Remember
```

- Observe: user requests, files, notes, and tools
- Understand: reasoning performed by the selected model
- Act: write, research, analyze, organize, create, or run tools
- Remember: update durable workspace knowledge when appropriate

This is not a complicated agent framework. The filesystem conventions are the architecture.

## Folder Map

```text
Brain       -> memory/
Evidence    -> sources/
Abilities   -> skills/
Workflows   -> workflows/
Rules       -> system/ and AGENTS.md
History     -> logs/
AI engine   -> adapters/ and config/
```

Important separation:

- `sources/` contains original material supplied by you. The agent should not silently rewrite it.
- `memory/` contains agent-maintained summaries, beliefs, preferences, project knowledge, and decisions.
- `system/` contains behavior rules.
- `skills/` contains reusable Markdown instructions for tasks.
- `adapters/` contains provider-specific notes. The core workspace does not belong to any one provider.

## Inspired By LLM Wiki

This project is inspired by Andrej Karpathy's LLM Wiki idea: durable knowledge can be written down, improved, and reused by models over time.

```text
Raw information
      |
      v
AI-maintained knowledge
      |
      v
Continuously improved understanding
```

This starter extends that pattern from persistent knowledge toward:

```text
persistent knowledge + skills + workflows + tools
```

This is not an endorsement by Andrej Karpathy. It is an educational implementation of the broader pattern.

## Start Here

macOS or Linux:

```bash
python3 scripts/setup.py
```

Windows:

```powershell
py scripts\setup.py
```

The setup script asks a few questions, creates your starter memory, configures your selected AI runtime, and tells you what to run next.

For more detail, read [INSTALL.md](INSTALL.md).

## Four Levels Of Use

Level 1, simple generation:

```text
Help me write a short project update.
```

Level 2, personalized task:

```text
Write a project update using my preferred communication style.
```

Level 3, context-rich task:

```text
Prepare an update on Project Atlas using everything we know about it.
```

Level 4, agentic task:

```text
Research three approaches to the problem Project Atlas is facing,
compare them against our requirements, recommend an approach,
and prepare a briefing.
```

As tasks become more sophisticated, the architecture stays the same: the agent reads memory, checks sources, uses skills, acts, and updates memory only when appropriate.

## Human Checkpoints

More automation is not always better. This starter uses clear operating modes:

- Assist: help think, draft, or explain
- Recommend: compare options and suggest a path
- Act with approval: prepare an action, then ask before doing it
- Act autonomously: proceed when the action is low-risk and reversible

Default examples:

- Research: autonomous when web/tools are available
- Draft email: autonomous
- Send email: approval
- Delete files: approval
- Change core system instructions: approval
- Rewrite original source material: do not do this silently

## Example Student Journey

Day 1:

You install the repository. The AI interviews you. Memory now contains your profile, preferences, and maybe one project.

Day 3:

You drop meeting notes into `sources/inbox/` and say:

```text
Process my inbox.
```

The agent preserves the original notes, creates summaries if useful, and updates relevant memory.

Day 7:

You say:

```text
Prepare me for tomorrow's Project Atlas meeting.
```

The agent uses accumulated project context, decisions, sources, and your preferences.

Week 3:

You create:

```text
skills/customer-interviews/SKILL.md
```

Your workspace is now becoming your personal operating environment, not merely a chatbot.

## Try The Demo Workspace

Open:

```text
examples/demo-workspace/
```

It contains a fictional student profile, project, notes, decision, and memory index. No real personal information is included.

## Switching AI Providers

Run:

macOS or Linux:

```bash
python3 scripts/switch_provider.py
```

Windows:

```powershell
py scripts\switch_provider.py
```

Switching providers updates configuration and wrapper files. It does not modify `memory/` or `sources/`.

Supported starter providers:

- Claude Code
- OpenAI Codex / OpenAI-compatible coding agents
- Gemini CLI
- Ollama / local models
- OpenRouter / hosted model catalog
- Generic / configure later

When you choose OpenRouter, setup offers a short model menu:

- Auto Router: easiest default
- Free Models Router: low-friction trial option
- Latest OpenAI flagship alias
- Latest Claude Sonnet alias
- Custom model slug

Different providers have different capabilities. This starter does not pretend they are identical.

## Diagnose Problems

Run:

macOS or Linux:

```bash
python3 scripts/doctor.py
```

Windows:

```powershell
py scripts\doctor.py
```

It checks the workspace structure, configuration, selected runtime, Python, Git, memory index, and common beginner issues.

## Common First-Time Confusions

If the agent seems lost, tell it:

```text
Read AGENTS.md, then read memory/index.md before looking at other memory files.
```

If a model cannot browse, run commands, or edit files, that is a provider capability difference. Check `adapters/` and `config/providers.yaml`.

If memory looks wrong, inspect `git diff`, then ask the agent to explain or revise the memory update. Original evidence in `sources/` should not be silently rewritten.

If context gets too large, start from `memory/index.md` and only open the relevant files. Do not paste the whole workspace into a simple model.

If you are unsure where something belongs:

- raw notes and documents go in `sources/`
- durable summaries and preferences go in `memory/`
- behavior rules go in `system/`
- reusable task instructions go in `skills/`
- repeatable sequences go in `workflows/`

## Git As A Safety Net

Git lets you see what changed:

```bash
git diff
```

If your agent updates memory, inspect the diff. You do not need to become a Git expert, but version history helps you stay in control.

## Experiment

Try changing your agent's operating principles. Create a new skill. Add a workflow. Switch models. Compare how different models use the same memory. Give your agent a new source document. Ask it to reorganize memory. Inspect the Git diff.

The teaching goals are simple:

1. The model is not the whole agent.
2. Persistent context can live outside the model.
3. Memory can be represented as files.
4. Instructions shape agent behavior.
5. Skills describe reusable capabilities.
6. Workflows compose capabilities.
7. Tools let agents act on the world.
8. Different models can operate over the same workspace.
9. Human judgment still matters.
10. You can inspect and modify every important part of your agent.
