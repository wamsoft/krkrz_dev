"""Convert legacy Kirikiri specification HTML to Markdown.

Input:  document/specification/*.html
Output: doc/specification/*.md

The source HTML is hand-written, SJIS-encoded, and uses tables, headings,
and `<div class="title_bar">` blocks for sections. This converter:

  - Decodes Shift_JIS / cp932
  - Drops the surrounding navigation banner / top link
  - Converts <h1>/<h3> -> # / ###
  - Converts <div class="title_bar"><a name="X">Title</a></div> -> ## Title
  - Converts <table> with rowspan -> Markdown table (rowspan cells repeated)
  - Converts <p>/<br/> -> paragraphs with newlines
  - Converts <a href="X.html"> -> [text](X.md), external URLs preserved
  - Drops empty <a name="..."></a> anchors (mkdocs handles its own anchors)

Usage:
  python tools/docgen/html2spec.py [--src PATH] [--out PATH]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString, Tag

REPO = Path(__file__).resolve().parents[2]
DEFAULT_SRC = REPO / "document" / "specification"
DEFAULT_OUT = REPO / "doc" / "specification"


def read_text(path: Path) -> str:
    raw = path.read_bytes()
    for enc in ("cp932", "shift_jis", "utf-8"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace")


# ---------------------------------------------------------------------------
# Inline rendering
# ---------------------------------------------------------------------------

def render_inline(node) -> str:
    """Render inline elements to Markdown text."""
    if isinstance(node, NavigableString):
        return str(node)
    if not isinstance(node, Tag):
        return ""
    name = node.name.lower()
    inner = "".join(render_inline(c) for c in node.children)
    if name == "br":
        return "\n"
    if name in ("b", "strong"):
        return f"**{inner}**" if inner.strip() else inner
    if name in ("i", "em"):
        return f"*{inner}*" if inner.strip() else inner
    if name == "code":
        return f"`{inner}`" if inner.strip() else inner
    if name in ("sub", "sup"):
        return inner
    if name == "a":
        href = (node.get("href") or "").strip()
        # bare anchor (used for in-page targets) -> drop
        if not href and node.get("name"):
            return inner
        if not href:
            return inner
        # Only rewrite RELATIVE .html -> .md (leave external URLs alone)
        is_external = bool(re.match(r"^[a-z][a-z0-9+.-]*://", href, re.I))
        if not is_external and href.endswith(".html"):
            href = href[:-5] + ".md"
        return f"[{inner}]({href})"
    if name == "img":
        src = (node.get("src") or "").strip()
        alt = (node.get("alt") or "").strip()
        return f"![{alt}]({src})"
    if name == "span":
        return inner
    return inner


def cell_text(td: Tag) -> str:
    """Extract a table cell as a single line (newlines -> <br>)."""
    txt = render_inline(td).strip()
    txt = re.sub(r"\s*\n\s*", "<br>", txt)
    txt = txt.replace("|", "\\|")
    return txt or "&nbsp;"


# ---------------------------------------------------------------------------
# Table rendering with rowspan/colspan handling
# ---------------------------------------------------------------------------

def render_table(table: Tag) -> str:
    """Convert <table> to a Markdown table. Expands rowspan/colspan by
    repeating the cell content (Markdown has no native rowspan)."""
    rows: list[list[str]] = []
    headers: list[str] | None = None

    # We'll build a 2D matrix to handle rowspan
    matrix: list[list[str | None]] = []

    def get_row(r):
        while len(matrix) <= r:
            matrix.append([])
        return matrix[r]

    def place(r, c, value):
        row = get_row(r)
        while len(row) <= c:
            row.append(None)
        row[c] = value

    def first_free(row, start):
        c = start
        while c < len(row) and row[c] is not None:
            c += 1
        return c

    rowspan_iter = []
    for row_idx, tr in enumerate(table.find_all("tr")):
        cells = tr.find_all(["td", "th"])
        row = get_row(row_idx)
        col = 0
        for td in cells:
            col = first_free(row, col)
            text = cell_text(td)
            try:
                rspan = int(td.get("rowspan", "1"))
            except ValueError:
                rspan = 1
            try:
                cspan = int(td.get("colspan", "1"))
            except ValueError:
                cspan = 1
            for dr in range(rspan):
                for dc in range(cspan):
                    place(row_idx + dr, col + dc, text)
            col += cspan

    # Determine if first row is in <thead>
    thead = table.find("thead")
    if thead is not None:
        # The first matrix row is the header
        if matrix:
            headers = matrix[0]
            data_rows = matrix[1:]
        else:
            data_rows = []
    else:
        # All rows are data; synthesize an empty header
        if not matrix:
            return ""
        ncols = max(len(r) for r in matrix)
        headers = [""] * ncols
        data_rows = matrix

    # Normalize row widths
    width = max(len(headers), *(len(r) for r in data_rows)) if data_rows else len(headers)
    headers = headers + [""] * (width - len(headers))
    data_rows = [r + [""] * (width - len(r)) for r in data_rows]

    out = ["| " + " | ".join(c or "&nbsp;" for c in headers) + " |",
           "| " + " | ".join("---" for _ in headers) + " |"]
    for r in data_rows:
        out.append("| " + " | ".join(c or "&nbsp;" for c in r) + " |")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Block rendering
# ---------------------------------------------------------------------------

def render_block(node) -> str:
    if isinstance(node, NavigableString):
        s = str(node).strip()
        return s
    if not isinstance(node, Tag):
        return ""
    name = node.name.lower()
    if name == "h1":
        return f"# {render_inline(node).strip()}"
    if name == "h2":
        return f"## {render_inline(node).strip()}"
    if name == "h3":
        return f"### {render_inline(node).strip()}"
    if name == "h4":
        return f"#### {render_inline(node).strip()}"
    if name == "h5":
        return f"##### {render_inline(node).strip()}"
    if name == "p":
        text = render_inline(node).strip()
        return text
    if name == "pre":
        return "```\n" + node.get_text() + "\n```"
    if name == "blockquote":
        body = "\n".join(render_block(c) for c in node.children).strip()
        return "\n".join("> " + ln for ln in body.split("\n"))
    if name == "ul":
        items = []
        for li in node.find_all("li", recursive=False):
            items.append("- " + render_inline(li).strip())
        return "\n".join(items)
    if name == "ol":
        items = []
        for i, li in enumerate(node.find_all("li", recursive=False), 1):
            items.append(f"{i}. " + render_inline(li).strip())
        return "\n".join(items)
    if name == "table":
        return render_table(node)
    if name == "div":
        cls = node.get("class", [])
        if "title_bar" in cls:
            # Extract heading text + preserve original anchor name as {#id}
            title = render_inline(node).strip()
            anchor_name = ""
            inner_a = node.find("a", attrs={"name": True})
            if inner_a is not None:
                anchor_name = inner_a.get("name", "").strip()
            if not title:
                return ""
            if anchor_name:
                return f"## {title} {{ #{anchor_name} }}"
            return f"## {title}"
        # Generic div: recurse
        return "\n\n".join(render_block(c) for c in node.children if not _is_blank(c))
    if name == "br":
        return ""
    # Default: recurse
    return "\n\n".join(render_block(c) for c in node.children if not _is_blank(c))


def _is_blank(node) -> bool:
    if isinstance(node, NavigableString):
        return not str(node).strip()
    return False


# ---------------------------------------------------------------------------
# Page conversion
# ---------------------------------------------------------------------------

def convert(html: str) -> tuple[str, str]:
    soup = BeautifulSoup(html, "html.parser")
    title_tag = soup.find("title")
    title = (title_tag.get_text() if title_tag else "").strip()
    # title format is often "<site> / <page>" — keep just the page
    if "/" in title:
        title = title.rsplit("/", 1)[-1].strip()

    # Drop navigation chrome
    for sel in ("#top_link", ".title-banner", "#title-banner", "script", "style"):
        for el in soup.select(sel):
            el.decompose()
    # Drop empty <a name="..."></a> anchors
    for a in soup.find_all("a"):
        if a.get("name") and not a.get("href") and not a.text.strip():
            a.decompose()

    content = soup.find("div", class_="content")
    body_root = content if content is not None else (soup.body or soup)

    parts = [f"# {title}"] if title else []
    for child in body_root.children:
        block = render_block(child)
        if block and block.strip():
            parts.append(block.strip())

    md = "\n\n".join(parts).strip() + "\n"
    md = re.sub(r"\n{3,}", "\n\n", md)
    return title, md


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--src", default=str(DEFAULT_SRC),
                    help="directory of *.html spec files")
    ap.add_argument("--out", default=str(DEFAULT_OUT),
                    help="output directory under doc/")
    args = ap.parse_args(argv)

    src = Path(args.src)
    out = Path(args.out)
    if not src.exists():
        print(f"error: source not found: {src}", file=sys.stderr)
        return 2
    out.mkdir(parents=True, exist_ok=True)

    pages = []
    for html_path in sorted(src.glob("*.html")):
        text = read_text(html_path)
        title, md = convert(text)
        target = out / (html_path.stem + ".md")
        target.write_text(md, encoding="utf-8")
        pages.append((html_path.stem, title))
        print(f"wrote {target.relative_to(REPO)}")
    print(f"done: {len(pages)} page(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
