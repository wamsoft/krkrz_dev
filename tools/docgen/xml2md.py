"""Legacy kirikiri-z XML reference -> Markdown converter.

Input  : document/kirikiriz/j_in/**/*.xml  (legacy format, see to_html.pl)
Output : doc/reference/<Class>.md  (one file per class doc)
         doc/guide/<Topic>.md      (non-class docs)
         doc/_assets/*             (images from j_in/imgsrc/)
         doc/_index.md             (top-level TOC)

Usage: python tools/docgen/xml2md.py [--src PATH] [--out PATH]
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DEFAULT_SRC = REPO / "document" / "kirikiriz" / "j_in"
DEFAULT_OUT = REPO / "doc"

# ---------------------------------------------------------------------------
# Class-name registry (built from classes/f_*.xml filenames)
# ---------------------------------------------------------------------------

def collect_class_names(src: Path) -> set[str]:
    out: set[str] = set()
    for p in (src / "classes").glob("f_*.xml*"):
        name = p.name
        if name.endswith(".xml.in"):
            name = name[:-7]
        elif name.endswith(".xml"):
            name = name[:-4]
        else:
            continue
        if name.startswith("f_"):
            out.add(name[2:])
    return out

# ---------------------------------------------------------------------------
# Link helpers
# ---------------------------------------------------------------------------

def slug(name: str) -> str:
    """GitHub-flavored markdown auto-anchor for a heading."""
    s = name.strip().lower()
    s = re.sub(r"[^\w\- ]+", "", s, flags=re.UNICODE)
    s = s.replace(" ", "-")
    return s

def class_link(cls: str, member: str | None = None) -> str:
    anchor = f"#{slug(member)}" if member else ""
    return f"{cls}.md{anchor}"

def guide_link(topic: str, member: str | None = None) -> str:
    anchor = f"#{slug(member)}" if member else ""
    return f"../guide/{topic}.md{anchor}"

def resolve_href(href: str, classes: set[str]) -> tuple[str, str]:
    """Map legacy href like 'f_Layer.html' or 'f_Layer_onClick.html' or
    'EventSystem.html' -> (relative_md_path, title_hint).
    """
    h = href.strip()
    if h.endswith(".html"):
        h = h[:-5]
    if h.startswith("f_"):
        body = h[2:]
        # split on first underscore: class_member
        if "_" in body:
            cls, _, mem = body.partition("_")
            # handle "Window.BasicDrawDevice_foo" by preferring longest known class
            for cand in classes:
                if body.startswith(cand + "_"):
                    cls = cand
                    mem = body[len(cand) + 1:]
                    break
            return (class_link(cls, mem), f"{cls}.{mem}")
        return (class_link(body), body)
    if "#" in h:
        topic, _, anch = h.partition("#")
        return (guide_link(topic, anch), f"{topic}.{anch}")
    return (guide_link(h), h)

# ---------------------------------------------------------------------------
# Inline rendering
# ---------------------------------------------------------------------------

INLINE_TAGS = {
    "kw", "tt", "ref", "at", "a", "b", "i", "sup", "nobr", "wave", "r",
    "colorbox", "comlink", "anchor", "img",
}

BLOCK_TAGS = {
    "para", "ptitle", "desc", "note", "bq", "example", "dl", "dt", "dd",
    "ul", "ol", "li", "hr", "member", "arg", "argitem", "name", "type",
    "shortdesc", "result", "access", "default", "title", "doc",
}

def _text(x: str | None) -> str:
    return x or ""

def esc_inline(s: str) -> str:
    # minimal escape; the legacy docs already have reasonable whitespace.
    return s.replace("\r", "")

def render_inline(elem: ET.Element, ctx: "Ctx") -> str:
    """Render an element's mixed content, returning inline markdown."""
    parts: list[str] = [esc_inline(_text(elem.text))]
    for child in elem:
        parts.append(render_inline_tag(child, ctx))
        parts.append(esc_inline(_text(child.tail)))
    return "".join(parts)

def render_inline_tag(e: ET.Element, ctx: "Ctx") -> str:
    tag = e.tag
    inner = render_inline(e, ctx)
    if tag == "r":
        return "  \n"  # hard line break in markdown
    if tag == "kw":
        return f"**{inner}**"
    if tag == "tt":
        return f"`{inner}`" if inner else ""
    if tag in ("b",):
        return f"**{inner}**"
    if tag == "i":
        return f"*{inner}*"
    if tag in ("sup", "nobr"):
        return inner
    if tag == "wave":
        return f"*{inner}*"
    if tag == "ref":
        return resolve_ref(inner, ctx)
    if tag == "at":
        href = e.get("href", "")
        if not href:
            return inner
        path, _title = resolve_href(href, ctx.classes)
        label = inner or _title
        return f"[{label}]({path})"
    if tag == "a":
        href = e.get("href", "")
        return f"[{inner}]({href})" if href else inner
    if tag == "comlink":
        href = e.get("href", "")
        if href:
            path, title = resolve_href(href, ctx.classes)
            return f" ( → [{title}]({path}) )"
        return f" ( → {inner} )"
    if tag == "anchor":
        name = e.get("name", "")
        return f'<a id="{name}"></a>{inner}' if name else inner
    if tag == "colorbox":
        color = e.get("color", "")
        return f"`{color}`" if color else inner
    if tag == "img":
        src = e.get("src", "")
        alt = e.get("alt", "")
        # map imgsrc/foo.png -> ../_assets/foo.png
        src = re.sub(r"^(?:\./)?imgsrc/", "../_assets/", src)
        return f"![{alt}]({src})"
    # unknown inline -> fall back to inner
    return inner

def resolve_ref(txt: str, ctx: "Ctx") -> str:
    """`<ref>Layer.visible</ref>` -> markdown link or inline code."""
    raw = txt.strip()
    if not raw:
        return ""
    # longest matching class prefix
    best = None
    for cls in ctx.classes:
        if raw == cls:
            return f"[{raw}]({class_link(cls)})"
        if raw.startswith(cls + "."):
            if best is None or len(cls) > len(best):
                best = cls
    if best:
        member = raw[len(best) + 1:]
        return f"[{raw}]({class_link(best, member)})"
    return f"`{raw}`"

# ---------------------------------------------------------------------------
# Block rendering
# ---------------------------------------------------------------------------

class Ctx:
    def __init__(self, classes: set[str], kind: str):
        self.classes = classes
        self.kind = kind  # "class" or "guide"

_IDEO_WS = "\u3000"  # full-width space used as legacy indent marker

def strip_indent_space(s: str) -> str:
    # legacy docs use ideographic/leading spaces heavily for indent.
    out: list[str] = []
    for ln in s.splitlines():
        ln = ln.rstrip()
        stripped = ln.lstrip(" \t" + _IDEO_WS)
        out.append(stripped)
    return "\n".join(out).strip("\n")

def _clean_table_cell(s: str) -> str:
    s = s.replace("\r", "")
    s = s.replace("  \n", " ").replace("\n", " ")
    s = re.sub(r"[ \t\u3000]+", " ", s).strip()
    return s.replace("|", "\\|")

def render_children_blocks(parent: ET.Element, ctx: Ctx) -> str:
    chunks: list[str] = []
    # leading free text
    lead = esc_inline(_text(parent.text)).strip()
    if lead:
        chunks.append(lead)
    for child in parent:
        chunks.append(render_block(child, ctx))
        tail = esc_inline(_text(child.tail)).strip()
        if tail:
            chunks.append(tail)
    return "\n\n".join(c for c in chunks if c)

def render_block(e: ET.Element, ctx: Ctx) -> str:
    tag = e.tag
    if tag == "para":
        title_elem = e.find("ptitle")
        title = render_inline(title_elem, ctx).strip() if title_elem is not None else ""
        # Strip <ptitle> from the tree so render_mixed skips it, then let
        # render_mixed handle inline vs. block children uniformly.
        stripped = ET.Element(e.tag, e.attrib)
        stripped.text = e.text
        for ch in e:
            if ch.tag == "ptitle":
                # preserve tail text after ptitle
                if ch.tail:
                    if len(stripped) == 0:
                        stripped.text = (stripped.text or "") + ch.tail
                    else:
                        last = stripped[-1]
                        last.tail = (last.tail or "") + ch.tail
                continue
            stripped.append(ch)
        body = render_mixed(stripped, ctx)
        heading = f"## {title}\n\n" if title else ""
        return heading + body
    if tag == "ptitle":
        return f"## {render_inline(e, ctx).strip()}"
    if tag == "desc":
        return render_mixed(e, ctx)
    if tag == "note":
        body = render_mixed(e, ctx).strip()
        if not body:
            return ""
        quoted = "\n".join("> " + ln if ln else ">" for ln in body.splitlines())
        return "> **Note:**\n" + quoted
    if tag == "bq" or tag == "example":
        # Raw concatenation: preserve tabs / spaces inside code blocks, do
        # NOT apply strip_indent_space. <r/> marks a line break in legacy
        # markup; XML newlines between lines are accidental whitespace.
        buf: list[str] = []
        if e.text:
            buf.append(e.text)
        for ch in e:
            if ch.tag == "r":
                buf.append("\n")
            else:
                buf.append(render_inline_tag(ch, ctx))
            if ch.tail:
                buf.append(ch.tail)
        body = "".join(buf)
        # Remove the stray XML-formatting newlines that immediately follow
        # an <r/>-generated "\n" (so "\n\n" collapses, but explicit blank
        # lines authored with two <r/>s also collapse — acceptable).
        body = re.sub(r"\n[ \t]*\n", "\n", body)
        body = "\n".join(ln.rstrip() for ln in body.splitlines()).strip("\n")
        return "```\n" + body + "\n```"
    if tag == "dl":
        items: list[str] = []
        pending_dt: str | None = None
        for ch in e:
            if ch.tag == "dt":
                if pending_dt is not None:
                    items.append(f"- **{pending_dt}**")
                pending_dt = render_inline(ch, ctx).strip()
            elif ch.tag == "dd":
                dd_text = render_mixed(ch, ctx).strip()
                dd_text = dd_text.replace("\n", "\n  ")
                label = pending_dt or ""
                pending_dt = None
                items.append(f"- **{label}**  \n  {dd_text}")
        if pending_dt is not None:
            items.append(f"- **{pending_dt}**")
        return "\n".join(items)
    if tag in ("ul", "ol"):
        marker_fn = (lambda _i: "-") if tag == "ul" else (lambda i: f"{i+1}.")
        rows = []
        for i, ch in enumerate(e.findall("li")):
            body = render_mixed(ch, ctx).strip()
            body = body.replace("\n", "\n  ")
            rows.append(f"{marker_fn(i)} {body}")
        return "\n".join(rows)
    if tag == "hr":
        return "---"
    if tag == "img":
        return render_inline_tag(e, ctx)
    # inline tags encountered at block position -> wrap in paragraph
    if tag in INLINE_TAGS:
        return render_inline_tag(e, ctx)
    # unknown block -> render children
    return render_mixed(e, ctx)

def render_mixed(elem: ET.Element, ctx: Ctx) -> str:
    """Render mixed content. Inline text runs are cleaned of legacy indent;
    block children (code fences, tables, notes) are passed through verbatim
    so their internal formatting survives."""
    out: list[str] = []
    buf: list[str] = []

    def flush_buf():
        if buf:
            s = "".join(buf)
            cleaned = strip_indent_space(s)
            if cleaned:
                out.append(cleaned)
            buf.clear()

    if elem.text:
        buf.append(esc_inline(elem.text))
    for ch in elem:
        if ch.tag in INLINE_TAGS:
            buf.append(render_inline_tag(ch, ctx))
        else:
            flush_buf()
            out.append(render_block(ch, ctx))
        if ch.tail:
            buf.append(esc_inline(ch.tail))
    flush_buf()
    return "\n\n".join(p for p in out if p)

# ---------------------------------------------------------------------------
# Class doc rendering
# ---------------------------------------------------------------------------

MEMBER_TYPE_JA = {
    "property": "プロパティ",
    "method": "メソッド",
    "event": "イベント",
    "constructor": "コンストラクタ",
}

def render_member(m: ET.Element, ctx: Ctx) -> str:
    name = (m.findtext("name") or "").strip()
    mtype = (m.findtext("type") or "").strip()
    shortdesc = render_inline(m.find("shortdesc") or ET.Element("x"), ctx).strip()
    access = (m.findtext("access") or "").strip()
    desc_el = m.find("desc")
    result_el = m.find("result")
    arg_el = m.find("arg")

    parts: list[str] = []
    parts.append(f"### {name}")
    meta: list[str] = []
    if mtype:
        meta.append(MEMBER_TYPE_JA.get(mtype, mtype))
    if access:
        meta.append(f"アクセス: `{access}`")
    if meta:
        parts.append(" / ".join(meta))
    if shortdesc:
        parts.append(shortdesc)

    if arg_el is not None and arg_el.find("argitem") is not None:
        tbl: list[str] = ["| 引数 | 既定値 | 説明 |", "| --- | --- | --- |"]
        for ai in arg_el.findall("argitem"):
            an = (ai.findtext("name") or "").strip() or "&nbsp;"
            ad = (ai.findtext("default") or "").strip() or "&nbsp;"
            desc_sub = ai.find("desc")
            if desc_sub is not None:
                ddesc = render_inline(desc_sub, ctx).strip()
            else:
                ddesc = render_inline(ai, ctx).strip()
            ddesc = _clean_table_cell(ddesc)
            if not ddesc:
                ddesc = "&nbsp;"
            tbl.append(f"| `{an}` | `{ad}` | {ddesc} |")
        parts.append("**引数**\n\n" + "\n".join(tbl))

    if result_el is not None:
        rtxt = render_mixed(result_el, ctx).strip()
        if rtxt:
            parts.append("**戻り値**\n\n" + rtxt)

    if desc_el is not None:
        dtxt = render_mixed(desc_el, ctx).strip()
        if dtxt:
            parts.append("**解説**\n\n" + dtxt)

    refs = m.findall("ref")
    if refs:
        links = []
        for r in refs:
            inner = render_inline(r, ctx).strip()
            if inner:
                links.append(resolve_ref(inner, ctx))
        if links:
            parts.append("**関連:** " + " / ".join(links))

    return "\n\n".join(parts)

def convert_class(xml_path: Path, ctx: Ctx) -> tuple[str, str]:
    root = ET.parse(xml_path).getroot()
    title = (root.findtext("title") or xml_path.stem[2:]).strip()
    top_desc = root.find("desc")
    top_desc_md = render_mixed(top_desc, ctx).strip() if top_desc is not None else ""

    members = list(root.findall("member"))
    out: list[str] = [f"# {title}"]
    if top_desc_md:
        out.append(top_desc_md)

    if members:
        toc: list[str] = []
        by_type: dict[str, list[tuple[str, str]]] = {}
        for m in members:
            name = (m.findtext("name") or "").strip()
            mtype = (m.findtext("type") or "").strip()
            sd = render_inline(m.find("shortdesc") or ET.Element("x"), ctx).strip()
            by_type.setdefault(mtype, []).append((name, sd))
        toc_blocks: list[str] = ["## メンバー一覧"]
        for t in ("constructor", "property", "method", "event"):
            rows = by_type.get(t, [])
            if not rows:
                continue
            section = [f"### {MEMBER_TYPE_JA.get(t, t)}"]
            for name, sd in rows:
                label = f"[{name}](#{slug(name)})"
                sd1 = sd.replace("\n", " ")
                section.append(f"- {label}" + (f" — {sd1}" if sd1 else ""))
            toc_blocks.append("\n".join(section))
        out.append("\n\n".join(toc_blocks))
        out.append("---")
        for m in members:
            out.append(render_member(m, ctx))
            out.append("---")

    return title, "\n\n".join(out).rstrip() + "\n"

def convert_guide(xml_path: Path, ctx: Ctx) -> tuple[str, str]:
    root = ET.parse(xml_path).getroot()
    title = (root.findtext("title") or xml_path.stem).strip()
    # Drop <title> from the tree so it does not render as body text.
    for t in list(root.findall("title")):
        root.remove(t)
    body = render_mixed(root, ctx).strip()
    md = f"# {title}\n\n{body}\n"
    return title, md

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default=str(DEFAULT_SRC))
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    args = ap.parse_args()
    src = Path(args.src)
    out = Path(args.out)

    if not src.exists():
        print(f"source not found: {src}", file=sys.stderr)
        return 2

    classes = collect_class_names(src)
    print(f"[xml2md] known classes: {len(classes)}")

    ref_dir = out / "reference"
    guide_dir = out / "guide"
    assets_dir = out / "_assets"
    for d in (ref_dir, guide_dir, assets_dir):
        d.mkdir(parents=True, exist_ok=True)

    # copy images
    imgsrc = src / "imgsrc"
    if imgsrc.exists():
        for p in imgsrc.iterdir():
            if p.is_file():
                shutil.copy2(p, assets_dir / p.name)

    ctx_cls = Ctx(classes, "class")
    ctx_guide = Ctx(classes, "guide")

    # classes
    class_titles: list[tuple[str, str]] = []
    for xml in sorted((src / "classes").glob("f_*.xml*")):
        if xml.name.endswith(".xml.in"):
            stem = xml.name[:-7][2:]
        elif xml.name.endswith(".xml"):
            stem = xml.stem[2:]
        else:
            continue
        try:
            title, md = convert_class(xml, ctx_cls)
        except ET.ParseError as ex:
            print(f"[xml2md] parse error {xml}: {ex}", file=sys.stderr)
            continue
        (ref_dir / f"{stem}.md").write_text(md, encoding="utf-8")
        class_titles.append((stem, title))
        print(f"[xml2md] class {stem}")

    # guides
    guide_titles: list[tuple[str, str]] = []
    for xml in sorted(src.glob("*.xml")):
        if xml.name == "frame.xml":
            continue  # legacy navigation frame, not a doc
        try:
            title, md = convert_guide(xml, ctx_guide)
        except ET.ParseError as ex:
            print(f"[xml2md] parse error {xml}: {ex}", file=sys.stderr)
            continue
        (guide_dir / f"{xml.stem}.md").write_text(md, encoding="utf-8")
        guide_titles.append((xml.stem, title))
        print(f"[xml2md] guide {xml.stem}")

    # index
    idx_lines: list[str] = ["# 吉里吉里Z リファレンス", "", "## ガイド", ""]
    for stem, title in sorted(guide_titles, key=lambda x: x[0].lower()):
        idx_lines.append(f"- [{title}](guide/{stem}.md)")
    idx_lines += ["", "## クラスリファレンス", ""]
    for stem, title in sorted(class_titles, key=lambda x: x[0].lower()):
        idx_lines.append(f"- [{title}](reference/{stem}.md)")
    idx_lines.append("")
    (out / "_index.md").write_text("\n".join(idx_lines), encoding="utf-8")
    print(f"[xml2md] wrote _index.md ({len(class_titles)} classes, {len(guide_titles)} guides)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
