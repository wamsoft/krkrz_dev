# Threepp.Vector2

2D vector class

Represents a two-dimensional vector. It can also be converted from an array [x, y] or a dictionary %[x:, y:].

## Members

### Constructors

- [Vector2](#vector2)

### Properties

- [x](#x)
- [y](#y)

### Methods

- [set](#set)
- [setScalar](#setscalar)
- [copy](#copy)
- [add](#add)
- [addScalar](#addscalar)
- [sub](#sub)
- [subScalar](#subscalar)
- [multiplyScalar](#multiplyscalar)
- [divideScalar](#dividescalar)
- [negate](#negate)
- [dot](#dot)
- [cross](#cross)
- [lengthSq](#lengthsq)
- [length](#length)
- [normalize](#normalize)
- [distanceTo](#distanceto)
- [distanceToSquared](#distancetosquared)
- [lerp](#lerp)
- [equals](#equals)
- [floor](#floor)
- [ceil](#ceil)
- [round](#round)

---

### Vector2

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `0` | X component. |
| `y` | `0` | Y component. |

**Description**

Constructor

---

### x

Property \ Access: `r/w`

**Description**

X component

---

### y

Property \ Access: `r/w`

**Description**

Y component

---

### set

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**Description**

Sets the values

---

### setScalar

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `value` | `&nbsp;` |  |

**Description**

Sets all components to the same value

---

### copy

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**Description**

Copies another vector

---

### add

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**Description**

Adds a vector

---

### addScalar

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `s` | `&nbsp;` |  |

**Description**

Adds a scalar

---

### sub

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**Description**

Subtracts a vector

---

### subScalar

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `s` | `&nbsp;` |  |

**Description**

Subtracts a scalar

---

### multiplyScalar

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `s` | `&nbsp;` |  |

**Description**

Multiplies by a scalar

---

### divideScalar

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `s` | `&nbsp;` |  |

**Description**

Divides by a scalar

---

### negate

Method

**Description**

Negates the vector

---

### dot

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**Description**

Dot product

---

### cross

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**Description**

Cross product (returns a scalar)

---

### lengthSq

Method

**Description**

Squared length

---

### length

Method

**Description**

Length

---

### normalize

Method

**Description**

Normalizes the vector

---

### distanceTo

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**Description**

Distance to another vector

---

### distanceToSquared

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**Description**

Squared distance

---

### lerp

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `v` | `&nbsp;` |  |
| `alpha` | `&nbsp;` |  |

**Description**

Linear interpolation

---

### equals

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**Description**

Equality test

---

### floor

Method

**Description**

Rounds each component down

---

### ceil

Method

**Description**

Rounds each component up

---

### round

Method

**Description**

Rounds each component to the nearest integer

---
