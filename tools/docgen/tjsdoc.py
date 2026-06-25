"""manual.tjs (TJS pseudo-code with javadoc) -> Markdown reference generator.

Input  : a manual.tjs file or a directory containing manual.tjs files
Output : doc/reference/<ClassName>.md (one file per class)

Usage:
  python tools/docgen/tjsdoc.py --in src/plugins/binaryStream/manual.tjs
  python tools/docgen/tjsdoc.py --in src/plugins --out doc/reference
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class Doc:
    summary: str = ""
    description: str = ""
    params: list = field(default_factory=list)  # list[(name, type, desc)]
    returns: str = ""
    return_type: str = ""
    type_hint: str = ""
    kind_hint: str = ""  # @kind event -> "event"
    sees: list = field(default_factory=list)  # @see X.Y entries


@dataclass
class Member:
    kind: str  # "function" | "property" | "const"
    name: str
    args: list = field(default_factory=list)  # list[(name, default)]
    access: str = ""  # "r" | "w" | "rw"
    value: str = ""
    doc: Doc = field(default_factory=Doc)


@dataclass
class ClassDef:
    name: str
    extends: str = ""
    doc: Doc = field(default_factory=Doc)
    members: list = field(default_factory=list)
    source: str = ""  # plugin name or "" for core/main definition


# ---------------------------------------------------------------------------
# Tokenizer helpers
# ---------------------------------------------------------------------------

def skip_string(text, pos):
    quote = text[pos]
    pos += 1
    while pos < len(text):
        c = text[pos]
        if c == "\\":
            pos += 2
            continue
        if c == quote:
            return pos + 1
        pos += 1
    return pos


def find_block_end(text, open_pos):
    """text[open_pos] == '{' -> return index of matching '}'. Skips strings/comments."""
    assert text[open_pos] == "{"
    depth = 1
    pos = open_pos + 1
    n = len(text)
    while pos < n:
        c = text[pos]
        if c in ('"', "'"):
            pos = skip_string(text, pos)
            continue
        if text[pos:pos+2] == "/*":
            e = text.find("*/", pos + 2)
            pos = e + 2 if e != -1 else n
            continue
        if text[pos:pos+2] == "//":
            e = text.find("\n", pos)
            pos = e if e != -1 else n
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return pos
        pos += 1
    return n


def parse_args_str(s):
    """Parse function arg list. Returns [(name, default), ...]."""
    s = s.strip()
    if not s:
        return []
    parts = []
    depth = 0
    cur = ""
    pos = 0
    n = len(s)
    while pos < n:
        c = s[pos]
        if c in ('"', "'"):
            np = skip_string(s, pos)
            cur += s[pos:np]
            pos = np
            continue
        if c in "([{":
            depth += 1
        elif c in ")]}":
            depth -= 1
        if c == "," and depth == 0:
            parts.append(cur.strip())
            cur = ""
            pos += 1
            continue
        cur += c
        pos += 1
    if cur.strip():
        parts.append(cur.strip())
    out = []
    for a in parts:
        if "=" in a:
            name_part, _, default = a.partition("=")
        else:
            name_part, default = a, ""
        name_part = name_part.strip()
        # name[:Type] convention used in some manual.tjs
        if ":" in name_part:
            name, _, type_hint = name_part.partition(":")
            out.append((name.strip(), default.strip(), type_hint.strip()))
        else:
            out.append((name_part, default.strip(), ""))
    return out


# ---------------------------------------------------------------------------
# Comment block collector + javadoc parser
# ---------------------------------------------------------------------------

JAVADOC_TAG_RE = re.compile(r"^@(\w+)(?:\s+(.*))?$")

HEADING_WORDS = {
    "定数", "定義", "プロパティ", "メソッド", "イベント",
    "コンストラクタ", "デストラクタ", "タイプ", "フラグ", "モード",
}
HEADING_SUFFIX_RE = re.compile(
    r"(定義|定数|系|関連|種類|一覧|タイプ|フラグ|モード|定数群)\s*$"
)


def is_section_heading(text):
    """Heuristic: short categorical comments like '// 定数' or '// FontStyle 定義'
    are section headings, not member documentation. Skip them silently."""
    t = text.strip()
    if not t:
        return False
    if t in HEADING_WORDS:
        return True
    if HEADING_SUFFIX_RE.search(t) and len(t) <= 20:
        return True
    return False


def collect_doc_block(text, pos):
    """Skip whitespace; collect /** */ and // comments preceding the next token.
    A blank line resets the accumulated block."""
    block_parts = []
    n = len(text)
    while pos < n:
        c = text[pos]
        if c == "\n":
            la = pos + 1
            while la < n and text[la] in " \t":
                la += 1
            saw_blank = la < n and text[la] == "\n"
            pos += 1
            if saw_blank and block_parts:
                block_parts = []
            continue
        if c in " \t\r":
            pos += 1
            continue
        if text[pos:pos+3] == "/**":
            e = text.find("*/", pos + 3)
            if e == -1:
                pos = n
                break
            block_parts.append(text[pos:e+2])
            pos = e + 2
            continue
        if text[pos:pos+2] == "/*":
            e = text.find("*/", pos + 2)
            pos = e + 2 if e != -1 else n
            continue
        if text[pos:pos+2] == "//":
            e = text.find("\n", pos)
            if e == -1:
                e = n
            block_parts.append(text[pos:e])
            pos = e
            continue
        break
    return "\n".join(block_parts), pos


def collect_trailing_line_comment(text, pos):
    """At pos (just after a ';'), pick up any same-line // comment."""
    n = len(text)
    while pos < n and text[pos] in " \t":
        pos += 1
    if pos + 1 < n and text[pos:pos+2] == "//":
        e = text.find("\n", pos)
        if e == -1:
            e = n
        comment = text[pos+2:e].strip()
        return comment, e
    return "", pos


def clean_javadoc_lines(text):
    text = text.strip()
    if text.startswith("/**"):
        text = text[3:]
    elif text.startswith("/*"):
        text = text[2:]
    if text.endswith("*/"):
        text = text[:-2]
    out = []
    for ln in text.split("\n"):
        m = re.match(r"^\s*\*\s?(.*)$", ln.rstrip())
        out.append(m.group(1) if m else ln.strip())
    return out


def parse_doc_block(comment_block):
    if not comment_block.strip():
        return Doc()

    segments = []  # list[(kind, text)]
    pos = 0
    n = len(comment_block)
    while pos < n:
        if comment_block[pos:pos+3] == "/**":
            e = comment_block.find("*/", pos + 3)
            if e == -1:
                break
            segments.append(("javadoc", comment_block[pos:e+2]))
            pos = e + 2
            continue
        if comment_block[pos:pos+2] == "//":
            e = comment_block.find("\n", pos)
            if e == -1:
                e = n
            txt = comment_block[pos+2:e].strip()
            if txt.startswith("<"):
                txt = txt[1:].strip()
            segments.append(("line", txt))
            pos = e + 1
            continue
        pos += 1

    # Drop section-heading line comments ('// 定数', '// FontStyle 定義' etc.)
    segments = [s for s in segments
                if not (s[0] == "line" and is_section_heading(s[1]))]

    doc = Doc()
    summary_lines = []
    desc_lines = []
    line_only = []
    in_tag = None
    tag_buffer = ""

    def flush():
        nonlocal in_tag, tag_buffer
        if not in_tag:
            return
        txt = tag_buffer.strip()
        if in_tag == "param":
            # JSDoc-style: @param {Type} name desc
            m = re.match(r"^\{([^{}]+)\}\s*(\S+)\s*(.*)$", txt, re.DOTALL)
            if m:
                doc.params.append((m.group(2), m.group(1).strip(),
                                   m.group(3).strip()))
            else:
                m = re.match(r"^(\S+)\s*(.*)$", txt, re.DOTALL)
                if m:
                    doc.params.append((m.group(1), "", m.group(2).strip()))
        elif in_tag in ("return", "returns"):
            # JSDoc-style: @return {Type} desc
            m = re.match(r"^\{([^{}]+)\}\s*(.*)$", txt, re.DOTALL)
            if m:
                doc.return_type = m.group(1).strip()
                doc.returns = m.group(2).strip()
            else:
                doc.returns = txt
        elif in_tag == "description":
            desc_lines.append(txt)
        elif in_tag == "type":
            doc.type_hint = txt
        elif in_tag == "kind":
            doc.kind_hint = txt.strip()
        elif in_tag == "see":
            for ref in txt.splitlines():
                ref = ref.strip()
                if ref:
                    doc.sees.append(ref)
        in_tag = None
        tag_buffer = ""

    for kind, text in segments:
        if kind == "javadoc":
            for ln in clean_javadoc_lines(text):
                m = JAVADOC_TAG_RE.match(ln.strip())
                if m:
                    flush()
                    in_tag = m.group(1)
                    tag_buffer = m.group(2) or ""
                    continue
                if in_tag:
                    cont = ln.lstrip()
                    tag_buffer += ("\n" + cont) if cont else "\n"
                else:
                    if ln.strip():
                        if not summary_lines:
                            summary_lines.append(ln.strip())
                        else:
                            desc_lines.append(ln.strip())
                    else:
                        if desc_lines:
                            desc_lines.append("")
            flush()
        else:
            line_only.append(text)

    if line_only:
        joined = " ".join(t for t in line_only if t).strip()
        if not summary_lines and joined:
            summary_lines.append(joined)
        elif joined:
            desc_lines.append(joined)

    doc.summary = " ".join(summary_lines).strip()
    doc.description = "\n".join(desc_lines).strip()
    return doc


# ---------------------------------------------------------------------------
# Top-level parser
# ---------------------------------------------------------------------------

CLASS_RE = re.compile(r"class\s+([\w.]+)(?:\s+extends\s+([\w.]+))?\s*\{")
FUNCTION_RE = re.compile(r"function\s+(\w+)\s*\(")
EVENT_RE = re.compile(r"event\s+(\w+)\s*\(")
PROPERTY_RE = re.compile(r"property\s+(\w+)\s*(\{|;)")
CONST_RE = re.compile(r"const\s+(\w+)(?:\s*=\s*([^,;\n]*?))?\s*(?:[,;]|(?=\n))")


def parse_class_body(body, nested_out=None, parent_name=""):
    """Parse the body of a class (text inside the outer { }).
    If nested_out is a list, nested class definitions are appended to it
    (with names qualified by parent_name)."""
    members = []
    pos = 0
    n = len(body)
    while pos < n:
        comment_block, pos = collect_doc_block(body, pos)
        if pos >= n:
            break

        m = CLASS_RE.match(body, pos)
        if m and nested_out is not None:
            inner_name = m.group(1)
            qualified = f"{parent_name}.{inner_name}" if parent_name else inner_name
            inner_cls = ClassDef(
                name=qualified,
                extends=m.group(2) or "",
                doc=parse_doc_block(comment_block),
            )
            brace = m.end() - 1
            end = find_block_end(body, brace)
            inner_cls.members = parse_class_body(
                body[brace+1:end], nested_out=nested_out, parent_name=qualified)
            nested_out.append(inner_cls)
            pos = end + 1
            continue

        # `event NAME(args)` is sugar for a function with kind=event
        is_event_kw = False
        m = FUNCTION_RE.match(body, pos)
        if not m:
            m_evt = EVENT_RE.match(body, pos)
            if m_evt:
                m = m_evt
                is_event_kw = True
        if m:
            name = m.group(1)
            paren = m.end() - 1
            depth = 1
            p = paren + 1
            while p < n and depth > 0:
                c = body[p]
                if c in ('"', "'"):
                    p = skip_string(body, p)
                    continue
                if c == "(":
                    depth += 1
                elif c == ")":
                    depth -= 1
                p += 1
            args = parse_args_str(body[paren+1:p-1])
            while p < n and body[p] in " \t":
                p += 1
            if p < n and body[p] == "{":
                p = find_block_end(body, p) + 1
            while p < n and body[p] in " \t":
                p += 1
            if p < n and body[p] == ";":
                p += 1
            trailing, p = collect_trailing_line_comment(body, p)
            doc = parse_doc_block(comment_block)
            if trailing and not doc.summary:
                doc.summary = trailing.lstrip("<").strip()
            if is_event_kw and not doc.kind_hint:
                doc.kind_hint = "event"
            members.append(Member(kind="function", name=name, args=args, doc=doc))
            pos = p
            continue

        m = PROPERTY_RE.match(body, pos)
        if m:
            name = m.group(1)
            access = "rw"
            if m.group(2) == "{":
                brace = m.end() - 1
                end = find_block_end(body, brace)
                inside = body[brace+1:end]
                has_g = bool(re.search(r"\bgetter\b", inside))
                has_s = bool(re.search(r"\bsetter\b", inside))
                if has_g and has_s:
                    access = "rw"
                elif has_g:
                    access = "r"
                elif has_s:
                    access = "w"
                else:
                    access = "rw"
                p = end + 1
            else:
                p = m.end()
            while p < n and body[p] in " \t":
                p += 1
            if p < n and body[p] == ";":
                p += 1
            trailing, p = collect_trailing_line_comment(body, p)
            doc = parse_doc_block(comment_block)
            if trailing and not doc.summary:
                doc.summary = trailing.lstrip("<").strip()
            tl = (doc.summary + " " + doc.description).lower()
            if "read only" in tl or "read-only" in tl:
                if access == "rw":
                    access = "r"
            members.append(Member(kind="property", name=name, access=access, doc=doc))
            pos = p
            continue

        m = CONST_RE.match(body, pos)
        if m:
            name = m.group(1)
            value = (m.group(2) or "").strip()
            doc = parse_doc_block(comment_block)
            members.append(Member(kind="const", name=name, value=value, doc=doc))
            pos = m.end()
            # const grouped with comma share one declaration; advance again
            continue

        pos += 1
    return members


def parse_file(text):
    classes = []
    pos = 0
    n = len(text)
    while pos < n:
        comment_block, pos = collect_doc_block(text, pos)
        if pos >= n:
            break
        m = CLASS_RE.match(text, pos)
        if m:
            cls = ClassDef(
                name=m.group(1),
                extends=m.group(2) or "",
                doc=parse_doc_block(comment_block),
            )
            brace = m.end() - 1
            end = find_block_end(text, brace)
            nested = []
            cls.members = parse_class_body(
                text[brace+1:end], nested_out=nested, parent_name=cls.name)
            classes.append(cls)
            classes.extend(nested)
            pos = end + 1
            continue
        pos += 1
    return classes


# ---------------------------------------------------------------------------
# Markdown rendering
# ---------------------------------------------------------------------------

def slug(name):
    s = name.strip().lower()
    s = re.sub(r"[^\w\- ]+", "", s, flags=re.UNICODE)
    return s.replace(" ", "-")


def md_cell(text):
    """Escape content for a markdown table cell. Collapses whitespace runs and
    blank lines (a single \\n becomes <br>; multiple newlines become a single
    <br>; leading whitespace on continuation lines is dropped)."""
    s = text.replace("\\", "\\\\").replace("|", "\\|")
    # Strip leading spaces on each line so continuation indents don't bleed.
    s = "\n".join(ln.lstrip() for ln in s.split("\n"))
    # Collapse blank-line runs and multi-newline to a single <br>.
    s = re.sub(r"\n\s*\n", "<br>", s)
    s = s.replace("\n", "<br>")
    s = re.sub(r"(<br>)+", "<br>", s)
    return s.strip()


def md_table(headers, rows):
    out = ["| " + " | ".join(headers) + " |",
           "| " + " | ".join("---" for _ in headers) + " |"]
    for r in rows:
        out.append("| " + " | ".join(md_cell(c) for c in r) + " |")
    return "\n".join(out)


def render_member(m, cls):
    parts = [f"### {m.name}"]
    if m.kind == "function":
        short = cls.name.split(".")[-1]
        if m.doc.kind_hint == "event":
            kind = "イベント"
        elif m.name == short:
            kind = "コンストラクタ"
        else:
            kind = "メソッド"
        parts.append(kind)
        if m.args:
            parts.append("**引数**")
            # Merge type info from signature and javadoc; signature wins.
            jdoc_types = {p[0]: p[1] for p in m.doc.params if p[1]}
            jdoc_descs = {p[0]: p[2] for p in m.doc.params}
            merged = []
            for arg_name, arg_default, arg_type in m.args:
                t = arg_type or jdoc_types.get(arg_name, "")
                d = jdoc_descs.get(arg_name, "")
                merged.append((arg_name, arg_default, t, d))
            has_type = any(t for _, _, t, _ in merged)
            headers = (["引数", "型", "既定値", "説明"] if has_type
                       else ["引数", "既定値", "説明"])
            rows = []
            for arg_name, arg_default, t, d in merged:
                default_md = f"`{arg_default}`" if arg_default else "`&nbsp;`"
                if has_type:
                    type_md = f"`{t}`" if t else "`&nbsp;`"
                    rows.append([f"`{arg_name}`", type_md, default_md, d])
                else:
                    rows.append([f"`{arg_name}`", default_md, d])
            parts.append(md_table(headers, rows))
        if m.doc.returns or m.doc.return_type:
            parts.append("**戻り値**")
            if m.doc.return_type:
                parts.append(f"型: `{m.doc.return_type}`")
            if m.doc.returns:
                parts.append(m.doc.returns)
    elif m.kind == "property":
        access = {"r": "r", "w": "w", "rw": "r/w"}[m.access]
        parts.append(f"プロパティ \\ アクセス: `{access}`")
        if m.doc.type_hint:
            parts.append(f"**型**: `{m.doc.type_hint}`")
    elif m.kind == "const":
        parts.append("定数")
        if m.value:
            parts.append(f"値: `{m.value}`")

    if m.doc.summary or m.doc.description:
        parts.append("**解説**")
        if m.doc.summary:
            parts.append(m.doc.summary)
        if m.doc.description:
            parts.append(m.doc.description)
    if m.doc.sees:
        links = []
        for ref in m.doc.sees:
            if "." in ref:
                cls_name, _, mem = ref.partition(".")
                links.append(f"[{ref}]({cls_name}.md#{slug(mem)})")
            else:
                links.append(f"[{ref}]({ref}.md)")
        parts.append("**関連:** " + " / ".join(links))
    return "\n\n".join(parts)


def _split_members(cls):
    short = cls.name.split(".")[-1]
    ctors = [m for m in cls.members if m.kind == "function" and m.name == short and m.doc.kind_hint != "event"]
    events = [m for m in cls.members if m.kind == "function" and m.doc.kind_hint == "event"]
    methods = [m for m in cls.members if m.kind == "function" and m.name != short and m.doc.kind_hint != "event"]
    props = [m for m in cls.members if m.kind == "property"]
    consts = [m for m in cls.members if m.kind == "const"]
    return ctors, props, methods, events, consts


def _render_index(ctors, props, methods, events, consts,
                  heading_level=2, item_heading_level=3):
    h = "#" * heading_level
    h2 = "#" * item_heading_level
    parts = [f"{h} メンバー一覧"]
    if ctors:
        parts.append(f"{h2} コンストラクタ")
        parts.append("\n".join(f"- [{m.name}](#{slug(m.name)})" for m in ctors))
    if props:
        parts.append(f"{h2} プロパティ")
        parts.append("\n".join(f"- [{m.name}](#{slug(m.name)})" for m in props))
    if methods:
        parts.append(f"{h2} メソッド")
        parts.append("\n".join(f"- [{m.name}](#{slug(m.name)})" for m in methods))
    if events:
        parts.append(f"{h2} イベント")
        parts.append("\n".join(f"- [{m.name}](#{slug(m.name)})" for m in events))
    if consts:
        parts.append(f"{h2} 定数")
        parts.append("\n".join(f"- [{m.name}](#{slug(m.name)})" for m in consts))
    return "\n\n".join(parts)


def render_primary(cls):
    parts = [f"# {cls.name}"]
    if cls.doc.summary:
        parts.append(cls.doc.summary)
    if cls.doc.description:
        parts.append(cls.doc.description)
    if cls.extends:
        parts.append(f"継承元: [{cls.extends}]({cls.extends}.md)")

    ctors, props, methods, events, consts = _split_members(cls)
    parts.append(_render_index(ctors, props, methods, events, consts))
    parts.append("---")

    for m in ctors + props + methods + events + consts:
        parts.append(render_member(m, cls))
        parts.append("---")
    return "\n\n".join(parts)


def render_extension(cls):
    label = cls.source or "拡張"
    parts = [f"## プラグイン拡張: {label}"]
    if cls.doc.summary:
        parts.append(cls.doc.summary)
    if cls.doc.description:
        parts.append(cls.doc.description)

    ctors, props, methods, events, consts = _split_members(cls)
    parts.append(_render_index(ctors, props, methods, events, consts,
                               heading_level=3, item_heading_level=4))
    parts.append("---")

    for m in ctors + props + methods + events + consts:
        parts.append(render_member(m, cls))
        parts.append("---")
    return "\n\n".join(parts)


def render_group(group):
    """Render a list of ClassDef sharing the same name into one Markdown file.

    - 1 source: render as primary.
    - 2+ sources, one with empty source (= core): core is primary, rest extensions.
    - 2+ sources, all plugins: synthesize a bare # heading, all are extensions.
    """
    if len(group) == 1:
        return render_primary(group[0]) + "\n"

    primary = next((c for c in group if not c.source), None)
    if primary is None:
        # No core — synthesize a stub primary
        name = group[0].name
        parts = [f"# {name}",
                 f"このクラスは複数のプラグインから拡張されています。"]
        for ext in group:
            parts.append(render_extension(ext))
        return "\n\n".join(parts) + "\n"

    others = [c for c in group if c is not primary]
    parts = [render_primary(primary)]
    for ext in others:
        parts.append(render_extension(ext))
    return "\n\n".join(parts) + "\n"


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def infer_source(p: Path) -> str:
    """Return plugin name for `src/plugins/<name>/manual.tjs`, '' otherwise."""
    parts = p.parts
    if "plugins" in parts:
        i = parts.index("plugins")
        if i + 1 < len(parts):
            return parts[i + 1]
    return ""


def iter_inputs(src: Path):
    if src.is_file():
        yield src, infer_source(src)
        return
    seen = set()
    for pattern in ("manual.tjs", "*.manual.tjs"):
        for p in sorted(src.rglob(pattern)):
            if p in seen:
                continue
            seen.add(p)
            yield p, infer_source(p)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--in", dest="src", action="append", required=True,
                    help="input manual.tjs file or directory (repeatable)")
    ap.add_argument("--out", dest="out", default=str(REPO / "doc" / "reference"),
                    help="output directory (default: doc/reference)")
    args = ap.parse_args(argv)

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    all_classes = []
    for src_arg in args.src:
        src = Path(src_arg)
        if not src.exists():
            print(f"error: {src} not found", file=sys.stderr)
            return 2
        for path, source in iter_inputs(src):
            text = path.read_text(encoding="utf-8", errors="replace")
            classes = parse_file(text)
            if not classes:
                print(f"warning: no class in {path}", file=sys.stderr)
                continue
            for cls in classes:
                cls.source = source
                all_classes.append(cls)

    # Group by class name and render
    groups = {}
    for cls in all_classes:
        groups.setdefault(cls.name, []).append(cls)

    for name, group in groups.items():
        target = out_dir / f"{name}.md"
        target.write_text(render_group(group), encoding="utf-8")
        sources = ", ".join(c.source or "(core)" for c in group)
        print(f"wrote {target} ({sum(len(c.members) for c in group)} members from {sources})")
    print(f"done: {len(groups)} class(es)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
