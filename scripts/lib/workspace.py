from __future__ import annotations

from datetime import date
from pathlib import Path

from .indexer import rebuild_index
from .providers import write_provider_config


REQUIRED_DIRS = [
    "system",
    "memory/user",
    "memory/projects",
    "memory/people",
    "memory/organisations",
    "memory/decisions",
    "memory/topics",
    "sources/inbox",
    "sources/documents",
    "sources/notes",
    "skills",
    "workflows",
    "logs",
    "adapters",
    "config",
    "templates",
]


def ensure_dirs(root: Path) -> None:
    for rel in REQUIRED_DIRS:
        (root / rel).mkdir(parents=True, exist_ok=True)


def write_if_missing(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def setup_workspace(
    root: Path,
    name: str,
    role: str,
    help_areas: str,
    provider_id: str,
    workspace_name: str = "My Personal Agent OS",
) -> list[Path]:
    ensure_dirs(root)
    today = date.today().isoformat()
    created: list[Path] = []
    files = {
        root / "memory/user/profile.md": f"""# User Profile

## Name

{name or "Not set yet."}

## Role

{role or "Not set yet."}

## Responsibilities

- Not set yet.

## Goals

- Not set yet.

## Last updated

{today}
""",
        root / "memory/user/preferences.md": f"""# User Preferences

## Communication

- Not set yet.

## Working Preferences

- Not set yet.

## AI Assistance Preferences

- {help_areas or "Not set yet."}

## Last updated

{today}
""",
        root / "memory/user/working-style.md": f"""# Working Style

## Best Ways To Help

- Not set yet.

## Recurring Tasks

- Not set yet.

## Human Checkpoints

- Ask before high-impact or irreversible actions.

## Last updated

{today}
""",
        root / "logs/activity.md": "# Activity Log\n\nAppend visible actions here. Do not log private reasoning.\n",
        root / "logs/memory-changes.md": "# Memory Changes\n\nAppend material memory changes here. Do not log raw chain-of-thought.\n",
    }
    for path, content in files.items():
        if write_if_missing(path, content):
            created.append(path)
    write_provider_config(root, provider_id, workspace_name)
    rebuild_index(root)
    return created


def check_structure(root: Path) -> list[str]:
    missing = []
    for rel in REQUIRED_DIRS:
        if not (root / rel).exists():
            missing.append(rel)
    for rel in ("AGENTS.md", "memory/index.md"):
        if not (root / rel).exists():
            missing.append(rel)
    return missing

