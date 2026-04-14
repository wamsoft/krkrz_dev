"""Extract TJS native class / member inventory from src/core.

Scans C++ sources under src/core/common (plus optional --extra paths) for:
  - tTJSNC_<Class>::tTJSNC_<Class>(...)  constructor bodies
  - TJS_BEGIN_NATIVE_METHOD_DECL(/*func. name*/foo)        -> method
  - TJS_BEGIN_NATIVE_PROP_DECL(foo)                        -> property
  - TJS_BEGIN_NATIVE_EVENT_DECL(foo)                       -> event

Each member is assigned to the *most recently opened* tTJSNC_X constructor
above it in the same file. The classes-of-interest list below filters noise
(tjs2 internals like tTJSNC_Array are excluded by default).

Writes doc/_inventory.json with shape:
  {
    "<ClassName>": {
       "file": "<rel path>",
       "methods": [...], "properties": [...], "events": [...]
    }
  }

Usage: python tools/docgen/scan_tjs.py [--out PATH]
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DEFAULT_OUT = REPO / "doc" / "_inventory.json"

# Classes whose binding files we want to scan. These correspond to the
# TJS-exposed application object model documented in doc/reference/. Add or
# remove as the public surface evolves.
CLASSES = {
    "Layer", "Bitmap", "BitmapLayerTreeOwner", "Font", "ImageFunction",
    "Window", "NullDrawDevice", "BasicDrawDevice",
    "Scripts", "Storages", "System", "Timer", "Debug", "Clipboard",
    "AsyncTrigger", "Plugins", "Rect", "Console", "VideoOverlay",
    "WaveSoundBuffer", "SoundBuffer",
    "TextWriteStream", "TextReadStream", "BinaryStream",
}

CTOR_RE = re.compile(
    r"tTJSNC_(\w+)\s*::\s*tTJSNC_\1\s*\("
    r"|TVPCreateNativeClass_(\w+)\s*\("
)
DECL_RES = {
    "method":  re.compile(r"TJS_BEGIN_NATIVE_METHOD_DECL\(\s*(?:/\*[^*]*\*/\s*)?(\w+)\s*\)"),
    "property": re.compile(r"TJS_BEGIN_NATIVE_PROP_DECL\(\s*(?:/\*[^*]*\*/\s*)?(\w+)\s*\)"),
    "event":   re.compile(r"TJS_BEGIN_NATIVE_EVENT_DECL\(\s*(?:/\*[^*]*\*/\s*)?(\w+)\s*\)"),
}

def scan_file(path: Path) -> dict[str, dict]:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return {}

    # Gather constructor openings: (class_name, offset).
    ctor_spans: list[tuple[int, str]] = []
    for m in CTOR_RE.finditer(text):
        name = m.group(1) or m.group(2)
        if name:
            ctor_spans.append((m.start(), name))
    if not ctor_spans:
        return {}
    ctor_spans.sort()

    def class_at(offset: int) -> str | None:
        last = None
        for off, name in ctor_spans:
            if off > offset:
                break
            last = name
        return last

    classes: dict[str, dict] = {}
    for kind, rx in DECL_RES.items():
        for m in rx.finditer(text):
            cls = class_at(m.start())
            if cls is None or cls not in CLASSES:
                continue
            bucket = classes.setdefault(cls, {
                "file": None,
                "methods": [],
                "properties": [],
                "events": [],
            })
            name = m.group(1)
            key = {"method": "methods", "property": "properties", "event": "events"}[kind]
            if name not in bucket[key]:
                bucket[key].append(name)

    return classes

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    ap.add_argument("--root", default=str(REPO / "src" / "core"))
    args = ap.parse_args()

    root = Path(args.root)
    if not root.exists():
        print(f"src/core not found: {root}")
        return 2

    inventory: dict[str, dict] = {}
    file_count = 0
    for p in root.rglob("*.cpp"):
        # skip external / generated / build output
        parts = set(p.parts)
        if "external" in parts or "build" in parts or "tp_stub" in parts:
            continue
        found = scan_file(p)
        if not found:
            continue
        file_count += 1
        for cls, info in found.items():
            existing = inventory.setdefault(cls, {
                "file": str(p.relative_to(REPO)).replace("\\", "/"),
                "methods": [],
                "properties": [],
                "events": [],
            })
            # Prefer the first file we found that defines this class.
            for k in ("methods", "properties", "events"):
                for name in info[k]:
                    if name not in existing[k]:
                        existing[k].append(name)

    # sort member lists for stable diffs
    for info in inventory.values():
        for k in ("methods", "properties", "events"):
            info[k].sort()

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(inventory, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    total = sum(len(v["methods"]) + len(v["properties"]) + len(v["events"])
                for v in inventory.values())
    print(f"[scan_tjs] scanned {file_count} binding files, "
          f"{len(inventory)} classes, {total} members -> {out_path}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
