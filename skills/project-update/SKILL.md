# Project Update Skill

## Purpose

Create concise project updates using project memory, decisions, and the user's communication preferences.

## When to use

Use when the user asks for a status update, weekly update, stakeholder note, or progress summary.

## Inputs

- Project name
- Audience
- Time period
- Desired tone and length

## Process

1. Read `memory/index.md`.
2. Read the relevant project memory.
3. Check recent decisions and source notes.
4. Check user communication preferences.
5. Draft the update with progress, risks, blockers, and next steps.

## Output

A ready-to-edit project update.

## Memory behaviour

If the update reveals durable project changes, ask whether to update project memory.

## Capability requirements

```yaml
requires:
  - filesystem
```

