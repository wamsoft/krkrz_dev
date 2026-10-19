# Threepp.GLTFLoader

General-purpose glTF/GLB loader

Loads files as plain glTF without interpreting VRM extensions. GLB (self-contained) is the most reliable.
Skinned meshes are loaded in their bind pose (T-pose). Playing bone animations requires a separate animation mechanism (the model's own animations cannot currently be played back; this loader is meant for props, terrain and buildings with fixed poses, or for moving transforms from TJS).

## Members

### Constructors

- [GLTFLoader](#gltfloader)

### Methods

- [load](#load)
- [loadStorage](#loadstorage)

---

### GLTFLoader

Constructor

---

### load

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `osPath` | `&nbsp;` |  |

**Description**

Loads from an OS path (.gltf with external resources can also be resolved) -> GLTFModel

---

### loadStorage

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `storageName` | `&nbsp;` |  |

**Description**

Loads from a Kirikiri storage name (GLB recommended) -> GLTFModel

---
