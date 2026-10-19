"""reference (tjsdoc.py の生成物) の翻訳カタログ。

方針は TODO-i18n.md の C。生成された md を直接訳すと再生成で消えるので、
manual.tjs の解説文をメンバー単位で JSON カタログへ抜き出し、訳をそこに書く。
tjsdoc.py の --extract / --lang から呼ばれる。

カタログ: doc/i18n/<lang>/reference/<Class>.json

    {
      "class": "Layer",
      "entries": {
        "Layer":            { ... },   # クラス自身の解説
        "Layer.width":      { ... },   # メンバー
        "Rect.Rect@2":      { ... },   # 同名 (オーバーロード) の 2 個目以降は @n
        "krkr_richtext:RichText.draw": { ... }   # プラグイン拡張は "<plugin>:" 前置
      }
    }

各エントリ:

    {
      "hash":  "原文のハッシュ (12 桁)",
      "ja":    { "summary": "...", "description": "...", "returns": "...",
                 "params": { "名前": "説明" } },       # 原文 (参照用。毎回上書き)
      "tr":    { 同じ形。訳した項目だけ書く。空文字は未訳扱い },
      "stale": true                                  # 訳した後で原文が変わった (任意)
    }

--extract は原文 ("ja" と "hash") を更新し、"tr" は保つ。原文が変わったエントリで
"tr" があれば "stale": true を付ける (訳し直したら消す。check_translations.py が数える)。
原文から消えたエントリはカタログからも消す。

見出し語 (「引数」「戻り値」等): doc/i18n/<lang>/reference_labels.json
(tjsdoc.py の L と同じキー。無いキーは日本語のまま)。"untranslated" は未訳の
解説文の前に付ける印 (例 "*(Not yet translated)*")。

言語名はここに直書きしない (言語を増やすときはカタログと見出し語を足すだけ)。
"""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

FIELDS = ("summary", "description", "returns")


def _doc_fields(doc):
    d = {k: getattr(doc, k) for k in FIELDS if getattr(doc, k)}
    params = {p[0]: p[2] for p in doc.params if p[2]}
    if params:
        d["params"] = params
    return d


def _hash(fields):
    raw = json.dumps(fields, ensure_ascii=False, sort_keys=True)
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()[:12]


def _iter_keys(group):
    """(key, doc) をグループ内の定義順に返す。"""
    for cls in group:
        pre = f"{cls.source}:" if cls.source else ""
        yield pre + cls.name, cls.doc
        seen = {}
        for m in cls.members:
            base = f"{pre}{cls.name}.{m.name}"
            n = seen.get(base, 0) + 1
            seen[base] = n
            yield (base if n == 1 else f"{base}@{n}"), m.doc


def _catalog_path(name, lang, i18n_dir: Path):
    return i18n_dir / lang / "reference" / f"{name}.json"


def _load(path: Path):
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def _save(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return False
    path.write_bytes(text.encode("utf-8"))
    return True


def extract(groups, lang, i18n_dir: Path):
    changed = 0
    total = 0
    for name, group in groups.items():
        path = _catalog_path(name, lang, i18n_dir)
        old = _load(path) or {}
        old_entries = old.get("entries", {})
        entries = {}
        for key, doc in _iter_keys(group):
            fields = _doc_fields(doc)
            if not fields:
                continue
            h = _hash(fields)
            prev = old_entries.get(key, {})
            e = {"hash": h, "ja": fields}
            tr = prev.get("tr")
            if tr:
                e["tr"] = tr
                if prev.get("stale") or (prev.get("hash") and prev.get("hash") != h):
                    e["stale"] = True
            entries[key] = e
        total += len(entries)
        if not entries:
            continue
        if _save(path, {"class": name, "entries": entries}):
            changed += 1
    print(f"extract '{lang}': {len(groups)} class(es), {total} entr(ies), {changed} catalog(s) updated")
    return 0


def load_labels(lang, i18n_dir: Path):
    path = i18n_dir / lang / "reference_labels.json"
    data = _load(path)
    return data or {}


def apply(group, lang, i18n_dir: Path, untranslated_mark=""):
    """訳を当てたグループのコピーを返す。訳が 1 つも無ければ None。"""
    name = group[0].name
    cat = _load(_catalog_path(name, lang, i18n_dir))
    if not cat:
        return None
    entries = cat.get("entries", {})
    if not any(e.get("tr") for e in entries.values()):
        return None
    out = copy.deepcopy(group)
    for key, doc in _iter_keys(out):
        e = entries.get(key)
        tr = (e or {}).get("tr") or {}
        fields = _doc_fields(doc)
        if not fields:
            continue
        hit = False
        for k in FIELDS:
            if tr.get(k):
                setattr(doc, k, tr[k])
                hit = True
        tparams = tr.get("params") or {}
        if tparams:
            doc.params = [(p[0], p[1], tparams.get(p[0]) or p[2]) for p in doc.params]
            hit = True
        if not hit and untranslated_mark:
            # 未訳: 日本語のまま出し、印を付ける
            if doc.summary:
                doc.summary = f"{untranslated_mark} {doc.summary}"
            elif doc.description:
                doc.description = f"{untranslated_mark} {doc.description}"
    return out


def stats(lang, i18n_dir: Path):
    """クラスごとの (エントリ数, 訳済み, 要再訳) を返す。"""
    res = {}
    base = i18n_dir / lang / "reference"
    if not base.exists():
        return res
    for p in sorted(base.glob("*.json")):
        cat = _load(p) or {}
        es = cat.get("entries", {}).values()
        res[cat.get("class", p.stem)] = (
            len(es),
            sum(1 for e in es if e.get("tr")),
            sum(1 for e in es if e.get("stale")),
        )
    return res


# ---------------------------------------------------------------------------
# 翻訳作業用 CLI
#   python tools/docgen/refi18n.py dump  <lang> <Class> [--all]   未訳 (と要再訳) の原文を JSON で表示
#   python tools/docgen/refi18n.py merge <lang> <Class> <file>    {key: {summary,description,returns,params}}
#                                                                 を tr へ取り込み、stale を外す
# 取り込み後に tjsdoc.py --lang <lang> で md を生成する。
# ---------------------------------------------------------------------------

def _cli(argv):
    import sys
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    i18n_dir = Path(__file__).resolve().parents[2] / "doc" / "i18n"
    if len(argv) < 3 or argv[0] not in ("dump", "merge"):
        print(__doc__)
        print("usage: refi18n.py dump <lang> <Class> [--all] | merge <lang> <Class> <file>")
        return 2
    cmd, lang, name = argv[0], argv[1], argv[2]
    path = _catalog_path(name, lang, i18n_dir)
    cat = _load(path)
    if cat is None:
        print(f"error: カタログがありません: {path} (先に tjsdoc.py --extract {lang})")
        return 1
    entries = cat["entries"]
    if cmd == "dump":
        show_all = "--all" in argv[3:]
        out = {k: e["ja"] for k, e in entries.items()
               if show_all or not e.get("tr") or e.get("stale")}
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return 0
    src = json.loads(Path(argv[3]).read_text(encoding="utf-8"))
    unknown = [k for k in src if k not in entries]
    for k, tr in src.items():
        if k not in entries:
            continue
        tr = {f: v for f, v in tr.items() if v}
        if not tr:
            continue
        entries[k]["tr"] = tr
        entries[k].pop("stale", None)
    _save(path, cat)
    left = sum(1 for e in entries.values() if not e.get("tr"))
    print(f"merged {len(src) - len(unknown)} entr(ies) into {name} ({left} untranslated left)")
    for k in unknown:
        print(f"  warning: unknown key {k}")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(_cli(sys.argv[1:]))
