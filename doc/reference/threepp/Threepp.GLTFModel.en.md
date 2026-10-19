# Threepp.GLTFModel

A loaded glTF model (returned by GLTFLoader)

Holds the model's scene graph and animation information.

## Members

### Methods

- [getScene](#getscene)
- [getAnimationCount](#getanimationcount)
- [getAnimationName](#getanimationname)
- [getAnimationDuration](#getanimationduration)
- [getPartCount](#getpartcount)
- [getPartGeometry](#getpartgeometry)
- [getPartMaterial](#getpartmaterial)
- [getPartName](#getpartname)

---

### getScene

Method

**Description**

-> Threepp.Group (add it to a Scene to render it)

---

### getAnimationCount

Method

**Description**

-> int (number of built-in animation clips)

---

### getAnimationName

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `i` | `&nbsp;` |  |

**Description**

(i) -> string (clip name)

---

### getAnimationDuration

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `i` | `&nbsp;` |  |

**Description**

(i) -> float (seconds)

---

### getPartCount

Method

**Description**

-> int (number of meshes in the model, in depth-first order of appearance)

To place hundreds of copies of the same model, loading the GLB once per copy and placing Meshes
results in one draw call per copy. Extracting the parts with getPartGeometry / getPartMaterial and
combining them into an InstancedMesh needs only one.

---

### getPartGeometry

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `i` | `&nbsp;` |  |

**Description**

(i) -> BufferGeometry

---

### getPartMaterial

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `i` | `&nbsp;` |  |

**Description**

(i) -> Material (shares the original, since it holds the textures)

---

### getPartName

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `i` | `&nbsp;` |  |

**Description**

(i) -> string (for telling parts apart)

---
