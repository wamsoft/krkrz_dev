"""Scan plugin C++ for property registrations and rewrite manual.tjs.

For each `src/plugins/<name>/manual.tjs`, look at the plugin's C++ files
(top-level *.cpp / *.h, excluding third-party subdirectories) for property
registrations and determine read-only / read-write status.

If a manual.tjs declares `property NAME;` (bare) and the C++ binding is
read-only, rewrite to `property NAME { getter; }`. Read-write bare properties
are left alone (bare = rw is the convention).

Usage:
  python tools/docgen/fix_props.py [--dry-run]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
PLUGINS_DIR = REPO / "src" / "plugins"

# Subdirectories under plugins/* that vendor third-party code; skip these.
THIRD_PARTY_DIRS = {"thorvg", "jerry", "rapidjson"}

NULL_TOKENS = {"0", "nullptr", "NULL", "(int)0", "(void*)0"}


def is_null(expr: str) -> bool:
    return expr.replace(" ", "") in NULL_TOKENS


# Argument matcher that allows balanced parens at one level (`(int)0`, `(void*)0`).
ARG = r"(?:[^,()]|\([^()]*\))+?"


# Property(TJS_W("name"), getter, setter)  —  3 args
NCB_PROPERTY_RE = re.compile(
    r"\bProperty\s*\(\s*TJS_W\s*\(\s*\"([^\"]+)\"\s*\)\s*,\s*"
    + ARG + r"\s*,\s*(" + ARG + r")\s*[,)]"
)

# RawCallback("name", getter, setter, flags)  —  4 args (= property)
RAWCB_PROPERTY_RE = re.compile(
    r"\bRawCallback\s*\(\s*(?:TJS_W\s*\(\s*)?\"([^\"]+)\"[\s)]*,\s*"
    + ARG + r"\s*,\s*(" + ARG + r")\s*,\s*"
    + ARG + r"\s*\)"
)

# Macros that imply read-only / read-write:
RO_MACROS = (
    re.compile(r"\bNCB_PROPERTY_RO\s*\(\s*(\w+)\s*,"),
    re.compile(r"\bNCB_GDIP_PROPERTY_RO\s*\(\s*(\w+)\s*,"),
    re.compile(r"\bINTPROP\s*\(\s*(\w+)\s*\)"),
    re.compile(r"\bNCB_PROPERTY_PROXY_RO\s*\(\s*(\w+)\b"),  # layerExDraw AutoProp
)
RW_MACROS = (
    re.compile(r"\bNCB_PROPERTY\s*\(\s*(\w+)\s*,"),
    re.compile(r"\bNCB_GDIP_PROPERTY\s*\(\s*(\w+)\s*,"),
    re.compile(r"\bNCB_PROPERTY_PROXY\s*\(\s*(\w+)\b"),
)


def merge_access(existing: str, new: str) -> str:
    """If we see 'r' for a name already marked 'rw' (or vice versa),
    prefer 'rw' (the more permissive view) — different overloads exist."""
    if not existing:
        return new
    if existing == new:
        return existing
    return "rw"


def scan_cpp_text(text: str) -> dict:
    """Return {prop_name: 'r' | 'rw'} for property registrations found."""
    out: dict[str, str] = {}

    def add(name: str, access: str):
        out[name] = merge_access(out.get(name, ""), access)

    for m in NCB_PROPERTY_RE.finditer(text):
        add(m.group(1), "r" if is_null(m.group(2).strip()) else "rw")
    for m in RAWCB_PROPERTY_RE.finditer(text):
        add(m.group(1), "r" if is_null(m.group(2).strip()) else "rw")
    for rx in RO_MACROS:
        for m in rx.finditer(text):
            add(m.group(1), "r")
    for rx in RW_MACROS:
        for m in rx.finditer(text):
            add(m.group(1), "rw")

    return out


def collect_plugin_access(plugin_dir: Path) -> dict:
    """Scan top-level C++/H files in the plugin directory."""
    access: dict[str, str] = {}
    for child in plugin_dir.iterdir():
        if child.is_dir():
            continue
        if child.suffix not in (".cpp", ".h", ".hpp"):
            continue
        try:
            text, _ = read_text_lenient(child)
        except OSError:
            continue
        for name, ac in scan_cpp_text(text).items():
            access[name] = merge_access(access.get(name, ""), ac)
    return access


# ---------------------------------------------------------------------------
# Rewriter
# ---------------------------------------------------------------------------

# Match a bare `property NAME;` (no `{ ... }` block).
# Captures preceding indent, the keyword, and any trailing same-line comment.
BARE_PROPERTY_RE = re.compile(
    r"(?P<indent>^[ \t]*)property[ \t]+(?P<name>\w+)[ \t]*;"
    r"(?P<trail>[ \t]*//[^\n]*)?",
    re.MULTILINE,
)


def read_text_lenient(path: Path) -> tuple[str, str]:
    """Read text trying utf-8 first, falling back to cp932 (SJIS)."""
    raw = path.read_bytes()
    for enc in ("utf-8", "cp932"):
        try:
            return raw.decode(enc), enc
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace"), "utf-8"


def rewrite_manual(manual_path: Path, access_map: dict, dry_run: bool):
    text, enc = read_text_lenient(manual_path)
    changes = []

    def repl(m: re.Match) -> str:
        name = m.group("name")
        access = access_map.get(name)
        if access != "r":  # rw or unknown → leave bare alone
            return m.group(0)
        indent = m.group("indent")
        trail = m.group("trail") or ""
        new = f"{indent}property {name} {{ getter; }}{trail}"
        changes.append((name, m.group(0).strip(), new.strip()))
        return new

    new_text = BARE_PROPERTY_RE.sub(repl, text)
    if changes and not dry_run:
        manual_path.write_text(new_text, encoding=enc)
    return changes


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true",
                    help="Print changes without writing")
    ap.add_argument("--plugin", default=None,
                    help="Process a single plugin (e.g., 'binaryStream')")
    args = ap.parse_args(argv)

    total = 0
    plugin_iter = (
        [PLUGINS_DIR / args.plugin] if args.plugin
        else sorted(p for p in PLUGINS_DIR.iterdir() if p.is_dir())
    )

    for plugin_dir in plugin_iter:
        manual = plugin_dir / "manual.tjs"
        if not manual.exists():
            continue
        access = collect_plugin_access(plugin_dir)
        if not access:
            continue
        changes = rewrite_manual(manual, access, args.dry_run)
        if changes:
            print(f"\n## {plugin_dir.name}/manual.tjs")
            for name, before, after in changes:
                print(f"  {name}: {before}  →  {after}")
            total += len(changes)

    verb = "would change" if args.dry_run else "changed"
    print(f"\n{verb} {total} property declaration(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
