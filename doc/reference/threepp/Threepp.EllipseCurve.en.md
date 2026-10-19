# Threepp.EllipseCurve

Ellipse curve

A curve representing an ellipse or an arc.

## Members

### Constructors

- [EllipseCurve](#ellipsecurve)

### Properties

- [aX](#ax)
- [aY](#ay)
- [xRadius](#xradius)
- [yRadius](#yradius)
- [aStartAngle](#astartangle)
- [aEndAngle](#aendangle)
- [aClockwise](#aclockwise)
- [aRotation](#arotation)

### Methods

- [getLength](#getlength)
- [getPoint](#getpoint)

---

### EllipseCurve

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `aX` | `0` | X coordinate of the center. |
| `aY` | `0` | Y coordinate of the center. |
| `xRadius` | `1` | Radius along X. |
| `yRadius` | `1` | Radius along Y. |
| `aStartAngle` | `0` | Start angle (radians). |
| `aEndAngle` | `Math.PI*2` | End angle (radians). |
| `aClockwise` | `false` | Whether the ellipse is drawn clockwise. |
| `aRotation` | `0` | Rotation angle of the ellipse (radians). |

**Description**

Constructor

---

### aX

Property \ Access: `r/w`

**Description**

X coordinate of the center

---

### aY

Property \ Access: `r/w`

**Description**

Y coordinate of the center

---

### xRadius

Property \ Access: `r/w`

**Description**

Radius along X

---

### yRadius

Property \ Access: `r/w`

**Description**

Radius along Y

---

### aStartAngle

Property \ Access: `r/w`

**Description**

Start angle

---

### aEndAngle

Property \ Access: `r/w`

**Description**

End angle

---

### aClockwise

Property \ Access: `r/w`

**Description**

Clockwise flag

---

### aRotation

Property \ Access: `r/w`

**Description**

Rotation angle

---

### getLength

Method

**Description**

Gets the length of the curve

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
