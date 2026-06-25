# RichTextRenderBase

TextRender 互換テキストレンダリングクラス

../textrender の TextRender クラスと API 互換のインターフェースを提供します。
内部では richtext ライブラリ（StyledLayout）を使用して描画を行います。

TextRender のエスケープ記法入りテキストを受け取り、レイアウト結果を
文字情報・タイミング情報・リンク情報として返します。

入力用特殊テキスト書式:
\n      改行
\t      タブ文字
\i      インデント開始（次行から）※非対応
\r      インデント解除（次行から）※非対応
\w      空白相当分表示位置を進める
\k      キー入力待ち情報を生成
\x      nul文字相当
\文字   エスケープ指定（特殊機能を無効化）
[xxxx]         ルビ指定（次の1文字にかかる）
[xxxx,文字数]  ルビ指定（次の指定個数の文字にかかる）

フォント指定:
%f名前;     フォントフェイス指定
%bX         ボールド指定（0:off 1:on その他:デフォルト）
%iX         イタリック指定（0:off 1:on その他:デフォルト）
%sX         影指定（0:off 1:on その他:デフォルト）
%eX         エッジ指定（0:off 1:on その他:デフォルト）
%数値;      フォントサイズ指定（デフォルトに対するパーセント）
%B          大サイズフォント
%S          小サイズフォント
#xxxxxx;    色指定（16進RGB）
%s#xxxxxx;  影色指定
%e#xxxxxx;  エッジ色指定
%r          フォントリセット

スタイル指定:
%C          センタリング
%R          右よせ
%L          左寄せ
%p数値;     ピッチ（字間）

特殊指定:
%d数値;     文字あたり表示時間（標準に対するパーセント、100で標準速度）
%a数値;     文字あたり表示時間（ms）
%w数値;     時間待ち（1文字時間に対するパーセント、100で1文字分）
%t数値;     時間待ち（ms）
%D数値;     時間同期指定（ms）
%D$xxx;     時間同期指定（ラベル参照）

$xxx;       埋め込み指定（変数名）※onEval で処理
&xxx;       グラフィック文字指定（画像名）※onGetGraphSize で処理

リンク指定:
%lリンク名;  リンク指定開始
%l;          リンク指定解除

非対応:
縦書き、rubyoffset、ワードブレーク制御（%k0/%k1）

使用フロー:
clear() → setFont/setStyle → render() [複数回可] → done()
→ getCharacters() / calcShowCount() / getKeyWait() 等で結果取得

使用例:
var tr = new TextRenderBase();
tr.setDefault(%[ face: "MSゴシック", fontsize: 24, color: 0xFFFFFF ]);
tr.setRenderSize(400, 300);
tr.clear();
tr.render("こんにちは%B世界%r！\n2行目", 0, 30, 0, false);
tr.done();

var chars = tr.getCharacters(0, 0);  // 全文字情報取得
var count = tr.calcShowCount(500);    // 500ms時点の表示文字数

## メンバー一覧

### プロパティ

- [timeScale](#timescale)
- [fontScale](#fontscale)
- [defaultFace](#defaultface)
- [defaultFontSize](#defaultfontsize)
- [defaultBigFontSize](#defaultbigfontsize)
- [defaultSmallFontSize](#defaultsmallfontsize)
- [defaultLineSize](#defaultlinesize)
- [defaultLineSpacing](#defaultlinespacing)
- [defaultPitch](#defaultpitch)
- [defaultAlign](#defaultalign)
- [defaultValign](#defaultvalign)
- [defaultRubySize](#defaultrubysize)
- [defaultColor](#defaultcolor)
- [defaultShadow](#defaultshadow)
- [defaultShadowColor](#defaultshadowcolor)
- [defaultEdge](#defaultedge)
- [defaultEdgeColor](#defaultedgecolor)
- [defaultBold](#defaultbold)
- [defaultItalic](#defaultitalic)
- [renderOver](#renderover)
- [renderLines](#renderlines)
- [renderCount](#rendercount)
- [renderDelay](#renderdelay)
- [renderLeft](#renderleft)
- [renderTop](#rendertop)
- [renderRight](#renderright)
- [renderBottom](#renderbottom)
- [renderText](#rendertext)

### メソッド

- [TextRenderBase](#textrenderbase)
- [setOption](#setoption)
- [setDefault](#setdefault)
- [setRenderSize](#setrendersize)
- [clear](#clear)
- [setFont](#setfont)
- [resetFont](#resetfont)
- [setStyle](#setstyle)
- [resetStyle](#resetstyle)
- [render](#render)
- [newline](#newline)
- [done](#done)
- [onEval](#oneval)
- [onLabel](#onlabel)
- [onGetGraphSize](#ongetgraphsize)
- [getKeyWait](#getkeywait)
- [calcShowCount](#calcshowcount)
- [calcLineOffset](#calclineoffset)
- [getCharacters](#getcharacters)
- [getLinkNames](#getlinknames)
- [getLinkRects](#getlinkrects)
- [getLinkCharacters](#getlinkcharacters)
- [isLinkContains](#islinkcontains)
- [getLinkOfPosition](#getlinkofposition)
- [drawToLayer](#drawtolayer)

---

### timeScale

プロパティ \ アクセス: `r/w`

**解説**

レンダリング時間補正

---

### fontScale

プロパティ \ アクセス: `r/w`

**解説**

フォントサイズ補正倍率

---

### defaultFace

プロパティ \ アクセス: `r/w`

**解説**

デフォルト値プロパティ

---

### defaultFontSize

プロパティ \ アクセス: `r/w`

---

### defaultBigFontSize

プロパティ \ アクセス: `r/w`

---

### defaultSmallFontSize

プロパティ \ アクセス: `r/w`

---

### defaultLineSize

プロパティ \ アクセス: `r/w`

---

### defaultLineSpacing

プロパティ \ アクセス: `r/w`

---

### defaultPitch

プロパティ \ アクセス: `r/w`

---

### defaultAlign

プロパティ \ アクセス: `r/w`

---

### defaultValign

プロパティ \ アクセス: `r/w`

---

### defaultRubySize

プロパティ \ アクセス: `r/w`

---

### defaultColor

プロパティ \ アクセス: `r/w`

---

### defaultShadow

プロパティ \ アクセス: `r/w`

---

### defaultShadowColor

プロパティ \ アクセス: `r/w`

---

### defaultEdge

プロパティ \ アクセス: `r/w`

---

### defaultEdgeColor

プロパティ \ アクセス: `r/w`

---

### defaultBold

プロパティ \ アクセス: `r/w`

---

### defaultItalic

プロパティ \ アクセス: `r/w`

---

### renderOver

プロパティ \ アクセス: `r/w`

**解説**

/ レンダリング結果が領域をはみ出ているかどうか

---

### renderLines

プロパティ \ アクセス: `r/w`

**解説**

/ レンダリング結果の行数

---

### renderCount

プロパティ \ アクセス: `r/w`

**解説**

/ レンダリング結果の文字数

---

### renderDelay

プロパティ \ アクセス: `r/w`

**解説**

/ レンダリング結果の総表示時間

---

### renderLeft

プロパティ \ アクセス: `r/w`

**解説**

/ レンダリング結果領域情報

---

### renderTop

プロパティ \ アクセス: `r/w`

---

### renderRight

プロパティ \ アクセス: `r/w`

---

### renderBottom

プロパティ \ アクセス: `r/w`

---

### renderText

プロパティ \ アクセス: `r/w`

**解説**

/ レンダリング結果テキスト（エスケープ除去済み）

---

### TextRenderBase

メソッド

**解説**

コンストラクタ

---

### setOption

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `elm` | `&nbsp;` | 辞書 |

**解説**

レンダリングオプションの設定

設定可能なキー:
ignore_color  色指定を無視
ignore_size   サイズ指定を無視
ignore_type   フォント種別指定を無視（bold/italic/shadow/edge）
ignore_face   フォントフェイス指定を無視
ignore_style  スタイル指定を無視（align/pitch）
ignore_ruby   ルビ指定を無視
ignore_delay  時間指定を無視
width_time_scale  文字幅による時間補正（0:しない 1:する）
locale        ロケール文字列（例: "ja_JP"）

---

### setDefault

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `elm` | `&nbsp;` | 辞書 |

**解説**

デフォルト値の設定

辞書に含まれるキーのみが反映される（含まれないキーは現在値を維持）。
setDefault 呼び出し後は内部で resetFont() / resetStyle() 相当の処理が走り、
現在のフォント・スタイル状態がデフォルト値に同期される。

設定可能なキー:
face          フォントフェイス
registerCollection で登録したコレクション名のほか、
registerFont の登録名、フォントファイル内の family 名
（例: "Noto Sans JP"）、"family Style" 連結名
（例: "Noto Sans JP Bold"）でも指定可能。
fontsize      フォントサイズ
bigfontsize   大サイズフォントサイズ（%B 用）
smallfontsize 小サイズフォントサイズ（%S 用）
bold          太字
italic        イタリック
color         文字色（RGB）
shadow        影指定
shadowcolor   影色
edge          縁指定
edgecolor     縁色
linespacing   行間
pitch         文字間
linesize      行サイズ
align         水平アライン（-1:左 0:中央 1:右）
valign        垂直アライン（-1:上 0:中央 1:下）
rubysize      ルビサイズ

---

### setRenderSize

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `width` | `&nbsp;` | 領域横幅（0で無制限） |
| `height` | `&nbsp;` | 領域縦幅（0で無制限） |

**解説**

レンダリング領域のサイズ指定

---

### clear

メソッド

**解説**

レンダリング結果の消去

---

### setFont

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `elm` | `&nbsp;` | 辞書 |

**解説**

フォント指定

設定可能なキー:
face, fontsize, bold, italic, color, shadow, shadowcolor, edge, edgecolor

---

### resetFont

メソッド

**解説**

フォント状態をデフォルトに戻す

---

### setStyle

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `elm` | `&nbsp;` | 辞書 |

**解説**

スタイル指定

設定可能なキー:
linespacing, pitch, linesize, align, valign

---

### resetStyle

メソッド

**解説**

スタイル指定をデフォルトに戻す

---

### render

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `str` | `&nbsp;` | レンダリングする文字列（エスケープ記法含む） |
| `autoIndent` | `0` | 自動インデント指定（0:無効 1:有効 -1:逆字下げ）※現在非対応 |
| `diff` | `0` | 一文字当たり表示時間（ms） |
| `all` | `0` | 総時間指定（0は自動、ms） |
| `noResetDelay` | `false` | true だと以前の表示時間を維持する |

**戻り値**

はみ出ることなくレンダリングに成功したら true

**解説**

テキストのレンダリング

clear() 後に複数回呼び出せます。done() を呼ぶまで結果は確定しません。

---

### newline

メソッド

**解説**

新規行にする

---

### done

メソッド

**解説**

レンダリング完了

render() で蓄積したテキストを一括でレイアウトし、
タイミング・リンク等の情報を確定します。

---

### onEval

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 変数名 |

**戻り値**

変数値（文字列）

**解説**

レンダリング中の変数参照処理

$xxx; 記法で参照されたときに呼ばれます。
継承して上書き可能。

---

### onLabel

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` | ラベル名 |

**戻り値**

tick値（ms）

**解説**

レンダリング中のラベル参照処理

%D$xxx; 記法で参照されたときに呼ばれます。

---

### onGetGraphSize

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 画像名 |

**戻り値**

%[width: 横幅, height: 縦幅]

**解説**

グラフィック文字のサイズ情報取得

&xxx; 記法で参照されたときに呼ばれます。

---

### getKeyWait

メソッド

**戻り値**

[%[pos: 文字位置, time: 時間], ...]

**解説**

キー待ち情報の配列を返す

---

### calcShowCount

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `time` | `&nbsp;` | 時間（ms） |

**戻り値**

表示文字数

**解説**

指定時間での表示文字数を返す

---

### calcLineOffset

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `lineno` | `&nbsp;` | 行番号 |

**戻り値**

オフセット値

**解説**

指定行のオフセット値を返す

---

### getCharacters

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `start` | `&nbsp;` | 開始文字位置 |
| `num` | `&nbsp;` | 取得文字数（0で末尾まで） |

**戻り値**

描画情報の配列

**解説**

レンダリング結果文字情報の取得

各要素は辞書で以下のキーを持ちます:
text       表示するテキスト
graph      グラフィック表示時の画像名（通常文字は void）
x          表示座標X
y          表示座標Y
cw         表示幅
size       フォントサイズ
face       フォントフェイス
color      表示色
bold       BOLD指定
italic     ITALIC指定
shadow     影指定
edge       縁指定
shadowColor  影の色
edgeColor    縁の色
delay      表示タイミング（表示開始時からの経過時間）
link       リンク番号（無い場合は-1）
linkName   リンク名（無い場合は void）
ruby       ルビ配列 [%[text, x, y, size], ...]

---

### getLinkNames

メソッド

**戻り値**

リンク名の配列（重複する名前もそのまま列挙）

**解説**

含まれるリンク名の一覧を返す

---

### getLinkRects

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `link` | `&nbsp;` | リンク番号 |

**戻り値**

領域情報の配列 [%[left, top, width, height], ...]

**解説**

リンクの領域情報を取得

複数行にまたがる場合は複数の矩形が返ります

---

### getLinkCharacters

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `link` | `&nbsp;` | リンク番号 |

**戻り値**

描画情報の配列（getCharacters と同形式）

**解説**

リンクに属する文字情報を取得

---

### isLinkContains

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `link` | `&nbsp;` | リンク番号 |
| `x` | `&nbsp;` | X位置 |
| `y` | `&nbsp;` | Y位置 |

**戻り値**

リンク中に含まれているなら true

**解説**

リンク中に含まれるかどうかの判定

---

### getLinkOfPosition

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | X位置 |
| `y` | `&nbsp;` | Y位置 |

**戻り値**

リンク番号（-1:なし）

**解説**

指定位置のリンク番号を返す

---

### drawToLayer

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 描画先レイヤーオブジェクト |
| `x` | `&nbsp;` | 描画開始X座標 |
| `y` | `&nbsp;` | 描画開始Y座標 |
| `maxChars` | `-1` | 描画する文字数の上限（-1で全て、省略時: -1） |

**戻り値**

描画領域の配列 [x, y, width, height]

**解説**

レンダリング結果をレイヤーに描画

done() で確定したレンダリング結果を指定レイヤーに描画します。
maxChars を指定することで文字送りアニメーションが実現できます。

使用例:
tr.render("テキスト", 0, 50, 0);
tr.done();
tr.drawToLayer(layer, 10, 10);

// 文字送り
var count = tr.calcShowCount(elapsed);
tr.drawToLayer(layer, 10, 10, count);

---
