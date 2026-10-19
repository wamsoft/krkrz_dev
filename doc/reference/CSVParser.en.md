# CSVParser

## Members

### Constructors

- [CSVParser](#csvparser)

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

### CSVParser

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `target` | `&nbsp;` | Target to forward events to. If omitted, events are sent to this object. |
| `separator` | `&nbsp;` | Separator character. Defaults to ",". |
| `newline` | `&nbsp;` | Newline character used in data when a field spans lines. Defaults to "\\r\\n". |

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
| `readmode` | `false` | Read mode.<br>typeof readmode == "String"  : reads the text the same way as Array.load<br>typeof readmode == "Integer" : true reads as UTF-8; otherwise reads as CP_ACP text<br>Note: if the plugin is compiled with /D:CSVPARSER_DEFAULT_TEXTSTREAM=1, readmode='' becomes the default when omitted. |

**Description**

Initializes the text to process

---

### getNextLine

Method

**Return value**

Column data (Array).

**Description**

Gets the next line as an array

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
| `readmode` | `&nbsp;` | Read mode (see initStorage for details). |

**Description**

Parses text

---

### doLine

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `columns` | `&nbsp;` | Column data (Array). |
| `lineNo` | `&nbsp;` | Logical line number (starting at 1). |

**Description**

Event called from parse/parseStorage

---
