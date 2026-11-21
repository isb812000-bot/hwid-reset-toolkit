"""Loads the optional C# native helper via pythonnet."""
from __future__ import annotations

import logging
from pathlib import Path

log = logging.getLogger(__name__)


def load_native_helper(class_name: str):
    try:
        import clr  # type: ignore
    except ImportError:
        log.info("pythonnet missing; native helper disabled")
        return None

    dll = Path("src-native/bin/Release/net8.0/HwidNative.dll").resolve()
    if not dll.exists():
        log.info("native helper not built: %s", dll)
        return None
    clr.AddReference(str(dll))
    module, cls = class_name.rsplit(".", 1)
    return getattr(__import__(module, fromlist=[cls]), cls)