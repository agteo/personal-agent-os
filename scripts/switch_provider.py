#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.providers import (
    OPENROUTER_MODEL_CHOICES,
    get_provider,
    provider_names,
    read_default_provider,
    runtime_status,
    write_provider_config,
)


def choose_openrouter_model() -> str:
    print("\nChoose an OpenRouter model profile:\n")
    for index, choice in enumerate(OPENROUTER_MODEL_CHOICES, start=1):
        recommended = " (recommended)" if choice["id"] == "auto" else ""
        print(f"{index}. {choice['label']}{recommended}")
        print(f"   {choice['model']} - {choice['description']}")
    print(f"{len(OPENROUTER_MODEL_CHOICES) + 1}. Custom model slug")
    while True:
        answer = input("\nSelect [1]: ").strip() or "1"
        if answer.isdigit():
            selected = int(answer)
            if 1 <= selected <= len(OPENROUTER_MODEL_CHOICES):
                return OPENROUTER_MODEL_CHOICES[selected - 1]["model"]
            if selected == len(OPENROUTER_MODEL_CHOICES) + 1:
                custom = input("Paste an OpenRouter model slug: ").strip()
                if custom:
                    return custom
        for choice in OPENROUTER_MODEL_CHOICES:
            if answer in {choice["id"], choice["model"]}:
                return choice["model"]
        print("Please choose a number from the list or enter a listed model slug.")


def main() -> int:
    root = Path.cwd()
    config_path = root / "config" / "config.yaml"
    current = read_default_provider(config_path)
    names = provider_names()
    print("Choose your AI runtime:\n")
    for index, provider_id in enumerate(names, start=1):
        provider = get_provider(provider_id)
        marker = " (current)" if provider_id == current else ""
        print(f"{index}. {provider['name']}{marker}")
    answer = input("\nSelect: ").strip()
    if not answer:
        print("No change made.")
        return 0
    if answer.isdigit() and 1 <= int(answer) <= len(names):
        selected = names[int(answer) - 1]
    elif answer in names:
        selected = answer
    else:
        print(f"Unknown provider: {answer}")
        return 2
    model = choose_openrouter_model() if selected == "openrouter" else None
    write_provider_config(root, selected, model=model)
    status, message = runtime_status(selected)
    print(f"\nProvider changed to {get_provider(selected)['name']}.")
    if model:
        print(f"Model: {model}")
    print("Memory and sources were not modified.")
    print(f"Runtime check: {message}")
    if status == "warn":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
