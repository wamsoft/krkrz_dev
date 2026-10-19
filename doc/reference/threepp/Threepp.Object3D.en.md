# Threepp.Object3D

Base class for 3D objects

The base class for all 3D objects in the scene graph.

## Members

### Constructors

- [Object3D](#object3d)

### Properties

- [type](#type)
- [id](#id)
- [name](#name)
- [visible](#visible)
- [castShadow](#castshadow)
- [receiveShadow](#receiveshadow)
- [frustumCulled](#frustumculled)
- [renderOrder](#renderorder)
- [position](#position)
- [rotation](#rotation)
- [quaternion](#quaternion)
- [scale](#scale)
- [up](#up)

### Methods

- [setPosition](#setposition)
- [setRotation](#setrotation)
- [setScale](#setscale)
- [add](#add)
- [remove](#remove)
- [removeFromParent](#removefromparent)
- [clear](#clear)
- [lookAt](#lookat)
- [rotateX](#rotatex)
- [rotateY](#rotatey)
- [rotateZ](#rotatez)
- [rotateOnAxis](#rotateonaxis)
- [rotateOnWorldAxis](#rotateonworldaxis)
- [translateX](#translatex)
- [translateY](#translatey)
- [translateZ](#translatez)
- [translateOnAxis](#translateonaxis)
- [updateMatrix](#updatematrix)
- [updateMatrixWorld](#updatematrixworld)
- [treeJson](#treejson)
- [setQuaternion](#setquaternion)
- [getWorldPosition](#getworldposition)
- [getWorldQuaternion](#getworldquaternion)
- [getWorldScale](#getworldscale)

---

### Object3D

Constructor

**Description**

Constructor

---

### type

Property \ Access: `r/w`

**Description**

Object type (read-only)

---

### id

Property \ Access: `r/w`

**Description**

Object ID (read-only)

---

### name

Property \ Access: `r/w`

**Description**

Object name

---

### visible

Property \ Access: `r/w`

**Description**

Visibility

---

### castShadow

Property \ Access: `r/w`

**Description**

Whether the object casts shadows

---

### receiveShadow

Property \ Access: `r/w`

**Description**

Whether the object receives shadows

---

### frustumCulled

Property \ Access: `r/w`

**Description**

Whether frustum culling is performed

---

### renderOrder

Property \ Access: `r/w`

**Description**

Render order

---

### position

Property \ Access: `r/w`

**Description**

Position (Vector3; a copy of the value, so effectively read-only)

Note: the position/rotation/scale/quaternion getters return a copy of the value, so
writing obj.position.set(...) or obj.position.x = ... does not affect the object.
Use setPosition/setRotation/setScale (setQuaternion for quaternion) to change the position, rotation and scale.

---

### rotation

Property \ Access: `r/w`

**Description**

Rotation (Euler; a copy of the value, so effectively read-only)

---

### quaternion

Property \ Access: `r/w`

**Description**

Rotation (Quaternion; a copy of the value, so effectively read-only)

---

### scale

Property \ Access: `r/w`

**Description**

Scale (Vector3; a copy of the value, so effectively read-only)

---

### up

Property \ Access: `r/w`

**Description**

Up vector (Vector3; a copy of the value)

---

### setPosition

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**Description**

Sets the position (use this instead of position.set)

---

### setRotation

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**Description**

Sets the rotation (Euler angles in radians)

---

### setScale

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**Description**

Sets the scale

---

### add

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `object` | `&nbsp;` | Object3D to add. |

**Description**

Adds a child object

---

### remove

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `object` | `&nbsp;` | Object3D to remove. |

**Description**

Removes a child object

---

### removeFromParent

Method

**Description**

Removes this object from its parent

---

### clear

Method

**Description**

Removes all child objects

---

### lookAt

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | X coordinate. |
| `y` | `&nbsp;` | Y coordinate. |
| `z` | `&nbsp;` | Z coordinate. |

**Description**

Rotates the object to face a point

---

### rotateX

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `angle` | `&nbsp;` |  |

**Description**

Rotates around the X axis

---

### rotateY

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `angle` | `&nbsp;` |  |

**Description**

Rotates around the Y axis

---

### rotateZ

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `angle` | `&nbsp;` |  |

**Description**

Rotates around the Z axis

---

### rotateOnAxis

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `axis` | `&nbsp;` |  |
| `angle` | `&nbsp;` |  |

**Description**

Rotates around an arbitrary axis (local space)

---

### rotateOnWorldAxis

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `axis` | `&nbsp;` |  |
| `angle` | `&nbsp;` |  |

**Description**

Rotates around an arbitrary axis (world space)

---

### translateX

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `distance` | `&nbsp;` |  |

**Description**

Translates along the X axis

---

### translateY

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `distance` | `&nbsp;` |  |

**Description**

Translates along the Y axis

---

### translateZ

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `distance` | `&nbsp;` |  |

**Description**

Translates along the Z axis

---

### translateOnAxis

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `axis` | `&nbsp;` |  |
| `distance` | `&nbsp;` |  |

**Description**

Translates along an arbitrary axis

---

### updateMatrix

Method

**Description**

Updates the local matrix

---

### updateMatrixWorld

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `force` | `&nbsp;` |  |

**Description**

Updates the world matrix

---

### treeJson

Method

**Return value**

JSON string.

**Description**

Dumps the whole subtree as a JSON string (for displaying the scene tree in an external inspector).

Each node = {id,name,type,visible,pos:[x,y,z],children:[…]}

---

### setQuaternion

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |

**Description**

Sets the rotation from quaternion components

The quaternion property returns a copy of the value, so use this to write it back (Object3D only).

---

### getWorldPosition

Method

**Description**

-> Vector3 (world position)

getWorldPosition / getWorldQuaternion / getWorldScale are computed from matrixWorld.
For the result to be up to date, render or call updateMatrixWorld(true) just before
(the world matrix must be resolved by walking up the parents).
Useful for getting the world coordinates of bones (head, hips, etc.) when framing a character portrait.

---

### getWorldQuaternion

Method

**Description**

-> Quaternion (world rotation)

---

### getWorldScale

Method

**Description**

-> Vector3 (world scale)

---
