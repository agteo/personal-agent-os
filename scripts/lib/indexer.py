from __future__ import annotations

from pathlib import Path


SECTIONS = {
    "User": "user",
    "Active Projects": "projects",
    "People": "people",
    "Organisations": "organisations",
    "Important Decisions": "decisions",
    "Topics": "topics",
}


def title_from_file(path: Path) -> str:
    try:
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    except UnicodeDecodeError:
        pass
    return path.stem.replace("-", " ").replace("_", " ").title()


def wiki_link(memory_root: Path, path: Path) -> str:
    rel = path.relative_to(memory_root).with_suffix("")
    return f"[[{rel.as_posix()}]]"


def markdown_files(folder: Path) -> list[Path]:
    if not folder.exists():
        return []
    return sorted(
        path
        for path in folder.glob("*.md")
        if path.name.lower() != "readme.md" and path.name.lower() != "index.md"
    )


def build_index(root: Path) -> str:
    memory_root = root / "memory"
    lines = [
        "# Memory Index",
        "",
        "Start here before browsing memory deeply.",
        "",
    ]
    for heading, folder_name in SECTIONS.items():
        lines.extend([f"## {heading}", ""])
        files = markdown_files(memory_root / folder_name)
        if files:
            for path in files:
                lines.append(f"- {wiki_link(memory_root, path)}")
        else:
            lines.append(empty_message(heading))
        lines.append("")
    lines.extend(
        [
            "## Maintenance Notes",
            "",
            "- Rebuild with `python3 scripts/rebuild_index.py` on macOS/Linux or `py scripts\\rebuild_index.py` on Windows.",
            "",
        ]
    )
    return "\n".join(lines)


def empty_message(heading: str) -> str:
    messages = {
        "User": "- No user memory recorded yet.",
        "Active Projects": "- No active projects yet.",
        "People": "- No people recorded yet.",
        "Organisations": "- No organisations recorded yet.",
        "Important Decisions": "- No decisions recorded yet.",
        "Topics": "- No topics recorded yet.",
    }
    return messages.get(heading, "- Nothing recorded yet.")


def rebuild_index(root: Path) -> Path:
    index_path = root / "memory" / "index.md"
    index_path.parent.mkdir(parents=True, exist_ok=True)
    index_path.write_text(build_index(root), encoding="utf-8")
    return index_path
