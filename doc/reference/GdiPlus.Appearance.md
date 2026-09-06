# GdiPlus.Appearance

このクラスは複数のプラグインから拡張されています。

## プラグイン拡張: layerExDraw

描画外観情報

Illustrator のアピアランスをイメージしてください。
描画に対して、複数のブラシ（塗り）とペン（線）を指定できます。
先に追加した方が下に入ります

### メンバー一覧

#### コンストラクタ

- [Appearance](#appearance)

#### メソッド

- [clear](#clear)
- [addBrush](#addbrush)
- [addPen](#addpen)

---

### Appearance

コンストラクタ

**解説**

コンストラクタ

---

### clear

メソッド

**解説**

情報のクリア

---

### addBrush

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `colorOrBrush` | `&nbsp;` | ARGB色指定またはブラシ情報（辞書） |
| `ox` | `&nbsp;` | 表示オフセットX |
| `oy` | `&nbsp;` | 表示オフセットY |

**解説**

ブラシの追加

ブラシ情報定義
基本  点指定は [x,y] の配列または %[x:x, y:y] の辞書
矩形指定は [x,y,width,height] の配列または %[x:x, y:y, width:w, height:h] の辞書
色指定は ARGB 32bit整数値
パラメータについては GDI+ のドキュメントを見て研究してください

type: ブラシ種別 BrushType で指定

BrushTypeSolidColor の場合 ※直接ARGBで色指定した場合と同じです
color: 色指定(未指定時は白)

BrushTypeHatchFill の場合
hatchStyle: ハッチの種類(未指定時は HatchStyleHorizontal)
foreColor: 前景色(未指定時は白)
backColor: 背景色(未指定時は黒)

BrushTypeTextureFill の場合
image: 画像指定
wrapMode: 繰り返しパターン指定(未指定時は WrapModeTile)
dstRect: テクスチャ領域矩形指定(未指定時は画像全部)

BrushTypePathGradient の場合
points: 点指定の配列
centerColor: 中心色
centerPoint: 中心点
focusScale: focus scales指定 [xScale,yScale] または %[xScale:, yScale:]
surroundColors: 周囲色指定。色の配列
---- 以下は BrushTypeLinearGradientでも共通
blend: ブレンドファクター指定。数値配列で [blendFactors, blendPositions] または辞書
blendBellShape: ブレンド形状指定(bell形状) [focus, scale]
blendTriangularShape: ブレンド形状指定(三角形状) [focus, scale]
gammaCorrection: ガンマ補正を有効にするかどうか true/false
interpolationColors: [presetColors(色配列), blendPositions(数値配列)]

BrushTypeLinearGradient の場合
共通
color1: 開始色指定
color2: 終了色指定
wrapMode: 繰り返しパターン指定(未指定時は WrapModeTile)
ポイント指定
point1: 開始点
point2: 終了点
※角度は自動で決まる模様
矩形指定
rect: ポイント指定。左上が開始、右下が終了
angle: 角度指定 (rect指定の場合だけ有効)
isAngleScalable (角度指定がスケーラブルかどうか)
mode: モード指定(省略時は LinearGradientModeHorizontal) angle 指定が無い場合に有効

---

### addPen

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `colorOrBrush` | `&nbsp;` | ARGB色指定またはブラシ情報（辞書） |
| `widthOrOption` | `&nbsp;` | ペン幅またはペン情報（辞書） |
| `ox` | `&nbsp;` | 表示オフセットX |
| `oy` | `&nbsp;` | 表示オフセットY |

**解説**

ペンの追加

ペン情報定義: widthOrOption が辞書の場合は詳細情報定義になります
パラメータについては GDI+ のドキュメントを見て研究してください

width: ペン幅指定
alignment: アラインメント：省略時は PenAlignmentCenter
compoundArray: compound array 指定。数値配列
dashCap: ダッシュの cap style の指定。省略時は DashCapFlat
dashOffset: ダッシュのオフセット指定。省略時は0
dashStyle: ダッシュスタイル。配列にするとユーザ定義(数値配列)。デフォルトは DasyStyleSolid
startCap: 開始位置の cap style の指定。省略時は LineCapFlat，辞書時はAdjustableArrowCap
endCap: 終了位置の cap style の指定。省略時は LineCapFlat，辞書時はAdjustableArrowCap
lineJoin: 結合形状指定。 省略時は LineJoinMiter
miterLimit: miter limit 指定（数値)

AdjustableArrowCap：LineCapArrowAnchorでは不満なあなたに
width(矢印幅), height(矢印高さ), filled(trueなら三角形，falseなら三又) が指定が可能

---

## プラグイン拡張: layerExVector

描画外観情報

Illustrator のアピアランスをイメージしてください。
描画に対して、複数のブラシ（塗り）とペン（線）を指定できます。
先に追加した方が下に入ります

### メンバー一覧

#### コンストラクタ

- [Appearance](#appearance)

#### メソッド

- [clear](#clear)
- [addBrush](#addbrush)
- [addPen](#addpen)

---

### Appearance

コンストラクタ

**解説**

コンストラクタ

---

### clear

メソッド

**解説**

情報のクリア

---

### addBrush

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `colorOrBrush` | `&nbsp;` | ARGB色指定またはブラシ情報（辞書） |
| `ox` | `0` | 表示オフセットX |
| `oy` | `0` | 表示オフセットY |

**解説**

ブラシの追加

ブラシ情報定義
基本  点指定は [x,y] の配列または %[x:x, y:y] の辞書
色指定は ARGB 32bit整数値

type: ブラシ種別 BrushType で指定

BrushTypeSolidColor の場合 ※直接ARGBで色指定した場合と同じです
color: 色指定(未指定時は白)

BrushTypePathGradient の場合 (RadialGradient として近似実装)
centerPoint: 中心点
centerColor: 中心色
radius: 半径(未指定時は100)

BrushTypeLinearGradient の場合
point1: 開始点
point2: 終了点
color1: 開始色指定
color2: 終了色指定

---

### addPen

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `colorOrBrush` | `&nbsp;` | ARGB色指定またはブラシ情報（辞書） |
| `widthOrOption` | `1.0` | ペン幅またはペン情報（辞書） |
| `ox` | `0` | 表示オフセットX |
| `oy` | `0` | 表示オフセットY |

**解説**

ペンの追加

ペン情報定義: widthOrOption が辞書の場合は詳細情報定義になります

width: ペン幅指定
startCap / endCap: cap style の指定。LineCap定数で指定。省略時は LineCapFlat
lineJoin: 結合形状指定。LineJoin定数で指定。省略時は LineJoinBevel
miterLimit: miter limit 指定（数値)
dashStyle: ダッシュパターン。数値の配列で指定
dashOffset: ダッシュのオフセット指定。省略時は0

---
