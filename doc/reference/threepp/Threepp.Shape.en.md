# Threepp.Shape

Shape (2D shape with holes)

A 2D shape class that inherits from Path and can have holes.
Used with ExtrudeGeometry and ShapeGeometry.

## Members

### Constructors

- [Shape](#shape)

### Properties

- [autoClose](#autoclose)
- [currentPoint](#currentpoint)

### Methods

- [getLength](#getlength)
- [getPoint](#getpoint)
- [getPointAt](#getpointat)
- [moveTo](#moveto)
- [lineTo](#lineto)
- [quadraticCurveTo](#quadraticcurveto)
- [bezierCurveTo](#beziercurveto)
- [arc](#arc)
- [absarc](#absarc)
- [absellipse](#absellipse)
- [splineThru](#splinethru)
- [closePath](#closepath)
- [addHole](#addhole)
- [getHole](#gethole)
- [getHoleCount](#getholecount)
- [uuid](#uuid)

---

### Shape

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `points` | `&nbsp;` | Array of initial points (optional). |

**Description**

Constructor

---

### autoClose

Property \ Access: `r/w`

**Description**

Whether to close the path automatically

---

### currentPoint

Property \ Access: `r/w`

**Description**

Current pen position (read-only)

---

### getLength

Method

**Description**

Gets the total length of the path

---

### getPoint

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `t` | `&nbsp;` |  |

**Description**

Gets the point at parameter t (0-1)

---

### getPointAt

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `u` | `&nbsp;` |  |

**Description**

Gets the point at arc-length parameter u

---

### moveTo

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**Description**

Moves the pen

---

### lineTo

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**Description**

Draws a straight line

---

### quadraticCurveTo

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `cpX` | `&nbsp;` |  |
| `cpY` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**Description**

Draws a quadratic Bezier curve

---

### bezierCurveTo

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `cp1x` | `&nbsp;` |  |
| `cp1y` | `&nbsp;` |  |
| `cp2x` | `&nbsp;` |  |
| `cp2y` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**Description**

Draws a cubic Bezier curve

---

### arc

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `radius` | `&nbsp;` |  |
| `startAngle` | `&nbsp;` |  |
| `endAngle` | `&nbsp;` |  |
| `clockwise` | `&nbsp;` |  |

**Description**

Draws an arc relative to the current position

---

### absarc

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `radius` | `&nbsp;` |  |
| `startAngle` | `&nbsp;` |  |
| `endAngle` | `&nbsp;` |  |
| `clockwise` | `&nbsp;` |  |

**Description**

Draws an arc at an absolute position

---

### absellipse

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `xRadius` | `&nbsp;` |  |
| `yRadius` | `&nbsp;` |  |
| `startAngle` | `&nbsp;` |  |
| `endAngle` | `&nbsp;` |  |
| `clockwise` | `&nbsp;` |  |
| `rotation` | `&nbsp;` |  |

**Description**

Draws an ellipse

---

### splineThru

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `points` | `&nbsp;` |  |

**Description**

Draws a spline through an array of points

---

### closePath

Method

**Description**

Closes the path

---

### addHole

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `hole` | `&nbsp;` |  |

**Description**

Adds a hole (a Path object)

---

### getHole

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` |  |

**Description**

Gets a hole

---

### getHoleCount

Method

**Description**

Gets the number of holes

---

### uuid

Method

**Description**

Gets the UUID of the shape

---
