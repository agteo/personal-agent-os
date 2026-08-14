#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.indexer import rebuild_index


def main() -> int:
    path = rebuild_index(Path.cwd())
    print(f"Rebuilt {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

