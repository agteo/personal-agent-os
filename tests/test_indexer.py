from pathlib import Path
import tempfile
import unittest

from scripts.lib.indexer import build_index, rebuild_index


class IndexerTests(unittest.TestCase):
    def test_rebuild_index_finds_project(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            projects = root / "memory" / "projects"
            projects.mkdir(parents=True)
            (projects / "project-atlas.md").write_text("# Project Atlas\n", encoding="utf-8")
            index = build_index(root)
            self.assertIn("[[projects/project-atlas]]", index)

    def test_rebuild_index_writes_cross_platform_paths(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "memory" / "people").mkdir(parents=True)
            (root / "memory" / "people" / "alice-smith.md").write_text("# Alice Smith\n", encoding="utf-8")
            path = rebuild_index(root)
            self.assertIn("[[people/alice-smith]]", path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()

