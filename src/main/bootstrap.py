"""Entry point for the hwid-reset-toolkit desktop shell."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from src.main.session import SpoofSession
from src.shared.game_registry import GameRegistry
from src.shared.logging_setup import configure_logging
from src.main.ipc.dispatcher import IpcDispatcher


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="hwid-reset-toolkit")
    p.add_argument("--games", nargs="*", default=None,
                   help="restrict spoofer to specific game ids")
    p.add_argument("--dry-run", action="store_true",
                   help="plan spoof without writing")
    p.add_argument("--restore", metavar="SNAPSHOT",
                   help="restore HWID snapshot by id")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    configure_logging(Path("logs"))
    registry = GameRegistry.load_default()
    session = SpoofSession(registry, dry_run=args.dry_run)

    if args.restore:
        return 0 if session.restore(args.restore) else 1

    targets = args.games or registry.enabled_ids()
    dispatcher = IpcDispatcher(session)
    return dispatcher.run(targets)


if __name__ == "__main__":
    sys.exit(main())