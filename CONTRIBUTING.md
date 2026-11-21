# Contributing to hwid-reset-toolkit

Thanks for helping out. This toolkit is a community-driven HWID spoofer /
reset utility for Fortnite, Valorant, CS2, Apex Legends and other titles
that bind a machine fingerprint to an account.

## Ground rules

- Keep changes scoped. One PR = one spoofer module, one adapter, or one fix.
- New game adapters go under `src/adapters/games/`.
- Native helpers go under `src-native/` and must build with `dotnet build`.
- Run `python -m pytest tests/` before opening a PR.
- Do not commit live HWID dumps, session tokens, or user logs.

## Adding a new game adapter

1. Subclass `GameAdapter` in `src/adapters/games/`.
2. Declare `game_id`, `process_names`, and `hwid_sources`.
3. Register it in `src/shared/game_registry.py`.
4. Add a stub test in `tests/`.

## Style

- Python 3.11+, type hints everywhere.
- 4-space indent, black-compatible, no wildcard imports.
- Comments only where the logic is non-obvious (registry paths, IOCTL codes).

## Disclaimer

Everything here is for educational and research purposes. Using a spoofer
against live anti-cheat systems violates ToS and may result in bans. Use at
your own risk.