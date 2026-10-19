"""公開ドキュメントの翻訳の鮮度チェック。方針は TODO-i18n.md の C。

手書きページ: doc/**/Foo.md の訳は隣の Foo.<lang>.md。訳の front-matter に
訳した時点の日本語原文のハッシュを持たせる:

    ---
    source_hash: 0123456789ab
    ---

原文のハッシュと違えば「要再訳」。訳が無ければ「未訳」(サイトでは日本語版が出る)。

reference (tjsdoc.py の生成物): 翻訳カタログ doc/i18n/<lang>/reference/*.json の
訳済み / 要再訳 (stale) を数える (refi18n.py)。

Usage:
  python tools/docgen/check_translations.py en              # 集計 + 要再訳の一覧
  python tools/docgen/check_translations.py en --missing    # 未訳ページも一覧
  python tools/docgen/check_translations.py en --stamp doc/guide/Startup.en.md
      # 訳し終えた (訳し直した) ページの source_hash を今の原文に合わせる

CI ではレポートのみ (常に終了コード 0)。言語は引数で受け、特定の言語を直書きしない。
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
DOC = REPO / "doc"
sys.path.insert(0, str(HERE))
import refi18n  # noqa: E402

FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)


def source_hash(path: Path) -> str:
    text = path.read_bytes().decode("utf-8").replace("\r\n", "\n")
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:12]


def read_fm_hash(path: Path):
    text = path.read_bytes().decode("utf-8").replace("\r\n", "\n")
    m = FM_RE.match(text)
    if not m:
        return None
    for ln in m.group(1).split("\n"):
        if ln.startswith("source_hash:"):
            return ln.split(":", 1)[1].strip()
    return None


def is_lang_file(p: Path):
    # Foo.en.md のような「名前.言語.md」は訳 (原文ではない)
    return len(p.suffixes) >= 2 and re.fullmatch(r"\.[a-z]{2,3}(-[A-Za-z]+)?", p.suffixes[-2])


def source_pages():
    for p in sorted(DOC.rglob("*.md")):
        rel = p.relative_to(DOC).as_posix()
        if rel.startswith("i18n/") or rel.startswith("_"):
            continue
        if is_lang_file(p):
            continue
        # reference は生成物 (カタログで管理)。手作りの索引ページだけ対象
        if rel.startswith("reference/") and p.name != "index.md":
            continue
        yield p


def stamp(path: Path, lang: str):
    path = path.resolve()
    src = path.with_name(path.name.replace(f".{lang}.md", ".md"))
    if src == path or not src.exists():
        print(f"error: 原文が見つかりません: {src}", file=sys.stderr)
        return 1
    h = source_hash(src)
    text = path.read_bytes().decode("utf-8").replace("\r\n", "\n")
    m = FM_RE.match(text)
    if m:
        lines = [ln for ln in m.group(1).split("\n") if not ln.startswith("source_hash:")]
        lines.append(f"source_hash: {h}")
        text = "---\n" + "\n".join(lines) + "\n---\n" + text[m.end():]
    else:
        text = f"---\nsource_hash: {h}\n---\n\n" + text
    path.write_bytes(text.encode("utf-8"))
    print(f"stamped {path.relative_to(REPO).as_posix()} ({h})")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("lang")
    ap.add_argument("--missing", action="store_true", help="未訳ページも一覧する")
    ap.add_argument("--stamp", nargs="+", metavar="FILE", help="訳ページの source_hash を更新する")
    args = ap.parse_args(argv)
    lang = args.lang
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    if args.stamp:
        rc = 0
        for f in args.stamp:
            rc |= stamp(Path(f), lang)
        return rc

    ok, stale, nohash, missing = [], [], [], []
    for src in source_pages():
        tr = src.with_name(src.stem + f".{lang}.md")
        rel = src.relative_to(DOC).as_posix()
        if not tr.exists():
            missing.append(rel)
            continue
        h = read_fm_hash(tr)
        if h is None:
            nohash.append(rel)
        elif h != source_hash(src):
            stale.append(rel)
        else:
            ok.append(rel)
    total = len(ok) + len(stale) + len(nohash) + len(missing)
    print(f"[{lang}] 手書きページ: {total} 件中 訳済み {len(ok)} / 要再訳 {len(stale)} / "
          f"ハッシュ無し {len(nohash)} / 未訳 {len(missing)}")
    for r in stale:
        print(f"  要再訳: {r}")
    for r in nohash:
        print(f"  ハッシュ無し (--stamp で付ける): {r}")
    if args.missing:
        for r in missing:
            print(f"  未訳: {r}")

    st = refi18n.stats(lang, DOC / "i18n")
    n = sum(v[0] for v in st.values())
    t = sum(v[1] for v in st.values())
    s = sum(v[2] for v in st.values())
    done = [c for c, v in st.items() if v[1] == v[0]]
    print(f"[{lang}] reference: {len(st)} クラス / {n} 項目中 訳済み {t} / 要再訳 {s} "
          f"(全項目訳済みのクラス {len(done)})")
    for c, v in st.items():
        if v[2]:
            print(f"  要再訳: {c} ({v[2]} 項目)")
    if args.missing:
        for c, v in st.items():
            if v[1] < v[0]:
                print(f"  未訳あり: {c} ({v[0] - v[1]}/{v[0]})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
