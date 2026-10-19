# TemporaryFiles

Manages temporary files.
Register the files you want to treat as temporary with this object;
when the object is destroyed,
the files are deleted automatically once they are closed.

## Members

### Constructors

- [TemporaryFiles](#temporaryfiles)

### Methods

- [entry](#entry)
- [entryFolder](#entryfolder)

---

### TemporaryFiles

Constructor

**Description**

Constructor

---

### entry

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `&nbsp;` | File name. |

**Return value**

true if the file was registered.

**Description**

Registers a file

---

### entryFolder

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `foldername` | `&nbsp;` | Folder name. |

**Return value**

true if the folder was registered.

**Description**

Registers a folder

---
