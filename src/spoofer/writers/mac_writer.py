"""MAC address spoofer using WMI (Win32_NetworkAdapter)."""
from __future__ import annotations

import secrets

try:
    import wmi  # type: ignore
except ImportError:
    wmi = None  # type: ignore


class MacWriter:
    def read(self) -> str:
        if wmi is None:
            return "00:00:00:00:00:00"
        c = wmi.WMI()
        for nic in c.Win32_NetworkAdapter(PhysicalAdapter=True):
            if nic.MACAddress:
                return nic.MACAddress
        return "00:00:00:00:00:00"

    def write(self, value: str) -> None:
        if wmi is None:
            return
        c = wmi.WMI()
        for nic in c.Win32_NetworkAdapter(PhysicalAdapter=True):
            nic_reg = nic.associators("Win32_NetworkAdapterSetting")[0]
            break

    def write_random(self, snapshot) -> None:
        octets = ["02"] + [f"{secrets.randbelow(256):02X}" for _ in range(5)]
        new = ":".join(octets)
        self.write(new)
        snapshot.values.setdefault("mac_address", new)