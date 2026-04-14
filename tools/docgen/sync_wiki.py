"""Flatten doc/ into a layout suitable for the GitHub Wiki repo.

GitHub Wiki uses a single flat namespace (no subdirectories). This script
copies every .md and asset from doc/ into a destination directory using
the flat naming scheme:

  doc/reference/Layer.md           -> <dst>/Class.Layer.md
  doc/reference/Window.Basic...md  -> <dst>/Class.Window.BasicDrawDevice.md
  doc/guide/EventSystem.md         -> <dst>/Guide.EventSystem.md
  doc/_assets/foo.png              -> <dst>/foo.png
  doc/_index.md                    -> <dst>/Home.md
  doc/_missing.md                  -> <dst>/_Docs-Diff-Report.md

Relative links inside the copied Markdown are rewritten:
  (Layer.md)                       -> (Class.Layer)
  (Layer.md#visible)               -> (Class.Layer#visible)
  (../guide/EventSystem.md)        -> (Guide.EventSystem)
  (../_assets/foo.png)             -> (foo.png)

Usage: python tools/docgen/sync_wiki.py <dst-dir>

The Action workflow checks out krkrz_dev.wiki.git into <dst-dir> and then
runs this script; the script overwrites files but does not delete anything
it did not produce (let the workflow decide retention).
"""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DOC = REPO / "doc"

# Link rewriters ---------------------------------------------------------

REF_MD_RE = re.compile(r"\]\((?!https?:|#|mailto:)([^)]+?)\.md(#[^)]*)?\)")
ASSET_RE = re.compile(r"\]\(\.\./_assets/([^)]+)\)")

def rewrite_links(text: str, in_kind: str) -> str:
    """Rewrite relative .md / asset links to wiki-flat form."""
    def repl_md(m: re.Match) -> str:
        target = m.group(1)
        anchor = m.group(2) or ""
        t = target
        if t.startswith("../"):
            t = t[3:]
        if t.startswith("guide/"):
            page = "Guide." + t[len("guide/"):]
        elif t.startswith("reference/"):
            page = "Class." + t[len("reference/"):]
        elif "/" in t:
            page = t.replace("/", ".")
        else:
            prefix = "Class." if in_kind == "class" else "Guide."
            page = prefix + t
        return f"]({page}{anchor})"

    def repl_asset(m: re.Match) -> str:
        return f"]({m.group(1)})"

    text = REF_MD_RE.sub(repl_md, text)
    text = ASSET_RE.sub(repl_asset, text)
    return text

# File copying -----------------------------------------------------------

def main() -> int:
    if len(sys.argv) != 2:
        print("usage: sync_wiki.py <dst-dir>", file=sys.stderr)
        return 2
    dst = Path(sys.argv[1])
    dst.mkdir(parents=True, exist_ok=True)

    written: list[str] = []

    # classes
    for md in sorted((DOC / "reference").glob("*.md")):
        out = dst / f"Class.{md.name}"
        out.write_text(rewrite_links(md.read_text(encoding="utf-8"), "class"), encoding="utf-8")
        written.append(out.name)

    # guides
    for md in sorted((DOC / "guide").glob("*.md")):
        out = dst / f"Guide.{md.name}"
        out.write_text(rewrite_links(md.read_text(encoding="utf-8"), "guide"), encoding="utf-8")
        written.append(out.name)

    # home (_index.md needs its links fully rewritten: it references
    # reference/Foo.md and guide/Foo.md — treat as "cross-section root").
    index = DOC / "_index.md"
    if index.exists():
        home = rewrite_links(index.read_text(encoding="utf-8"), "class")
        (dst / "Home.md").write_text(home, encoding="utf-8")
        written.append("Home.md")

    # diff report
    missing = DOC / "_missing.md"
    if missing.exists():
        (dst / "_Docs-Diff-Report.md").write_text(
            missing.read_text(encoding="utf-8"), encoding="utf-8"
        )
        written.append("_Docs-Diff-Report.md")

    # assets
    assets = DOC / "_assets"
    if assets.exists():
        for a in assets.iterdir():
            if a.is_file():
                shutil.copy2(a, dst / a.name)
                written.append(a.name)

    print(f"[sync_wiki] wrote {len(written)} files to {dst}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
