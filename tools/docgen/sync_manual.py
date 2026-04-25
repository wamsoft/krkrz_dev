"""Insert TODO stubs for members present in C++ but not in manual.tjs.

Reads:
  doc/_inventory.json             (from scan_tjs.py)
  doc/manual/<Class>.manual.tjs   (parsed via tjsdoc)

For each class with missing members, appends a stub block before the closing
`}` of the class body in `<Class>.manual.tjs`. Each stub carries a TODO
placeholder description so the human author can fill it in.

Member kinds:
  - method   -> `function name();`
  - property -> `property name;` (bare = r/w default)
  - event    -> `function name();` with `@kind event`

Re-running the tool is idempotent: members already declared (in any form) are
skipped, so it's safe to run after each scan_tjs / diff_docs cycle.

Usage:
  python tools/docgen/sync_manual.py [--dry-run] [--class NAME ...]
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DEFAULT_INV = REPO / "doc" / "_inventory.json"
DEFAULT_MANUAL = REPO / "doc" / "manual"

sys.path.insert(0, str(Path(__file__).parent))
from tjsdoc import parse_file  # noqa: E402


STUB_PROPERTY = '''\
\t/**
\t * TODO: {name} の説明
\t */
\tproperty {name};
'''

STUB_METHOD = '''\
\t/**
\t * TODO: {name} の説明
\t */
\tfunction {name}();
'''

STUB_EVENT = '''\
\t/**
\t * TODO: {name} の説明
\t * @kind event
\t */
\tfunction {name}();
'''


def existing_members(manual_path: Path):
    text = manual_path.read_text(encoding="utf-8", errors="replace")
    classes = parse_file(text)
    if not classes:
        return text, set()
    declared = set()
    for cls in classes:
        for m in cls.members:
            declared.add(m.name)
    return text, declared


def resolve_manual(manual_dir: Path, cls: str) -> Path:
    exact = manual_dir / f"{cls}.manual.tjs"
    if exact.exists():
        return exact
    for cand in manual_dir.glob(f"*.{cls}.manual.tjs"):
        return cand
    return exact


def insert_stubs(text: str, stubs: list) -> str:
    """Insert stubs immediately before the LAST `}` line of the file."""
    if not stubs:
        return text
    block = "\n" + "\n".join(stubs)
    lines = text.splitlines(keepends=True)
    # Find last line whose stripped content is exactly "}"
    last_close = None
    for i in range(len(lines) - 1, -1, -1):
        if lines[i].strip() == "}":
            last_close = i
            break
    if last_close is None:
        # Fallback: append at end
        return text + block + "\n}\n"
    head = "".join(lines[:last_close])
    tail = "".join(lines[last_close:])
    return head + block + tail


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--inventory", default=str(DEFAULT_INV))
    ap.add_argument("--manual", default=str(DEFAULT_MANUAL))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--class", dest="filter_classes", action="append",
                    help="Process only the given class (repeatable)")
    args = ap.parse_args()

    inv = json.loads(Path(args.inventory).read_text(encoding="utf-8"))
    manual_dir = Path(args.manual)

    total_stubs = 0
    classes_touched = 0

    for cls in sorted(inv.keys()):
        if args.filter_classes and cls not in args.filter_classes:
            continue
        info = inv[cls]
        manual_path = resolve_manual(manual_dir, cls)
        if not manual_path.exists():
            print(f"skip {cls}: no manual.tjs", file=sys.stderr)
            continue

        text, declared = existing_members(manual_path)

        stubs = []
        for name in sorted(info.get("properties", [])):
            if name in declared:
                continue
            stubs.append(STUB_PROPERTY.format(name=name))
        for name in sorted(info.get("methods", [])):
            if name in declared:
                continue
            stubs.append(STUB_METHOD.format(name=name))
        for name in sorted(info.get("events", [])):
            if name in declared:
                continue
            stubs.append(STUB_EVENT.format(name=name))

        if not stubs:
            continue

        new_text = insert_stubs(text, stubs)

        rel = manual_path.relative_to(REPO).as_posix()
        added = [s.strip().splitlines()[-1] for s in stubs]
        print(f"\n## {rel}: +{len(stubs)} stubs")
        for ln in added:
            print(f"  {ln}")
        total_stubs += len(stubs)
        classes_touched += 1
        if not args.dry_run:
            manual_path.write_text(new_text, encoding="utf-8")

    verb = "would insert" if args.dry_run else "inserted"
    print(f"\n{verb} {total_stubs} stub(s) in {classes_touched} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
