# Threepp.Box3

Axis-aligned bounding box (AABB) class

## Members

### Constructors

- [Box3](#box3)

### Properties

- [min](#min)
- [max](#max)

### Methods

- [set](#set)
- [clone](#clone)
- [copy](#copy)
- [makeEmpty](#makeempty)
- [isEmpty](#isempty)
- [getCenter](#getcenter)
- [getSize](#getsize)
- [expandByPoint](#expandbypoint)
- [expandByVector](#expandbyvector)
- [expandByScalar](#expandbyscalar)
- [containsPoint](#containspoint)
- [containsBox](#containsbox)
- [intersectsBox](#intersectsbox)
- [intersectsSphere](#intersectssphere)
- [intersectsPlane](#intersectsplane)
- [distanceToPoint](#distancetopoint)
- [intersect](#intersect)
- [union_](#union_)
- [applyMatrix4](#applymatrix4)
- [translate](#translate)
- [equals](#equals)

---

### Box3

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `min` | `&nbsp;` | Lower bound (Vector3). |
| `max` | `&nbsp;` | Upper bound (Vector3). |

**Description**

Constructor

---

### min

Property \ Access: `r/w`

**Description**

Lower bound (read-only)

---

### max

Property \ Access: `r/w`

**Description**

Upper bound (read-only)

---

### set

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `min` | `&nbsp;` |  |
| `max` | `&nbsp;` |  |

**Description**

Sets the values

---

### clone

Method

**Description**

Clones the box

---

### copy

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `box` | `&nbsp;` |  |

**Description**

Copies another box

---

### makeEmpty

Method

**Description**

Makes the box empty

---

### isEmpty

Method

**Description**

Whether the box is empty

---

### getCenter

Method

**Description**

Gets the center

---

### getSize

Method

**Description**

Gets the size

---

### expandByPoint

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `point` | `&nbsp;` |  |

**Description**

Expands the box to include a point

---

### expandByVector

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `vector` | `&nbsp;` |  |

**Description**

Expands the box by a vector

---

### expandByScalar

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `scalar` | `&nbsp;` |  |

**Description**

Expands the box by a scalar

---

### containsPoint

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `point` | `&nbsp;` |  |

**Description**

Whether the box contains a point

---

### containsBox

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `box` | `&nbsp;` |  |

**Description**

Whether the box contains another box

---

### intersectsBox

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `box` | `&nbsp;` |  |

**Description**

Whether the box intersects another box

---

### intersectsSphere

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `sphere` | `&nbsp;` |  |

**Description**

Whether the box intersects a sphere

---

### intersectsPlane

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `plane` | `&nbsp;` |  |

**Description**

Whether the box intersects a plane

---

### distanceToPoint

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `point` | `&nbsp;` |  |

**Description**

Distance to a point

---

### intersect

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `box` | `&nbsp;` |  |

**Description**

Gets the intersection

---

### union_

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `box` | `&nbsp;` |  |

**Description**

Gets the union

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

### translate

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `offset` | `&nbsp;` |  |

**Description**

Translates the box

---

### equals

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `box` | `&nbsp;` |  |

**Description**

Equality test

---
