# Process

Manual written as pseudo-code

Provides a mechanism for launching an external application and waiting for it to exit.

## Members

### Properties

- [status](#status)

### Methods

- [execute](#execute)
- [commandExecute](#commandexecute)
- [terminate](#terminate)
- [sendSignal](#sendsignal)
- [onExecuted](#onexecuted)
- [onOutput](#onoutput)

---

### status

Property \ Access: `r`

**Description**

Current state

0: not running
1: running

---

### execute

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `target` | `&nbsp;` | Program. |
| `param` | `void` | Arguments. |
| `folder` | `void` | Working folder (the current folder if omitted). |

**Return value**

true if the program was launched.

**Description**

Runs an external program in the background

The onExecuted event is raised when it finishes.

---

### commandExecute

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `target` | `&nbsp;` | Program. |
| `param` | `void` | Arguments. |
| `folder` | `void` | Working folder (the current folder if omitted). |

**Return value**

true if the program was launched.

**Description**

Runs a command-line program and captures its console output

The onOutput event is raised for each line of console output.
The onExecuted event is raised when it finishes.

---

### terminate

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `endCode` | `&nbsp;` | Exit code. |

**Description**

Forcibly terminates the running external program

---

### sendSignal

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `isBreak` | `&nbsp;` | Sends Ctrl+Break instead of Ctrl+C. |

**Return value**

true on success.

**Description**

Sends a Ctrl+C event (experimental: may not work in every environment)

---

### onExecuted

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `endCode` | `&nbsp;` | Exit code. |

**Description**

Event: the program has finished

---

### onOutput

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `line` | `&nbsp;` | Line number. |
| `text` | `&nbsp;` | Output text (one line at a time). |

**Description**

Event: console output

---
