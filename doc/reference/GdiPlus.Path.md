# GdiPlus.Path

このクラスは複数のプラグインから拡張されています。

## プラグイン拡張: layerExDraw

### メンバー一覧

#### コンストラクタ

- [Path](#path)

#### メソッド

- [startFigure](#startfigure)
- [closeFigure](#closefigure)
- [drawArc](#drawarc)
- [drawPie](#drawpie)
- [drawBezier](#drawbezier)
- [drawBeziers](#drawbeziers)
- [drawClosedCurve](#drawclosedcurve)
- [drawClosedCurve2](#drawclosedcurve2)
- [drawCurve](#drawcurve)
- [drawCurve2](#drawcurve2)
- [drawCurve3](#drawcurve3)
- [drawEllipse](#drawellipse)
- [drawLine](#drawline)
- [drawLines](#drawlines)
- [drawPolygon](#drawpolygon)
- [drawRectangle](#drawrectangle)
- [drawRectangles](#drawrectangles)

---

### Path

コンストラクタ

**解説**

パス情報クラス

---

### startFigure

メソッド

**解説**

現在の図形を閉じずに次の図形を開始します

---

### closeFigure

メソッド

**解説**

現在の図形を閉じます

---

### drawArc

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 左上座標 |
| `y` | `&nbsp;` | 左上座標 |
| `width` | `&nbsp;` | 横幅 |
| `height` | `&nbsp;` | 縦幅 |
| `startAngle` | `&nbsp;` | 時計方向円弧開始位置 |
| `sweepAngle` | `&nbsp;` | 描画角度 |

**解説**

円弧の描画

---

### drawPie

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 左上座標 |
| `y` | `&nbsp;` | 左上座標 |
| `width` | `&nbsp;` | 横幅 |
| `height` | `&nbsp;` | 縦幅 |
| `startAngle` | `&nbsp;` | 時計方向円弧開始位置 |
| `sweepAngle` | `&nbsp;` | 描画角度 |

**解説**

円錐の描画

---

### drawBezier

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x1` | `&nbsp;` |  |
| `y1` | `&nbsp;` |  |
| `x2` | `&nbsp;` |  |
| `y2` | `&nbsp;` |  |
| `x3` | `&nbsp;` |  |
| `y3` | `&nbsp;` |  |
| `x4` | `&nbsp;` |  |
| `y4` | `&nbsp;` |  |

**解説**

ベジェ曲線の描画

---

### drawBeziers

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 点の配列 [ [x1, y1], [x2, y2] .... ] |

**解説**

連続ベジェ曲線の描画

---

### drawClosedCurve

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 点の配列 [ [x1, y1], [x2, y2] .... ] |

**解説**

Closed cardinal spline の描画

---

### drawClosedCurve2

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 点の配列 [ [x1, y1], [x2, y2] .... ] |
| `tension` | `&nbsp;` | テンション |

**解説**

Closed cardinal spline の描画

---

### drawCurve

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 点の配列 [ [x1, y1], [x2, y2] .... ] |

**解説**

cardinal spline の描画

---

### drawCurve2

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 点の配列 [ [x1, y1], [x2, y2] .... ] |
| `tension` | `&nbsp;` | テンション |

**解説**

cardinal spline の描画

---

### drawCurve3

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 点の配列 [ [x1, y1], [x2, y2] .... ] |
| `offset` | `&nbsp;` |  |
| `numberOfSegments` | `&nbsp;` |  |
| `tension` | `&nbsp;` | テンション |

**解説**

cardinal spline の描画

---

### drawEllipse

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `width` | `&nbsp;` |  |
| `height` | `&nbsp;` |  |

**解説**

楕円の描画

---

### drawLine

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x1` | `&nbsp;` | 始点X座標 |
| `y1` | `&nbsp;` | 始点Y座標 |
| `x2` | `&nbsp;` | 終点X座標 |
| `y2` | `&nbsp;` | 終点Y座標 |

**解説**

線分の描画

---

### drawLines

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 点の配列 [ [x1, y1], [x2, y2] .... ] |

**解説**

連続線分の描画

---

### drawPolygon

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 点の配列 [ [x1, y1], [x2, y2] .... ] |

**解説**

多角形の描画

---

### drawRectangle

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `width` | `&nbsp;` |  |
| `height` | `&nbsp;` |  |

**解説**

矩形の描画

---

### drawRectangles

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `rects` | `&nbsp;` | 矩形の配列 [ [x1, y1, width1, height1], [x2, y2, width2, height2] .... ] |

**解説**

複数矩形の描画

---

## プラグイン拡張: layerExVector

### メンバー一覧

#### コンストラクタ

- [Path](#path)

#### メソッド

- [startFigure](#startfigure)
- [closeFigure](#closefigure)
- [drawArc](#drawarc)
- [drawPie](#drawpie)
- [drawBezier](#drawbezier)
- [drawBeziers](#drawbeziers)
- [drawClosedCurve](#drawclosedcurve)
- [drawClosedCurve2](#drawclosedcurve2)
- [drawCurve](#drawcurve)
- [drawCurve2](#drawcurve2)
- [drawCurve3](#drawcurve3)
- [drawEllipse](#drawellipse)
- [drawLine](#drawline)
- [drawLines](#drawlines)
- [drawPolygon](#drawpolygon)
- [drawRectangle](#drawrectangle)
- [drawRectangles](#drawrectangles)

---

### Path

コンストラクタ

**解説**

パス情報クラス

---

### startFigure

メソッド

**解説**

現在の図形を閉じずに次の図形を開始します

---

### closeFigure

メソッド

**解説**

現在の図形を閉じます

---

### drawArc

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 左上座標 |
| `y` | `&nbsp;` | 左上座標 |
| `width` | `&nbsp;` | 横幅 |
| `height` | `&nbsp;` | 縦幅 |
| `startAngle` | `&nbsp;` | 時計方向円弧開始位置 |
| `sweepAngle` | `&nbsp;` | 描画角度 |

**解説**

円弧の描画

---

### drawPie

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 左上座標 |
| `y` | `&nbsp;` | 左上座標 |
| `width` | `&nbsp;` | 横幅 |
| `height` | `&nbsp;` | 縦幅 |
| `startAngle` | `&nbsp;` | 時計方向円弧開始位置 |
| `sweepAngle` | `&nbsp;` | 描画角度 |

**解説**

円錐の描画

---

### drawBezier

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x1` | `&nbsp;` |  |
| `y1` | `&nbsp;` |  |
| `x2` | `&nbsp;` |  |
| `y2` | `&nbsp;` |  |
| `x3` | `&nbsp;` |  |
| `y3` | `&nbsp;` |  |
| `x4` | `&nbsp;` |  |
| `y4` | `&nbsp;` |  |

**解説**

ベジェ曲線の描画

---

### drawBeziers

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 点の配列 [ [x1, y1], [x2, y2] .... ] |

**解説**

連続ベジェ曲線の描画

---

### drawClosedCurve

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 点の配列 [ [x1, y1], [x2, y2] .... ] |

**解説**

Closed cardinal spline の描画

---

### drawClosedCurve2

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 点の配列 [ [x1, y1], [x2, y2] .... ] |
| `tension` | `&nbsp;` | テンション |

**解説**

Closed cardinal spline の描画

---

### drawCurve

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 点の配列 [ [x1, y1], [x2, y2] .... ] |

**解説**

cardinal spline の描画

---

### drawCurve2

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 点の配列 [ [x1, y1], [x2, y2] .... ] |
| `tension` | `&nbsp;` | テンション |

**解説**

cardinal spline の描画

---

### drawCurve3

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 点の配列 [ [x1, y1], [x2, y2] .... ] |
| `offset` | `&nbsp;` |  |
| `numberOfSegments` | `&nbsp;` |  |
| `tension` | `&nbsp;` | テンション |

**解説**

cardinal spline の描画

---

### drawEllipse

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `width` | `&nbsp;` |  |
| `height` | `&nbsp;` |  |

**解説**

楕円の描画

---

### drawLine

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x1` | `&nbsp;` | 始点X座標 |
| `y1` | `&nbsp;` | 始点Y座標 |
| `x2` | `&nbsp;` | 終点X座標 |
| `y2` | `&nbsp;` | 終点Y座標 |

**解説**

線分の描画

---

### drawLines

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 点の配列 [ [x1, y1], [x2, y2] .... ] |

**解説**

連続線分の描画

---

### drawPolygon

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 点の配列 [ [x1, y1], [x2, y2] .... ] |

**解説**

多角形の描画

---

### drawRectangle

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `width` | `&nbsp;` |  |
| `height` | `&nbsp;` |  |

**解説**

矩形の描画

---

### drawRectangles

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `rects` | `&nbsp;` | 矩形の配列 [ [x1, y1, width1, height1], [x2, y2, width2, height2] .... ] |

**解説**

複数矩形の描画

---
