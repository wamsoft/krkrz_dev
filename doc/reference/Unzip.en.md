# Unzip

ZIP extraction class

## Members

### Constructors

- [Unzip](#unzip)

### Methods

- [open](#open)
- [list](#list)
- [extract](#extract)
- [close](#close)

---

### Unzip

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
| `force_utf8` | `0` | 0: detect the file name encoding from the first file, 1: force UTF-8. |

**Description**

Opens a ZIP archive for extraction

---

### list

Method

**Return value**

List of files (an array of file information).
Each entry is a dictionary containing the following:
<dl>
<dt>filename <dd>Path within the archive
<dt>uncompressed_size <dd>Uncompressed size
<dt>compressed_size <dd>Compressed size
<dt>crypted <dd>Whether the file is encrypted
<dt>deflated <dd>Whether the file is compressed
<dt>deflateLevel <dd>Compression level
<dt>crc <dd>CRC of the file
</dl>

**Description**

Gets information on the files contained in the ZIP archive

---

### extract

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `srcname` | `&nbsp;` | Source file (path within the archive). |
| `destfile` | `&nbsp;` | Destination file (Kirikiri storage name). |
| `password` | `void` | Password. |

**Return value**

true if the file was extracted.

**Description**

Extracts a file

---

### close

Method

**Description**

Closes the ZIP archive

---
