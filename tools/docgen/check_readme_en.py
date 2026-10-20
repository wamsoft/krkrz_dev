#!/usr/bin/env python3
"""README_en.md (英語版 README) の鮮度チェック

krkrz_dev と外枠リポジトリ (krkrz_android / krkrz_ios / krkrz_linux / krkrz_gdk / krkrz_web)、
標準ツール (src/tools/krkrz_tools)、エンジン (src/core) の README_en.md は、先頭行に

    <!-- source_hash: 0123456789ab -->

を持つ。値は同じフォルダの README.md (日本語版) から計算したハッシュで、公開サイトの
check_translations.py と同じ計算 (改行を LF にそろえた UTF-8 の SHA-1 の先頭 12 桁)。
日本語版を書き換えると値が合わなくなり、英語版を見直す必要があると分かる。

    python tools/docgen/check_readme_en.py                 # 既定の場所を一覧
    python tools/docgen/check_readme_en.py <repo>...       # 指定したリポジトリ (フォルダ) だけ
    python tools/docgen/check_readme_en.py --stamp <repo>  # 訳し終えた英語版の値を今の日本語版に合わせる

既定の場所は krkrz_dev 自身と、その中の src/core / src/tools/krkrz_tools、および krkrz_dev の
隣 (KRKRZ_BASE) に clone した外枠リポジトリ。無いものは飛ばす。
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WRAPPERS = ["krkrz_android", "krkrz_ios", "krkrz_linux", "krkrz_gdk", "krkrz_web"]
HASH_RE = re.compile(r"\A<!-- source_hash: ([0-9a-f]{12}|[^>]*?) -->\r?\n")


def source_hash(path: Path) -> str:
    text = path.read_bytes().decode("utf-8").replace("\r\n", "\n")
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:12]


def default_repos() -> list[Path]:
    repos = [REPO, REPO / "src" / "core", REPO / "src" / "tools" / "krkrz_tools"]
    repos += [REPO.parent / w for w in WRAPPERS]
    return [r for r in repos if (r / "README.md").is_file()]


def read_stamp(en: Path):
    m = HASH_RE.match(en.read_bytes().decode("utf-8"))
    return m.group(1) if m else None


def stamp(repo: Path) -> None:
    ja, en = repo / "README.md", repo / "README_en.md"
    if not en.is_file():
        raise SystemExit(f"{en} がありません")
    raw = en.read_bytes().decode("utf-8")
    nl = "\r\n" if "\r\n" in raw else "\n"
    body = HASH_RE.sub("", raw, count=1)
    line = f"<!-- source_hash: {source_hash(ja)} -->{nl}"
    en.write_bytes((line + body).encode("utf-8"))
    print(f"stamped {en} ({source_hash(ja)})")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("repos", nargs="*", type=Path, help="README.md のあるフォルダ (省略時は既定の場所)")
    ap.add_argument("--stamp", action="store_true", help="指定したフォルダの README_en.md の source_hash を更新する")
    a = ap.parse_args(argv)

    if a.stamp:
        if not a.repos:
            ap.error("--stamp にはフォルダを指定してください")
        for r in a.repos:
            stamp(r)
        return 0

    repos = a.repos or default_repos()
    bad = 0
    for r in repos:
        ja, en = r / "README.md", r / "README_en.md"
        name = r.resolve().name
        if not ja.is_file():
            print(f"  ?? {name}: README.md がありません")
            continue
        if not en.is_file():
            print(f"  未訳     {name}")
            bad += 1
            continue
        h = read_stamp(en)
        if h is None:
            print(f"  ハッシュ無し {name}")
            bad += 1
        elif h != source_hash(ja):
            print(f"  要再訳   {name}")
            bad += 1
        else:
            print(f"  訳済み   {name}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
