"""Core spoofer: applies HWID writers driven by a SpoofPlan."""
from __future__ import annotations

import logging

from src.shared.models.spoof_plan import SpoofPlan
from src.shared.models.snapshot import HwidSnapshot
from src.spoofer.writers.registry_writer import RegistryWriter
from src.spoofer.writers.disk_writer import DiskWriter
from src.spoofer.writers.mac_writer import MacWriter

log = logging.getLogger(__name__)


class SpoofEngine:
    def __init__(self) -> None:
        self._writers = {
            "registry": RegistryWriter(),
            "disk_serial": DiskWriter(),
            "mac_address": MacWriter(),
        }

    def apply(self, plan: SpoofPlan, snapshot: HwidSnapshot) -> bool:
        for source in plan.sources:
            writer = self._writers.get(source)
            if writer is None:
                log.warning("no writer for source %s", source)
                continue
            try:
                writer.write_random(snapshot)
            except Exception as exc:  # noqa: BLE001
                log.error("writer %s failed: %s", source, exc)
                return False
        return True