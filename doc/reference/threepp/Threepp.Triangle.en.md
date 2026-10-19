# Threepp.Triangle

Triangle class

## Members

### Constructors

- [Triangle](#triangle)

### Properties

- [a](#a)
- [b](#b)
- [c](#c)

### Methods

- [set](#set)
- [clone](#clone)
- [copy](#copy)
- [getArea](#getarea)
- [getMidpoint](#getmidpoint)
- [getNormal](#getnormal)
- [getPlane](#getplane)
- [getBarycoord](#getbarycoord)
- [containsPoint](#containspoint)
- [isFrontFacing](#isfrontfacing)
- [closestPointToPoint](#closestpointtopoint)
- [equals](#equals)

---

### Triangle

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `a` | `&nbsp;` | Vertex A (Vector3). |
| `b` | `&nbsp;` | Vertex B (Vector3). |
| `c` | `&nbsp;` | Vertex C (Vector3). |

**Description**

Constructor

---

### a

Property \ Access: `r/w`

**Description**

Vertex A (read-only)

---

### b

Property \ Access: `r/w`

**Description**

Vertex B (read-only)

---

### c

Property \ Access: `r/w`

**Description**

Vertex C (read-only)

---

### set

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `a` | `&nbsp;` |  |
| `b` | `&nbsp;` |  |
| `c` | `&nbsp;` |  |

**Description**

Sets the values

---

### clone

Method

**Description**

Clones the triangle

---

### copy

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `triangle` | `&nbsp;` |  |

**Description**

Copies another triangle

---

### getArea

Method

**Description**

Area

---

### getMidpoint

Method

**Description**

Centroid

---

### getNormal

Method

**Description**

Normal

---

### getPlane

Method

**Description**

Plane containing the triangle

---

### getBarycoord

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `point` | `&nbsp;` |  |

**Description**

Gets barycentric coordinates

---

### containsPoint

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `point` | `&nbsp;` |  |

**Description**

Whether the triangle contains a point

---

### isFrontFacing

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `direction` | `&nbsp;` |  |

**Description**

Whether the triangle is front-facing

---

### closestPointToPoint

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `point` | `&nbsp;` |  |

**Description**

Closest point

---

### equals

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `triangle` | `&nbsp;` |  |

**Description**

Equality test

---
