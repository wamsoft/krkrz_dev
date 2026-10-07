# Scripts

Scripts クラスは TJS2 に関するメソッドやプロパティを管理します。このクラスからオブジェクトを作成することはできません。

## メンバー一覧

### プロパティ

- [textEncoding](#textencoding)

### メソッド

- [execStorage](#execstorage)
- [evalStorage](#evalstorage)
- [compileStorage](#compilestorage)
- [exec](#exec)
- [eval](#eval)
- [dump](#dump)
- [getTraceString](#gettracestring)
- [setCallMissing](#setcallmissing)
- [getClassNames](#getclassnames)
- [dumpStringHeap](#dumpstringheap)

---

### textEncoding

プロパティ \ アクセス: `r/w`

**解説**

スクリプトを読み込む時に使用するテキストエンコーディングを指定

スクリプトを読み込む時に使用するテキストエンコーディングを指定します。

現在指定できるのは"UTF-8"か"Shift_JIS"のどちらかです。

---

### execStorage

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 実行するストレージを指定します。 |
| `mode` | `''` | ファイルを読み込む際のモード文字列を指定します。"o" に続いてオフセットを10進で指定するとファイルのそのバイト位置からの読み込みになります。 |
| `context` | `global` | 実行コンテキストを指定します。 |

**戻り値**

スクリプトを実行した結果が戻ります。

**解説**

ストレージ上のスクリプトの実行

指定されたストレージを読み込み、その内容を TJS2 スクリプトとして実行します。

スクリプトを実行中に発生した例外はこのメソッド内では捕捉されませんので、このメソッドの
呼び出し側で捕捉することができます。

**関連:** [Scripts.evalStorage](Scripts.md#evalstorage)

---

### evalStorage

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 評価するストレージを指定します。 |
| `mode` | `''` | ファイルを読み込む際のモード文字列を指定します。"o" に続いてオフセットを10進で指定するとファイルのそのバイト位置からの読み込みになります。 |
| `context` | `global` | 実行コンテキストを指定します。 |

**戻り値**

式を評価した結果が戻ります。

**解説**

ストレージ上の式の評価

指定されたストレージを読み込み、その内容を TJS2 式として評価します。

スクリプトを実行中に発生した例外はこのメソッド内では捕捉されませんので、このメソッドの
呼び出し側で捕捉することができます。

**関連:** [Scripts.execStorage](Scripts.md#execstorage)

---

### compileStorage

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `inputfile` | `&nbsp;` | コンパイル対象ストレージを指定します。 |
| `outputfile` | `&nbsp;` | 出力バイトコードストレージを指定します。 |
| `isresult` | `false` | 戻り値が必要かどうかを指定します。 |
| `outputdebug` | `false` | デバッグ情報を含めるかどうかを指定します。 |
| `isexpression` | `false` | 式かどうかを指定します。 |

**解説**

ストレージ上のスクリプトのコンパイル

指定されたストレージを読み込み、その内容をコンパイルしてバイトコードファイルとして出力します。

コンパイルされたバイトコードファイルは execStorage もしくは、evalStorage で通常のスクリプトと同じように実行できます。

**関連:** [Scripts.execStorage](Scripts.md#execstorage) / [Scripts.evalStorage](Scripts.md#evalstorage)

---

### exec

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `script` | `&nbsp;` | 実行するスクリプトを文字列で指定します。 |
| `name` | `''` | エラーメッセージ用ファイル名の指定 |
| `linesof` | `0` | エラーメッセージ用行番号の指定 |
| `context` | `global` | 実行コンテキストを指定します。 |

**戻り値**

スクリプトを実行した結果が戻ります。

**解説**

スクリプトの実行

script で指定された文字列を TJS2 スクリプトとして実行します。

スクリプトを実行中に発生した例外はこのメソッド内では捕捉されませんので、このメソッドの
呼び出し側で捕捉することができます。

**関連:** [Scripts.execStorage](Scripts.md#execstorage) / [Scripts.eval](Scripts.md#eval)

---

### eval

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `expression` | `&nbsp;` | 実行する式を文字列で指定します。 |
| `name` | `''` | エラーメッセージ用ファイル名の指定 |
| `linesof` | `0` | エラーメッセージ用行番号の指定 |
| `context` | `global` | 実行コンテキストを指定します。 |

**戻り値**

式を評価した結果が戻ります。

**解説**

式の評価

expression で指定された文字列を TJS2 式として実行します。

スクリプトを実行中に発生した例外はこのメソッド内では捕捉されませんので、このメソッドの
呼び出し側で捕捉することができます。

**関連:** [Scripts.execStorage](Scripts.md#execstorage) / [Scripts.exec](Scripts.md#exec)

---

### dump

メソッド

**解説**

コンテキストのダンプ

現時点で TJS2 に読み込まれているスクリプトブロック内の各コンテキストの内容の詳細を
ローカルファイルに出力します。主に VM コードの逆アセンブル結果が出力されます。

出力ファイルは、吉里吉里の実行可能ファイルと同じフォルダに出力され、そのファイル名は
吉里吉里の実行可能ファイルに .dump.txt が付加されたものになります。

---

### getTraceString

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `limit` | `0` | 履歴を取得する最大呼び出し深さを指定します。この引数を省略するか 0 を指定すると、取得できる限りの履歴を取得します。 |

**戻り値**

呼び出し履歴を文字列化した物

**解説**

呼び出し履歴の取得

メソッドの呼び出し履歴を文字列として取得します。このメソッドが呼ばれた時点での履歴を取得することができます。

このメソッドを使用するには、コマンドラインオプションで -debug (デバッグモード) が有効になっていなければなりません。デバッグモードが無効の場合はこのメソッドは空文字列を返します。

返される文字列はたとえば 'messagelayer.tjs(1561)[(function) addButton] <-- mainwindow.tjs(4463)[(function expression) (anonymous)] <-- conductor.tjs(427)[(function) onTag] <-- conductor.tjs(95)[(function) timerCallback]' のような物です。

---

### setCallMissing

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `missing` | `&nbsp;` | メンバが見つからない時に呼び出されるハンドラ。 |

**解説**

メンバが見つからない時に呼び出されるハンドラの登録

メンバが見つからない時に呼び出されるハンドラを登録します。

---

### getClassNames

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `obect` | `&nbsp;` | クラス名を取得するオブジェクト。 |

**戻り値**

クラス名の配列

**解説**

クラス名を取得

オブジェクトからクラス名を取得します。

---

### dumpStringHeap

メソッド

**解説**

文字列ヒープのダンプ

TJS2 ランタイムが管理している文字列ヒープの内容をデバッグ出力します。
`TJS_DEBUG_DUMP_STRING` を有効にしてビルドされたエンジンでのみ呼び出せます。
メモリリーク調査などのデバッグ用途専用。

---

## プラグイン拡張: json

擬似コードによるマニュアル

### メンバー一覧

#### メソッド

- [evalJSON](#evaljson)
- [evalJSONStorage](#evaljsonstorage)
- [saveJSON](#savejson)
- [toJSONString](#tojsonstring)

---

### evalJSON

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `jsonText` | `&nbsp;` | JSON が格納されたテキスト |

**戻り値**

Array または Dictionary

**解説**

JSON の文字列を解析して Array または Dictionary を返す

---

### evalJSONStorage

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `jsonFile` | `&nbsp;` | JSON が格納されたテキストファイルのファイル名 |
| `utf8` | `false` | 入力エンコーディング指定。true なら UTF-8、falseなら現在のコードページ |

**戻り値**

Array または Dictionary

**解説**

JSON のファイルを解析して Array または Dictionary を返す

---

### saveJSON

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `jsonFile` | `&nbsp;` | 格納先ファイル |
| `obj` | `&nbsp;` | 保存対象オブジェクト |
| `utf8` | `false` | 出力エンコーディング指定。true なら UTF-8、falseなら現在のコードページ |
| `newline` | `0` | 改行コード 0:CRLF 1:LF |

**解説**

データを JSON 形式で保存する

---

### toJSONString

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `obj` | `&nbsp;` |  |
| `newline` | `0` | 改行コード 0:CRLF 1:LF |

**戻り値**

JSON 形式のテキスト

**解説**

データを JSON 形式の文字列に変換する

---

## プラグイン拡張: saveStruct

### メンバー一覧

#### メソッド

- [toStructString](#tostructstring)

---

### toStructString

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `target` | `&nbsp;` | 文字列化する対象（辞書・配列以外の int/real/string/octet/null/void も可能） |
| `newline` | `1` | 改行コード 0:CRLF 1:LF |
| `option` | `ssoIndent\|ssoSort` | 整形オプション sso* の組み合わせ（後述）もしくは直接数値指定 |

**戻り値**

saveStruct に準じた形の文字列を返す

**解説**

optionのデフォルト値がArray/Dictionaryと違うので注意（デバッグ用途を想定）

---

## プラグイン拡張: scriptsEx

### メンバー一覧

#### メソッド

- [getObjectKeys](#getobjectkeys)
- [getObjectCount](#getobjectcount)
- [getObjectContext](#getobjectcontext)
- [isNullContext](#isnullcontext)
- [equalStruct](#equalstruct)
- [equalStructNumericLoose](#equalstructnumericloose)
- [foreach](#foreach)
- [getMD5HashString](#getmd5hashstring)
- [clone](#clone)
- [rehash](#rehash)
- [propSet](#propset)
- [propGet](#propget)
- [safeEvalStorage](#safeevalstorage)

---

### getObjectKeys

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `obj` | `&nbsp;` | 対象オブジェクト |

**戻り値**

キーが格納された配列

**解説**

オブジェクトのメンバ名一覧を返す

---

### getObjectCount

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `obj` | `&nbsp;` | 対象オブジェクト |

**戻り値**

個数を返す

**解説**

オブジェクトのメンバ個数を返す

---

### getObjectContext

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `obj` | `&nbsp;` | 対象オブジェクト |

**戻り値**

コンテキストオブジェクト

**解説**

オブジェクトのコンテキストを返す

---

### isNullContext

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `obj` | `&nbsp;` | 対象オブジェクト |

**戻り値**

コンテキストが null

**解説**

オブジェクトのコンテキスト判定

---

### equalStruct

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `obj1` | `&nbsp;` | オブジェクトその1 |
| `obj2` | `&nbsp;` | オブジェクトその2 |

**戻り値**

等しければ true

**解説**

オブジェクト同士を比較する。辞書/配列の場合は中身の要素が再帰的に比較されます

---

### equalStructNumericLoose

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `obj1` | `&nbsp;` | オブジェクトその1 |
| `obj2` | `&nbsp;` | オブジェクトその2 |

**戻り値**

等しければ true

**解説**

オブジェクト同士を比較する。辞書/配列の場合は中身の要素が再帰的に比較されます

数値がゆるく比較されます(0.0 と 0 を等しいとして扱います)

---

### foreach

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `obj` | `&nbsp;` | 処理対象オブジェクト(辞書または配列) |
| `func` | `&nbsp;` | 呼び出し関数。func(key, value, args*) の形で呼ばれます。<br>無名関数などコンテキストが null の場合は自動的に thisコンテキストで動作します<br>関数がなにかしら値を返すと処理が中断されます |
| `args*` | `&nbsp;` |  |

**戻り値**

中断時に返された値

**解説**

オブジェクトのメンバの全参照

---

### getMD5HashString

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `octet` | `&nbsp;` | 対象オクテット |

**戻り値**

ハッシュ値（32文字の16進数ハッシュ文字列（小文字））

**解説**

octet の MD5ハッシュ値の取得

---

### clone

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `obj` | `&nbsp;` | クローン元<br>void/数値/文字列/octet は元の値をそのまま返します。<br>辞書・配列オブジェクトは、deep copy 処理したものを返します。入れ子は再帰処理されます。<br>一般オブジェクトは "clone" メソッドが存在すればその帰り値を、なければ元の値をそのまま返します |

**解説**

値のクローンを返す。

---

### rehash

メソッド

**解説**

TJSDoRehash()を呼ぶ

TJSCustomObjectベースのオブジェクトのハッシュテーブルサイズの再構築フラグを立てます。
（辞書やほとんどのクラスおよびインスタンスのオブジェクトが対象になります）

解説：
ハッシュテーブルサイズはそのオブジェクトの持つ要素数により決定されます。
フラグが立った後，オブジェクトに何か書き込んだタイミングで再計算を行い，
テーブルサイズが変わった場合にのみ再構築が行われます。（サイズ＝2^(要素数のビット数+2)程度？）
普段，吉里吉里は定期的（アイドル時かつ前回から1.5秒以上経過している時）に
TJSDoRehash()が呼ばれているので特に気にする必要はありませんが，
アイドルを挟まずに大量に要素を追加する場合において
カウンタで何千〜万回に1回等の間隔で呼び出すようにすると効果的かと思われます。

---

### propSet

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `obj` | `&nbsp;` | 対象オブジェクト |
| `member` | `&nbsp;` | メンバ名(typeof member == "Integer"ならProp{Set,Get}ByNumを呼ぶ) |
| `value` | `&nbsp;` | セットする値(propSetのみ) |
| `flag` | `Scripts.pfMemberEnsure` | フラグ(Scripts.pf* の"\|"(or)による組み合わせ指定，もしくは0)<br>Scripts.pfMemberEnsure    : (set時)メンバを新規追加する場合に指定（ない場合は既存メンバのみ書き換え可能）<br>Scripts.pfMemberMustExist : (get時)メンバがない場合はエラー（辞書のundefinedもvoidを返さずエラーになります）<br>Scripts.pfIgnoreProp      : (get/set時)プロパティの動作を無視（TJSの&指定と同じ動作です）<br>Scripts.pfHiddenMember    : (set時)隠しメンバ指定（assignStruct/saveStruct等のEnumMembers系の処理で無視されます）<br>Scripts.pfStaticMember    : (set時)Staticメンバ指定（クラスオブジェクトなどに使用します） |

**戻り値**

取得した値(propGetのみ，set時はvoid)

**解説**

指定オブジェクトのPropSet/Getを呼ぶ

---

### propGet

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `obj` | `&nbsp;` |  |
| `member` | `&nbsp;` |  |
| `flag` | `Scripts.pfMemberMustExist` |  |

---

### safeEvalStorage

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 評価するストレージ（バイトコードバイナリは不可／saveStructで(const)つきで保存された辞書／配列が対象） |
| `mode` | `&nbsp;` | モード文字列 |
| `context` | `&nbsp;` | 実行コンテキスト |

**戻り値**

評価されたデータ

**解説**

(const)つき辞書／配列を安全に評価する

---

## プラグイン拡張: windowEx

Scripts拡張

### メンバー一覧

#### メソッド

- [setEvalErrorLog](#setevalerrorlog)

---

### setEvalErrorLog

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `enabled` | `&nbsp;` | 出力許可 |

**戻り値**

元の値

**解説**

Scripts.evalのエラーログ出力抑制

enabled に false を設定すると Scripts.eval の評価処理を
TVPExecuteExpression 経由で行うようになり，例外発生時にログが出力されない
吉里吉里のバージョンアップに伴い仕様が変わる可能性があるので注意のこと

---
