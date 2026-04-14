# tools/docgen — 吉里吉里Z リファレンス生成

旧 `document/kirikiriz/j_in/*.xml` を **Markdown** に変換し、
`doc/` 配下で管理するためのツール一式。Wiki 反映は
`.github/workflows/docs-wiki.yml` が担当する。

`document/kirikiriz` は別リポジトリからの submodule 参照で、最終的には
破棄される予定。一度 `xml2md.py` を走らせて `doc/reference/` に変換すれば
以後は Markdown だけをメンテすればよい（旧 XML は参照しなくなる）。

## 構成

| 生成物                         | 元データ                                           | 生成ツール                    |
|-------------------------------|---------------------------------------------------|-------------------------------|
| `doc/reference/<Class>.md`    | `document/kirikiriz/j_in/classes/f_*.xml`         | `xml2md.py` *(初回のみ)*      |
| `doc/guide/<Topic>.md`        | `document/kirikiriz/j_in/*.xml`                   | `xml2md.py` *(初回のみ)*      |
| `doc/_assets/*`               | `document/kirikiriz/j_in/imgsrc/*`                | `xml2md.py` *(初回のみ)*      |
| `doc/_index.md`               | ファイル一覧                                      | `xml2md.py` *(初回のみ)*      |
| `doc/_inventory.json`         | `src/core/**/*.cpp` のバインド情報                | `scan_tjs.py`                 |
| `doc/_missing.md`             | 上2つの突合                                       | `diff_docs.py`                |

Python は `.venv`（Python 3.12）にあるものを使用する。追加依存は無し
（stdlib のみ）。

## 初回移行フロー（旧 XML → Markdown）

```bash
.venv/Scripts/python.exe tools/docgen/xml2md.py
```

これで `doc/reference/`, `doc/guide/`, `doc/_assets/`, `doc/_index.md`
が生成される。旧レイアウトの `<doc>/<member>/...` スキーマを以下の
Markdown 形式にマップしている:

- `<title>` → `# タイトル`
- トップ `<desc>` → クラス冒頭の解説
- `<member>` → `### <name>` 見出し
- `<type>` → 見出し直下のメタ行（プロパティ/メソッド/イベント/コンストラクタ）
- `<access>` → 同上のメタ行（r, r/w）
- `<shortdesc>` → 見出し直下の1行要約
- `<arg>/<argitem>` → 引数表（Markdown テーブル）
- `<result>` → **戻り値** セクション
- `<desc>` → **解説** セクション（`<bq>`/`<example>` はフェンスドコード化）
- `<ref>` → 相互リンク（クラス名を認識して `[Class.member](Class.md#member)` 化）
- `<at href="f_Foo.html">` → `[label](Foo.md)`
- `<at href="f_Foo_bar.html">` → `[label](Foo.md#bar)`
- `<img src="imgsrc/x.png"/>` → `![](../_assets/x.png)`
- `<kw>` / `<b>` → `**...**`, `<tt>` → `` `...` ``, `<i>` → `*...*`
- `<note>` → GFM Blockquote (`> **Note:**`)
- `<bq>` / `<example>` → ```` ``` ```` フェンスドコード

既存 XML の癖（全角 `　` でのインデント、`<r/>` 強制改行）は `xml2md.py`
側で吸収済み。コードブロック内だけはインデントを保持する。

## 運用フロー（src/core 側で新メソッドが増えたとき）

```bash
# 1. src/core のバインドからメンバー一覧を抽出
.venv/Scripts/python.exe tools/docgen/scan_tjs.py
# 2. 既存 Markdown と突き合わせ
.venv/Scripts/python.exe tools/docgen/diff_docs.py
```

`doc/_missing.md` に以下3種類の差分が列挙される:

- **ドキュメント未作成クラス** — `doc/reference/<Class>.md` を新規追加する
- **未記載メンバー** — クラスの `.md` に `### <name>` 節を追記する
- **コードに無いメンバー** — バインドから消えた節を `.md` から削除する

`diff_docs.py` を再実行してレポートが空に近づくまで繰り返し、
最後に `git commit` → push すると GitHub Actions が Wiki に自動反映される。

`_missing.md` 自体もコミットしておく（Wiki にも転送されるのでレビュワーが
進捗を確認しやすい）。

### scan_tjs.py の検出範囲

`TJS_BEGIN_NATIVE_METHOD_DECL` / `TJS_BEGIN_NATIVE_PROP_DECL` /
`TJS_BEGIN_NATIVE_EVENT_DECL` を、直前にある以下のいずれかのブロックに
紐付けて抽出する:

- `tTJSNC_<Class>::tTJSNC_<Class>(...)` コンストラクタ
- `TVPCreateNativeClass_<Class>(...)` ファクトリ関数

検出対象クラスは `CLASSES` セットで限定している（内部クラスや
`tTJSNC_Array` など TJS ランタイム自身のクラスを除外するため）。新しい
公開クラスを追加するときは、`scan_tjs.py` の `CLASSES` にも追記すること。

コンストラクタ／ファクトリは `TJS_BEGIN_NATIVE_*_DECL` マクロ越しでは
登録されないため、scan_tjs は「クラス名と同名のメンバー」を検出できない。
`diff_docs.py` 側で `stale` 一覧からクラス名自身を除外済み。

## Wiki 同期の仕組み

GitHub Wiki は **サブディレクトリを持てない** ため、`tools/docgen/sync_wiki.py`
が次の命名でフラット化する:

```
doc/reference/Layer.md             -> Class.Layer.md
doc/reference/Window.BasicDrawDevice.md -> Class.Window.BasicDrawDevice.md
doc/guide/EventSystem.md           -> Guide.EventSystem.md
doc/_assets/foo.png                -> foo.png
doc/_index.md                      -> Home.md
doc/_missing.md                    -> _Docs-Diff-Report.md
```

同時に Markdown 中の相対リンク（`(Layer.md#visible)`、`(../_assets/foo.png)`
等）を Wiki のフラット名前空間に書き換える（`(Class.Layer#visible)` 等）。

`.github/workflows/docs-wiki.yml` が `develop` / `master` への push 時に:

1. 本リポジトリをチェックアウト
2. `<repo>.wiki.git` を `.wiki/` にチェックアウト
3. `Class.*.md` / `Guide.*.md` / `Home.md` / `_Docs-Diff-Report.md` を削除
4. `sync_wiki.py .wiki` でフラット化出力
5. 差分があればコミット & push

Wiki に手動で追加した他の Markdown（`Class.` / `Guide.` / `Home` prefix を
持たないもの）は保持される。

## MkDocs Pages 対応（今後）

`doc/` 配下はそのまま MkDocs Material に載せられるレイアウトにしてある
（`doc/reference/` と `doc/guide/` のサブディレクトリ構成、`doc/_assets/`
の画像）。将来 Pages も有効化する場合は `mkdocs.yml` を `doc/` 直上に
追加し、`nav:` で `_index.md` → `reference/*`, `guide/*` を指す設定に
するだけでよい。
