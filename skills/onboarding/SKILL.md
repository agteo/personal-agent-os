# Onboarding Skill

## Purpose

Help a new user turn this folder into a useful personal agent workspace.

## When to use

Use after setup, or when the user says they want to onboard, personalize, or teach the agent about themselves.

## Inputs

- User role, learning goals, or personal focus area
- Typical responsibilities
- Current projects
- Recurring tasks
- Preferred communication style
- Goals
- Common collaborators
- Areas where AI help would be useful

## Process

1. Ask a few high-value questions conversationally.
2. Do not ask 30 questions at once.
3. Summarize what you understood.
4. Ask before recording memory unless memory policy is `automatic`.
5. Update relevant files such as `memory/user/profile.md`, `memory/user/preferences.md`, and `memory/projects/`.
6. Explain what memory was written.
7. Update `memory/index.md` and `logs/memory-changes.md`.
8. Explain how the user supplies material: copy files into `sources/inbox/`, `sources/notes/`, or `sources/documents/`. Make clear that nothing is imported automatically and that no email, calendar, or cloud-drive account is connected to this workspace.

## Output

A short onboarding summary and a list of memory files updated.

## Memory behaviour

Save stable preferences, goals, role context, recurring responsibilities, and current projects.

Do not save secrets or temporary remarks.

## Capability requirements

```yaml
requires:
  - filesystem
```
