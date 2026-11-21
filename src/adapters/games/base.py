from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class GameAdapter:
    game_id: str
    label: str
    process_names: list[str] = field(default_factory=list)
    hwid_sources: list[str] = field(default_factory=list)

    def is_running(self, running: set[str]) -> bool:
        return any(p.lower() in running for p in self.process_names)