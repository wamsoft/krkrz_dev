# Threepp.Vector3

3D vector class

Represents a three-dimensional vector. It can also be converted from an array [x, y, z] or a dictionary %[x:, y:, z:].

## Members

### Constructors

- [Vector3](#vector3)

### Properties

- [x](#x)
- [y](#y)
- [z](#z)

### Methods

- [set](#set)
- [setScalar](#setscalar)
- [setX](#setx)
- [setY](#sety)
- [setZ](#setz)
- [copy](#copy)
- [add](#add)
- [addScalar](#addscalar)
- [addVectors](#addvectors)
- [addScaledVector](#addscaledvector)
- [sub](#sub)
- [subScalar](#subscalar)
- [subVectors](#subvectors)
- [multiply](#multiply)
- [multiplyScalar](#multiplyscalar)
- [multiplyVectors](#multiplyvectors)
- [applyAxisAngle](#applyaxisangle)
- [applyEuler](#applyeuler)
- [applyMatrix3](#applymatrix3)
- [applyMatrix4](#applymatrix4)
- [applyQuaternion](#applyquaternion)
- [project](#project)
- [unproject](#unproject)
- [transformDirection](#transformdirection)
- [divide](#divide)
- [divideScalar](#dividescalar)
- [min](#min)
- [max](#max)
- [clamp](#clamp)
- [clampScalar](#clampscalar)
- [clampLength](#clamplength)
- [floor](#floor)
- [ceil](#ceil)
- [round](#round)
- [negate](#negate)
- [dot](#dot)
- [lengthSq](#lengthsq)
- [length](#length)
- [manhattanLength](#manhattanlength)
- [normalize](#normalize)
- [setLength](#setlength)
- [lerp](#lerp)
- [lerpVectors](#lerpvectors)
- [cross](#cross)
- [crossVectors](#crossvectors)
- [reflect](#reflect)
- [angleTo](#angleto)
- [distanceTo](#distanceto)
- [distanceToSquared](#distancetosquared)
- [manhattanDistanceTo](#manhattandistanceto)
- [setFromMatrixPosition](#setfrommatrixposition)
- [setFromMatrixScale](#setfrommatrixscale)
- [equals](#equals)

---

### Vector3

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `0` | X component. |
| `y` | `0` | Y component. |
| `z` | `0` | Z component. |

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

### z

Property \ Access: `r/w`

**Description**

Z component

---

### set

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

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

### setX

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `value` | `&nbsp;` |  |

**Description**

Sets the X component

---

### setY

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `value` | `&nbsp;` |  |

**Description**

Sets the Y component

---

### setZ

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `value` | `&nbsp;` |  |

**Description**

Sets the Z component

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

### addVectors

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `a` | `&nbsp;` |  |
| `b` | `&nbsp;` |  |

**Description**

Sets this vector to the sum of two vectors

---

### addScaledVector

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `v` | `&nbsp;` |  |
| `s` | `&nbsp;` |  |

**Description**

Adds a scaled vector

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

### subVectors

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `a` | `&nbsp;` |  |
| `b` | `&nbsp;` |  |

**Description**

Sets this vector to the difference of two vectors

---

### multiply

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**Description**

Component-wise multiplication by a vector

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

### multiplyVectors

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `a` | `&nbsp;` |  |
| `b` | `&nbsp;` |  |

**Description**

Sets this vector to the component-wise product of two vectors

---

### applyAxisAngle

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `axis` | `&nbsp;` |  |
| `angle` | `&nbsp;` |  |

**Description**

Rotates by an axis and an angle

---

### applyEuler

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `euler` | `&nbsp;` |  |

**Description**

Rotates by Euler angles

---

### applyMatrix3

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**Description**

Applies a 3x3 matrix

---

### applyMatrix4

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**Description**

Applies a 4x4 matrix

---

### applyQuaternion

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `q` | `&nbsp;` |  |

**Description**

Rotates by a quaternion

---

### project

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `camera` | `&nbsp;` |  |

**Description**

Projects the vector with a camera

---

### unproject

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `camera` | `&nbsp;` |  |

**Description**

Unprojects the vector

---

### transformDirection

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**Description**

Transforms a direction vector

---

### divide

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**Description**

Component-wise division by a vector

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

### min

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**Description**

Component-wise minimum

---

### max

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**Description**

Component-wise maximum

---

### clamp

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `min` | `&nbsp;` |  |
| `max` | `&nbsp;` |  |

**Description**

Clamps each component

---

### clampScalar

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `min` | `&nbsp;` |  |
| `max` | `&nbsp;` |  |

**Description**

Clamps to a scalar range

---

### clampLength

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `min` | `&nbsp;` |  |
| `max` | `&nbsp;` |  |

**Description**

Clamps the length

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

### manhattanLength

Method

**Description**

Manhattan length

---

### normalize

Method

**Description**

Normalizes the vector

---

### setLength

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `length` | `&nbsp;` |  |

**Description**

Sets the length

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

### lerpVectors

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `a` | `&nbsp;` |  |
| `b` | `&nbsp;` |  |
| `alpha` | `&nbsp;` |  |

**Description**

Linear interpolation between two vectors

---

### cross

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**Description**

Cross product

---

### crossVectors

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `a` | `&nbsp;` |  |
| `b` | `&nbsp;` |  |

**Description**

Cross product of two vectors

---

### reflect

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `normal` | `&nbsp;` |  |

**Description**

Reflection

---

### angleTo

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**Description**

Angle to another vector

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

### manhattanDistanceTo

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**Description**

Manhattan distance

---

### setFromMatrixPosition

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**Description**

Gets the translation component of a matrix

---

### setFromMatrixScale

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**Description**

Gets the scale component of a matrix

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
