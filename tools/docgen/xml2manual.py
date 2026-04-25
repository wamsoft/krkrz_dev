"""Convert legacy kirikiriz XML class references to manual.tjs format.

Input:  document/kirikiriz/j_in/classes/f_*.xml
Output: doc/manual/<Class>.manual.tjs

Each class becomes one .manual.tjs file containing the class definition
with javadoc-annotated members. This is the new SSOT for core class docs;
markdown is regenerated from these via tjsdoc.py.

Usage:
  python tools/docgen/xml2manual.py [--src PATH] [--out PATH]
"""

from __future__ import annotations

import argparse
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DEFAULT_SRC = REPO / "document" / "kirikiriz" / "j_in" / "classes"
DEFAULT_OUT = REPO / "doc" / "manual"

_IDEO_WS = "　"


def _text(x): return x or ""


# Class-name registry (built from filenames in --src) for <ref> resolution
_CLASSES: set = set()


def _slug(name: str) -> str:
    s = name.strip().lower()
    s = re.sub(r"[^\w\- ]+", "", s, flags=re.UNICODE)
    return s.replace(" ", "-")


def resolve_ref(text: str) -> str:
    """`<ref>Layer.visible</ref>` -> `[Layer.visible](Layer.md#visible)` etc."""
    raw = text.strip()
    if not raw:
        return ""
    # exact class name
    if raw in _CLASSES:
        return f"[{raw}]({raw}.md)"
    # longest matching dotted prefix (handles 'Window.BasicDrawDevice.foo')
    best = None
    for cls in _CLASSES:
        if raw.startswith(cls + "."):
            if best is None or len(cls) > len(best):
                best = cls
    if best:
        member = raw[len(best) + 1:]
        return f"[{raw}]({best}.md#{_slug(member)})"
    return raw  # unresolved -> plain text


# ---------------------------------------------------------------------------
# Inline rendering
# ---------------------------------------------------------------------------

def render_inline(e: ET.Element) -> str:
    if e is None:
        return ""
    parts = [_text(e.text)]
    for ch in e:
        parts.append(render_tag(ch))
        parts.append(_text(ch.tail))
    return "".join(parts)


def render_tag(e: ET.Element) -> str:
    tag = e.tag
    inner = render_inline(e)
    if tag == "r":
        return "\n"
    if tag in ("kw", "b"):
        return f"**{inner}**" if inner else ""
    if tag == "tt":
        return f"`{inner}`" if inner else ""
    if tag == "i":
        return f"*{inner}*" if inner else ""
    if tag == "ref":
        return resolve_ref(inner)
    if tag == "link":
        href = e.get("href", "")
        return f"[{inner}]({href})" if href else inner
    if tag == "img":
        src = e.get("src", "")
        alt = e.get("alt", "")
        src = re.sub(r"^(?:\./)?imgsrc/", "../_assets/", src)
        if not src.startswith(("http", "../", "/", "_assets/")):
            src = "../_assets/" + src
        return f"![{alt}]({src})"
    if tag == "li":
        return "- " + inner
    return inner  # ul/ol/dl/dt/dd/nobr/wave/etc -> pass-through


def clean_text(s: str) -> str:
    """Strip ideographic/leading indent per line; collapse blank runs."""
    if not s:
        return ""
    lines = []
    for ln in s.splitlines():
        lines.append(ln.rstrip().lstrip(" \t" + _IDEO_WS))
    out = "\n".join(lines).strip("\n")
    out = re.sub(r"\n{3,}", "\n\n", out)
    # Inside javadoc, '*/' would close the block; defensively escape.
    out = out.replace("*/", "*\\/")
    return out


# ---------------------------------------------------------------------------
# Member emission
# ---------------------------------------------------------------------------

def render_javadoc(short: str, desc: str,
                   params: list, returns: str,
                   kind: str = "",
                   sees: list = (),
                   indent: str = "\t") -> str:
    lines: list[str] = []
    if short:
        lines.append(short.strip())
    if desc:
        if lines:
            lines.append("")
        lines.extend(desc.split("\n"))
    for name, pdesc in params:
        first, *rest = (pdesc or "").split("\n")
        head = f"@param {name} {first}".rstrip()
        lines.append(head)
        for cont in rest:
            lines.append(cont)
    if returns:
        first, *rest = returns.split("\n")
        lines.append(f"@return {first}".rstrip())
        for cont in rest:
            lines.append(cont)
    if kind:
        lines.append(f"@kind {kind}")
    for s in sees:
        lines.append(f"@see {s}")
    if not lines:
        return ""
    body = "\n".join(
        (f"{indent} * {ln}".rstrip() if ln else f"{indent} *")
        for ln in lines
    )
    return f"{indent}/**\n{body}\n{indent} */"


def render_member(m: ET.Element, class_name: str, indent: str = "\t") -> str:
    name_el = m.find("name")
    type_el = m.find("type")
    if name_el is None or type_el is None:
        return ""
    name = (name_el.text or "").strip()
    typ = (type_el.text or "").strip()
    short = clean_text(render_inline(m.find("shortdesc"))) if m.find("shortdesc") is not None else ""
    desc = clean_text(render_inline(m.find("desc"))) if m.find("desc") is not None else ""
    returns = clean_text(render_inline(m.find("result"))) if m.find("result") is not None else ""
    access_el = m.find("access")
    access = (access_el.text or "").strip() if access_el is not None and access_el.text else ""
    arg_el = m.find("arg")

    params: list = []
    arg_decls: list = []
    if arg_el is not None:
        for ai in arg_el.findall("argitem"):
            an = (ai.findtext("name") or "").strip()
            ad = (ai.findtext("default") or "").strip()
            adesc = clean_text(render_inline(ai.find("desc"))) if ai.find("desc") is not None else ""
            params.append((an, adesc))
            arg_decls.append(f"{an} = {ad}" if ad else an)
    args_str = ", ".join(arg_decls)

    kind_hint = "event" if typ == "event" else ""
    sees = [
        (r.text or "").strip()
        for r in m.findall("ref")
        if r.text and (r.text or "").strip()
    ]
    parts = []
    javadoc = render_javadoc(short, desc, params, returns,
                             kind=kind_hint, sees=sees, indent=indent)
    if javadoc:
        parts.append(javadoc)

    if typ == "constructor":
        # Use last component of dotted class name (e.g., Foo.Bar -> Bar)
        ctor_name = class_name.split(".")[-1]
        parts.append(f"{indent}function {ctor_name}({args_str});")
    elif typ in ("method", "event"):
        parts.append(f"{indent}function {name}({args_str});")
    elif typ == "property":
        if access == "r":
            parts.append(f"{indent}property {name} {{ getter; }}")
        else:
            # bare = rw per convention
            parts.append(f"{indent}property {name};")
    else:
        # unknown type — fallback to method-style
        parts.append(f"{indent}function {name}({args_str});")
    return "\n".join(parts)


def render_class(root: ET.Element, class_name: str) -> str:
    desc_el = root.find("desc")
    class_desc = clean_text(render_inline(desc_el)) if desc_el is not None else ""

    out: list = []
    if class_desc:
        body = "\n".join(
            (f" * {ln}".rstrip() if ln else " *")
            for ln in class_desc.split("\n")
        )
        out.append(f"/**\n{body}\n */")
    out.append(f"class {class_name} {{")
    for m in root.findall("member"):
        rendered = render_member(m, class_name)
        if rendered:
            out.append(rendered)
            out.append("")  # blank line between members
    # drop trailing blank
    while out and out[-1] == "":
        out.pop()
    out.append("}")
    return "\n".join(out) + "\n"


def class_name_from_filename(p: Path) -> str:
    name = p.name
    for suf in (".xml.in", ".xml"):
        if name.endswith(suf):
            name = name[: -len(suf)]
            break
    if name.startswith("f_"):
        name = name[2:]
    return name


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--src", default=str(DEFAULT_SRC),
                    help="directory containing f_*.xml class files")
    ap.add_argument("--out", default=str(DEFAULT_OUT),
                    help="output directory for *.manual.tjs files")
    args = ap.parse_args(argv)

    src = Path(args.src)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    inputs = sorted(list(src.glob("f_*.xml")) + list(src.glob("f_*.xml.in")))
    if not inputs:
        print(f"error: no f_*.xml under {src}", file=sys.stderr)
        return 2

    # Build class-name registry for <ref> resolution
    _CLASSES.update(class_name_from_filename(p) for p in inputs)

    for path in inputs:
        cls = class_name_from_filename(path)
        try:
            root = ET.parse(path).getroot()
        except ET.ParseError as e:
            print(f"warning: parse error in {path}: {e}", file=sys.stderr)
            continue
        text = render_class(root, cls)
        target = out / f"{cls}.manual.tjs"
        target.write_text(text, encoding="utf-8")
        print(f"wrote {target}")

    print(f"done: {len(inputs)} class(es)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
