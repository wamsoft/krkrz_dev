# GdiPlus.Path

This class is extended by several plugins.

## Plugin extension: layerExDraw

### Members

#### Constructors

- [Path](#path)

#### Methods

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

Constructor

**Description**

Path class

---

### startFigure

Method

**Description**

Starts the next figure without closing the current one

---

### closeFigure

Method

**Description**

Closes the current figure

---

### drawArc

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | Top-left coordinate |
| `y` | `&nbsp;` | Top-left coordinate |
| `width` | `&nbsp;` | Width |
| `height` | `&nbsp;` | Height |
| `startAngle` | `&nbsp;` | Start angle of the arc, measured clockwise |
| `sweepAngle` | `&nbsp;` | Sweep angle |

**Description**

Draws an arc

---

### drawPie

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | Top-left coordinate |
| `y` | `&nbsp;` | Top-left coordinate |
| `width` | `&nbsp;` | Width |
| `height` | `&nbsp;` | Height |
| `startAngle` | `&nbsp;` | Start angle of the arc, measured clockwise |
| `sweepAngle` | `&nbsp;` | Sweep angle |

**Description**

Draws a pie (sector)

---

### drawBezier

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x1` | `&nbsp;` |  |
| `y1` | `&nbsp;` |  |
| `x2` | `&nbsp;` |  |
| `y2` | `&nbsp;` |  |
| `x3` | `&nbsp;` |  |
| `y3` | `&nbsp;` |  |
| `x4` | `&nbsp;` |  |
| `y4` | `&nbsp;` |  |

**Description**

Draws a Bezier curve

---

### drawBeziers

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `points` | `&nbsp;` | Array of points [ [x1, y1], [x2, y2] .... ] |

**Description**

Draws connected Bezier curves

---

### drawClosedCurve

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `points` | `&nbsp;` | Array of points [ [x1, y1], [x2, y2] .... ] |

**Description**

Draws a closed cardinal spline

---

### drawClosedCurve2

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `points` | `&nbsp;` | Array of points [ [x1, y1], [x2, y2] .... ] |
| `tension` | `&nbsp;` | Tension |

**Description**

Draws a closed cardinal spline

---

### drawCurve

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `points` | `&nbsp;` | Array of points [ [x1, y1], [x2, y2] .... ] |

**Description**

Draws a cardinal spline

---

### drawCurve2

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `points` | `&nbsp;` | Array of points [ [x1, y1], [x2, y2] .... ] |
| `tension` | `&nbsp;` | Tension |

**Description**

Draws a cardinal spline

---

### drawCurve3

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `points` | `&nbsp;` | Array of points [ [x1, y1], [x2, y2] .... ] |
| `offset` | `&nbsp;` |  |
| `numberOfSegments` | `&nbsp;` |  |
| `tension` | `&nbsp;` | Tension |

**Description**

Draws a cardinal spline

---

### drawEllipse

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `width` | `&nbsp;` |  |
| `height` | `&nbsp;` |  |

**Description**

Draws an ellipse

---

### drawLine

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x1` | `&nbsp;` | Start point X coordinate |
| `y1` | `&nbsp;` | Start point Y coordinate |
| `x2` | `&nbsp;` | End point X coordinate |
| `y2` | `&nbsp;` | End point Y coordinate |

**Description**

Draws a line segment

---

### drawLines

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `points` | `&nbsp;` | Array of points [ [x1, y1], [x2, y2] .... ] |

**Description**

Draws connected line segments

---

### drawPolygon

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `points` | `&nbsp;` | Array of points [ [x1, y1], [x2, y2] .... ] |

**Description**

Draws a polygon

---

### drawRectangle

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `width` | `&nbsp;` |  |
| `height` | `&nbsp;` |  |

**Description**

Draws a rectangle

---

### drawRectangles

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `rects` | `&nbsp;` | Array of rectangles [ [x1, y1, width1, height1], [x2, y2, width2, height2] .... ] |

**Description**

Draws multiple rectangles

---

## Plugin extension: layerExVector

### Members

#### Constructors

- [Path](#path)

#### Methods

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

Constructor

**Description**

Path class

---

### startFigure

Method

**Description**

Starts the next figure without closing the current one

---

### closeFigure

Method

**Description**

Closes the current figure

---

### drawArc

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | Top-left coordinate |
| `y` | `&nbsp;` | Top-left coordinate |
| `width` | `&nbsp;` | Width |
| `height` | `&nbsp;` | Height |
| `startAngle` | `&nbsp;` | Start angle of the arc, measured clockwise |
| `sweepAngle` | `&nbsp;` | Sweep angle |

**Description**

Draws an arc

---

### drawPie

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | Top-left coordinate |
| `y` | `&nbsp;` | Top-left coordinate |
| `width` | `&nbsp;` | Width |
| `height` | `&nbsp;` | Height |
| `startAngle` | `&nbsp;` | Start angle of the arc, measured clockwise |
| `sweepAngle` | `&nbsp;` | Sweep angle |

**Description**

Draws a pie (sector)

---

### drawBezier

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x1` | `&nbsp;` |  |
| `y1` | `&nbsp;` |  |
| `x2` | `&nbsp;` |  |
| `y2` | `&nbsp;` |  |
| `x3` | `&nbsp;` |  |
| `y3` | `&nbsp;` |  |
| `x4` | `&nbsp;` |  |
| `y4` | `&nbsp;` |  |

**Description**

Draws a Bezier curve

---

### drawBeziers

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `points` | `&nbsp;` | Array of points [ [x1, y1], [x2, y2] .... ] |

**Description**

Draws connected Bezier curves

---

### drawClosedCurve

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `points` | `&nbsp;` | Array of points [ [x1, y1], [x2, y2] .... ] |

**Description**

Draws a closed cardinal spline

---

### drawClosedCurve2

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `points` | `&nbsp;` | Array of points [ [x1, y1], [x2, y2] .... ] |
| `tension` | `&nbsp;` | Tension |

**Description**

Draws a closed cardinal spline

---

### drawCurve

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `points` | `&nbsp;` | Array of points [ [x1, y1], [x2, y2] .... ] |

**Description**

Draws a cardinal spline

---

### drawCurve2

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `points` | `&nbsp;` | Array of points [ [x1, y1], [x2, y2] .... ] |
| `tension` | `&nbsp;` | Tension |

**Description**

Draws a cardinal spline

---

### drawCurve3

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `points` | `&nbsp;` | Array of points [ [x1, y1], [x2, y2] .... ] |
| `offset` | `&nbsp;` |  |
| `numberOfSegments` | `&nbsp;` |  |
| `tension` | `&nbsp;` | Tension |

**Description**

Draws a cardinal spline

---

### drawEllipse

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `width` | `&nbsp;` |  |
| `height` | `&nbsp;` |  |

**Description**

Draws an ellipse

---

### drawLine

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x1` | `&nbsp;` | Start point X coordinate |
| `y1` | `&nbsp;` | Start point Y coordinate |
| `x2` | `&nbsp;` | End point X coordinate |
| `y2` | `&nbsp;` | End point Y coordinate |

**Description**

Draws a line segment

---

### drawLines

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `points` | `&nbsp;` | Array of points [ [x1, y1], [x2, y2] .... ] |

**Description**

Draws connected line segments

---

### drawPolygon

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `points` | `&nbsp;` | Array of points [ [x1, y1], [x2, y2] .... ] |

**Description**

Draws a polygon

---

### drawRectangle

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `width` | `&nbsp;` |  |
| `height` | `&nbsp;` |  |

**Description**

Draws a rectangle

---

### drawRectangles

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `rects` | `&nbsp;` | Array of rectangles [ [x1, y1, width1, height1], [x2, y2, width2, height2] .... ] |

**Description**

Draws multiple rectangles

---
