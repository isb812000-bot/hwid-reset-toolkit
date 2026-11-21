"""Capture and restore HWID snapshots."""
from __future__ import annotations

import json
import uuid
from pathlib import Path

from src.shared.models.snapshot import HwidSnapshot
from src.spoofer.writers.registry_writer import RegistryWriter
from src.spoofer.writers.disk_writer import DiskWriter
from src.spoofer.writers.mac_writer import MacWriter


class SnapshotManager:
    def __init__(self, dir_: Path | str = "snapshots") -> None:
        self._dir = Path(dir_)
        self._dir.mkdir(parents=True, exist_ok=True)
        self._writers = {"registry": RegistryWriter(),
                         "disk_serial": DiskWriter(),
                         "mac_address": MacWriter()}

    def capture(self, sources: list[str]) -> HwidSnapshot:
        snap = HwidSnapshot(snapshot_id=uuid.uuid4().hex[:12])
        for source in sources:
            w = self._writers.get(source)
            if w:
                snap.values[source] = w.read()
        self._persist(snap)
        return snap

    def load(self, snapshot_id: str) -> HwidSnapshot | None:
        path = self._dir / f"{snapshot_id}.json"
        if not path.exists():
            return None
        data = json.loads(path.read_text(encoding="utf-8"))
        return HwidSnapshot(snapshot_id=data["snapshot_id"], values=data["values"])

    def restore(self, snap: HwidSnapshot) -> bool:
        for source, value in snap.values.items():
            w = self._writers.get(source)
            if w:
                w.write(value)
        return True

    def _persist(self, snap: HwidSnapshot) -> None:
        path = self._dir / f"{snap.snapshot_id}.json"
        path.write_text(json.dumps(snap.to_dict(), indent=2), encoding="utf-8")