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

文字列描画方式を表します。値を設定することもできます。

値は以下のどちらかを指定します。

`**frGDI**      ` : GDI を使って文字を描画します

`**frFreeType** ` : FreeType を使って文字を描画します

FreeType を指定した場合、横書きにのみ対応しています。その他は未対応です。

このプロパティはスタティックです。Font.rasterizer を用いて値を設定してください。

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
