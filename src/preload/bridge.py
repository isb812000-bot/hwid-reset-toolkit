"""Bridge between renderer UI (pywebview) and main IPC dispatcher."""
from __future__ import annotations

import json
from typing import Any

from src.main.ipc.dispatcher import IpcDispatcher


class Bridge:
    def __init__(self, dispatcher: IpcDispatcher) -> None:
        self._dispatcher = dispatcher

    def call(self, channel: str, payload_json: str) -> str:
        payload: dict[str, Any] = json.loads(payload_json or "{}")
        return json.dumps(self._dispatcher.dispatch(channel, payload))

    # convenience helpers exposed to the renderer
    def plan(self, targets: list[str]) -> str:
        return self.call("spoof.plan", json.dumps({"targets": targets}))

    def start(self, targets: list[str]) -> str:
        return self.call("spoof.start", json.dumps({"targets": targets}))