from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class SpoofPlan:
    targets: list[str] = field(default_factory=list)
    sources: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {"targets": self.targets, "sources": self.sources}