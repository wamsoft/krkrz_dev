# スキル配布形 (install.sh) の課題メモ

作成: 2026-08-19 / 指摘元: `nexton_amakano2pe` 案件での利用側検査

正本 `.claude/skills/` は krkrz_dev の中では全リンクが解決するが、
**`tools/skills/install.sh` が組み立てた自己完結版のほうで内部リンクが 47 件切れている**。
同梱範囲 (`BUNDLE`) とパス書き換え範囲の設計から来ているもので、
スキル整理でのデグレではない。プラグイン側 (`dev-toolkit`) は 0 件。

利用側への実害は「深掘り先として案内された md が読めない」こと。
krkrz_dev のチェックアウトが手元にあれば `doc/` を直接読めば済むが、
スキルだけ配った相手には飛び先が無い。

## 検査方法

`~/.claude/skills/` (または `--dist` の出力) で:

```bash
python - <<'PY'
import re, os
bad = []
for root, dirs, files in os.walk('.'):
    for f in files:
        if not f.endswith('.md'): continue
        p = os.path.join(root, f)
        t = open(p, encoding='utf-8', errors='replace').read()
        for m in re.finditer(r'\]\(([^)]+)\)', t):
            l = m.group(1).split('#')[0].strip()
            if not l or l.startswith(('http', 'mailto:')): continue
            if not os.path.exists(os.path.normpath(os.path.join(root, l))):
                bad.append((p, l))
print(len(bad), "broken")
for b in bad: print(*b)
PY
```

## 内訳

| 件数 | パターン | 出どころ | 実体 | 直し方の案 |
|---:|---|---|---|---|
| 20 | `../guide/*.md` | `krkrz/references/*.md` (= `doc/reference/`) | `doc/guide/` | `BUNDLE` に追加 |
| 2 | `../../guide/*.md` | `tjs2/references/topics/wamsoft_changes.md` | 同上 | 同上 (同時に解決) |
| 1 | `../_assets/2DAffineMatrix.png` | `krkrz/references/Layer.md` | `doc/_assets/` | `BUNDLE` に追加 |
| 2 | `../core/*.md` (`repl.md` / `viewport.md`) | `tjs2/references/topics/wamsoft_changes.md` | `doc/topics/core/` | `BUNDLE` に追加 |
| 2 | `../../tjs2/*.md` | `tjs2/references/topics/*.md` | 同スキルの `references/` | sed 書き換えを references 配下にも掛ける |
| 14 | `../../reference/*.md` | `tjs2/references/topics/*.md` | **krkrz スキルの** `references/` | スキルをまたぐので相対では解決不能。素テキスト化 |
| 4 | `Gamepad.md` / `../external/elements/…` | `elements/references/ElementsDialog.md` | `src/core/doc/Gamepad.md` 他 | 同梱か素テキスト化 |
| 2 | engine ツリー相対 | 各所 | krkrz_dev のチェックアウト | 想定内 (配布版メモが断っている) |

### 1. `doc/guide` / `doc/_assets` / `doc/topics/core` の同梱で 25 件が消える

同梱先を `references/` ではなく**スキル直下**にすると、既存のリンクを書き換えずにそのまま当たる:

```
<skill>/references/Layer.md  の ../guide/GraphicSystem.md      → <skill>/guide/GraphicSystem.md
<skill>/references/Layer.md  の ../_assets/2DAffineMatrix.png  → <skill>/_assets/2DAffineMatrix.png
<skill>/references/topics/wamsoft_changes.md の ../../guide/…  → <skill>/guide/…
<skill>/references/topics/wamsoft_changes.md の ../core/…      → <skill>/references/core/…
```

つまり `BUNDLE` の宛先指定に「`references/` 配下ではなくスキル直下」を表せる形が要る
(今は `<to>` が常に `references/` 起点)。`doc/topics/core` だけは `references/core` へ。

* `guide` は 20 ファイル前後あるのでサイズ増を確認のこと (`du -sk doc/guide doc/_assets doc/topics/core`)
* `krkrz/SKILL.md` の「関連ドキュメント」節が `doc/guide/…` `doc/topics/core/*.md` と
  書いているので、同梱するなら SKILL.md 側の書き換え規則も足す
* `doc/topics/core/repl.md` は `krkrz-webui` が別途同梱している `REPL.md` と内容が重なる。
  二重同梱になってよいかは判断が要る

### 2. `references/` 配下にも sed を掛ける

今の install.sh は `BUNDLE` の書き換えを **`SKILL.md` にしか適用していない**。
同梱した md の中のリンクは無加工なので、`doc/tjs2/` → `references/` のような
移動を反映できていない (`../../tjs2/*.md` 2 件)。
`references/topics/*.md` に対しても `../../tjs2/` → `../` を掛ければ消える。

### 3. スキルをまたぐ参照 14 件は相対リンクでは直せない

`tjs2/references/topics/pitfalls.md` などが `../../reference/Window.md`
(= krkrz スキルの `references/Window.md`) を指している。
スキルは独立配置なので相対では届かない。install 時に

```
[Window.setInnerSize](../../reference/Window.md#setinnersize)
  → `Window.setInnerSize` (skill `krkrz` の references/Window.md)
```

のようにリンクを外して素テキストへ落とすのが確実。
(krkrz スキルも一緒に入れる前提なら、案内文だけで十分読み手は辿れる)

### 4. `elements/references/ElementsDialog.md` の 4 件

* `Gamepad.md` — 同ディレクトリ指定だが同梱されていない。実体は `src/core/doc/Gamepad.md`
* `../external/elements/external/elements_modal/README.md` × 3 — 実体は
  `src/core/external/elements/external/elements_modal/README.md`。
  配布版メモは「engine ソースツリー相対パス」を断っているが、これは
  **スキル内相対に見える書き方**なので読み手が誤解する。素テキスト化が望ましい

## 正本側の単純ミス (install.sh とは無関係)

* `.claude/skills/krkrz/SKILL.md:262` — ``- [`tjs2`](tjs2) — TJS2 言語仕様と…``
  スキル相対リンクは解決しない (krkrz_dev の中でも `.claude/skills/krkrz/tjs2` を指してしまう)。
  他のスキルは ``skill `tjs2` `` と素テキストで書いているので、それに揃える。

## 直った確認

上の検査スクリプトを `--dist` 出力に対して流し、0 件になること。
`--user` で入れ直したあと `~/.claude/skills` でも同じく 0 件になること。
