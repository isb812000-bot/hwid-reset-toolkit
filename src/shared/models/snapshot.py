from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class HwidSnapshot:
    snapshot_id: str
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    values: dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "snapshot_id": self.snapshot_id,
            "created_at": self.created_at.isoformat(),
            "values": self.values,
        }