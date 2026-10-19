# LineParser

## Members

### Constructors

- [LineParser](#lineparser)

### Properties

- [currentLineNumber](#currentlinenumber)

### Methods

- [init](#init)
- [initStorage](#initstorage)
- [getNextLine](#getnextline)
- [parse](#parse)
- [parseStorage](#parsestorage)
- [doLine](#doline)

---

### LineParser

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `target` | `&nbsp;` | Target to forward events to. If omitted, events are sent to this object. |

**Description**

Constructor

---

### currentLineNumber

Property \ Access: `r/w`

**Description**

Gets the number of the line processed so far

---

### init

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `text` | `&nbsp;` | Text. |

**Description**

Initializes the text to process

---

### initStorage

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `&nbsp;` | File name of the text. |
| `utf8` | `false` | true for a UTF-8 file. |

**Description**

Initializes the text to process

---

### getNextLine

Method

**Return value**

The line.

**Description**

Gets the next line as a string

---

### parse

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `text` | `&nbsp;` | Text. If omitted, the currently set text is parsed. |

**Description**

Parses text

Calls the doLine() event for each line.

---

### parseStorage

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `&nbsp;` | File name of the text. |
| `utf8` | `false` | true for a UTF-8 file. |

**Description**

Parses text

---

### doLine

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `text` | `&nbsp;` | Text of the line. |
| `lineNo` | `&nbsp;` | Line number (starting at 1). |

**Description**

Event called from parse/parseStorage

---
