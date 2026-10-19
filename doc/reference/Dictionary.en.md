# Dictionary

## Members

### Methods

- [saveStruct2](#savestruct2)
- [toStructString](#tostructstring)

---

### saveStruct2

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `&nbsp;` | Destination file. |
| `utf8` | `false` | Output encoding. true for UTF-8, false for the current code page. |
| `newline` | `0` | Newline code. 0: CRLF, 1: LF. |
| `option` | `0` | Formatting options: a combination of sso* flags (see below), or a numeric value. |

**Description**

Saves data in a format compatible with saveStruct

---

### toStructString

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `newline` | `1` | Newline code. 0: CRLF, 1: LF. |
| `option` | `0` | Formatting options: a combination of sso* flags (see below), or a numeric value. |

**Return value**

A string in a format compatible with saveStruct.

---
