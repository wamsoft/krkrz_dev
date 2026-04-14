"""Compare src/core TJS inventory to the Markdown reference docs.

Reads:
  doc/_inventory.json        (from scan_tjs.py)
  doc/reference/<Class>.md   (from xml2md.py, or hand-authored)

Emits:
  doc/_missing.md            human-readable report of:
    - classes in code but with no Markdown file
    - members present in code but not documented
    - members present in docs but not found in code (possibly renamed /
      removed; requires manual review)

The report is intended to drive additions to the hand-authored .md files.
After adding a new member to a class .md, re-run this tool to shrink the
report. When empty, the wiki is in sync with src/core.

Usage: python tools/docgen/diff_docs.py
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DEFAULT_INV = REPO / "doc" / "_inventory.json"
DEFAULT_REF = REPO / "doc" / "reference"
DEFAULT_OUT = REPO / "doc" / "_missing.md"

# heading lines like "### name"
HEADING_RE = re.compile(r"^###\s+([A-Za-z_][\w\.]*)\s*$", re.M)

def members_in_md(md_path: Path) -> set[str]:
    if not md_path.exists():
        return set()
    text = md_path.read_text(encoding="utf-8", errors="ignore")
    return set(HEADING_RE.findall(text))

def resolve_md_path(ref_dir: Path, cls: str) -> Path:
    """Some classes may be documented under a compound filename like
    Window.BasicDrawDevice.md. Try the exact class name first, then fall
    back to a file whose stem ends in .<cls>."""
    exact = ref_dir / f"{cls}.md"
    if exact.exists():
        return exact
    for cand in ref_dir.glob(f"*.{cls}.md"):
        return cand
    return exact  # non-existent, used to signal "missing class file"

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--inventory", default=str(DEFAULT_INV))
    ap.add_argument("--ref", default=str(DEFAULT_REF))
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    args = ap.parse_args()

    inv = json.loads(Path(args.inventory).read_text(encoding="utf-8"))
    ref_dir = Path(args.ref)

    lines: list[str] = [
        "# ドキュメント差分レポート",
        "",
        "`tools/docgen/scan_tjs.py` が `src/core` から抽出したメンバー一覧と、",
        "`doc/reference/*.md` の見出しを突き合わせた結果です。",
        "",
        "- **未記載メンバー**: C++ 側には存在するが Markdown リファレンスに見出しが無いもの。",
        "  対応する `.md` に `### <name>` 節を追加してください。",
        "- **コードに無いメンバー**: 旧 XML には存在したがバインドからは消えているもの。",
        "  リネーム/廃止を確認し、不要なら `.md` から節を削除してください。",
        "",
        "更新手順:",
        "",
        "1. `.venv/Scripts/python.exe tools/docgen/scan_tjs.py`",
        "2. `.venv/Scripts/python.exe tools/docgen/diff_docs.py`",
        "3. `doc/_missing.md` を見ながら `doc/reference/<Class>.md` を手編集",
        "4. 再度 `diff_docs.py` を走らせ、レポートが空になるまで繰り返す",
        "5. コミットすると GitHub Actions が Wiki に反映",
        "",
    ]

    missing_classes: list[str] = []
    total_missing_members = 0
    total_stale_members = 0

    for cls in sorted(inv.keys()):
        info = inv[cls]
        md_path = resolve_md_path(ref_dir, cls)
        documented = members_in_md(md_path)
        code_members: set[str] = set()
        for k in ("methods", "properties", "events"):
            code_members.update(info.get(k, []))

        if not md_path.exists():
            missing_classes.append(cls)
            continue

        missing = sorted(code_members - documented)
        # Exclude the class-name heading itself (constructors are documented
        # as `### <ClassName>` but scan_tjs cannot see them — they are
        # registered via factory functions, not TJS_BEGIN_NATIVE_METHOD_DECL).
        stale = sorted(documented - code_members - {cls})
        if not missing and not stale:
            continue

        lines.append(f"## {cls}")
        lines.append("")
        lines.append(f"- file: `{md_path.relative_to(REPO).as_posix()}`")
        lines.append(f"- code: `{info.get('file')}`")
        lines.append("")

        if missing:
            lines.append("### 未記載メンバー")
            for name in missing:
                kind = _kind_of(info, name)
                lines.append(f"- [ ] `{name}` ({kind})")
            lines.append("")
            total_missing_members += len(missing)

        if stale:
            lines.append("### コードに存在しないメンバー（要確認）")
            for name in stale:
                lines.append(f"- [ ] `{name}`")
            lines.append("")
            total_stale_members += len(stale)

    if missing_classes:
        lines.append("## ドキュメント未作成クラス")
        lines.append("")
        for cls in missing_classes:
            lines.append(f"- [ ] `{cls}` — `doc/reference/{cls}.md` を新規作成")
        lines.append("")

    summary = [
        "## サマリー",
        "",
        f"- クラス未作成: {len(missing_classes)}",
        f"- 未記載メンバー合計: {total_missing_members}",
        f"- コードに無いメンバー合計: {total_stale_members}",
        "",
    ]
    # Insert summary right after the header preamble (after line containing "更新手順" block)
    insert_at = next((i for i, ln in enumerate(lines) if ln == ""), 1)
    # put summary just before first "## ClassName"
    first_section = next((i for i, ln in enumerate(lines) if ln.startswith("## ")), len(lines))
    lines = lines[:first_section] + summary + lines[first_section:]

    Path(args.out).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[diff_docs] {len(missing_classes)} missing class files, "
          f"{total_missing_members} missing members, "
          f"{total_stale_members} stale members -> {args.out}")
    return 0

def _kind_of(info: dict, name: str) -> str:
    if name in info.get("methods", []):
        return "method"
    if name in info.get("properties", []):
        return "property"
    if name in info.get("events", []):
        return "event"
    return "?"

if __name__ == "__main__":
    raise SystemExit(main())
