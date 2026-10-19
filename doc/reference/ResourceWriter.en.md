# ResourceWriter

## Members

### Constructors

- [ResourceWriter](#resourcewriter)

### Methods

- [open](#open)
- [close](#close)
- [setLang](#setlang)
- [clear](#clear)
- [writeFromText](#writefromtext)
- [writeFromFile](#writefromfile)
- [writeFromOctet](#writefromoctet)

---

### ResourceWriter

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `file` | `&nbsp;` |  |
| `clean` | `&nbsp;` |  |

---

### open

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `file` | `&nbsp;` | File name (exe or dll). |
| `clean` | `false` | Whether to clear all existing resources.<br>In general, only files that are not currently open can be modified.<br>The running krkr.exe itself and plugins already linked with Plugins.link cannot be modified. |

**Description**

Opens the target file

---

### close

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `write` | `true` | true to write the changes.<br>With write=false, all writeFrom* and clear operations are discarded and nothing is written.<br>Even with write=true, nothing is written if writeFrom* / clear was never called. |

**Description**

Closes the target file and writes the changes

---

### setLang

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `primaryLang` | `&nbsp;` |  |
| `subLang` | `&nbsp;` |  |

**Description**

Sets the language to write

The arguments are the same as ResourceReader.setLang.

---

### clear

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `type` | `&nbsp;` | Resource type (a string, a number, or an rt* constant). |
| `name` | `&nbsp;` | Resource name (a string or a number).<br>Note: the change is not written until close(true) is called. |

**Description**

Deletes the target resource

---

### writeFromText

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `type` | `&nbsp;` | Resource type (a string, a number, or an rt* constant). |
| `name` | `&nbsp;` | Resource name (a string or a number). |
| `text` | `&nbsp;` | (writeFromText only) Text to write. |
| `utf8` | `false` | (writeFromText only) true to write UTF-8 encoded text (false writes Unicode). |

**Description**

Writes a resource

---

### writeFromFile

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `type` | `&nbsp;` |  |
| `name` | `&nbsp;` |  |
| `file` | `&nbsp;` |  |

---

### writeFromOctet

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `type` | `&nbsp;` |  |
| `name` | `&nbsp;` |  |
| `oct` | `&nbsp;` |  |

---
