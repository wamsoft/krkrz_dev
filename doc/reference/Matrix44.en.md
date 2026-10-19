# Matrix44

A 4x4 matrix.
Note that it is column-major, for OpenGL (column-major is also cheaper to compute).
Compared with DirectX and similar APIs it may look transposed (HLSL shaders are column-major too, so they match).

## Members

### Properties

- [array](#array)
- [m11](#m11)
- [m12](#m12)
- [m13](#m13)
- [m14](#m14)
- [m21](#m21)
- [m22](#m22)
- [m23](#m23)
- [m24](#m24)
- [m31](#m31)
- [m32](#m32)
- [m33](#m33)
- [m34](#m34)
- [m41](#m41)
- [m42](#m42)
- [m43](#m43)
- [m44](#m44)

### Methods

- [set](#set)
- [set](#set)
- [set](#set)
- [reset](#reset)
- [setTranslate](#settranslate)
- [setScale](#setscale)
- [setRotateZ](#setrotatez)
- [setRotate](#setrotate)
- [add](#add)
- [sub](#sub)
- [mul](#mul)
- [div](#div)
- [translate](#translate)
- [rotate](#rotate)
- [scale](#scale)
- [ortho](#ortho)
- [ortho](#ortho)
- [frustum](#frustum)
- [perspective](#perspective)
- [perspectiveFov](#perspectivefov)
- [project](#project)

---

### array

Property \ Access: `r/w`

**Description**

Gets the matrix as a one-dimensional array [r]

---

### m11

Property \ Access: `r/w`

**Description**

m11: value at [1][1]

---

### m12

Property \ Access: `r/w`

**Description**

m12: value at [1][2]

---

### m13

Property \ Access: `r/w`

**Description**

m13: value at [1][3]

---

### m14

Property \ Access: `r/w`

**Description**

m14: value at [1][4]

---

### m21

Property \ Access: `r/w`

**Description**

m21: value at [2][1]

---

### m22

Property \ Access: `r/w`

**Description**

m22: value at [2][2]

---

### m23

Property \ Access: `r/w`

**Description**

m23: value at [2][3]

---

### m24

Property \ Access: `r/w`

**Description**

m24: value at [2][4]

---

### m31

Property \ Access: `r/w`

**Description**

m31: value at [3][1]

---

### m32

Property \ Access: `r/w`

**Description**

m32: value at [3][2]

---

### m33

Property \ Access: `r/w`

**Description**

m33: value at [3][3]

---

### m34

Property \ Access: `r/w`

**Description**

m34: value at [3][4]

---

### m41

Property \ Access: `r/w`

**Description**

m41: value at [4][1]

---

### m42

Property \ Access: `r/w`

**Description**

m42: value at [4][2]

---

### m43

Property \ Access: `r/w`

**Description**

m43: value at [4][3]

---

### m44

Property \ Access: `r/w`

**Description**

m44: value at [4][4]

---

### set

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `m11` | `real` | `&nbsp;` | Value at [1][1]. |
| `m12` | `real` | `&nbsp;` | Value at [1][2]. |
| `m13` | `real` | `&nbsp;` | Value at [1][3]. |
| `m14` | `real` | `&nbsp;` | Value at [1][4]. |
| `m21` | `real` | `&nbsp;` | Value at [2][1]. |
| `m22` | `real` | `&nbsp;` | Value at [2][2]. |
| `m23` | `real` | `&nbsp;` | Value at [2][3]. |
| `m24` | `real` | `&nbsp;` | Value at [2][4]. |
| `m31` | `real` | `&nbsp;` | Value at [3][1]. |
| `m32` | `real` | `&nbsp;` | Value at [3][2]. |
| `m33` | `real` | `&nbsp;` | Value at [3][3]. |
| `m34` | `real` | `&nbsp;` | Value at [3][4]. |
| `m41` | `real` | `&nbsp;` | Value at [4][1]. |
| `m42` | `real` | `&nbsp;` | Value at [4][2]. |
| `m43` | `real` | `&nbsp;` | Value at [4][3]. |
| `m44` | `real` | `&nbsp;` | Value at [4][4]. |

**Description**

Sets the matrix

---

### set

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `array` | `Array` | `&nbsp;` | An array of 16 elements. |

**Description**

Sets the matrix

Copies from a one-dimensional array.

---

### set

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `matrix` | `Matrix44` | `&nbsp;` |  |

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
| `z` | `real` | `0.0` | Z coordinate to set. |

**Description**

Sets the translation

Sets the XYZ translation components of the matrix.
The values are only set; no operation with the current matrix is performed.

---

### setScale

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `x` | `real` | `&nbsp;` | Scale factor along the X axis. |
| `y` | `real` | `&nbsp;` | Scale factor along the Y axis. |
| `z` | `real` | `1.0` | Scale factor along the Z axis. |

**Description**

Sets the scale

Sets the XYZ scale components of the matrix.
The values are only set; no operation with the current matrix is performed.

---

### setRotateZ

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `degree` | `real` | `&nbsp;` | Rotation angle. |

**Description**

Sets the rotation

Sets a rotation around the Z axis.
The values are only set; no operation with the current matrix is performed.

---

### setRotate

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `degree` | `real` | `&nbsp;` | Rotation angle. |
| `x` | `real` | `&nbsp;` | X component of the rotation axis. |
| `y` | `real` | `&nbsp;` | Y component of the rotation axis. |
| `z` | `real` | `&nbsp;` | Z component of the rotation axis. |

**Description**

Sets the rotation

The values are only set; no operation with the current matrix is performed.
Normalizing the rotation axis is recommended.

---

### add

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `matrix` | `Matrix44` | `&nbsp;` | The matrix to add. |

**Description**

Adds a matrix to this matrix

---

### sub

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `matrix` | `Matrix44` | `&nbsp;` | The matrix to subtract. |

**Description**

Subtracts a matrix from this matrix

---

### mul

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `matrix` | `Matrix44` | `&nbsp;` | The matrix to multiply by. |

**Description**

Multiplies this matrix by a matrix

---

### div

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `matrix` | `Matrix44` | `&nbsp;` | The matrix to divide by. |

**Description**

Divides this matrix by a matrix

---

### translate

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `x` | `real` | `&nbsp;` | Amount to move along X. |
| `y` | `real` | `&nbsp;` | Amount to move along Y. |
| `z` | `real` | `0.0` | Amount to move along Z. |

**Description**

Translates the matrix

---

### rotate

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `degree` | `real` | `&nbsp;` | Rotation angle. |
| `x` | `real` | `&nbsp;` | X component of the rotation axis. |
| `y` | `real` | `&nbsp;` | Y component of the rotation axis. |
| `z` | `real` | `&nbsp;` | Z component of the rotation axis. |

**Description**

Rotates the matrix

---

### scale

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `x` | `real` | `&nbsp;` | Scale factor along the X axis. |
| `y` | `real` | `&nbsp;` | Scale factor along the Y axis. |
| `z` | `real` | `1.0` | Scale factor along the Z axis. |

**Description**

Scales the matrix

---

### ortho

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `left` | `real` | `&nbsp;` | Left edge. |
| `right` | `real` | `&nbsp;` | Right edge. |
| `bottom` | `real` | `&nbsp;` | Bottom edge. |
| `top` | `real` | `&nbsp;` | Top edge. |
| `znear` | `real` | `&nbsp;` | Near plane. |
| `zfar` | `real` | `&nbsp;` | Far plane. |

**Description**

Sets an orthographic projection matrix

---

### ortho

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `left` | `real` | `&nbsp;` | Left edge. |
| `right` | `real` | `&nbsp;` | Right edge. |
| `bottom` | `real` | `&nbsp;` | Bottom edge. |
| `top` | `real` | `&nbsp;` | Top edge. |

**Description**

Sets an orthographic projection matrix

---

### frustum

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `left` | `real` | `&nbsp;` | Left edge. |
| `right` | `real` | `&nbsp;` | Right edge. |
| `bottom` | `real` | `&nbsp;` | Bottom edge. |
| `top` | `real` | `&nbsp;` | Top edge. |
| `znear` | `real` | `&nbsp;` | Near plane. |
| `zfar` | `real` | `&nbsp;` | Far plane. |

**Description**

Sets a perspective projection matrix

---

### perspective

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `fovy` | `real` | `&nbsp;` | Field of view. |
| `aspect` | `real` | `&nbsp;` | Aspect ratio. |
| `znear` | `real` | `&nbsp;` | Near plane. |
| `zfar` | `real` | `&nbsp;` | Far plane. |

**Description**

Sets a projection matrix

---

### perspectiveFov

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `fovy` | `real` | `&nbsp;` | Field of view. |
| `width` | `real` | `&nbsp;` | Width. |
| `height` | `real` | `&nbsp;` | Height. |
| `znear` | `real` | `&nbsp;` | Near plane. |
| `zfar` | `real` | `&nbsp;` | Far plane. |

**Description**

Sets a projection matrix

---

### project

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `model` | `Matrix44` | `&nbsp;` | Model matrix. |
| `proj` | `Matrix44` | `&nbsp;` | Projection matrix. |
| `viewport` | `Rect` | `&nbsp;` | Viewport. |
| `x` | `real` | `&nbsp;` | X coordinate (in/out). |
| `y` | `real` | `&nbsp;` | Y coordinate (in/out). |
| `z` | `real` | `&nbsp;` | Z coordinate (in/out). |

**Description**

Transforms coordinates using the given matrices

This is a class method.

---
