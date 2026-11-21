"""Thin IPC dispatcher: routes UI/CLI messages to session services."""
from __future__ import annotations

from typing import Callable

from src.main.session import SpoofSession


class IpcDispatcher:
    def __init__(self, session: SpoofSession) -> None:
        self._session = session
        self._handlers: dict[str, Callable[[dict], dict]] = {
            "spoof.start": self._on_spoof_start,
            "spoof.plan": self._on_spoof_plan,
            "spoof.restore": self._on_spoof_restore,
        }

    def dispatch(self, channel: str, payload: dict) -> dict:
        handler = self._handlers.get(channel)
        if handler is None:
            return {"ok": False, "error": f"unknown channel {channel}"}
        return handler(payload)

    def run(self, targets: list[str]) -> int:
        result = self._on_spoof_start({"targets": targets})
        return 0 if result["ok"] else 1

    def _on_spoof_start(self, payload: dict) -> dict:
        ok = self._session.run(payload.get("targets", []))
        return {"ok": ok}

    def _on_spoof_plan(self, payload: dict) -> dict:
        plan = self._session.plan(payload.get("targets", []))
        return {"ok": True, "plan": plan.to_dict()}

    def _on_spoof_restore(self, payload: dict) -> dict:
        ok = self._session.restore(payload["snapshot_id"])
        return {"ok": ok}