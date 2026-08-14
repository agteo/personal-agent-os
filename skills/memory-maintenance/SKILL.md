# Memory Maintenance Skill

## Purpose

Keep memory useful, concise, and navigable.

## When to use

Use when the user says to maintain memory, rebuild the index, process stale notes, merge duplicate entries, or clean up memory.

## Inputs

- Target area of memory
- Whether user wants suggestions only or approved edits

## Process

1. Read `memory/index.md`.
2. Identify duplicate, stale, unclear, or overly long entries.
3. Preserve provenance.
4. Prefer consolidation over deletion.
5. Mark contradictions and uncertainty instead of hiding them.
6. Update `memory/index.md`.
7. Log material changes.

## Output

A short maintenance report listing what changed and what still needs human judgment.

## Memory behaviour

Memory maintenance edits memory directly only when policy and user request allow it. Do not delete potentially important information without approval.

## Capability requirements

```yaml
requires:
  - filesystem
```

