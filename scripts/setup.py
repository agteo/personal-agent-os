#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.providers import provider_names, runtime_status
from lib.workspace import setup_workspace


PROVIDER_LABELS = {
    "claude": "Claude Code",
    "openai": "OpenAI / Codex",
    "gemini": "Gemini CLI",
    "ollama": "Ollama / local model",
    "generic": "Generic / configure later",
}


def ask(prompt: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    answer = input(f"{prompt}{suffix}: ").strip()
    return answer or default


def choose_provider() -> str:
    names = provider_names()
    print("\nWhich AI runtime would you like to use?\n")
    for index, provider_id in enumerate(names, start=1):
        print(f"[{index}] {PROVIDER_LABELS[provider_id]}")
    while True:
        answer = ask("\nSelect", "5")
        if answer.isdigit() and 1 <= int(answer) <= len(names):
            return names[int(answer) - 1]
        if answer in names:
            return answer
        print("Please choose a number from the list.")


def main() -> int:
    root = Path.cwd()
    print("Welcome to your Personal Agent OS.\n")
    print("This setup creates readable Markdown memory, sources, skills, and provider config.")
    name = ask("\nWhat should your AI assistant call you?")
    role = ask("What kind of work or study do you usually do?")
    help_areas = ask("What are 2-3 things you would like your AI assistant to help with?")
    provider_id = choose_provider()
    created = setup_workspace(root, name, role, help_areas, provider_id)
    status, message = runtime_status(provider_id)
    print("\nSetup complete.")
    print(f"- Provider: {PROVIDER_LABELS[provider_id]}")
    print(f"- Memory index: {root / 'memory' / 'index.md'}")
    if created:
        print(f"- Starter memory files created: {len(created)}")
    print(f"- Runtime check: {message}")
    print("\nNext steps:")
    print("1. Run `python3 scripts/doctor.py` on macOS/Linux or `py scripts\\doctor.py` on Windows.")
    print("2. Start your selected AI runtime.")
    print("3. Ask it to read `AGENTS.md`.")
    print("4. Say: `Use the onboarding skill to help me personalize this workspace.`")
    if status == "warn":
        print("\nNote: your selected runtime may need installation or manual configuration.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
