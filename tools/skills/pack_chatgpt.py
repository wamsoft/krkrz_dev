#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""組み立て済みスキルを ChatGPT (カスタム GPT / プロジェクト) 用のパックにまとめる。

install.sh が組み立てた自己完結形のスキル (SKILL.md + references/ 等) を入力に、
ChatGPT のナレッジとして上げやすい形へ束ね直す。通常は pack_chatgpt.sh から呼ぶ。

  - ナレッジは 20 ファイルまでという制限に合わせ、スキル / 分野ごとに 1 ファイルへ連結する
  - 大きい分野 (本体クラスのリファレンス) はサイズで分割する
  - スキル間・ファイル間の相対リンクは「どのナレッジファイルのどのファイルか」の案内へ置き換える
  - Claude Code 向けの記述 (frontmatter、配布版メモ、"Read する" 等) を ChatGPT 向けに直す
  - 英語版 (*.en.md) は入れない (日本語版のパック)

使い方: pack_chatgpt.py <組み立て済み skills ディレクトリ> <出力先> [--zip]
"""

import datetime
import os
import re
import shutil
import subprocess
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(HERE, "chatgpt")

# ChatGPT の制限 (GPT の指示欄の文字数・ナレッジのファイル数)
MAX_INSTRUCTIONS = 8000
MAX_KNOWLEDGE_FILES = 20
# 本体リファレンスを分割する目安 (UTF-8 バイト)
CHUNK_BYTES = 900 * 1024

TJS2_BUILTINS = {
    "array", "dictionary", "date", "math", "octet", "randomgenerator",
    "regexp", "string", "exception",
}

# スキル名 → 本文中の「skill `x`」をどう読み替えるか
SKILL_ALIAS = {
    "tjs2": "ナレッジ 01〜03 (tjs2_*)",
    "krkrz": "ナレッジ 04〜08 (krkrz_*)",
    "elements": "ナレッジ 09_elements",
    "krkrz-repl": "ナレッジ 10_krkrz_repl",
    "krkrz-webui": "ナレッジ 11_krkrz_webui",
}

FENCE = re.compile(r"```.*?```", re.S)
LINK = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)\s]+)\)")


def md_files(root, rel_dir, recursive=False):
    """rel_dir 直下 (recursive なら配下全部) の日本語版 md をスキル相対パスで返す"""
    base = os.path.join(root, rel_dir)
    out = []
    if not os.path.isdir(base):
        return out
    if recursive:
        for d, _dirs, files in os.walk(base):
            for f in files:
                out.append(os.path.relpath(os.path.join(d, f), root))
    else:
        out = [os.path.join(rel_dir, f) for f in os.listdir(base)
               if os.path.isfile(os.path.join(base, f))]
    out = [p.replace(os.sep, "/") for p in out
           if p.endswith(".md") and not p.endswith(".en.md")]
    return sorted(out, key=str.lower)


def plan(skills_dir):
    """(出力ファイル名, 題, [(skill, スキル内相対パス), ...]) の並びを決める"""
    def files(skill, rel_dir, recursive=False):
        return [(skill, p) for p in md_files(os.path.join(skills_dir, skill), rel_dir, recursive)]

    tjs2_refs = files("tjs2", "references")
    lang = [x for x in tjs2_refs if os.path.basename(x[1])[:-3] not in TJS2_BUILTINS]
    builtins = [x for x in tjs2_refs if os.path.basename(x[1])[:-3] in TJS2_BUILTINS]

    groups = [
        ("01_tjs2_skill.md", "TJS2 言語: 概要と JavaScript との違い", [("tjs2", "SKILL.md")]),
        ("02_tjs2_language.md", "TJS2 言語仕様", lang),
        ("03_tjs2_builtins_topics.md", "TJS2 組み込みクラスと周辺トピック",
         builtins + files("tjs2", "references/topics", True)),
        ("04_krkrz_skill.md", "吉里吉里Z 本体 API: 入口・考え方・定型コード", [("krkrz", "SKILL.md")]),
    ]

    # 本体クラスのリファレンスはサイズで分割
    refs = files("krkrz", "references")
    chunks, cur, size = [], [], 0
    for item in refs:
        n = os.path.getsize(os.path.join(skills_dir, item[0], item[1]))
        if cur and size + n > CHUNK_BYTES:
            chunks.append(cur)
            cur, size = [], 0
        cur.append(item)
        size += n
    if cur:
        chunks.append(cur)
    for i, chunk in enumerate(chunks, 1):
        first = os.path.basename(chunk[0][1])[:-3]
        last = os.path.basename(chunk[-1][1])[:-3]
        groups.append((
            "05_krkrz_reference_{}.md".format(i),
            "吉里吉里Z クラスリファレンス ({}〜{})".format(first, last), chunk))

    groups += [
        ("06_krkrz_threepp.md", "吉里吉里Z 3D (threepp / VRM) プラグインのクラス",
         files("krkrz", "references/threepp", True)),
        ("07_krkrz_guide.md", "吉里吉里Z 解説 (guide)", files("krkrz", "guide", True)),
        ("08_krkrz_topics.md", "吉里吉里Z 個別トピック", files("krkrz", "topics", True)),
        ("09_elements.md", "Elements ダイアログ / 画面 UI",
         [("elements", "SKILL.md")] + files("elements", "references", True)),
        ("10_krkrz_repl.md", "REPL / Agent API で krkrz を操作する", [("krkrz-repl", "SKILL.md")]),
        ("11_krkrz_webui.md", "-replweb にブラウザ UI を載せる",
         [("krkrz-webui", "SKILL.md")] + files("krkrz-webui", "references", True)),
    ]
    return [g for g in groups if g[2]]


def strip_skill_header(text):
    """frontmatter を外して description を「用途」として残し、配布版の注記を落とす"""
    desc = ""
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if m:
        d = re.search(r"^description:\s*(.*)$", m.group(1), re.M)
        if d:
            desc = d.group(1).strip()
        text = text[m.end():]
    # 「> **配布版メモ**」「> **パスの基点**」で始まる引用ブロックを落とす
    text = re.sub(r"(?m)^> \*\*(配布版メモ|パスの基点)\*\*.*\n(?:>.*\n)*\n?", "", text)
    if desc:
        text = "> 用途: {}\n\n{}".format(desc, text.lstrip("\n"))
    return text


def adapt_wording(text):
    """Claude Code 向けの言い回しを ChatGPT 向けに直す"""
    def skill_ref(m):
        name = m.group(1)
        return SKILL_ALIAS.get(name, "Claude Code 用スキル `{}`".format(name))
    text = re.sub(r"(?:別 )?skill \(?`([\w:-]+)`\)?", skill_ref, text)
    # Claude のファイル読み取りツール (Read) を指す言い回し。順序に意味がある
    for before, after in (
        ("Read で取りに行く", "検索して確認する"),
        ("Read しに行く", "参照する"),
        ("Read する", "参照する"),
        ("を Read", "を参照する"),
        ("Read 先", "参照先"),
        ("Read で目視", "開いて目視"),
    ):
        text = text.replace(before, after)
    return text


def git_rev(path, *paths):
    """path のリポジトリの短縮コミット。取れなければ None

    パックの元になるパス (paths) に未コミットの変更があれば印を付ける
    (無関係な作業中ファイルでは付けない)。
    """
    def git(*args):
        r = subprocess.run(["git", "-C", path] + list(args),
                           capture_output=True, text=True, encoding="utf-8")
        return r.stdout.strip() if r.returncode == 0 else None
    rev = git("rev-parse", "--short", "HEAD")
    if rev is None:
        return None
    if git("status", "--porcelain", "--untracked-files=no", "--", *paths):
        rev += " (未コミットの変更あり)"
    return rev


def provenance():
    """INDEX に載せる版情報の行"""
    repo = os.path.normpath(os.path.join(HERE, "..", ".."))
    lines = ["- 生成日: {}".format(datetime.date.today().isoformat())]
    for label, path, srcs in (
            ("krkrz_dev", repo, (".claude/skills", "doc", "tools/skills")),
            ("src/core", os.path.join(repo, "src", "core"), ("doc",))):
        rev = git_rev(path, *srcs)
        if rev:
            lines.append("- {} のコミット: {}".format(label, rev))
    return lines


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    make_zip = "--zip" in argv
    if len(args) != 2:
        print(__doc__)
        return 1
    skills_dir, out = (os.path.abspath(a) for a in args)

    groups = plan(skills_dir)
    if len(groups) + 1 > MAX_KNOWLEDGE_FILES:
        print("error: ナレッジが {} ファイルになり上限 {} を超える"
              .format(len(groups) + 1, MAX_KNOWLEDGE_FILES))
        return 1

    # スキル内のパス → 入れたナレッジファイル
    where = {}
    for fname, _title, items in groups:
        for skill, rel in items:
            where[(skill, rel)] = fname

    def rewrite_links(body, skill, rel):
        base = os.path.dirname(rel)

        def fix(m):
            label, target = m.group(1), m.group(2)
            if target.startswith(("http://", "https://", "mailto:")):
                return m.group(0)
            if target.startswith("#"):
                return label
            path, _, anchor = target.partition("#")
            resolved = os.path.normpath(os.path.join(base, path)).replace(os.sep, "/")
            hit = where.get((skill, resolved))
            if hit is None:
                return label
            spot = "{}/{}".format(skill, resolved)
            if anchor:
                spot += "#" + anchor
            return "{} (→ {} の {})".format(label, hit, spot)

        fences = []

        def stash(m):
            fences.append(m.group(0))
            return "\0F{}\0".format(len(fences) - 1)

        body = FENCE.sub(stash, body)
        body = LINK.sub(fix, body)
        return re.sub(r"\0F(\d+)\0", lambda m: fences[int(m.group(1))], body)

    if os.path.isdir(out):
        shutil.rmtree(out)
    kdir = os.path.join(out, "knowledge")
    os.makedirs(kdir)

    index = [
        "# 00_INDEX — ナレッジファイルの対応表",
        "",
        "吉里吉里Z / TJS2 開発ナレッジパックの目次。本文に出てくる `references/Layer.md` や",
        "`guide/StorageSystem.md` のようなパスは元のスキル内のファイル名で、",
        "どのナレッジファイルに入っているかをこの表で引ける。",
        "各ナレッジファイルの中では、元のファイルごとに `[出典: <スキル>/<パス>]` の行で区切ってある。",
        "",
        "## このパックの版",
        "",
    ] + provenance() + [""]
    for fname, title, items in groups:
        parts = ["# {}\n\n吉里吉里Z / TJS2 開発ナレッジパックの一部 ({})。".format(title, fname),
                 "元のファイルごとに `[出典: ...]` の行で区切ってある。収録:\n"]
        parts.append("\n".join("- {}/{}".format(s, r) for s, r in items))
        index.append("## {} — {}\n".format(fname, title))
        for skill, rel in items:
            with open(os.path.join(skills_dir, skill, rel), encoding="utf-8") as fp:
                text = fp.read().replace("\r\n", "\n")
            if os.path.basename(rel) == "SKILL.md":
                text = strip_skill_header(text)
            text = adapt_wording(rewrite_links(text, skill, rel))
            parts.append("\n\n---\n\n[出典: {}/{}]\n\n{}".format(skill, rel, text.strip()))
            index.append("- {}/{}".format(skill, rel))
        index.append("")
        with open(os.path.join(kdir, fname), "w", encoding="utf-8", newline="\n") as fp:
            fp.write("\n".join(parts[:3]) + "".join(parts[3:]) + "\n")
    with open(os.path.join(kdir, "00_INDEX.md"), "w", encoding="utf-8", newline="\n") as fp:
        fp.write("\n".join(index))

    # 指示文と README はテンプレートをそのまま
    with open(os.path.join(TEMPLATE_DIR, "instructions.md"), encoding="utf-8") as fp:
        instr = fp.read()
    if len(instr) > MAX_INSTRUCTIONS:
        print("error: instructions.md が {} 文字で上限 {} を超える".format(len(instr), MAX_INSTRUCTIONS))
        return 1
    shutil.copy(os.path.join(TEMPLATE_DIR, "instructions.md"), out)
    shutil.copy(os.path.join(TEMPLATE_DIR, "README.md"), out)

    # SKILL.md を読めるツール向けに、元の自己完結形もそのまま添える
    # Codex 等ではスキルのフォルダだけを置くので、版情報は各 SKILL.md にも入れる
    # (frontmatter の直後。スキルの読み込みには影響しない)
    shutil.copytree(skills_dir, os.path.join(out, "skills"))
    stamp = "> **このパックの版** — " + " / ".join(
        l[2:] for l in provenance()) + "\n\n"
    for name in os.listdir(os.path.join(out, "skills")):
        p = os.path.join(out, "skills", name, "SKILL.md")
        if not os.path.isfile(p):
            continue
        with open(p, encoding="utf-8") as fp:
            text = fp.read()
        m = re.match(r"---\n.*?\n---\n", text, re.S)
        if m:
            text = text[:m.end()] + stamp + text[m.end():]
            with open(p, "w", encoding="utf-8", newline="\n") as fp:
                fp.write(text)
    with open(os.path.join(out, "VERSION.md"), "w", encoding="utf-8", newline="\n") as fp:
        fp.write("# このパックの版\n\n" + "\n".join(provenance()) + "\n")

    print("ChatGPT パック: {}".format(out))
    print("  instructions.md : {} 文字 (上限 {})".format(len(instr), MAX_INSTRUCTIONS))
    names = ["00_INDEX.md"] + [g[0] for g in groups]
    for n in names:
        kb = os.path.getsize(os.path.join(kdir, n)) // 1024
        print("  knowledge/{:<32} {:>6} KB".format(n, kb))
    print("  ナレッジ {} ファイル (上限 {})".format(len(names), MAX_KNOWLEDGE_FILES))

    if make_zip:
        zpath = out.rstrip("/\\") + ".zip"
        with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
            for d, _dirs, fs in os.walk(out):
                for f in fs:
                    p = os.path.join(d, f)
                    z.write(p, os.path.relpath(p, os.path.dirname(out)))
        print("  zip: {} ({} KB)".format(zpath, os.path.getsize(zpath) // 1024))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
