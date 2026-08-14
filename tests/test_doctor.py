from pathlib import Path
import tempfile
import unittest

from scripts.lib.providers import runtime_status, write_provider_config
from scripts.lib.workspace import check_structure, ensure_dirs


class DoctorSupportTests(unittest.TestCase):
    def test_missing_runtime_detection_is_understandable(self):
        status, message = runtime_status("generic")
        self.assertEqual(status, "warn")
        self.assertIn("Manual provider", message)

    def test_invalid_structure_lists_missing_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            ensure_dirs(root)
            write_provider_config(root, "generic")
            missing = check_structure(root)
            self.assertIn("AGENTS.md", missing)
            self.assertIn("memory/index.md", missing)


if __name__ == "__main__":
    unittest.main()

