#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.providers import get_provider, provider_names, read_default_provider, runtime_status, write_provider_config


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
    write_provider_config(root, selected)
    status, message = runtime_status(selected)
    print(f"\nProvider changed to {get_provider(selected)['name']}.")
    print("Memory and sources were not modified.")
    print(f"Runtime check: {message}")
    if status == "warn":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

