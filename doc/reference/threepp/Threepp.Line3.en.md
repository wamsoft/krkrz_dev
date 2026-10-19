# Threepp.Line3

3D line segment class

## Members

### Constructors

- [Line3](#line3)

### Properties

- [start](#start)
- [end](#end)

### Methods

- [set](#set)
- [clone](#clone)
- [copy](#copy)
- [getCenter](#getcenter)
- [delta](#delta)
- [distanceSq](#distancesq)
- [distance](#distance)
- [at](#at)
- [closestPointToPoint](#closestpointtopoint)
- [closestPointToPointParameter](#closestpointtopointparameter)
- [applyMatrix4](#applymatrix4)
- [equals](#equals)

---

### Line3

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `start` | `&nbsp;` | Start point (Vector3). |
| `end` | `&nbsp;` | End point (Vector3). |

**Description**

Constructor

---

### start

Property \ Access: `r/w`

**Description**

Start point (read-only)

---

### end

Property \ Access: `r/w`

**Description**

End point (read-only)

---

### set

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `start` | `&nbsp;` |  |
| `end` | `&nbsp;` |  |

**Description**

Sets the values

---

### clone

Method

**Description**

Clones the line

---

### copy

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `line` | `&nbsp;` |  |

**Description**

Copies another line

---

### getCenter

Method

**Description**

Gets the center

---

### delta

Method

**Description**

Gets the direction vector

---

### distanceSq

Method

**Description**

Squared length

---

### distance

Method

**Description**

Length

---

### at

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `t` | `&nbsp;` |  |

**Description**

Gets the point at a parameter position

---

### closestPointToPoint

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `point` | `&nbsp;` |  |
| `clamp` | `&nbsp;` |  |

**Description**

Gets the closest point

---

### closestPointToPointParameter

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `point` | `&nbsp;` |  |
| `clamp` | `&nbsp;` |  |

**Description**

Parameter of the closest point

---

### applyMatrix4

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**Description**

Applies a matrix

---

### equals

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `line` | `&nbsp;` |  |

**Description**

Equality test

---
