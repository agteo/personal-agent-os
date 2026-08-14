# Research Skill

## Purpose

Research a question and produce a decision-useful answer.

## When to use

Use when the user asks for information requiring investigation, comparison, or evidence.

## Inputs

- Question
- Desired depth
- Relevant project context
- Constraints or decision criteria

## Process

1. Understand the question.
2. Search existing memory.
3. Review relevant sources.
4. Gather external information if the provider has web access.
5. Compare evidence.
6. State confidence and uncertainty.
7. Produce findings.
8. Save durable insights only when likely to matter again.

## Output

A concise research brief with findings, trade-offs, recommendation if requested, and sources.

## Memory behaviour

Save only durable findings. Do not record every search result.

## Capability requirements

```yaml
requires:
  - filesystem
optional:
  - web
```

