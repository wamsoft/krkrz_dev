# Threepp.VRMLoader

VRM loader

Loads a .vrm file and returns a VRM. Supports both VRM 0.x and 1.0.

## Members

### Constructors

- [VRMLoader](#vrmloader)

### Methods

- [load](#load)
- [loadStorage](#loadstorage)

---

### VRMLoader

Constructor

---

### load

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `osPath` | `&nbsp;` | Absolute or relative path on the file system. |

**Return value**

VRM (void on failure)

**Description**

Loads from an OS path (for debugging / standalone use).

---

### loadStorage

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `storageName` | `&nbsp;` | Storage name (e.g. Storages.getPlacedPath("model.vrm")). |

**Return value**

VRM (void on failure)

**Description**

Loads from a Kirikiri storage name (for production; archives supported).

---
