# Process Inbox Workflow

## Where inbox items come from

`sources/inbox/` is a folder the user fills manually. This workspace has no email, calendar, or cloud-drive connection, so nothing arrives in the inbox on its own.

If `sources/inbox/` is empty, do not report an error and do not go looking for the user's email. Say the inbox folder is empty, remind the user that items are added by copying files into `sources/inbox/`, and offer to work from `sources/notes/`, `sources/documents/`, or a file the user names instead.

## Steps

1. Inspect files in `sources/inbox/`.
2. Identify what each item concerns.
3. Preserve originals.
4. Create summaries only when useful.
5. Update relevant memory with provenance links.
6. Update `memory/index.md`.
7. Append entries to `logs/activity.md` and `logs/memory-changes.md`.
8. Report what changed and what needs human review.

