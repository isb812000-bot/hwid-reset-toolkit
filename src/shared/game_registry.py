"""Registry of supported game adapters."""
from __future__ import annotations

from src.adapters.games.fortnite import FortniteAdapter
from src.adapters.games.valorant import ValorantAdapter
from src.adapters.games.cs2 import Cs2Adapter
from src.adapters.games.apex import ApexAdapter
from src.adapters.games.base import GameAdapter


class GameRegistry:
    def __init__(self, adapters: list[GameAdapter]) -> None:
        self._adapters: dict[str, GameAdapter] = {a.game_id: a for a in adapters}

    @classmethod
    def load_default(cls) -> "GameRegistry":
        return cls([FortniteAdapter(), ValorantAdapter(), Cs2Adapter(), ApexAdapter()])

    def get(self, game_id: str) -> GameAdapter:
        if game_id not in self._adapters:
            raise KeyError(f"no adapter registered for {game_id}")
        return self._adapters[game_id]

    def enabled_ids(self) -> list[str]:
        return list(self._adapters.keys())