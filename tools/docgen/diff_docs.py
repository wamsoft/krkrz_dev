"""Compare src/core TJS inventory to the manual.tjs source-of-truth.

Reads:
  doc/_inventory.json             (from scan_tjs.py)
  doc/manual/<Class>.manual.tjs   (the SSOT, from xml2manual.py / hand-edits)

Emits:
  doc/_missing.md                 human-readable report of:
    - classes in code but with no manual.tjs file
    - members present in code but not declared in manual.tjs
    - members declared in manual.tjs but not found in code (renamed/removed;
      requires manual review)

After updating the corresponding `manual.tjs`, re-run this tool to shrink
the report. When empty, the docs source matches src/core.

Usage: python tools/docgen/diff_docs.py
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DEFAULT_INV = REPO / "doc" / "_inventory.json"
DEFAULT_MANUAL = REPO / "doc" / "manual"
DEFAULT_OUT = REPO / "doc" / "_missing.md"

# Reuse the tjsdoc.py parser
sys.path.insert(0, str(Path(__file__).parent))
from tjsdoc import parse_file  # noqa: E402


def members_in_manual(manual_path: Path):
    """Parse a manual.tjs and return (props_set, methods_set, events_set, ctors_count)."""
    if not manual_path.exists():
        return set(), set(), set(), 0
    text = manual_path.read_text(encoding="utf-8", errors="replace")
    classes = parse_file(text)
    props, methods, events = set(), set(), set()
    ctors = 0
    for cls in classes:
        short = cls.name.split(".")[-1]
        for m in cls.members:
            if m.kind == "function":
                if m.doc.kind_hint == "event":
                    events.add(m.name)
                elif m.name == short:
                    ctors += 1
                else:
                    methods.add(m.name)
            elif m.kind == "property":
                props.add(m.name)
    return props, methods, events, ctors


def resolve_manual(manual_dir: Path, cls: str) -> Path:
    """Find manual.tjs for a class. Try <Class>.manual.tjs first, then any
    file ending in .<Class>.manual.tjs (e.g., for compound dotted names)."""
    exact = manual_dir / f"{cls}.manual.tjs"
    if exact.exists():
        return exact
    for cand in manual_dir.glob(f"*.{cls}.manual.tjs"):
        return cand
    return exact  # non-existent => "missing class manual"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--inventory", default=str(DEFAULT_INV))
    ap.add_argument("--manual", default=str(DEFAULT_MANUAL))
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    args = ap.parse_args()

    inv = json.loads(Path(args.inventory).read_text(encoding="utf-8"))
    manual_dir = Path(args.manual)

    lines = [
        "# ドキュメント差分レポート",
        "",
        "`tools/docgen/scan_tjs.py` が `src/core` から抽出したメンバー一覧と、",
        "`doc/manual/*.manual.tjs` （SSOT）の宣言を突き合わせた結果です。",
        "",
        "- **未記載メンバー**: C++ 側には存在するが manual.tjs に宣言が無いもの。",
        "  対応する `manual.tjs` に `function`/`property` 宣言を追加してください。",
        "- **コードに無いメンバー**: manual.tjs にはあるが C++ バインドには存在しないもの。",
        "  リネーム/廃止を確認し、不要なら `manual.tjs` から削除してください。",
        "",
        "更新手順:",
        "",
        "1. `python tools/docgen/scan_tjs.py`",
        "2. `python tools/docgen/diff_docs.py`",
        "3. `doc/_missing.md` を見ながら `doc/manual/<Class>.manual.tjs` を編集",
        "4. `python tools/docgen/tjsdoc.py --in doc/manual --in src/plugins` で md 再生成",
        "5. 再度 `diff_docs.py` を走らせ、レポートが空になるまで繰り返す",
        "",
    ]

    missing_classes = []
    total_missing_members = 0
    total_stale_members = 0
    sections = []

    for cls in sorted(inv.keys()):
        info = inv[cls]
        manual_path = resolve_manual(manual_dir, cls)
        if not manual_path.exists():
            missing_classes.append(cls)
            continue

        m_props, m_methods, m_events, _ctors = members_in_manual(manual_path)
        documented = m_props | m_methods | m_events

        code_props = set(info.get("properties", []))
        code_methods = set(info.get("methods", []))
        code_events = set(info.get("events", []))
        code_members = code_props | code_methods | code_events

        missing = sorted(code_members - documented)
        # The class-name heading is documented as a constructor in manual.tjs
        # (function ClassName(...)); scan_tjs.py doesn't see those. Exclude.
        stale = sorted(documented - code_members - {cls})
        if not missing and not stale:
            continue

        sec = [f"## {cls}", "",
               f"- manual: `{manual_path.relative_to(REPO).as_posix()}`",
               f"- code: `{info.get('file')}`",
               ""]
        if missing:
            sec.append("### 未記載メンバー")
            for name in missing:
                kind = ("property" if name in code_props
                        else "event" if name in code_events
                        else "method")
                sec.append(f"- [ ] `{name}` ({kind})")
            sec.append("")
            total_missing_members += len(missing)
        if stale:
            sec.append("### コードに存在しないメンバー（要確認）")
            for name in stale:
                sec.append(f"- [ ] `{name}`")
            sec.append("")
            total_stale_members += len(stale)
        sections.append(sec)

    summary = [
        "## サマリー",
        "",
        f"- クラス未作成: {len(missing_classes)}",
        f"- 未記載メンバー合計: {total_missing_members}",
        f"- コードに無いメンバー合計: {total_stale_members}",
        "",
    ]

    out_lines = lines + summary
    for sec in sections:
        out_lines.extend(sec)
    if missing_classes:
        out_lines.append("## manual.tjs 未作成クラス")
        out_lines.append("")
        for cls in missing_classes:
            out_lines.append(f"- [ ] `{cls}` — `doc/manual/{cls}.manual.tjs` を新規作成")
        out_lines.append("")

    Path(args.out).write_text("\n".join(out_lines) + "\n", encoding="utf-8")
    print(f"[diff_docs] {len(missing_classes)} missing class manuals, "
          f"{total_missing_members} missing members, "
          f"{total_stale_members} stale members -> {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
