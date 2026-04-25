# tools/docgen — 吉里吉里Z リファレンス生成

`manual.tjs` (TJS擬似コード + javadoc) を SSOT (Single Source of Truth) として、
Markdown リファレンスと mkdocs サイトを自動生成するツール一式。

## パイプライン

```
document/kirikiriz/j_in/classes/f_*.xml ──[xml2manual.py]──┐
                                                           ├──> doc/manual/<Class>.manual.tjs ──┐
src/plugins/<plugin>/manual.tjs (手書き or 既存) ─────────┘                                     ├──[tjsdoc.py]──> doc/reference/<Class>.md ──[mkdocs]──> Pages
                                                                                                 │
src/core/**/*.cpp + src/plugins/**/*.cpp ──[scan_tjs.py]──> doc/_inventory.json ──[diff_docs.py]─┘──> doc/_missing.md
```

## ツール

| ツール             | 入力                                              | 出力                              |
|-------------------|--------------------------------------------------|-----------------------------------|
| `xml2manual.py`   | `document/kirikiriz/j_in/classes/f_*.xml`        | `doc/manual/<Class>.manual.tjs`   |
| `xml2md.py`       | `document/kirikiriz/j_in/*.xml` (ガイド/imgsrc)  | `doc/guide/`, `doc/_assets/`      |
| `tjsdoc.py`       | `*.manual.tjs` (複数ディレクトリ集約可)          | `doc/reference/<Class>.md`        |
| `fix_props.py`    | `src/plugins/<plugin>/*.cpp`                     | `manual.tjs` の bare property 書き換え |
| `scan_tjs.py`     | `src/core/**/*.cpp` のバインド情報               | `doc/_inventory.json`             |
| `diff_docs.py`    | `_inventory.json` + `doc/manual/*.manual.tjs`    | `doc/_missing.md`                 |

Python は 3.12 系。追加依存はサイト構築時のみ (`requirements.txt`)。

## 通常の運用フロー

### 1. core クラスのドキュメント追加・更新

```bash
# 旧 XML から manual.tjs を初期生成（初回のみ）
python tools/docgen/xml2manual.py

# 以後、`doc/manual/<Class>.manual.tjs` を直接編集する
# （TJS の擬似コード + javadoc 形式で記述）
```

### 2. C++ バインドが増減したとき

```bash
# C++ 側のバインドを抽出
python tools/docgen/scan_tjs.py

# manual.tjs と突合
python tools/docgen/diff_docs.py

# `doc/_missing.md` を見て manual.tjs を編集
# 再度 diff_docs.py を実行してレポートが空になるまで繰り返す
```

### 3. プラグインの property を C++ から自動修正

```bash
# C++ で readonly な property に対して manual.tjs の bare 宣言を
# `{ getter; }` に書き換え
python tools/docgen/fix_props.py --dry-run
python tools/docgen/fix_props.py
```

### 4. Markdown と mkdocs サイトの再生成

```bash
# core (doc/manual/) と plugins (src/plugins/) を統合して md を再生成
python tools/docgen/tjsdoc.py --in doc/manual --in src/plugins

# ローカルでサイトプレビュー
pip install -r tools/docgen/requirements.txt
mkdocs serve
```

## manual.tjs の書式

```tjs
/**
 * クラスの説明（要約）
 *
 * 詳細説明（任意・複数行可）
 */
class Foo {
    /**
     * メソッドの要約
     *
     * 詳細説明
     * @param x 引数x の説明
     * @param y = 0 引数y の説明（既定値あり）
     * @return 戻り値の説明
     * @see Foo.bar
     */
    function method(x, y = 0);

    /**
     * プロパティの要約
     */
    property name { getter; setter; }    // r/w
    property readOnly { getter; }        // r
    property writeOnly { setter; }       // w

    /**
     * イベントの要約
     * @kind event
     */
    function onSomething(arg);

    /**
     * 定数の要約
     */
    const KIND_FOO = 0;
}
```

主な javadoc タグ:

- `@param NAME desc` — 引数の説明
- `@return desc` / `@returns desc` — 戻り値の説明
- `@description desc` — 詳細説明（要約と分離したい場合）
- `@type T` — プロパティの型ヒント
- `@kind event` — メソッドをイベントとして分類
- `@see X.Y` — 関連メンバーへのリンク

## tjsdoc.py のマージ仕様

- `doc/manual/Layer.manual.tjs`（core）と `src/plugins/layerExSave/manual.tjs`
  などが同一クラス `Layer` を含む場合、core を主・plugin を「## プラグイン拡張: <name>」
  セクションとして 1 つの `Layer.md` にまとめる。
- core が無く plugin のみの場合は、`# Layer` のスタブ + 全 plugin を拡張節として配置。
- ネストクラス（`class GdiPlus { class Font { ... } }`）は `GdiPlus.Font.md` として
  独立した md ファイルに展開。
- 単一ファイルにつき複数ファイル名: `manual.tjs` および `*.manual.tjs` をどちらも対象。

## scan_tjs.py の検出範囲

`TJS_BEGIN_NATIVE_METHOD_DECL` / `TJS_BEGIN_NATIVE_PROP_DECL` /
`TJS_BEGIN_NATIVE_EVENT_DECL` を、直前にある以下のいずれかのブロックに
紐付けて抽出する:

- `tTJSNC_<Class>::tTJSNC_<Class>(...)` コンストラクタ
- `TVPCreateNativeClass_<Class>(...)` ファクトリ関数

検出対象クラスは `CLASSES` セットで限定している（内部クラスや
`tTJSNC_Array` など TJS ランタイム自身のクラスを除外するため）。新しい
公開クラスを追加するときは `scan_tjs.py` の `CLASSES` にも追記すること。

コンストラクタ／ファクトリは `TJS_BEGIN_NATIVE_*_DECL` マクロ越しでは
登録されないため、scan_tjs は「クラス名と同名のメンバー」を検出できない。
`diff_docs.py` 側で `stale` 一覧からクラス名自身を除外済み。

## fix_props.py の検出範囲

各 `src/plugins/<name>/` 直下の `*.cpp` `*.h` を走査。検出パターン:

- `Property(TJS_W("name"), getter, setter)` — NCB 形式（3引数 = property）
- `RawCallback(TJS_W("name"), getter, setter, flags)` — 4引数形式（= property）
- `NCB_PROPERTY_RO(name, get)` / `NCB_PROPERTY(name, get, set)` 等のマクロ
- `NCB_GDIP_PROPERTY[_RO](...)`（layerExDraw 専用マクロ）
- `INTPROP(name)`（psdfile 専用マクロ）

setter が `0` / `(int)0` / `nullptr` のいずれかなら readonly と判定し、
manual.tjs 側の `property NAME;` を `property NAME { getter; }` に書き換え。
read-write のものは bare 宣言のまま据え置き（bare = rw が規約）。

## サイト公開（GitHub Pages）

`.github/workflows/docs-pages.yml` が `develop` / `master` への push 時に:

1. mkdocs-material をインストール
2. `mkdocs build` で `site/` を生成
3. `actions/deploy-pages` で公開

mkdocs の設定は `mkdocs.yml`（リポジトリ直下）。検索は組み込み plugin
（lunr.js ベース、日本語対応の separator 設定済み）。
