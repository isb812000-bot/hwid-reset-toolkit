"""Renderer-side helper for the game target list."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TargetRow:
    game_id: str
    label: str
    enabled: bool = True


def build_rows(registry_items: list[dict]) -> list[TargetRow]:
    return [
        TargetRow(game_id=it["game_id"], label=it["label"], enabled=it.get("enabled", True))
        for it in registry_items
    ]