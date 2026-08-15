# Install

You need:

- Git
- Python 3.9 or newer
- One AI runtime, or choose Generic and configure later

Run:

macOS or Linux:

```bash
python3 scripts/setup.py
```

Windows:

```powershell
py scripts\setup.py
```

Then follow the prompts.

After setup, run:

macOS or Linux:

```bash
python3 scripts/doctor.py
```

Windows:

```powershell
py scripts\doctor.py
```

If your selected runtime is missing, the doctor will explain what to install.

The workspace still works as a readable folder even before an AI runtime is installed.

## Giving The Agent Material To Work With

The agent only knows about files inside this workspace. Nothing is imported automatically, and no email, calendar, or cloud-drive account is connected.

To give the agent something to work from, copy files into `sources/`:

- `sources/inbox/` for new items you want processed, such as meeting notes or an exported email thread
- `sources/notes/` for notes and meeting records you want to keep
- `sources/documents/` for longer documents

Then ask your agent:

```text
Process my inbox.
```
