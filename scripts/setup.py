#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.providers import OPENROUTER_MODEL_CHOICES, provider_names, runtime_status
from lib.workspace import setup_workspace


PROVIDER_LABELS = {
    "claude": "Claude Code",
    "openai": "OpenAI / Codex",
    "gemini": "Gemini CLI",
    "ollama": "Ollama / local model",
    "openrouter": "OpenRouter / hosted model catalog",
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
        answer = ask("\nSelect", str(len(names)))
        if answer.isdigit() and 1 <= int(answer) <= len(names):
            return names[int(answer) - 1]
        if answer in names:
            return answer
        print("Please choose a number from the list.")


def choose_openrouter_model() -> str:
    print("\nWhich OpenRouter model profile should this workspace use?\n")
    for index, choice in enumerate(OPENROUTER_MODEL_CHOICES, start=1):
        recommended = " (recommended)" if choice["id"] == "auto" else ""
        print(f"[{index}] {choice['label']}{recommended}")
        print(f"    {choice['model']} - {choice['description']}")
    print(f"[{len(OPENROUTER_MODEL_CHOICES) + 1}] Custom model slug")
    while True:
        answer = ask("\nSelect", "1")
        if answer.isdigit():
            selected = int(answer)
            if 1 <= selected <= len(OPENROUTER_MODEL_CHOICES):
                return OPENROUTER_MODEL_CHOICES[selected - 1]["model"]
            if selected == len(OPENROUTER_MODEL_CHOICES) + 1:
                custom = ask("Paste an OpenRouter model slug, for example openai/gpt-4o")
                if custom:
                    return custom
        for choice in OPENROUTER_MODEL_CHOICES:
            if answer in {choice["id"], choice["model"]}:
                return choice["model"]
        print("Please choose a number from the list or enter a listed model slug.")


def main() -> int:
    root = Path.cwd()
    print("Welcome to your Personal Agent OS.\n")
    print("This setup creates readable Markdown memory, sources, skills, and provider config.")
    name = ask("\nWhat should your AI assistant call you?")
    role = ask("What kind of work, learning, or personal projects do you usually do?")
    help_areas = ask("What are 2-3 things you would like your AI assistant to help with?")
    provider_id = choose_provider()
    model = choose_openrouter_model() if provider_id == "openrouter" else None
    created = setup_workspace(root, name, role, help_areas, provider_id, model=model)
    status, message = runtime_status(provider_id)
    print("\nSetup complete.")
    print(f"- Provider: {PROVIDER_LABELS[provider_id]}")
    if model:
        print(f"- Model: {model}")
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
