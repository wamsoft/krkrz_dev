---
name: tjs2
description: TJS2 (吉里吉里Z 内蔵スクリプト言語) の言語仕様と組み込みクラスのリファレンス。.tjs ファイル / *.ks (KAG) 内の埋め込みスクリプト / TJS2 コード断片 を扱う、書く、レビューする、デバッグするときに使う。JavaScript / TypeScript に似ているが文法と意味論が違うので、JS の感覚で書くと壊れる場合が多い。組み込みクラス (Array / Dictionary / Date / Math / RegExp / Exception) の API もここに集約。**呼び出されたら必ず「JS との主な違い」セクションを最初に確認し、その上で必要な詳細リファレンスを Read で取りに行くこと。** 吉里吉里Z 本体のクラス API (Window / Layer / System / Storages / Bitmap 等) や engine 内部はこのスキルの対象外。
---

# TJS2 言語リファレンス

TJS2 (TJS Just Script 2) は吉里吉里 / 吉里吉里Z (kirikiri Z) 内蔵の
スクリプト言語。本スキルは TJS2 **言語仕様** と **組み込みクラス** の
情報源で、本体エンジン API (Layer / System / Window 等) は対象外。

## 重要: 作業に入る前に

1. **JS や Python の感覚で書かない**。下の「JS との主な違い」を必ず確認する
2. **詳細はファイルを Read する**。下の「ファイル索引」から該当ドキュメントを開く
3. **疑わしい時はリファレンスを優先**。記憶や類推より、ドキュメント原文を信頼する

## JS との主な違い (高頻度の落とし穴)

### 変数と型

- 変数は **必ず `var` で宣言**。`let` / `const` は **存在しない**。未宣言変数は使えない。
- 同じ名前の変数を二回 `var` で宣言してもエラーにならない。二度目に初期値があれば代入される。
- 内部型は 6 種類: `void` / `Integer` (64bit) / `Real` (double) / `String` (UTF-16LE, サロゲートペア対応) / `Object` / `Octet` (バイナリ列)。
- **`void` は JS の undefined / null とは別物**。初期化されていない変数は `void` 型。
- `void` 同士の比較は `===` (識別演算子) を使う。`==` だと数値比較に巻き込まれる。
- `typeof` は文字列 `"void"` / `"Integer"` / `"Real"` / `"String"` / `"Object"` / `"Octet"` を返す。

### リテラル

- 配列リテラルは `[1, 2, 3]` (Array クラス)
- **配列リテラルの末尾カンマは「もう 1 要素 void を追加」の意味** (JS と真逆)。 `[a, b,]` は `count == 3` で `[2] == void` になる。 `[]` の中身を書き換えていて末尾に `,` を残すと空要素混入で下流が壊れるので必ず外す
- **辞書リテラルは `%[ "key" => "value", "k2" => v2 ]`** ( `%[ ... ]` が正しい。JS の `{}` ではない。区切りは `=>`、 `:` ではない )
- **辞書リテラルの末尾カンマは無害** (Array と挙動が違うので注意)
- 正規表現リテラルは `/pat/flags` (RegExp クラス)
- 文字列リテラルは `"..."` または `'...'`
- 整数は `0x` (16進), `0o` (8進), `0b` (2進) リテラル可。`123_456` のように `_` で桁区切りも可

### 演算子

- **`new` には括弧が必須**: `new Foo()` は OK、`new Foo` は **構文エラー**
- `>>>` は符号なし右シフト (左辺を unsigned int として扱う唯一の演算子)
- `<->` は **swap 演算子** (左右を交換、結果は取れない)
- `,` (カンマ) は順次評価演算子 (左から評価、結果は最後の値)
- 後置 `if` 演算子: `a = b if b != 0;` (右側が真のときだけ左を評価)
- `incontextof` でオブジェクトのコンテキスト ( this 相当 ) を差し替えてクロージャを作る
- `instanceof "Class"` のように **クラス名を文字列で** 指定する。`instanceof "Array"` 等
- **`#` 演算子は文字コード取得** (`#c` で `c` の最初の一文字の char code を返す)、`$n` は逆 (文字コード → 一文字文字列)。JS の `charCodeAt` / `String.fromCharCode` 相当

### クラスと関数

- クラス本体: `class Foo { var x; function Foo() { ... } function finalize() { ... } property p { getter() { ... } setter(v) { ... } } }`
- **コンストラクタはクラスと同名のメソッド** (JS の `constructor` キーワードではない)
- `finalize()` は GC / 明示破棄時に呼ばれる省略可能なデストラクタ
- メソッド内から **同じクラスを `new` するときは `global.Foo()` と書く** ( `new Foo()` だとコンストラクタ自身を参照してエラー )
- プロパティ宣言は専用構文 `property name { getter() { ... } setter(v) { ... } }`、JS の `get` / `set` キーワード構文ではない
- 関数の引数末尾に `*` を書くと可変長引数 ( `function foo(a, b*)` の `b` は arguments 相当 )

### 真偽値

- 0 / 空文字列 / `void` は偽
- それ以外の文字列は **数値に変換しようとして成功すればその値が真偽**、失敗すれば偽
- → 文字列をそのまま truthy 判定すると JS と挙動が違うことがある (例: `"foo"` は数値変換失敗で偽)

### スコープ

- ブロック `{ ... }` 内で `var` 宣言すると **ブロックスコープ** (JS の `var` と違って関数スコープではない、 `let` 相当の挙動)
- 同名のシャドウィングは可、ブロックを抜けると消える
- 最外側 ( グローバルスコープ ) の `var` は `global` オブジェクトのメンバになる

### 文字列操作 (JS の常識で壊れやすい)

- **`String` クラスは実在しない** ( `typeof "abc" == "String"` だが、実体は特殊化された値 )
- 文字コード取得は **`charCodeAt` 無し** → **`#c` 演算子**を使う (`c` は 1 文字文字列)。存在しないメソッド呼び出しは実行時例外 "メンバ `charCodeAt` が見つかりません" になる
- 一文字取り出しは `str.charAt(n)` (範囲外は空文字) または `str[n]` (範囲外は例外)
- ASCII 判定は `c >= "0" && c <= "9"` のような**文字列同士の比較**が使える (ワイド文字コード順で比較される)。`isDigit` 相当を書くならこの形が楽

### クロージャの落とし穴 ( TJS のスコープキャプチャ )

- **無名関数 (関数リテラル) の中から外側関数の local 変数を参照できない** 場合が多い
- 特にプラグイン (`Scripts.foreach` / `Array.some` 相当) にコールバックを渡すとき、コールバックの実行コンテキストは呼び出し元プラグイン側になり、**外側の local 変数を参照するとランタイム例外** ( "メンバ 'foo' が見つかりません" )
- 対策 1: プラグインの追加引数機構でデータを渡す ( 例: `Scripts.foreach(obj, func, arg1, arg2, ...)` → `function(k, v, arg1, arg2)` )
- 対策 2: `Scripts.getObjectKeys(obj)` で keys 配列を取ってから普通の `for` ループでイテレートする ( 通常のスコープが効く )
- 対策 3: `function() { ... } incontextof this` で `this` を捕捉 ( ただし外側 local var は依然として不可 )
- **推奨**: 迷ったら「素の for ループ + Scripts.getObjectKeys」でよい。プラグイン依存のコールバック機構より確実

### ファイル読み込み (テキストエンコーディング)

kirikiri のテキストストリーム (`tTVPTextReadStream`) 挙動 (`src/core/common/base/TextStream.cpp` より):

1. **BOM 判定が最優先**
   - `EF BB BF` → UTF-8 として decode
   - `FF FE`    → UTF-16 LE として直接ロード
   - `FE FE`    → 暗号化テキスト (`c` モード 相当) / 圧縮テキスト (`z` モード 相当)
2. **BOM 無し**: **`DefaultReadEncoding`** で decode
   - "UTF-8"     → UTF-8 として decode (失敗すれば `TJSNarrowToWideConversionError`)
   - "Shift_JIS" → SJIS として decode (失敗すれば同上)
   - それ以外    → `TVPUnsupportedEncoding` を throw
3. **`DefaultReadEncoding` の初期値は `Shift_JIS`**。`TVPSetDefaultReadEncoding("UTF-8")` (TJS からは `Scripts.textEncoding = "UTF-8"` 相当) で切替可能

**BOM 無し UTF-8 が読めるかはプロジェクトの `DefaultReadEncoding` 設定次第**。「新しい engine は BOM 必須」というのは誤りで、engine 実装は昔から同じ。プロジェクト側の設定を確認する。

### ファイル書き出し (テキスト系)

- `Array.save(filename)` は**組み込み**だが、**UTF-16 LE + BOM 出力固定** (エンコーディング選べない)。git diff の可読性が悪い / 外部ツールとの相性が悪い
- **UTF-8 で書きたいときは `saveStruct.dll` プラグインをリンク**して `Array.save2(filename, utf8=true, newline=0)` を使う ( `newline` は 0=CRLF, 1=LF )
- `Dictionary.saveStruct2(filename, utf8=true, newline=0, option=ssoIndent|ssoSort)` で Dictionary をそのまま TJS 表現 ( saveStruct 形式 ) で保存できる
- 同機能を持つ `PackinOne.dll` も存在するが、init 時に fstat 経由で `'/' must be specified at the end of given directory name.` を throw する場合がある ( 呼び出し順や環境依存 )。standalone tool を書くなら**素の `saveStruct.dll` の方が事故が少ない**
- `saveStruct.dll` / `PackinOne.dll` は Array / Dictionary / Scripts に `toStructString(newline=1, option=0)` も生やす (メモリ上での文字列化)

## 組み込みクラス・型

| クラス | 用途 | 詳細 Read 先 |
|---|---|---|
| Array | 順序付きリスト、`[ ]` リテラル | `tjs2/array.md` |
| Dictionary | 文字列キー辞書、`%[ k=>v ]` リテラル | `tjs2/dictionary.md` |
| String | 文字列 (UTF-16LE) | `tjs2/string.md` |
| Octet | バイナリ列 | `tjs2/octet.md` |
| Math | 数学関数 | `tjs2/math.md` |
| Math.RandomGenerator | 乱数 | `tjs2/randomgenerator.md` |
| Date | 日付/時刻 | `tjs2/date.md` |
| RegExp | 正規表現、`/.../` リテラル | `tjs2/regexp.md` |
| Exception | 例外オブジェクト | `tjs2/exception.md` |

## ファイル索引 (深掘り時に Read する)

ドキュメントは krkrz_dev リポジトリルート相対で `doc/tjs2/` にあります
( 以下の索引はこのディレクトリからの相対名 )。
オンライン版は <https://wamsoft.github.io/krkrz_dev/tjs2/> 。

### 言語仕様

- `about.md` — TJS2 概要
- `simple.md` — 基本的な使い方 / 埋め込み API
- `types.md` — データ型 (void / Integer / Real / String / Object / Octet)
- `variant.md` — `tTJSVariant` 型 (C++ 連携時)
- `variable.md` — 変数 / `var` / スコープ
- `class.md` — クラス、継承、コンストラクタ、finalize
- `function.md` — 関数、引数、可変長
- `property.md` — プロパティ宣言、getter/setter
- `interface.md` — `iTJSDispatch2` (C++ 側のオブジェクトインターフェース)
- `expr_and_op.md` — 式と演算子全リスト (優先順位含む)
- `factor.md` — 項 (リテラル等の最小単位)
- `token.md` — 字句 / 予約語
- `statement_and_block.md` — 文とブロック
- `if.md` / `for.md` / `while.md` / `switch.md` / `with.md` / `try.md` — 制御構文
- `pp.md` — プリプロセッサ
- `style.md` — 推奨スタイル
- `vmcodes.md` — TJS2 仮想マシンの命令コード一覧
- `ttjs.md` — `tTJS` (C++ ホスト側 API)

### 組み込みクラス

- `basictypes.md` — 基本型全般のメソッド/プロパティ
- `array.md` — `Array`
- `dictionary.md` — `Dictionary`
- `string.md` — String 系メソッド
- `octet.md` — `Octet`
- `math.md` — `Math`
- `randomgenerator.md` — `Math.RandomGenerator`
- `date.md` — `Date`
- `regexp.md` — `RegExp`
- `exception.md` — `Exception`

### 周辺情報 (`doc/topics/tjs2/`)

- `tooltip.md` / `asyncimageload.md` / `playmovie.md` / `check_2_z.md` /
  `deleted.md` / `fileformat.md` / `type_specified.md`

## 関連スキル

- 吉里吉里Z 本体クラス API (Window / Layer / System / Storages / Bitmap 等) は skill `krkrz`
- 吉里吉里Z 内部構造 (engine internals) は対象スキルなし

これらは本スキルの対象外。
