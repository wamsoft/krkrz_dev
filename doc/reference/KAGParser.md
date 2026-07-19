# KAGParser

擬似コードによるマニュアル

吉里吉里Z KAGParserEx プラグイン。

KAG シナリオファイルを解析する KAGParser クラスを提供します。
Plugins.link("KAGParserEx.dll") でリンクすると、KAGParser クラスが本プラグ
インの拡張版に置き換わります ( アンリンクすると元に戻ります )。

KAGParser は KAG シナリオを先頭 ( または指定ラベル ) から解釈し、
getNextTag() を呼ぶたびに「次のタグ」を辞書として返す字句解析器です。
文字の表示やタグの実行そのものは行いません ( KAG3 の MainWindow などの
利用側が getNextTag() の返すタグを解釈して実行します )。

使用例:
var parser = new KAGParser();
parser.loadScenario("first.ks");
parser.goToLabel("*start");
var tag;
while((tag = parser.getNextTag()) !== void) {
// tag.tagname にタグ名、その他のメンバに属性が入る
}

getNextTag() が返す辞書には、タグ名が tagname メンバとして、タグの属性が
「属性名 => 値 ( 文字列 )」の形で格納されます。地の文は 1 文字ずつ
tagname が "ch" の擬似タグ ( text メンバに文字 ) として、改行は tagname が
"r" の擬似タグ ( 行末では eol=true 付き ) として返されます。

processSpecialTags が真 ( 既定 ) のとき、以下のシステムタグはパーサ内部で
処理され、getNextTag() の返り値としては現れません:
if / ignore / elsif / else / endif / endignore ( 条件分岐 )、
macro / endmacro / erasemacro ( マクロの記録・削除 )、
pmacro / erasepmacro ( パラメータマクロの登録・削除 )、
jump / call / return ( シナリオ内ジャンプ・呼び出し )、
emb ( 式の評価結果の埋め込み )。

オリジナルの KAGParser ( 吉里吉里Z 本体組み込み版 ) からの拡張点:
- multiLineTagEnabled プロパティによるタグの複数行記述
( 行末に " \" を置き、次の行の先頭を ";" で始める )
- getNextTag() の返り値に taglist メンバ ( タグ名を記載順に格納した
配列 ) を追加
- パラメータマクロ展開機能 ( paramMacros プロパティ / pmacro ・
erasepmacro システムタグ )。登録済みのパラメータ名がタグ中に現れると、
そこに登録済みパラメータ列を差し込んだものとして処理されます
- emb タグに escape パラメータを追加。escape=false を指定すると
"[～]" 形式の評価結果をエスケープせず通常のタグとして評価します
- マクロ展開の「*」( 残りの全パラメータ ) より前に書かれたパラメータも
有効になります ( オリジナルでは上書きされて消える )

## メンバー一覧

### コンストラクタ

- [KAGParser](#kagparser)

### プロパティ

- [curStorage](#curstorage)
- [curLabel](#curlabel)
- [curLine](#curline)
- [curPos](#curpos)
- [curLineStr](#curlinestr)
- [processSpecialTags](#processspecialtags)
- [ignoreCR](#ignorecr)
- [debugLevel](#debuglevel)
- [macros](#macros)
- [paramMacros](#parammacros)
- [macroParams](#macroparams)
- [mp](#mp)
- [callStackDepth](#callstackdepth)
- [multiLineTagEnabled](#multilinetagenabled)

### メソッド

- [loadScenario](#loadscenario)
- [goToLabel](#gotolabel)
- [callLabel](#calllabel)
- [getNextTag](#getnexttag)
- [assign](#assign)
- [clear](#clear)
- [store](#store)
- [restore](#restore)
- [clearCallStack](#clearcallstack)
- [interrupt](#interrupt)
- [resetInterrupt](#resetinterrupt)

---

### KAGParser

コンストラクタ

**解説**

コンストラクタ（引数なし）

---

### curStorage

プロパティ \ アクセス: `r/w`

**解説**

現在解析中のシナリオのストレージ名。値を設定すると loadScenario() と同じ動作をする

---

### curLabel

プロパティ \ アクセス: `r`

**解説**

最後に通過したラベル名（読み取り専用）

---

### curLine

プロパティ \ アクセス: `r`

**解説**

現在解析中の行番号 ( 0 起点 )（読み取り専用）

---

### curPos

プロパティ \ アクセス: `r`

**解説**

現在解析中の行内の文字位置 ( 0 起点 )（読み取り専用）

---

### curLineStr

プロパティ \ アクセス: `r`

**解説**

現在解析中の行の内容（読み取り専用）

---

### processSpecialTags

プロパティ \ アクセス: `r/w`

**解説**

システムタグ ( if / macro / jump / emb など ) をパーサ内部で処理するか。

偽にするとこれらも通常のタグとして getNextTag() から返される。既定は真

---

### ignoreCR

プロパティ \ アクセス: `r/w`

**解説**

真にするとシナリオ中の改行を無視する ( "r" 擬似タグを返さない )。既定は偽

---

### debugLevel

プロパティ \ アクセス: `r/w`

**解説**

デバッグ出力のレベル。0 ( 出力しない )、1 ( 簡易 )、2 ( 詳細 ) のいずれか

---

### macros

プロパティ \ アクセス: `r`

**解説**

記録されているマクロの辞書 ( マクロ名 => マクロ内容の文字列 )（読み取り専用）

---

### paramMacros

プロパティ \ アクセス: `r`

**解説**

パラメータマクロの辞書（読み取り専用・KAGParserEx 拡張）。

「パラメータ名 => [ パラメータ名, 値, パラメータ名, 値, ... ]」の形で
登録すると、タグ中に登録済みパラメータ名が現れたとき、そこに登録内容を
差し込んだものとして処理される。値の先頭の % や & は実行時に展開される。
pmacro / erasepmacro システムタグでも登録・削除できる

---

### macroParams

プロパティ \ アクセス: `r`

**解説**

現在実行中のマクロに渡された引数の辞書（読み取り専用）

---

### mp

プロパティ \ アクセス: `r`

**解説**

macroParams の別名（読み取り専用）

---

### callStackDepth

プロパティ \ アクセス: `r`

**解説**

callLabel() による呼び出しスタックの深さ（読み取り専用）

---

### multiLineTagEnabled

プロパティ \ アクセス: `r/w`

**解説**

タグの複数行記述を有効にするか ( KAGParserEx 拡張 )。既定は偽。

真にすると、行末に " \" ( 直前に 1 つ以上の空白が必要 ) を置き、
次の行の先頭を ";" で始めることで、タグを複数行に分けて記述できる。
タグ名は必ず 1 行目に記述する必要がある

---

### loadScenario

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 読み込むシナリオファイル ( .ks ) のストレージ名 |

**解説**

シナリオファイルを読み込む

解析位置はファイルの先頭になります。すでに同じストレージが
読み込まれている場合は再読み込みは行われません。

---

### goToLabel

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `label` | `&nbsp;` | 移動先のラベル名。"*ラベル名" のように先頭に * を付けて指定 |

**解説**

指定ラベルへ移動する

現在のシナリオファイル内の指定ラベル位置へ解析位置を移動します。

---

### callLabel

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `label` | `&nbsp;` | 移動先のラベル名。"*ラベル名" のように先頭に * を付けて指定 |

**解説**

呼び出しスタックに現在位置を積んでから指定ラベルへ移動する

return システムタグで呼び出し元の位置へ戻ることができます。
現在の呼び出しの深さは callStackDepth プロパティで取得できます。

---

### getNextTag

メソッド

**戻り値**

タグの情報が格納された辞書オブジェクト。シナリオ終端に達した
場合は void

**解説**

次のタグを取得する

タグ名が tagname メンバに、タグの属性が「属性名 => 値」の
形で格納されます。地の文は tagname="ch" ( text メンバに 1 文字 )、
改行は tagname="r" ( 行末では eol=true 付き ) の擬似タグとして返ります。
interrupt() による中断要求があった場合は tagname="interrupt" の擬似タグが
返ります。

KAGParserEx 拡張として、taglist メンバ ( その辞書に格納されたタグ名を
記載順に並べた配列 ) が追加されています。

返される辞書オブジェクトは KAGParser が内部で使い回すため、内容を保持
したい場合は複製してください。

---

### assign

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `src` | `&nbsp;` | 複製元の KAGParser オブジェクト |

**解説**

他の KAGParser オブジェクトの状態を複製する

---

### clear

メソッド

**解説**

状態をクリアする

読み込んだシナリオ・呼び出しスタック・マクロなどの状態を
初期状態に戻します。

---

### store

メソッド

**戻り値**

現在の状態 ( 解析位置・呼び出しスタック・マクロ等 ) を表す
辞書オブジェクト

**解説**

状態を辞書として取り出す

返された辞書を保存しておき、restore() に渡すことで状態を
復元できます。栞 ( セーブデータ ) への保存に利用できます。

---

### restore

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `dic` | `&nbsp;` | store() の返した辞書オブジェクト |

**解説**

store() で取り出した状態を復元する

---

### clearCallStack

メソッド

**解説**

呼び出しスタックをクリアする

callLabel() で積まれた呼び出しスタックをすべて破棄します。

---

### interrupt

メソッド

**解説**

解析の中断を要求する

次に getNextTag() がタグを返すタイミングで、通常のタグの
かわりに tagname="interrupt" の擬似タグが返ります。非同期イベント処理
などから解析ループを中断したい場合に使用します。

---

### resetInterrupt

メソッド

**解説**

interrupt() による中断要求を取り消す

---
