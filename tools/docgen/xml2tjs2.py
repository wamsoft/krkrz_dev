"""Convert legacy TJS2 language reference XML to Markdown.

Input:  document/tjs2/j_in/*.xml      (legacy XML, SJIS-encoded)
Output: doc/tjs2/<name>.md             (Markdown for mkdocs)
        doc/tjs2/_assets/*             (images from imgsrc/, if any)

The TJS2 XMLs use a flat `<para><ptitle>...</ptitle>...</para>` schema
without `<member>` blocks, so all entries are converted as guides.
The xml2md helpers (`convert_guide`, `render_mixed`, ...) are reused.

Usage:
  python tools/docgen/xml2tjs2.py [--src PATH] [--out PATH]
"""

from __future__ import annotations

import argparse
import shutil
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DEFAULT_SRC = REPO / "document" / "tjs2" / "j_in"
DEFAULT_OUT = REPO / "doc" / "tjs2"

sys.path.insert(0, str(Path(__file__).parent))
from xml2md import convert_guide, Ctx  # noqa: E402


def parse_sjis_xml(xml_path: Path) -> ET.Element:
    """Python's expat may lack multi-byte encoding support. Decode SJIS and
    rewrite the encoding declaration so ET parses unicode safely."""
    raw = xml_path.read_bytes()
    for enc in ("cp932", "shift_jis", "utf-8"):
        try:
            text = raw.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    else:
        text = raw.decode("utf-8", errors="replace")
    # Strip any explicit encoding so ET treats the str as unicode.
    text = text.replace('encoding="Shift_JIS"', 'encoding="UTF-8"')
    text = text.replace("encoding='Shift_JIS'", "encoding='UTF-8'")
    return ET.fromstring(text)


def convert_guide_sjis(xml_path: Path, ctx: Ctx) -> tuple[str, str]:
    """Reimplementation of xml2md.convert_guide that uses SJIS-safe parsing."""
    from xml2md import render_mixed
    root = parse_sjis_xml(xml_path)
    title = (root.findtext("title") or xml_path.stem).strip()
    for t in list(root.findall("title")):
        root.remove(t)
    body = render_mixed(root, ctx).strip()
    return title, f"# {title}\n\n{body}\n"


# Friendly Japanese titles for the navigation. Falls back to the XML <title>
# when an entry is not in this map.
TITLE_OVERRIDES = {
    "about": "TJS2 について",
}

# Categorisation hint for callers (mkdocs nav). Not enforced by this script.
CLASS_LIKE = {
    "array", "dictionary", "date", "exception", "octet",
    "randomgenerator", "regexp", "string", "math", "basictypes",
}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--src", default=str(DEFAULT_SRC),
                    help="directory of TJS2 j_in *.xml files")
    ap.add_argument("--out", default=str(DEFAULT_OUT),
                    help="output directory under doc/")
    args = ap.parse_args(argv)

    src = Path(args.src)
    out = Path(args.out)

    if not src.exists():
        print(f"error: source not found: {src}", file=sys.stderr)
        return 2

    out.mkdir(parents=True, exist_ok=True)
    assets = out / "_assets"
    assets.mkdir(exist_ok=True)

    # Copy images if any exist (TJS2 docs are mostly text but be defensive)
    img_exts = {".png", ".jpg", ".jpeg", ".gif", ".svg"}
    for img_root in (src / "imgsrc", src.parent / "j" / "contents"):
        if not img_root.exists():
            continue
        for p in img_root.iterdir():
            if p.is_file() and p.suffix.lower() in img_exts:
                dest = assets / p.name
                if not dest.exists():
                    shutil.copy2(p, dest)

    # TJS2 has no class registry — pass empty set so <ref> falls back to inline
    # code formatting (the legacy XML rarely uses <ref> anyway).
    ctx = Ctx(classes=set(), kind="guide")

    pages = []
    for xml in sorted(src.glob("*.xml")):
        if xml.name == "frame.xml":
            continue  # legacy navigation frame
        try:
            title, md = convert_guide_sjis(xml, ctx)
        except (ET.ParseError, ValueError) as ex:
            print(f"warning: parse error {xml}: {ex}", file=sys.stderr)
            continue
        title = TITLE_OVERRIDES.get(xml.stem, title)
        # Replace the # heading with the override title if needed
        if xml.stem in TITLE_OVERRIDES:
            md = md.replace(md.split("\n", 1)[0], f"# {title}", 1)
        target = out / f"{xml.stem}.md"
        target.write_text(md, encoding="utf-8")
        pages.append((xml.stem, title))
        print(f"wrote {target.relative_to(REPO)}")

    # Replace the placeholder index with a real one
    index_lines = [
        "# TJS2 言語リファレンス",
        "",
        "TJS2 (TJS Just Script 2) は吉里吉里Z 内蔵のスクリプト言語です。",
        "",
        "## 言語仕様",
        "",
    ]
    for stem, title in pages:
        if stem in CLASS_LIKE:
            continue
        index_lines.append(f"- [{title}]({stem}.md)")
    index_lines += ["", "## 組み込みクラス・型", ""]
    for stem, title in pages:
        if stem in CLASS_LIKE:
            index_lines.append(f"- [{title}]({stem}.md)")
    index_lines.append("")
    (out / "index.md").write_text("\n".join(index_lines), encoding="utf-8")
    print(f"wrote {(out / 'index.md').relative_to(REPO)}")

    print(f"done: {len(pages)} page(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
