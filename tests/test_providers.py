from pathlib import Path
import tempfile
import unittest

from scripts.lib.providers import get_provider, read_default_provider, write_provider_config


class ProviderTests(unittest.TestCase):
    def test_known_provider(self):
        provider = get_provider("openai")
        self.assertEqual(provider["command"], "codex")

    def test_invalid_provider(self):
        with self.assertRaises(ValueError):
            get_provider("missing")

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


if __name__ == "__main__":
    unittest.main()

