# Threepp.Box2

2D axis-aligned bounding box class

## Members

### Constructors

- [Box2](#box2)

### Properties

- [min](#min)
- [max](#max)

### Methods

- [set](#set)
- [clone](#clone)
- [copy](#copy)
- [makeEmpty](#makeempty)
- [isEmpty](#isempty)
- [expandByPoint](#expandbypoint)
- [expandByVector](#expandbyvector)
- [expandByScalar](#expandbyscalar)
- [containsPoint](#containspoint)
- [containsBox](#containsbox)
- [intersectsBox](#intersectsbox)
- [distanceToPoint](#distancetopoint)
- [intersect](#intersect)
- [union_](#union_)
- [translate](#translate)
- [equals](#equals)

---

### Box2

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `min` | `&nbsp;` | Lower bound (Vector2). |
| `max` | `&nbsp;` | Upper bound (Vector2). |

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
| `v` | `&nbsp;` |  |

**Description**

Expands the box by a vector

---

### expandByScalar

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `s` | `&nbsp;` |  |

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

Union

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
