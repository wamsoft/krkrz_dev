# Matrix32

A 3x2 matrix for 2D.
Note that it is column-major, for OpenGL.

## Members

### Constructors

- [Matrix32](#matrix32)
- [Matrix32](#matrix32)

### Properties

- [array](#array)
- [m11](#m11)
- [m12](#m12)
- [m21](#m21)
- [m22](#m22)
- [m31](#m31)
- [m32](#m32)

### Methods

- [set](#set)
- [set](#set)
- [set](#set)
- [reset](#reset)
- [setTranslate](#settranslate)
- [setScale](#setscale)
- [setRotate](#setrotate)
- [setSkewX](#setskewx)
- [setSkewY](#setskewy)
- [translate](#translate)
- [rotate](#rotate)
- [rotate](#rotate)
- [scale](#scale)
- [preScale](#prescale)
- [skewX](#skewx)
- [skewY](#skewy)
- [transform](#transform)
- [multiply](#multiply)
- [premultiply](#premultiply)

---

### Matrix32

Constructor

**Description**

Constructor (identity matrix)

---

### Matrix32

Constructor

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `m11` | `real` | `&nbsp;` | Value at [1][1]. |
| `m12` | `real` | `&nbsp;` | Value at [1][2]. |
| `m21` | `real` | `&nbsp;` | Value at [2][1]. |
| `m22` | `real` | `&nbsp;` | Value at [2][2]. |
| `m31` | `real` | `&nbsp;` | Value at [3][1]. |
| `m32` | `real` | `&nbsp;` | Value at [3][2]. |

**Description**

Constructor

Initializes the matrix with the given values.

---

### array

Property \ Access: `r/w`

**Description**

Gets the matrix as a one-dimensional array [r]

---

### m11

Property \ Access: `r/w`

**Description**

Value at [1][1] [r/w]

---

### m12

Property \ Access: `r/w`

**Description**

Value at [1][2] [r/w]

---

### m21

Property \ Access: `r/w`

**Description**

Value at [2][1] [r/w]

---

### m22

Property \ Access: `r/w`

**Description**

Value at [2][2] [r/w]

---

### m31

Property \ Access: `r/w`

**Description**

Value at [3][1] [r/w]

---

### m32

Property \ Access: `r/w`

**Description**

Value at [3][2] [r/w]

---

### set

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `m11` | `real` | `&nbsp;` | Value at [1][1]. |
| `m12` | `real` | `&nbsp;` | Value at [1][2]. |
| `m21` | `real` | `&nbsp;` | Value at [2][1]. |
| `m22` | `real` | `&nbsp;` | Value at [2][2]. |
| `m31` | `real` | `&nbsp;` | Value at [3][1]. |
| `m32` | `real` | `&nbsp;` | Value at [3][2]. |

**Description**

Sets the matrix

---

### set

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `array` | `Array` | `&nbsp;` | An array of 6 elements. |

**Description**

Sets the matrix

Copies from a one-dimensional array.

---

### set

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `matrix` | `Matrix32` | `&nbsp;` | A Matrix32 instance. |

**Description**

Sets the matrix

Copies from matrix.

---

### reset

Method

**Description**

Resets to the identity matrix

---

### setTranslate

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `x` | `real` | `&nbsp;` | X coordinate to set. |
| `y` | `real` | `&nbsp;` | Y coordinate to set. |

**Description**

Sets a translation matrix

---

### setScale

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `x` | `real` | `&nbsp;` | Scale factor along the X axis. |
| `y` | `real` | `&nbsp;` | Scale factor along the Y axis. |

**Description**

Sets a scaling matrix

---

### setRotate

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `degree` | `real` | `&nbsp;` | Rotation angle. |

**Description**

Sets a rotation matrix

---

### setSkewX

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `degree` | `real` | `&nbsp;` | Skew angle. |

**Description**

Sets an X-axis skew matrix

---

### setSkewY

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `degree` | `real` | `&nbsp;` | Skew angle. |

**Description**

Sets a Y-axis skew matrix

---

### translate

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `x` | `real` | `&nbsp;` | Amount to move along X. |
| `y` | `real` | `&nbsp;` | Amount to move along Y. |

**Description**

Translates the matrix

---

### rotate

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `degree` | `real` | `&nbsp;` | Rotation angle. |

**Description**

Rotates the matrix

---

### rotate

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `degree` | `real` | `&nbsp;` | Rotation angle. |
| `px` | `real` | `&nbsp;` | Center point. |
| `py` | `real` | `&nbsp;` | Center point. |

**Description**

Rotates the matrix

---

### scale

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `x` | `real` | `&nbsp;` | Scale factor along X. |
| `y` | `real` | `&nbsp;` | Scale factor along Y. |

**Description**

Scales the matrix

---

### preScale

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `x` | `real` | `&nbsp;` | Scale factor along X. |
| `y` | `real` | `&nbsp;` | Scale factor along Y. |

**Description**

Scales the matrix (pre-scale)

---

### skewX

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `degree` | `real` | `&nbsp;` | Skew angle. |

**Description**

Skews the matrix along the X axis

---

### skewY

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `degree` | `real` | `&nbsp;` | Skew angle. |

**Description**

Skews the matrix along the Y axis

---

### transform

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `x` | `real` | `&nbsp;` | X coordinate. |
| `y` | `real` | `&nbsp;` | Y coordinate. |

**Description**

Transforms XY coordinates by this matrix

The input arguments are overwritten with the result.

---

### multiply

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `matrix` | `Matrix32` | `&nbsp;` | The matrix to multiply by. |

**Description**

Multiplies by a matrix (this = this * matrix)

---

### premultiply

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `matrix` | `Matrix32` | `&nbsp;` | The matrix to multiply by. |

**Description**

Multiplies by a matrix in the opposite order (this = matrix * this)

---
