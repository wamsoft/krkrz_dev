# Debug

The Debug class provides debugging features for Kirikiri. You cannot create objects of this class.

Kirikiri's console log is named krkr.console.log. The file created when a hardware exception occurs is named hwexcept.log.

By default these log files are written to the project directory. However, they are not written if the project directory cannot be written to, such as when it is an archive.

You can change where log files are written with the logLocation property.

## Members

### Properties

- [logLocation](#loglocation)
- [logToFileOnError](#logtofileonerror)
- [clearLogFileOnError](#clearlogfileonerror)

### Methods

- [message](#message)
- [notice](#notice)
- [startLogToFile](#startlogtofile)
- [logAsError](#logaserror)
- [addLoggingHandler](#addlogginghandler)
- [removeLoggingHandler](#removelogginghandler)
- [getLastLog](#getlastlog)
- [prettyPrint](#prettyprint)

---

### logLocation

Property \ Access: `r/w`

**Description**

Log file location

Represents the directory log files are written to. This property can also be written.

By default it is set to the data folder (the -datapath command-line option).

After you change this value, subsequent logs are written as *.console.log under that directory.

---

### logToFileOnError

Property \ Access: `r/w`

**Description**

Whether to write the console log to a file when an error occurs

If true, writing the console log to a file starts when an error
occurs.

If false, writing the log to a file does not start even when an error occurs.

**See also:** [Debug.startLogToFile](Debug.md#startlogtofile) / [Debug.clearLogFileOnError](Debug.md#clearlogfileonerror)

---

### clearLogFileOnError

Property \ Access: `r/w`

**Description**

Whether to clear the console log file when an error occurs

If true, the console log is cleared automatically when an error occurs.

If false, it is not cleared and the log is appended to the existing log file.

**See also:** [Debug.startLogToFile](Debug.md#startlogtofile) / [Debug.logToFileOnError](Debug.md#logtofileonerror)

---

### message

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `message` | `&nbsp;` | Message to write. |

**Description**

Writes a message to the console

Writes a message to the **console**.

---

### notice

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `message` | `&nbsp;` | Message to write. |

**Description**

Writes an important message to the console

Writes a message to the **console**.

Unlike [Debug.message](Debug.md#message), messages written here are always written to the log file, even if writing to the log file
starts partway through (messages written with Debug.message are written only back to a certain point).
Use it for important information that will be useful when log files are collected.

---

### startLogToFile

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `clear` | `false` | If true, the log file is cleared.<br>If false, the log is appended to the existing file. |

**Description**

Starts writing the console log to a file

Starts writing the console log to a file.

**See also:** [Debug.logToFileOnError](Debug.md#logtofileonerror) / [Debug.clearLogFileOnError](Debug.md#clearlogfileonerror)

---

### logAsError

Method

**Description**

Starts writing the log to a file as if an error had occurred

Makes Kirikiri handle the error log file the same way it does when an error occurs.
That is, if
[Debug.logToFileOnError](Debug.md#logtofileonerror) is true, it starts writing the console log
to a file, and if [Debug.clearLogFileOnError](Debug.md#clearlogfileonerror) is true, it clears
the file first.

In contrast, [Debug.startLogToFile](Debug.md#startlogtofile) unconditionally starts writing the console log
to a file.

**See also:** [Debug.startLogToFile](Debug.md#startlogtofile) / [Debug.logToFileOnError](Debug.md#logtofileonerror) / [Debug.clearLogFileOnError](Debug.md#clearlogfileonerror)

---

### addLoggingHandler

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `handler` | `&nbsp;` | Logging handler. |

**Description**

Adds a logging handler

Registers a handler that is called each time an error log entry is written.

The handler is called with the log message as its argument.

Logging from within the registered method does not cause a recursive call; it is ignored.

---

### removeLoggingHandler

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `handler` | `&nbsp;` | Logging handler. |

**Description**

Removes a logging handler

Removes a registered logging handler.

---

### getLastLog

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `lines` | `void` | Number of lines to get. If omitted, up to the maximum number of<br>lines held is returned. |

**Description**

Gets log lines not yet written

Gets log lines that have not been written out yet.

---

### prettyPrint

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `value` | `&nbsp;` | Value to format. |
| `depth` | `2` | Depth of recursive expansion. Default is 2. |
| `compact` | `false` | If true, produces compact single-line output. Default is false. |

**Return value**

The formatted string.

**Description**

Pretty-prints a value

Formats any TJS value, including the contents of dictionaries, arrays and objects, into a readable string
and returns it. Intended for debugging in the REPL and in log output.

---
