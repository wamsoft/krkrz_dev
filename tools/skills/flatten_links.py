#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""組み立て済みスキル内の「解決できないリンク」を素テキストへ落とす。

install.sh が同梱 (BUNDLE) と相対リンクの張り替え (LINKFIX) を済ませたあとに
掛ける最終処理。スキルは単独で配布されるので、飛び先が同梱されていない
リンクは読み手にとって死にリンクにしかならない。リンク書式を外して
「どこにあるか」の案内文へ落とす。

  - 画像は常に落とす (参照用の図。スキルの読み手には本文で足りる)
  - リンクは実際にファイルが在るかを確かめ、無いものだけ落とす

使い方: flatten_links.py <スキルディレクトリ> [...]
"""

import os
import re
import sys

# ```fenced``` の中はリンクではなくコード。誤検出を避けるため退避する
FENCE = re.compile(r"```.*?```", re.S)
IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
LINK = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)]+)\)")

# 落とす先の案内文。飛び先のパスから「本当はどこにあるか」を推測する
#   <飛び先に含まれる目印>, <案内文>, <ラベルが既に場所を語っている時の短縮形>
HINTS = (
    ("/external/", "engine の external/{tail}", "engine ソースツリー"),
    ("/reference/", "skill `krkrz` の references/{name}", "skill `krkrz`"),
    ("/topics/core/", "krkrz_dev の doc/topics/core/{name}", "krkrz_dev の doc/"),
    ("/topics/tjs2/", "skill `tjs2` の references/topics/{name}", "skill `tjs2`"),
    ("/guide/", "krkrz_dev の doc/guide/{name}", "krkrz_dev の doc/"),
    ("/tjs2/", "skill `tjs2` の references/{name}", "skill `tjs2`"),
)


def describe(target, label=""):
    """飛び先の案内文を組み立てる。

    ラベルが既にパスやファイル名を含んでいる場合 ( 本文が
    ``external/…/README.md`` のように場所を語っている場合 ) は、
    同じパスを二度書かないよう短縮形を使う。
    """
    path = target.split("#")[0]
    name = path.rsplit("/", 1)[-1]
    said = name and name in label
    probe = "/" + path.lstrip("./")
    for key, fmt, short in HINTS:
        if key in probe:
            if said:
                return short
            tail = probe.split("/external/", 1)[-1] if key == "/external/" else path
            return fmt.format(name=name, tail=tail)
    return "krkrz_dev の {}".format(name if said else path.lstrip("./"))


def is_external(target):
    return target.startswith(("http://", "https://", "mailto:", "#"))


def flatten(path):
    """1 ファイル処理して (画像を落とした数, リンクを落とした数) を返す"""
    with open(path, encoding="utf-8") as fp:
        text = fp.read()

    # フェンスを退避
    fences = []

    def stash(m):
        fences.append(m.group(0))
        return "\0FENCE{}\0".format(len(fences) - 1)

    body = FENCE.sub(stash, text)
    base = os.path.dirname(path)
    counts = [0, 0]

    def fix_image(m):
        counts[0] += 1
        name = m.group(2).split("#")[0].rsplit("/", 1)[-1]
        return "( 図 {} は省略 — オンライン版ドキュメント参照 )".format(name)

    def fix_link(m):
        label, target = m.group(1), m.group(2).strip()
        if is_external(target):
            return m.group(0)
        resolved = os.path.normpath(os.path.join(base, target.split("#")[0]))
        if os.path.exists(resolved):
            return m.group(0)
        counts[1] += 1
        return "`{}` ( {} )".format(label, describe(target, label))

    body = IMAGE.sub(fix_image, body)
    body = LINK.sub(fix_link, body)

    # フェンスを戻す
    body = re.sub(r"\0FENCE(\d+)\0", lambda m: fences[int(m.group(1))], body)

    if body != text:
        with open(path, "w", encoding="utf-8", newline="\n") as fp:
            fp.write(body)
    return counts


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 1
    total = [0, 0, 0]
    for skill_dir in argv[1:]:
        for root, _dirs, files in os.walk(skill_dir):
            for name in files:
                if not name.endswith(".md"):
                    continue
                img, link = flatten(os.path.join(root, name))
                total[0] += img
                total[1] += link
                total[2] += 1
    print("  リンク整理: {} ファイル / 図 {} 件・未同梱リンク {} 件を素テキスト化"
          .format(total[2], total[0], total[1]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
