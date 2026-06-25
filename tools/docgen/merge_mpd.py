"""Merge multi_platform_design class definitions into doc/manual/.

multi_platform_design (MPD) provides updated TJS pseudo-code class
definitions including new classes (Canvas, Matrix32, ShaderProgram, ...)
and new members on existing classes.

For each MPD class file:
  - If a corresponding doc/manual/<Class>.manual.tjs does not exist,
    copy the MPD content as a new manual.tjs.
  - Otherwise, parse both, find members in MPD that are missing in our
    manual.tjs (or whose only doc is a `TODO:` stub) and insert/replace
    them with the full MPD definition. Members already documented in
    our manual.tjs are kept unchanged.

The MPD format uses `event NAME(args)` as sugar for events (the parser
now understands it natively). Inserted blocks preserve the original
spacing and indent (one tab) consistent with the rest of doc/manual/.

Usage:
  python tools/docgen/merge_mpd.py [--mpd PATH] [--out PATH] [--dry-run]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DEFAULT_MPD = REPO.parent / "multi_platform_design" / "classes"
DEFAULT_OUT = REPO / "doc" / "manual"

# TJS2 built-in classes are documented under doc/tjs2/ (prose), not as
# manual.tjs. Don't synthesize duplicate manual.tjs files for them.
TJS2_BUILTINS = {
    "Array", "Date", "Dictionary", "Exception", "Math", "Math.RandomGenerator",
    "Octet", "RegExp", "String",
}

# Reserved word filter — if MPD source has a typo like `property property X;`
# the parser would otherwise emit a bogus member named "property".
TJS_KEYWORDS = {"property", "function", "event", "var", "const", "class"}

# Markers used by MPD to indicate Android-only members. The user has confirmed
# Android isn't yet wired into the engine code, so skip those entirely.
ANDROID_MARKER_RE = re.compile(r"\[Android(?:\+|2\.\d+\+|)?\]", re.I)

sys.path.insert(0, str(Path(__file__).parent))
from tjsdoc import parse_file  # noqa: E402


# ---------------------------------------------------------------------------
# Block extractor: pull /** */ + decl text for each member out of a .tjs file
# ---------------------------------------------------------------------------

def _skip_string(text, pos):
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


def _find_block_end(text, open_pos):
    depth = 1
    pos = open_pos + 1
    n = len(text)
    while pos < n:
        c = text[pos]
        if c in ('"', "'"):
            pos = _skip_string(text, pos)
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


_DECL_RE = re.compile(
    r"\b(function|event|property)\s+(\w+)"
)


def extract_members(text: str) -> list[dict]:
    """Return list of {name, kind, raw, span} blocks (member level only).

    Each `raw` is the full text of the leading /** ... */ block (if any)
    plus the declaration line(s) up to and including the terminator (`;`
    or matching `}` of the body). `span` is `(start, end)` in absolute
    file offsets covering the same range — needed for in-place rewrites.
    """
    # Locate the outer `class X { ... }` body
    cm = re.search(r"class\s+[\w.]+(?:\s+extends\s+[\w.]+)?\s*\{", text)
    if not cm:
        return []
    body_start = cm.end() - 1  # at `{`
    body_end = _find_block_end(text, body_start)
    body = text[body_start + 1:body_end]
    base_offset = body_start + 1

    members: list[dict] = []
    pos = 0
    n = len(body)

    while pos < n:
        # Capture leading whitespace
        ws_start = pos
        while pos < n and body[pos] in " \t\r\n":
            pos += 1
        if pos >= n:
            break

        # Capture leading javadoc / line comments
        doc_start = pos
        while pos < n:
            if body[pos:pos+3] == "/**":
                e = body.find("*/", pos + 3)
                pos = e + 2 if e != -1 else n
                while pos < n and body[pos] in " \t\r\n":
                    pos += 1
                continue
            if body[pos:pos+2] == "/*":
                e = body.find("*/", pos + 2)
                pos = e + 2 if e != -1 else n
                while pos < n and body[pos] in " \t\r\n":
                    pos += 1
                continue
            if body[pos:pos+2] == "//":
                e = body.find("\n", pos)
                pos = (e + 1) if e != -1 else n
                continue
            break

        if pos >= n:
            break

        m = _DECL_RE.match(body, pos)
        if not m:
            # Skip unknown — advance one char and continue
            pos += 1
            continue

        kind_kw = m.group(1)
        name = m.group(2)

        if name in TJS_KEYWORDS:
            # Likely a typo in source ('property property X;'); skip
            pos = m.end()
            continue

        # Find end of declaration:
        end = m.end()
        # Skip past `(...)`
        if kind_kw in ("function", "event"):
            # find matching ')'
            while end < n and body[end] != "(":
                end += 1
            if end < n:
                depth = 1
                end += 1
                while end < n and depth > 0:
                    c = body[end]
                    if c in ('"', "'"):
                        end = _skip_string(body, end)
                        continue
                    if c == "(":
                        depth += 1
                    elif c == ")":
                        depth -= 1
                    end += 1
        # Optional `{ body }` after function/event (rare in MPD)
        while end < n and body[end] in " \t":
            end += 1
        if end < n and body[end] == "{":
            end = _find_block_end(body, end) + 1
        # property might have `{ getter; setter; }`
        if kind_kw == "property":
            while end < n and body[end] in " \t":
                end += 1
            if end < n and body[end] == "{":
                end = _find_block_end(body, end) + 1
        # Consume the rest of the declaration line: covers TJS-Z return-type
        # annotations like `function foo() : Array;`, plain `;`, and bare
        # decls with no terminator at all (stop at newline either way).
        while end < n and body[end] != "\n":
            if body[end] == ";":
                end += 1
                break
            end += 1
        # Trailing same-line comment after `;` is uncommon but possible
        while end < n and body[end] in " \t":
            end += 1
        if end < n - 1 and body[end:end+2] == "//":
            e = body.find("\n", end)
            end = e if e != -1 else n

        raw = body[doc_start:end].rstrip()
        # Skip Android-only members
        if ANDROID_MARKER_RE.search(raw):
            pos = end
            continue
        members.append({
            "name": name,
            "kind": "property" if kind_kw == "property" else "function",
            "is_event": kind_kw == "event",
            "raw": raw,
            "span": (base_offset + doc_start, base_offset + end),
        })
        pos = end
    return members


# ---------------------------------------------------------------------------
# Existing-doc inspection
# ---------------------------------------------------------------------------

def existing_member_state(manual_path: Path) -> dict[str, str]:
    """Return {name: 'real'|'todo'|'absent'} for existing manual members."""
    text = manual_path.read_text(encoding="utf-8")
    classes = parse_file(text)
    state = {}
    for cls in classes:
        for m in cls.members:
            summary = (m.doc.summary or "").strip()
            desc = (m.doc.description or "").strip()
            if summary.startswith("TODO") or desc.startswith("TODO"):
                state[m.name] = "todo"
            else:
                state[m.name] = "real"
    return state


def _normalize_block(new_block: str, indent: str = "\t") -> str:
    """Strip leading tabs from each non-empty line and re-prefix with `indent`.

    The first line of an extracted MPD block (`/**`) often arrives with zero
    leading whitespace while later lines carry one tab — taking the common
    minimum (0) and adding one tab would push javadoc body to two tabs. So
    we tab-normalize per line instead. Leading spaces are preserved, which
    matters for the single space in javadoc `\\t * text`.
    """
    out = []
    for ln in new_block.splitlines():
        if not ln.strip():
            out.append("")
            continue
        out.append(indent + ln.lstrip("\t"))
    return "\n".join(out)


def replace_member_block(text: str, name: str, new_block: str) -> str | None:
    """Replace `function/event/property NAME(...)` block (with its leading
    javadoc) in `text` with `new_block`. Returns updated text, or None if
    the member is not found.

    Uses `extract_members` to locate the exact span instead of a regex —
    a regex with `re.DOTALL` would over-match across the entire class body
    when the target is the last member, deleting unrelated content.
    """
    for m in extract_members(text):
        if m["name"] != name:
            continue
        start, end = m["span"]
        block = _normalize_block(new_block)
        # Slot the new block in at the same span — but the span begins
        # AFTER leading whitespace, while the normalized block starts with
        # a fresh `\t`. Strip its leading tab so we don't double-indent.
        if block.startswith("\t"):
            block = block[1:]
        return text[:start] + block + text[end:]
    return None


def append_member_block(text: str, new_block: str) -> str:
    """Insert new_block before the closing `}` of the class body."""
    block = _normalize_block(new_block)
    insert = "\n" + block + "\n"
    lines = text.splitlines(keepends=True)
    for i in range(len(lines) - 1, -1, -1):
        if lines[i].strip() == "}":
            return "".join(lines[:i]) + insert + "".join(lines[i:])
    return text + insert + "}\n"


# ---------------------------------------------------------------------------
# MPD source -> manual.tjs body builder (for new classes)
# ---------------------------------------------------------------------------

def _normalize_indent(text: str) -> str:
    """Reformat MPD source to use a single tab per nesting level. The MPD
    files mostly already use tab indent but there are stray spaces."""
    lines = []
    for ln in text.splitlines():
        # Tabify leading spaces in groups of 4 (best-effort)
        m = re.match(r"^([ \t]*)(.*)$", ln)
        if not m:
            lines.append(ln)
            continue
        ind, rest = m.group(1), m.group(2)
        # Already-tab indent: leave; otherwise convert pairs of 4 spaces -> tab
        ind = ind.replace("    ", "\t")
        lines.append(ind + rest)
    return "\n".join(lines)


def write_new_class(mpd_path: Path, dest_path: Path):
    """Copy a new MPD class file as our manual.tjs (lightly normalized)."""
    raw = mpd_path.read_text(encoding="utf-8", errors="replace")
    text = _normalize_indent(raw)
    if not text.endswith("\n"):
        text += "\n"
    dest_path.write_text(text, encoding="utf-8")


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--mpd", default=str(DEFAULT_MPD),
                    help="path to multi_platform_design/classes")
    ap.add_argument("--out", default=str(DEFAULT_OUT),
                    help="path to doc/manual")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)

    mpd = Path(args.mpd)
    out = Path(args.out)

    if not mpd.exists():
        print(f"error: MPD source not found: {mpd}", file=sys.stderr)
        return 2

    new_classes = []
    inserted = 0
    replaced = 0

    for tjs in sorted(mpd.glob("*.tjs")):
        if tjs.name == "const.tjs":
            continue  # handled separately if at all
        cls_name = tjs.stem
        if cls_name in TJS2_BUILTINS:
            continue  # documented under doc/tjs2/ instead
        dest = out / f"{cls_name}.manual.tjs"

        if not dest.exists():
            new_classes.append(cls_name)
            print(f"\n## {cls_name}: NEW class")
            if not args.dry_run:
                write_new_class(tjs, dest)
            continue

        # Existing class: merge member-level
        mpd_text = tjs.read_text(encoding="utf-8", errors="replace")
        members = extract_members(mpd_text)
        if not members:
            continue

        state = existing_member_state(dest)
        cur_text = dest.read_text(encoding="utf-8")

        local_inserted = []
        local_replaced = []
        for m in members:
            name = m["name"]
            block = m["raw"]
            if name not in state:
                cur_text = append_member_block(cur_text, block)
                local_inserted.append(name)
                continue
            if state[name] == "todo":
                upd = replace_member_block(cur_text, name, block)
                if upd is not None:
                    cur_text = upd
                    local_replaced.append(name)
                else:
                    cur_text = append_member_block(cur_text, block)
                    local_inserted.append(name)

        if local_inserted or local_replaced:
            print(f"\n## {cls_name}.manual.tjs:"
                  f" +{len(local_inserted)} new,"
                  f" {len(local_replaced)} replaced")
            for n in local_replaced:
                print(f"  replace TODO  {n}")
            for n in local_inserted:
                print(f"  insert        {n}")
            inserted += len(local_inserted)
            replaced += len(local_replaced)
            if not args.dry_run:
                dest.write_text(cur_text, encoding="utf-8")

    print(f"\n=== summary ===")
    print(f"  new classes:   {len(new_classes)} ({', '.join(new_classes)})")
    print(f"  members added: {inserted}")
    print(f"  TODOs filled:  {replaced}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
