from pathlib import Path
import tempfile
import unittest

from scripts.lib.workspace import check_structure, setup_workspace


class SetupTests(unittest.TestCase):
    def test_fresh_setup(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            setup_workspace(root, "Jamie", "Student", "writing, research", "generic")
            self.assertTrue((root / "memory" / "user" / "profile.md").exists())
            self.assertTrue((root / "sources" / "inbox").exists())
            self.assertTrue((root / "config" / "config.yaml").exists())

    def test_existing_workspace_detection(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            setup_workspace(root, "Jamie", "Student", "writing", "generic")
            missing = check_structure(root)
            self.assertIn("AGENTS.md", missing)
            (root / "AGENTS.md").write_text("instructions", encoding="utf-8")
            self.assertNotIn("memory/index.md", check_structure(root))


if __name__ == "__main__":
    unittest.main()

