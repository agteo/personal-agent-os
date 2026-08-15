from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from scripts.lib.providers import get_provider, read_default_provider, runtime_status, write_provider_config


class ProviderTests(unittest.TestCase):
    def test_known_provider(self):
        provider = get_provider("openai")
        self.assertEqual(provider["command"], "codex")

    def test_invalid_provider(self):
        with self.assertRaises(ValueError):
            get_provider("missing")

    def test_openrouter_provider_has_easy_default(self):
        provider = get_provider("openrouter")
        self.assertEqual(provider["base_url"], "https://openrouter.ai/api/v1")
        self.assertEqual(provider["api_key_env"], "OPENROUTER_API_KEY")
        self.assertEqual(provider["model"], "openrouter/auto")
        self.assertTrue(any(choice["model"] == "openrouter/free" for choice in provider["model_choices"]))

    def test_openrouter_runtime_status_mentions_api_key(self):
        with patch.dict("os.environ", {}, clear=True):
            status, message = runtime_status("openrouter")
        self.assertEqual(status, "warn")
        self.assertIn("OPENROUTER_API_KEY", message)

    def test_switch_provider_writes_config_without_memory(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            memory = root / "memory" / "user"
            memory.mkdir(parents=True)
            profile = memory / "profile.md"
            profile.write_text("keep me", encoding="utf-8")
            write_provider_config(root, "ollama")
            self.assertEqual(read_default_provider(root / "config" / "config.yaml"), "ollama")
            self.assertEqual(profile.read_text(encoding="utf-8"), "keep me")

    def test_write_openrouter_config_can_override_model(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_provider_config(root, "openrouter", model="custom/provider-model")
            providers_yaml = (root / "config" / "providers.yaml").read_text(encoding="utf-8")
            self.assertIn("default_provider: openrouter", providers_yaml)
            self.assertIn("model: custom/provider-model", providers_yaml)


if __name__ == "__main__":
    unittest.main()
