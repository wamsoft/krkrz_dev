# Threepp.Raycaster

Raycaster

Uses a ray to test for intersections with objects.

## Members

### Constructors

- [Raycaster](#raycaster)

### Properties

- [nearPlane](#nearplane)
- [farPlane](#farplane)

### Methods

- [set](#set)
- [setFromCameraNDC](#setfromcamerandc)
- [setFromCameraPixel](#setfromcamerapixel)
- [intersectObjects](#intersectobjects)

---

### Raycaster

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `origin` | `&nbsp;` | Origin. |
| `direction` | `&nbsp;` | Direction. |
| `near` | `0` | Near distance. |
| `far` | `Infinity` | Far distance. |

**Description**

Constructor

---

### nearPlane

Property \ Access: `r/w`

**Description**

Near distance

---

### farPlane

Property \ Access: `r/w`

**Description**

Far distance

---

### set

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `origin` | `&nbsp;` |  |
| `direction` | `&nbsp;` |  |

**Description**

Sets the origin and direction (direction must be normalized)

---

### setFromCameraNDC

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `ndcX` | `&nbsp;` | Normalized device coordinate X [-1,1] (left edge of the screen -1, right edge +1). |
| `ndcY` | `&nbsp;` | Normalized device coordinate Y [-1,1] (bottom edge of the screen -1, top edge +1). |
| `camera` | `&nbsp;` | PerspectiveCamera or OrthographicCamera. |

**Description**

Sets the ray from a camera and normalized device coordinates (equivalent to three.js's setFromCamera)

---

### setFromCameraPixel

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `px` | `&nbsp;` | Pixel X (top-left origin; Kirikiri layer coordinates). |
| `py` | `&nbsp;` | Pixel Y (top-left origin; positive downward). |
| `viewW` | `&nbsp;` | Viewport width (width of the drawing layer). |
| `viewH` | `&nbsp;` | Viewport height (height of the drawing layer). |
| `camera` | `&nbsp;` | Camera. |

**Description**

Convenience version that sets the ray from pixel coordinates (top-left origin) and the viewport size

You can pass mouse coordinates directly; they are converted to NDC internally.

---

### intersectObjects

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `objects` | `&nbsp;` | Array of Object3D to test (e.g. [vrm.getScene(), boxMesh]). |
| `recursive` | `true` | Whether to test descendants recursively (default true). |

**Return value**

Array of hits. Each element is a dictionary:
object   … the hit root object passed in the argument array (the same instance).
Even when recursive finds a hit on a descendant, the corresponding ancestor in the argument array is returned.
distance … distance from the ray origin
x, y, z  … hit point in world coordinates
The array is sorted by ascending distance (result[0] is the nearest). With no hits, count=0.

**Description**

Tests for intersections with a set of objects and returns the hits as an array sorted by distance, nearest first

---
