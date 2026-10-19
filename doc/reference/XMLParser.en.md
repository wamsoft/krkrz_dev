# XMLParser

Manual written as pseudo-code

Copyright 2005-2009 GoWatanabe

Parsing is done by expat, and the corresponding methods are called back automatically.
See XML.tjs for a concrete DOM implementation example.

## Members

### Properties

- [errorCode](#errorcode)
- [errorString](#errorstring)
- [currentByteIndex](#currentbyteindex)
- [currentLineNumber](#currentlinenumber)
- [currentColumnNumber](#currentcolumnnumber)
- [currentByteCount](#currentbytecount)

### Methods

- [parse](#parse)
- [parseStorage](#parsestorage)

---

### errorCode

Property \ Access: `r`

**Description**

Error code (number)

---

### errorString

Property \ Access: `r`

**Description**

Error code (string)

---

### currentByteIndex

Property \ Access: `r`

**Description**

Current byte index

---

### currentLineNumber

Property \ Access: `r`

**Description**

Current line number

---

### currentColumnNumber

Property \ Access: `r`

**Description**

Current column number

---

### currentByteCount

Property \ Access: `r`

**Description**

Current byte count

---

### parse

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `text` | `&nbsp;` | Text. If omitted, the currently set text is parsed. |

**Description**

Parses text

---

### parseStorage

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `&nbsp;` | File name of the text. |

**Description**

Parses text

---
