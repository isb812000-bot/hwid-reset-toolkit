"""Dev helper: run every registered adapter with --dry-run by default."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.main.bootstrap import main as bootstrap_main  # noqa: E402


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--write", action="store_true", help="actually write")
    args = p.parse_args()
    argv = [] if args.write else ["--dry-run"]
    sys.exit(bootstrap_main(argv))