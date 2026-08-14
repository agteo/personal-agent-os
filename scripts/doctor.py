#!/usr/bin/env python3
from __future__ import annotations

import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.providers import get_provider, read_default_provider, runtime_status
from lib.workspace import check_structure


def ok(message: str) -> None:
    print(f"OK  {message}")


def warn(message: str) -> None:
    print(f"WARN {message}")


def fail(message: str) -> None:
    print(f"FAIL {message}")


def main() -> int:
    root = Path.cwd()
    exit_code = 0
    print("Personal Agent OS Doctor\n")
    missing = check_structure(root)
    if missing:
        exit_code = 1
        fail("Workspace structure is incomplete.")
        for item in missing:
            print(f"     Missing: {item}")
    else:
        ok("Workspace structure")
    if (root / "AGENTS.md").exists():
        ok("Canonical instructions: AGENTS.md")
    else:
        fail("AGENTS.md is missing")
        exit_code = 1
    if (root / "memory" / "index.md").exists():
        ok("Memory index")
    else:
        fail("memory/index.md is missing")
        exit_code = 1
    provider_id = read_default_provider(root / "config" / "config.yaml")
    try:
        provider = get_provider(provider_id)
        ok(f"Provider configuration: {provider['name']}")
        status, message = runtime_status(provider_id)
        if status == "ok":
            ok(message)
        else:
            warn(message)
    except ValueError as exc:
        fail(str(exc))
        exit_code = 1
    if shutil.which("git"):
        ok("Git detected")
    else:
        warn("Git was not found. Git is optional, but useful as a safety net.")
    version = sys.version_info
    if version.major == 3 and version.minor >= 9:
        ok(f"Python {version.major}.{version.minor}.{version.micro}")
    else:
        fail("Python 3.9 or newer is recommended.")
        exit_code = 1
    if not (root / ".env").exists():
        ok("No .env file detected. Secrets are not being tracked by default.")
    else:
        warn(".env exists. Make sure it is not committed.")
    provider_id = read_default_provider(root / "config" / "config.yaml")
    if provider_id == "ollama":
        warn("Web search is unavailable by default for plain Ollama.")
    if not (root / ".mcp.json").exists():
        warn("No MCP configuration detected. This is fine for v1.")
    print("\nDoctor complete.")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())

