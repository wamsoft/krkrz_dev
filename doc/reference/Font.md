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

値は整数のインデックスで、利用可能な値と番号は**ビルドによって異なります**:

`**0**` : FreeType ラスタライザ ( 全ビルド。SDL / 汎用ビルドの既定 )

`**1**` ( WINVER のみ ) : GDI ラスタライザ ( WINVER の既定 )。SDL / 汎用ビルドでは
この番号が glyphware になります。

`**2**` ( WINVER ) / `**1**` ( 非 WINVER ) : glyphware ( 統一フォントエンジン。
FreeType + HarfBuzz )。GDI 既定を変えず、選択時のみ drawText のグリフ生成が glyphware
経由になります ( 埋め込みビットマップではなくアウトライン描画・カラー絵文字対応 )。
なお drawText 経路は 1 コードポイントずつの cell-stepping で**シェイピングは行いません**
( BiDi / 複雑スクリプトのシェイピングが必要な場合は
[Layer.drawGlyphwareText](Layer.md#drawglyphwaretext) を用います )。

FreeType / glyphware を指定した場合、横書きにのみ対応しています。その他は未対応です。

利用可能な番号は [System.buildVariantName](System.md#buildvariantname) で判定するか、
番号を設定してから読み戻して ( 設定が反映されない = 未対応 ) 検出できます。

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

---
