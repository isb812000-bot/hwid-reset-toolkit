"""Disk serial spoofer adapter (delegates to native helper when available)."""
from __future__ import annotations

import secrets

from src.native_bridge.clr_loader import load_native_helper


class DiskWriter:
    def __init__(self) -> None:
        self._helper = load_native_helper("HwidNative.DiskSpoofer")

    def read(self) -> str:
        if self._helper is None:
            return "UNKNOWN"
        return self._helper.ReadSerial(0)

    def write(self, value: str) -> None:
        if self._helper is not None:
            self._helper.WriteSerial(0, value)

    def write_random(self, snapshot) -> None:
        new = secrets.token_hex(8).upper()
        self.write(new)
        snapshot.values.setdefault("disk_serial", new)