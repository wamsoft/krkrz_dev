# GdiPlus.Appearance

このクラスは複数のプラグインから拡張されています。

## プラグイン拡張: layerExDraw

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

---

### clear

メソッド

---

### addBrush

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `colorOrBrush` | `&nbsp;` |  |
| `ox` | `&nbsp;` |  |
| `oy` | `&nbsp;` |  |

---

### addPen

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `colorOrBrush` | `&nbsp;` |  |
| `widthOrOption` | `&nbsp;` |  |
| `ox` | `&nbsp;` |  |
| `oy` | `&nbsp;` |  |

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
