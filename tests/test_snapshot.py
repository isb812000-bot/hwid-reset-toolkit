import tempfile
from pathlib import Path

from src.spoofer.snapshot_manager import SnapshotManager


def test_snapshot_roundtrip(tmp_path: Path):
    mgr = SnapshotManager(tmp_path)
    snap = mgr.capture(["registry"])
    loaded = mgr.load(snap.snapshot_id)
    assert loaded is not None
    assert loaded.snapshot_id == snap.snapshot_id