# Threepp.VRMAnimationLoader

VRM animation loader

## Members

### Constructors

- [VRMAnimationLoader](#vrmanimationloader)

### Methods

- [load](#load)
- [loadStorage](#loadstorage)
- [exportPoseSeq](#exportposeseq)

---

### VRMAnimationLoader

Constructor

---

### load

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `osPath` | `&nbsp;` |  |

**Description**

Loads from an OS path (for debugging) -> VRMAnimation

---

### loadStorage

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `storageName` | `&nbsp;` |  |

**Description**

Loads from a Kirikiri storage name (for production) -> VRMAnimation

---

### exportPoseSeq

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `boneNames` | `&nbsp;` | [bone name,…] (nBones) |
| `times` | `&nbsp;` | [seconds,…] (nKeys) |
| `quatsFlat` | `&nbsp;` | [qx,qy,qz,qw,… in (key,bone) row-major order] (nKeys*nBones*4) |
| `hipsFlat` | `&nbsp;` | Hips offsets [dx,dy,dz,…] (nKeys*3; an empty array = no track) |
| `exprNames` | `&nbsp;` | Expression names [] (omitted/empty = no expression track) |
| `exprWeightsFlat` | `&nbsp;` | Expression weights (expr-major flat array, nExpr*nKeys) |
| `path` | `&nbsp;` | Output storage name (a bare name goes directly under data/) |

**Description**

Writes a pose sequence to a single VRMA file (.vrma = glTF-JSON + base64).

The input is flat parallel arrays. The written file can be read back with loadStorage.

---
