# Zip

ZIP compression class

## Members

### Constructors

- [Zip](#zip)

### Methods

- [open](#open)
- [add](#add)
- [close](#close)

---

### Zip

Constructor

**Description**

Constructor

---

### open

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `&nbsp;` | File name. |
| `overwrite` | `0` | 0: create normally, 1: overwrite, 2: append. |

**Description**

Opens a ZIP archive for writing

---

### add

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `srcfile` | `&nbsp;` | File to add (Kirikiri storage name). |
| `destfile` | `&nbsp;` | Name in the archive (path within the archive). |
| `commpressLevel` | `void` |  |
| `password` | `void` | Encryption password. |
| `compressionMethod` | `Zip.CompressionMethodDeflate` | Compression method. |
| `clearDate` | `false` | Leaves the date empty. By default, the file's date is stored. |

**Return value**

true if the file was added.

**Description**

Adds a file to the archive

---

### close

Method

**Description**

Closes the ZIP archive

---
