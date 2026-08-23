# Font

Font クラスは、**フォント**を管理するためのクラスです。

## メンバー一覧

### コンストラクタ

- [Font](#font)

### プロパティ

- [face](#face)
- [height](#height)
- [bold](#bold)
- [italic](#italic)
- [strikeout](#strikeout)
- [underline](#underline)
- [angle](#angle)
- [rasterizer](#rasterizer)
- [emojiMode](#emojimode)
- [weight](#weight)
- [variations](#variations)
- [defaultUseVarStyle](#defaultusevarstyle)
- [defaultEmojiMode](#defaultemojimode)
- [emojiFaceName](#emojifacename)
- [colorEmojiFaceName](#coloremojifacename)
- [defaultFaceName](#defaultfacename)
- [faceIsFileName](#faceisfilename)

### メソッド

- [getTextWidth](#gettextwidth)
- [getTextHeight](#gettextheight)
- [getEscWidthX](#getescwidthx)
- [getEscWidthY](#getescwidthy)
- [getEscHeightX](#getescheightx)
- [getEscHeightY](#getescheighty)
- [getGlyphDrawRect](#getglyphdrawrect)
- [getList](#getlist)
- [mapPrerenderedFont](#mapprerenderedfont)
- [unmapPrerenderedFont](#unmapprerenderedfont)
- [addFont](#addfont)
- [registerFontFile](#registerfontfile)
- [queryFonts](#queryfonts)
- [getFontInfo](#getfontinfo)
- [getVarAxes](#getvaraxes)

---

### Font

コンストラクタ

**解説**

コンストラクタ

Layerメンバのfontは、引数にLayerを渡す特殊版。
単体使用する場合は引数なしで生成する。

---

### face

プロパティ \ アクセス: `r/w`

**解説**

フォント名

フォント名を表します。値を設定することもできます。

カンマで区切って複数の候補を指定することができます。この場合は、実際に存在するフォントが使用され、先頭に書いたものほど優先されます。実際に存在するフォントかどうかは OS のフォントのリストを参照することにより行われます。どの候補にも合致しなかった場合は、デフォルトのフォントが使用されます (現バージョンでは "ＭＳ Ｐゴシック" 固定)。

先頭をカンマにし、直後にフォント名を書くと、実際にそのフォントをOSが列挙しなくても、OSにそのフォントを指定しようとします (たとえば ",My Original Font" )。これにより AddFontResource Win32 API 等で登録した列挙不可能なフォントを使用することができます。

---

### height

プロパティ \ アクセス: `r/w`

**解説**

フォント高さ

描画される文字の高さをピクセル単位で表します。値を設定することもできます。

---

### bold

プロパティ \ アクセス: `r/w`

**解説**

ボールド

ボールド ( 太字 ) であるかどうかを表します。値を設定することもできます。

真を指定するとボールドになります。

---

### italic

プロパティ \ アクセス: `r/w`

**解説**

イタリック

イタリック ( 斜体 ) であるかどうかを表します。値を設定することもできます。

真を指定するとイタリックになります。

---

### strikeout

プロパティ \ アクセス: `r/w`

**解説**

取消線

取消線を描画するかどうか表します。値を設定することもできます。

真を指定すると文字の上に取消線を描画します。

---

### underline

プロパティ \ アクセス: `r/w`

**解説**

アンダーライン

アンダーライン ( 下線または傍線 ) を描画するかどうか表します。値を設定することもできます。

真を指定するとアンダーラインを描画します。

---

### angle

プロパティ \ アクセス: `r/w`

**解説**

文字描画角度

文字描画角度を表します。値を設定することもできます。

単位は角度 ( degree ) の 10 倍の値です。0 ～ 3600 の値をとります。

縦書きを行う場合はフォント名に縦書き用のフォント名を指定した上で、このプロパティ
に 2700 を指定します。

---

### rasterizer

プロパティ \ アクセス: `r/w`

**解説**

文字列描画方式

[Layer.drawText](Layer.md#drawtext) で使用するラスタライザ ( 文字列描画方式 ) を
表します。値を設定することもできます。

値は整数のインデックスで、番号は**全ビルド共通**です:

`**0**` : FreeType ラスタライザ ( 全ビルドに搭載。SDL / 汎用ビルドの既定 )

`**1**` : GDI ラスタライザ ( WINVER のみ搭載。WINVER の既定 )

`**2**` : glyphware ( 統一フォントエンジン。FreeType + HarfBuzz )。既定を変えず、
選択時のみ drawText のグリフ生成が glyphware 経由になります ( 埋め込みビットマップ
ではなくアウトライン描画・カラー絵文字対応 )。
なお drawText 経路は 1 コードポイントずつの cell-stepping で**シェイピングは行いません**
( BiDi / 複雑スクリプトのシェイピングが必要な場合は
[Layer.drawShapedText](Layer.md#drawshapedtext) を用います )。

そのビルドに搭載されていない番号 ( 例: SDL / 汎用ビルドで 1 ) を設定した場合は
FreeType ( 0 ) へフォールバックし、読み戻すとフォールバック後の実効値が返ります。
このため「設定して読み戻し、値が一致しない = そのラスタライザは未搭載」で検出
できます。

FreeType / glyphware を指定した場合、横書きにのみ対応しています。その他は未対応です。

このプロパティはスタティックです。Font.rasterizer を用いて値を設定してください。

---

### emojiMode

プロパティ \ アクセス: `r/w`

**解説**

絵文字の描画モード

該当するコードポイントを絵文字フォントにフォールバックして描画するモードを
表します。値を設定することもできます。

`**-1** ` : グローバル既定 ( `Font.defaultEmojiMode` ) に従う ( 既定 )

`** 0** ` : 絵文字フォントを使わない ( 元フォントのみ )

`** 1** ` : モノクロ絵文字フォントで描画する

`** 2** ` : カラー絵文字フォントで描画する

この機能は FreeType ラスタライザ ( `rasterizer` = 0 ) 使用時のみ有効です。
GDI ラスタライザ ( WINVER 既定 ) では効果がありません。

絵文字フォントは実行ファイルに標準で埋め込まれています ( モノクロ = Noto Emoji、
カラー = Noto Color Emoji )。`emojiFaceName` / `colorEmojiFaceName` と `addFont`
で任意の絵文字フォントに差し替えることもできます。

注: ★ や ❤ など元フォントにも字形があるコードポイントは、元フォント側が優先され
モノクロ表示になる場合があります。

これを文字単位で明示指定したい場合は、テキスト中で対象文字の直後に異体字
セレクタを付けます。**VS16** ( U+FE0F ) を付けるとその 1 文字だけ絵文字フォントを
優先し、**VS15** ( U+FE0E ) を付けると元フォント ( テキスト表示 ) を強制します。
( 例: "❤"+U+FE0F でカラー、"❤"+U+FE0E でモノクロ )。セレクタ無しでの自動判定
( Emoji_Presentation 既定 ) は行いません ( 高度な多言語処理は対象外 )。

---

### weight

プロパティ \ アクセス: `r/w`

**解説**

フォントウェイト ( バリアブルフォント )

フォントのウェイトを表します。値を設定することもできます。100〜900 の数値、
または void ( 未指定 = フォント既定 ) を指定します。

バリアブルフォントで `wght` 軸を持つ face に対して可変軸として効きます
( [variations](#variations) に `wght` を明示した場合はそちらが優先 )。

効くのは glyphware 経路 — [Layer.drawShapedText](Layer.md#drawshapedtext) 系
( 常時 ) と、[rasterizer](#rasterizer) = 2 のときの [Layer.drawText](Layer.md#drawtext)
— のみです。旧 FreeType / GDI ラスタライザでは無視されます ( 起動後 1 回警告 )。

---

### variations

プロパティ \ アクセス: `r/w`

**解説**

可変軸指定 ( バリアブルフォント )

バリアブルフォントの可変軸を `"wght=700,wdth=87.5"` 形式で指定します。
値を設定することもできます。void または空文字列でクリアします。

設定時に正規化されます: タグは小文字化、タグ昇順に並べ替え、同タグは後勝ち、
値は量子化 ( `wght` は 1 刻み、その他の軸は 0.5 刻み — 軸アニメーションで
キャッシュが際限なく増えないため )。不正な書式は例外になります。

実際に適用されるのは「フォールバック連鎖の各 face が実際に持つ同名軸」だけです。
利用できる軸は [getVarAxes](#getvaraxes) で調べられます。適用範囲 ( glyphware
経路のみ ) は [weight](#weight) と同じです。

---

### defaultUseVarStyle

プロパティ \ アクセス: `r/w`

**解説**

bold / italic の可変軸マッピング ( クラスプロパティ )

真にすると、`bold` / `italic` 指定を可変軸で表現できる face ( `wght` /
`slnt` / `ital` 軸を持つバリアブルフォント ) では、合成ボールド / 合成
イタリックの代わりに軸 ( wght=700 / slnt=-10 / ital=1 ) を使い、二重適用を
防ぐため合成スタイルを無効化します。既定は偽 ( 既存の見た目を変えないため )。

軸の有無はフォールバック連鎖の先頭 ( primary ) face で判定されます。
glyphware 経路でのみ効きます。

---

### defaultEmojiMode

プロパティ \ アクセス: `r/w`

**型**: `Integer`

**解説**

絵文字描画モードのグローバル既定

`emojiMode` が -1 のフォントに適用される既定の絵文字描画モードを取得 / 設定します。
値は `emojiMode` と同じ ( 0 = 使わない / 1 = モノクロ / 2 = カラー )。
このプロパティはスタティックです。

---

### emojiFaceName

プロパティ \ アクセス: `r/w`

**型**: `String`

**解説**

モノクロ絵文字フォールバックに使う face 名

`emojiMode` = 1 ( モノクロ ) のときに使用する絵文字フォントの face 名を
取得 / 設定します。既定は埋め込みの Noto Emoji ( "Noto Emoji Regular" )。
`addFont` で登録した任意フォントの face 名を指定できます。
このプロパティはスタティックです。

---

### colorEmojiFaceName

プロパティ \ アクセス: `r/w`

**型**: `String`

**解説**

カラー絵文字フォールバックに使う face 名

`emojiMode` = 2 ( カラー ) のときに使用する絵文字フォントの face 名を
取得 / 設定します。既定は埋め込みの Noto Color Emoji ( "Noto Color Emoji Regular" )。
カラー絵文字は COLRv0 / CBDT / sbix 形式に対応します ( COLRv1 は非対応 )。
このプロパティはスタティックです。

---

### defaultFaceName

プロパティ \ アクセス: `r/w`

**型**: `String`

**解説**

既定フォントの face 名

フォント未指定時に使用される既定フォントの face 名を取得 / 設定します。
クラス静的プロパティとして全レイヤから共有されます。

---

### faceIsFileName

プロパティ \ アクセス: `r/w`

**型**: `Boolean`

**解説**

face 名をファイル名として扱うかどうか

真にすると `face` プロパティに指定した名前をフォントファイル名として
開きます ( FreeType 使用時のみ有効 )。

注: このフラグを真にしたレイヤで IME を有効化した場合、IME の入力欄では
`DEFAULT_GUI_FONT` が使用されます。

---

### getTextWidth

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 横幅を得たい文字列を指定します。 |

**戻り値**

指定された文字列の横幅がピクセル単位で戻ります

**解説**

文字列の横幅を得る

このメソッドでは、現在のフォントの設定で指定の文字列を描画したときに必要な
横幅を得ることができます。

**関連:** [Font.getTextHeight](Font.md#gettextheight)

---

### getTextHeight

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 縦幅を得たい文字列を指定します。 |

**戻り値**

指定された文字列の縦幅がピクセル単位で戻ります

**解説**

文字列の縦幅を得る

このメソッドでは、このフォントで指定の文字列を描画したときに必要な縦幅を得ることができます。

**関連:** [Font.getTextWidth](Font.md#gettextwidth)

---

### getEscWidthX

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 文字の横方向への X 座標の移動量を得たい文字列を指定します。 |

**戻り値**

文字の横方向への X 座標の移動量がピクセル単位で戻ります

**解説**

文字の横方向への X 座標の移動量

現在のフォントの設定で指定された文字を描画したときに必要な文字描画位置の移動量を
得ることができます。

このメソッドでは、文字の描画方向に対して横 ( 左 ) に進んだときの X 座標上での移動量を
得ることができます。

**関連:** [Font.getEscWidthY](Font.md#getescwidthy) / [Font.getEscHeightX](Font.md#getescheightx) / [Font.getEscHeightY](Font.md#getescheighty)

---

### getEscWidthY

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 文字の横方向への Y 座標の移動量を得たい文字列を指定します。 |

**戻り値**

文字の横方向への Y 座標の移動量がピクセル単位で戻ります

**解説**

文字の横方向への Y 座標の移動量

現在のフォントの設定で指定された文字を描画したときに必要な文字描画位置の移動量を
得ることができます。

このメソッドでは、文字の描画方向に対して横 ( 左 ) に進んだときの Y 座標上での移動量を
得ることができます。

**関連:** [Font.getEscWidthX](Font.md#getescwidthx) / [Font.getEscHeightX](Font.md#getescheightx) / [Font.getEscHeightY](Font.md#getescheighty)

---

### getEscHeightX

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 文字の縦方向への X 座標の移動量を得たい文字列を指定します。 |

**戻り値**

文字の縦方向への X 座標の移動量がピクセル単位で戻ります

**解説**

文字の縦方向への X 座標の移動量

現在のフォントの設定で指定された文字を描画したときに必要な文字描画位置の移動量を
得ることができます。

このメソッドでは、文字の描画方向に対して縦 ( 下 ) に進んだときの X 座標上での移動量を
得ることができます。

**関連:** [Font.getEscWidthX](Font.md#getescwidthx) / [Font.getEscWidthY](Font.md#getescwidthy) / [Font.getEscHeightY](Font.md#getescheighty)

---

### getEscHeightY

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 文字の縦方向への Y 座標の移動量を得たい文字列を指定します。 |

**戻り値**

文字の縦方向への Y 座標の移動量がピクセル単位で戻ります

**解説**

文字の縦方向への Y 座標の移動量

現在のフォントの設定で指定された文字を描画したときに必要な文字描画位置の移動量を
得ることができます。

このメソッドでは、文字の描画方向に対して縦 ( 下 ) に進んだときの Y 座標上での移動量を
得ることができます。

**関連:** [Font.getEscWidthX](Font.md#getescwidthx) / [Font.getEscWidthY](Font.md#getescwidthy) / [Font.getEscHeightX](Font.md#getescheightx)

---

### getGlyphDrawRect

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 範囲を得たい文字列を指定します。 |

**戻り値**

文字列の実描画範囲

**解説**

文字列の実描画範囲

現在のフォントの設定で指定された文字を描画したときに、グリフ画像が描かれる範囲を得ることができます。

得られる範囲は 0,0 座標を基準にした Rect クラスのオブジェクトです。

横向きのみ対応しています。

**関連:** [Rect](Rect.md)

---

### getList

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `flags` | `&nbsp;` | フォントをどのように列挙するかを指定します。<br>次の値のビット論理和による組み合わせ指定します。<br>`**fsfFixedPitch**    ` : 固定ピッチフォントのみ列挙します<br>`**fsfSameCharSet**   ` : 同じキャラクタセットのフォントのみ列挙します<br>`**fsfNoVertical**    ` : 縦書き用フォントを列挙しません<br>`**fsfTrueTypeOnly**  ` : TrueType フォントのみ列挙します<br>`**fsfIgnoreSymbol**  ` : シンボルキャラセットを除外します<br>fsfSameCharSet を指定した場合は、現在選択されているフォントと同じキャラクタセットの<br>フォントが列挙されます。 |

**戻り値**

フォント名(文字列)が各要素として格納されている配列

**解説**

フォント名の列挙

フォント名を列挙し、配列として返します。

---

### mapPrerenderedFont

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `fontstorage` | `&nbsp;` | レンダリング済みフォントストレージを指定します。 |

**解説**

レンダリング済みフォントの割り当て

現在選択されているフォント名に対して**レンダリング済みフォント**の割り当てを行います。

以降、同じ設定のフォントに対しては指定されたレンダリング済みフォントが代わりに使われます。

すべてのレイヤに対して設定が有効になります。

**関連:** [Font.unmapPrerenderedFont](Font.md#unmapprerenderedfont)

---

### unmapPrerenderedFont

メソッド

**解説**

レンダリング済みフォントの割り当て解除

現在選択されているフォント名に対する**レンダリング済みフォント**の割り当てを解除します。

**関連:** [Font.mapPrerenderedFont](Font.md#mapprerenderedfont)

---

### addFont

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | フォントファイル名 |

**戻り値**

ファイルに入っているフェイス名を配列で返す。

**解説**

フォントシステムにフォントを追加する。

---

### registerFontFile

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | フォントファイル名 |
| `family` | `&nbsp;` | 登録するフォント名 ( 省略時は即時ロード ) |

**戻り値**

family 省略時は収録フェイス名の配列、指定時は void

**解説**

フォントを登録する (遅延登録対応版)。

`family` を省略すると `addFont` と同様にフォントファイルを即座に読み込み、
収録フェイス名の配列を返します。

`family` を指定すると **ファイルを開かずに名前だけを登録**します
( `fonts.json` の 1 エントリ相当の遅延登録 )。実ファイルは
その名前が初めて使用されたときに読み込まれます。大きなフォントを
起動時間に影響させずに登録したい場合に使用します。

---

### queryFonts

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `query` | `&nbsp;` | 検索条件の辞書 ( 省略可 ) |

**戻り値**

該当フォント情報 ( 辞書 ) の配列

**解説**

登録済みフォントをリッチ検索する。

`fonts.json` 宣言・`addFont`/`registerFontFile` による実行時登録の
フォントから、条件に合う face をランク順 ( 一致度の高い順 ) で返します。
検索条件はすべて省略可能で、省略した項目は制約しません。
引数自体を省略すると全登録フォントを返します。

+ `name` : フォント名 ( family / 別名 / fullName / PostScript 名 )
+ `weight` : ウェイト ( 100〜900、400=Regular / 700=Bold )
+ `slant` : 0=normal, 1=italic, 2=oblique
+ `italic` : 真ならイタリック ( slant の簡易指定 )
+ `script` : ISO-15924 スクリプトタグ ( 例 "Jpan" "Hans" "Zsye" )
+ `containsText` : この文字列の全コードポイントを収録していること
+ `monospace` : 等幅かどうか
+ `color` : カラー絵文字フォントかどうか

返る配列の各要素は `getFontInfo` と同じ形式の辞書です。

---

### getFontInfo

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `nameOrPath` | `&nbsp;` | フォント名またはストレージパス |

**戻り値**

メタデータ辞書 ( 解決できなければ void )

**解説**

フォントのメタデータを取得する。

フォント名 ( 宣言名・SFNT 実名 ) またはストレージパスを解決し、
SFNT メタデータの辞書を返します。解決できない場合は void を返します。

辞書のメンバ:
+ `key` : フォントキー ( ストレージパス等 )
+ `faceIndex` : TTC 内の face 番号
+ `family` / `subfamily` / `fullName` / `postScriptName` : 名前情報
+ `weight` : 100〜900
+ `slant` : 0=normal, 1=italic, 2=oblique
+ `bold` / `color` / `monospace` / `scalable` : 属性 ( 0/1 )

バリアブルフォントの場合は次も入ります ( 非 VF では省略 ):
+ `axes` : 可変軸の配列 ( [getVarAxes](#getvaraxes) と同形式 )
+ `namedInstances` : fvar named instance の配列
`%[ name : "SemiBold", coords : %[ wght : 600, ... ] ]`

( `queryFonts` は「フォントを開かず宣言値で判定する」性質を守るため、
軸情報は返しません。軸は本メソッドか getVarAxes で取得してください )

---

### getVarAxes

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `nameOrPath` | `&nbsp;` | フォント名またはストレージパス |

**戻り値**

可変軸の配列 ( 解決できなければ void )

**解説**

バリアブルフォントの可変軸一覧を取得する。

フォント名 ( 宣言名・SFNT 実名 ) またはストレージパスを解決し、fvar の
可変軸を配列で返します。各要素は
`%[ tag : "wght", name : "Weight", min : 300, default : 400, max : 700 ]`
の辞書です。バリアブルフォントでなければ空配列、解決できない場合は void を
返します。

```tjs
var axes = Font.getVarAxes("MyFont");
for (var i = 0; i < axes.count; i++)
Debug.message(axes[i].tag + ": " + axes[i].min + ".." + axes[i].max);
```

---
