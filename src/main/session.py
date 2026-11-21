"""Spoof session: orchestrates adapters and HWID source writers."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable

from src.shared.game_registry import GameRegistry
from src.shared.models.spoof_plan import SpoofPlan
from src.shared.models.snapshot import HwidSnapshot
from src.spoofer.snapshot_manager import SnapshotManager
from src.spoofer.engine import SpoofEngine


@dataclass
class SpoofSession:
    registry: GameRegistry
    dry_run: bool = False
    _snapshots: SnapshotManager = field(default_factory=SnapshotManager)
    _engine: SpoofEngine = field(default_factory=SpoofEngine)

    def plan(self, game_ids: Iterable[str]) -> SpoofPlan:
        adapters = [self.registry.get(g) for g in game_ids]
        sources = {s for a in adapters for s in a.hwid_sources}
        return SpoofPlan(targets=[a.game_id for a in adapters], sources=sorted(sources))

    def run(self, game_ids: Iterable[str]) -> bool:
        plan = self.plan(game_ids)
        snap = self._snapshots.capture(plan.sources)
        if self.dry_run:
            return True
        ok = self._engine.apply(plan, snapshot=snap)
        if not ok:
            self._snapshots.restore(snap)
        return ok

    def restore(self, snapshot_id: str) -> bool:
        snap: HwidSnapshot | None = self._snapshots.load(snapshot_id)
        if snap is None:
            return False
        return self._snapshots.restore(snap)