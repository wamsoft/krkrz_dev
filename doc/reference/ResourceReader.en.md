# ResourceReader

## Members

### Constructors

- [ResourceReader](#resourcereader)

### Methods

- [open](#open)
- [close](#close)
- [setLang](#setlang)
- [isExistentResource](#isexistentresource)
- [readToText](#readtotext)
- [readToFile](#readtofile)
- [readToOctet](#readtooctet)
- [enumTypes](#enumtypes)
- [enumNames](#enumnames)
- [enumLangs](#enumlangs)

---

### ResourceReader

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `file` | `&nbsp;` |  |

---

### open

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `file` | `&nbsp;` | File name (exe or dll). |

**Description**

Opens the target file

---

### close

Method

**Description**

Closes the target file

---

### setLang

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `primaryLang` | `&nbsp;` | Primary language. |
| `subLang` | `&nbsp;` | Sublanguage. |

**Return value**

The WORD value that was set.
Each argument is a LANG_* / SUBLANG_* string or a number.
See MAKELANGID and related documentation for details.

**Description**

Sets the language to read

---

### isExistentResource

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `type` | `&nbsp;` | Resource type (a string, a number, or an rt* constant). |
| `name` | `&nbsp;` | Resource name (a string or a number). |

**Return value**

true if it exists.

**Description**

Checks whether a resource exists

---

### readToText

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `type` | `&nbsp;` | Resource type (a string, a number, or an rt* constant). |
| `name` | `&nbsp;` | Resource name (a string or a number). |
| `utf8` | `false` | (readToText only) true if the resource is UTF-8 encoded (false means Unicode). |

**Return value**

void if the resource does not exist; otherwise the value depends on the method.

**Description**

Reads a resource

---

### readToFile

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `type` | `&nbsp;` |  |
| `name` | `&nbsp;` |  |
| `file` | `&nbsp;` |  |

**Description**

-> size of the written file

---

### readToOctet

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `type` | `&nbsp;` |  |
| `name` | `&nbsp;` |  |

**Description**

-> the resource as an octet

---

### enumTypes

Method

**Return value**

[ type1, type2, ... ]

**Description**

Lists the resource types

---

### enumNames

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `type` | `&nbsp;` | Resource type (a string, a number, or an rt* constant). |

**Return value**

[ name1, name2, ... ]

**Description**

Lists the resource names

---

### enumLangs

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `type` | `&nbsp;` | Resource type (a string, a number, or an rt* constant). |
| `name` | `&nbsp;` | Resource name (a string or a number). |

**Return value**

[ lang1, lang2, ... ]
Note that each language is a single number combining primaryLang and subLang.
To pass it to setLang, use setLang(lang&0x3FF, lang>>10).

**Description**

Lists the resource languages

---
