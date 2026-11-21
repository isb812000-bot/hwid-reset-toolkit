"""Spoof MachineGuid and related registry identifiers via winreg."""
from __future__ import annotations

import uuid

try:
    import winreg  # type: ignore
except ImportError:  # non-windows dev
    winreg = None  # type: ignore


class RegistryWriter:
    KEY = r"SOFTWARE\Microsoft\Cryptography"
    VALUE = "MachineGuid"

    def read(self) -> str:
        if winreg is None:
            return "00000000-0000-0000-0000-000000000000"
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, self.KEY) as key:
            return winreg.QueryValueEx(key, self.VALUE)[0]

    def write(self, value: str) -> None:
        if winreg is None:
            return
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, self.KEY, 0,
                            winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, self.VALUE, 0, winreg.REG_SZ, value)

    def write_random(self, snapshot) -> None:
        new = str(uuid.uuid4())
        self.write(new)
        snapshot.values.setdefault("registry", new)