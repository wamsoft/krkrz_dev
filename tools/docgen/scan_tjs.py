"""Extract TJS native class / member inventory from src/core.

Scans C++ sources under src/core/common (plus optional --extra paths) for:
  - tTJSNC_<Class>::tTJSNC_<Class>(...)  constructor bodies
  - TJS_BEGIN_NATIVE_METHOD_DECL(/*func. name*/foo)        -> method
  - TJS_BEGIN_NATIVE_PROP_DECL(foo)                        -> property
  - TJS_BEGIN_NATIVE_EVENT_DECL(foo)                       -> event

Macro-based decls are assigned to the *most recently opened* tTJSNC_X
constructor above them in the same file.

Additionally, two runtime-registration patterns are detected and assigned
to the file's *primary* tTJSNC_X (when there's exactly one class-of-interest
constructor in the file):

  - PropSet(TJS_MEMBERENSURE, TJS_W("name"), ...)  -> property/event
        Used in Initialize() bodies to register members at construction time
        (e.g. System::exceptionHandler, System::onActivate). Names matching
        ^on[A-Z] are categorized as events, else as properties.
  - static ttstr eventname(TJS_W("name"))          -> event
        The standard pattern for TVPPostEvent dispatch (e.g. Window::onClick,
        Window::onHintChanged, Window::onDisplayRotate). Always categorized
        as an event.

The classes-of-interest list below filters noise (tjs2 internals like
tTJSNC_Array are excluded by default).

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

# Members present in the C++ binding but intentionally excluded from the
# documented surface — typically platform-specific things that the project
# decided not to advertise. Keyed as "Class.member".
EXCLUDED_MEMBERS = {
    # Android はビルド対象外（multi_platform_design 由来の C++ は残るが
    # ドキュメントには載せない方針）
    "System.isAndroid",
}

CTOR_RE = re.compile(
    r"tTJSNC_(\w+)\s*::\s*tTJSNC_\1\s*\("
    # require return-type prefix so we don't match factory CALLS
    # (e.g. `BitmapClass = TVPCreateNativeClass_Bitmap();` in
    # BitmapDrawDevice.cpp would otherwise misattribute Show()'s onDraw to
    # Bitmap).
    r"|tTJSNativeClass\s*\*\s*TVPCreateNativeClass_(\w+)\s*\("
)
DECL_RES = {
    "method":  re.compile(r"TJS_BEGIN_NATIVE_METHOD_DECL\(\s*(?:/\*[^*]*\*/\s*)?(\w+)\s*\)"),
    "property": re.compile(r"TJS_BEGIN_NATIVE_PROP_DECL\(\s*(?:/\*[^*]*\*/\s*)?(\w+)\s*\)"),
    "event":   re.compile(r"TJS_BEGIN_NATIVE_EVENT_DECL\(\s*(?:/\*[^*]*\*/\s*)?(\w+)\s*\)"),
}

# Runtime-registration patterns. Both produce member names that must be
# attributed to the file's primary tTJSNC class (ctor proximity does not
# work — these calls live in Initialize() bodies or free functions outside
# any ctor span).
PROPSET_RE = re.compile(
    # require bare `PropSet(...)` (implicit `this->`) — exclude
    # `dict->PropSet(...)` which populates a returned dictionary, not the
    # class itself.
    r'(?<![\w.>])PropSet\s*\(\s*TJS_MEMBERENSURE\s*,\s*TJS_W\(\s*"(\w+)"\s*\)'
)
EVENTNAME_RE = re.compile(
    r'static\s+ttstr\s+eventname\s*\(\s*TJS_W\(\s*"(\w+)"\s*\)\s*\)'
)
EVENT_NAME_PREFIX_RE = re.compile(r"^on[A-Z]")

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

    def add(cls: str, key: str, name: str):
        if f"{cls}.{name}" in EXCLUDED_MEMBERS:
            return
        bucket = classes.setdefault(cls, {
            "file": None,
            "methods": [],
            "properties": [],
            "events": [],
        })
        if name not in bucket[key]:
            bucket[key].append(name)

    for kind, rx in DECL_RES.items():
        for m in rx.finditer(text):
            cls = class_at(m.start())
            if cls is None or cls not in CLASSES:
                continue
            key = {"method": "methods", "property": "properties", "event": "events"}[kind]
            add(cls, key, m.group(1))

    # Runtime-registration patterns are tied to the file as a whole, since
    # PropSet / TVPPostEvent calls usually sit in Initialize() bodies or free
    # helper functions that are outside any tTJSNC_X constructor span. Only
    # apply them when the file has exactly one class-of-interest constructor
    # — otherwise we'd guess wrong on multi-class binding files.
    cls_in_file = [n for _, n in ctor_spans if n in CLASSES]
    primary = cls_in_file[0] if len(set(cls_in_file)) == 1 else None
    if primary:
        for m in PROPSET_RE.finditer(text):
            name = m.group(1)
            key = "events" if EVENT_NAME_PREFIX_RE.match(name) else "properties"
            add(primary, key, name)
        for m in EVENTNAME_RE.finditer(text):
            add(primary, "events", m.group(1))

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
