from __future__ import annotations

import copy
import shutil
from pathlib import Path
from typing import Any


PROVIDERS: dict[str, dict[str, Any]] = {
    "claude": {
        "name": "Claude Code",
        "type": "cli",
        "command": "claude",
        "adapter": "adapters/claude",
        "capabilities": {
            "filesystem": True,
            "shell": True,
            "web": True,
            "mcp": True,
            "structured_tools": True,
        },
    },
    "openai": {
        "name": "OpenAI Codex",
        "type": "cli",
        "command": "codex",
        "adapter": "adapters/openai",
        "capabilities": {
            "filesystem": True,
            "shell": True,
            "web": True,
            "mcp": False,
            "structured_tools": True,
        },
    },
    "gemini": {
        "name": "Gemini CLI",
        "type": "cli",
        "command": "gemini",
        "adapter": "adapters/gemini",
        "capabilities": {
            "filesystem": True,
            "shell": True,
            "web": True,
            "mcp": False,
            "structured_tools": True,
        },
    },
    "ollama": {
        "name": "Ollama",
        "type": "local",
        "base_url": "http://localhost:11434",
        "model": "qwen3",
        "adapter": "adapters/ollama",
        "capabilities": {
            "filesystem": "partial",
            "shell": False,
            "web": False,
            "mcp": False,
            "structured_tools": False,
        },
    },
    "generic": {
        "name": "Generic / configure later",
        "type": "manual",
        "adapter": "adapters/generic",
        "capabilities": {
            "filesystem": "partial",
            "shell": False,
            "web": False,
            "mcp": False,
            "structured_tools": False,
        },
    },
}


def provider_names() -> list[str]:
    return list(PROVIDERS.keys())


def get_provider(provider_id: str) -> dict[str, Any]:
    if provider_id not in PROVIDERS:
        raise ValueError(f"Unknown provider: {provider_id}")
    return copy.deepcopy(PROVIDERS[provider_id])


def runtime_status(provider_id: str) -> tuple[str, str]:
    provider = get_provider(provider_id)
    provider_type = provider.get("type")
    if provider_type == "manual":
        return "warn", "Manual provider selected; configure your runtime when ready."
    if provider_type == "local" and provider_id == "ollama":
        if shutil.which("ollama"):
            return "ok", "Ollama command detected."
        return "warn", "Ollama command was not found. Install Ollama from https://ollama.com/."
    command = provider.get("command")
    if command and shutil.which(command):
        return "ok", f"{command} command detected."
    if command:
        return "warn", f"{command} command was not found on PATH."
    return "warn", "No runtime command configured."


def wrapper_files(provider_id: str) -> dict[str, str]:
    if provider_id == "claude":
        return {"CLAUDE.md": "# Claude Code Wrapper\n\nRead `AGENTS.md` and follow it as the canonical workspace instructions.\n"}
    if provider_id == "gemini":
        return {"GEMINI.md": "# Gemini CLI Wrapper\n\nRead `AGENTS.md` and follow it as the canonical workspace instructions.\n"}
    return {}


def providers_yaml(default_provider: str) -> str:
    lines = [f"default_provider: {default_provider}", "", "providers:"]
    for provider_id, provider in PROVIDERS.items():
        lines.append(f"  {provider_id}:")
        for key in ("name", "type", "command", "base_url", "model", "adapter"):
            if key in provider:
                lines.append(f"    {key}: {provider[key]}")
        lines.append("    capabilities:")
        for cap, value in provider["capabilities"].items():
            rendered = str(value).lower() if isinstance(value, bool) else value
            lines.append(f"      {cap}: {rendered}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def config_yaml(default_provider: str, workspace_name: str = "My Personal Agent OS") -> str:
    return f"""workspace:
  name: {workspace_name}

provider:
  default: {default_provider}

memory:
  auto_update: suggest
  maintain_index: true

behaviour:
  approval_for_destructive_actions: true
"""


def read_default_provider(config_path: Path) -> str:
    if not config_path.exists():
        return "generic"
    lines = config_path.read_text(encoding="utf-8").splitlines()
    in_provider = False
    for line in lines:
        stripped = line.strip()
        if stripped == "provider:":
            in_provider = True
            continue
        if in_provider and stripped.startswith("default:"):
            return stripped.split(":", 1)[1].strip()
        if in_provider and line and not line.startswith(" "):
            in_provider = False
    return "generic"


def write_provider_config(root: Path, provider_id: str, workspace_name: str = "My Personal Agent OS") -> None:
    get_provider(provider_id)
    config_dir = root / "config"
    config_dir.mkdir(parents=True, exist_ok=True)
    (config_dir / "config.yaml").write_text(config_yaml(provider_id, workspace_name), encoding="utf-8")
    (config_dir / "providers.yaml").write_text(providers_yaml(provider_id), encoding="utf-8")
    for filename, content in wrapper_files(provider_id).items():
        (root / filename).write_text(content, encoding="utf-8")
