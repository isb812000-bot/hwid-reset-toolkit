"""Minimal pywebview renderer shell for hwid-reset-toolkit."""
from __future__ import annotations

from pathlib import Path

import webview

from src.preload.bridge import Bridge


def launch(bridge: Bridge) -> None:
    html = Path(__file__).with_name("index.html")
    window = webview.create_window(
        "hwid-reset-toolkit",
        url=html.as_uri(),
        js_api=bridge,
        width=980,
        height=680,
    )
    webview.start(debug=False)
    window.destroy()