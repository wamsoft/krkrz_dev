# Scripts

The Scripts class manages methods and properties related to TJS2. You cannot create objects of this class.

## Members

### Properties

- [textEncoding](#textencoding)

### Methods

- [execStorage](#execstorage)
- [evalStorage](#evalstorage)
- [compileStorage](#compilestorage)
- [exec](#exec)
- [eval](#eval)
- [dump](#dump)
- [getTraceString](#gettracestring)
- [setCallMissing](#setcallmissing)
- [getClassNames](#getclassnames)
- [dumpStringHeap](#dumpstringheap)

---

### textEncoding

Property \ Access: `r/w`

**Description**

Text encoding used to read scripts

Specifies the text encoding used to read scripts.

Currently either "UTF-8" or "Shift_JIS" can be specified.

---

### execStorage

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `storage` | `&nbsp;` | Storage to execute. |
| `mode` | `''` | Mode string used when reading the file. "o" followed by a decimal offset starts reading from that byte position in the file. |
| `context` | `global` | Execution context. |

**Return value**

The result of executing the script.

**Description**

Executes a script in a storage

Reads the specified storage and executes its contents as a TJS2 script.

Exceptions raised while the script runs are not caught inside this method, so the caller
can catch them.

**See also:** [Scripts.evalStorage](Scripts.md#evalstorage)

---

### evalStorage

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `storage` | `&nbsp;` | Storage to evaluate. |
| `mode` | `''` | Mode string used when reading the file. "o" followed by a decimal offset starts reading from that byte position in the file. |
| `context` | `global` | Execution context. |

**Return value**

The result of evaluating the expression.

**Description**

Evaluates an expression in a storage

Reads the specified storage and evaluates its contents as a TJS2 expression.

Exceptions raised while the script runs are not caught inside this method, so the caller
can catch them.

**See also:** [Scripts.execStorage](Scripts.md#execstorage)

---

### compileStorage

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `inputfile` | `&nbsp;` | Storage to compile. |
| `outputfile` | `&nbsp;` | Output bytecode storage. |
| `isresult` | `false` | Whether a return value is needed. |
| `outputdebug` | `false` | Whether to include debug information. |
| `isexpression` | `false` | Whether the contents are an expression. |

**Description**

Compiles a script in a storage

Reads the specified storage, compiles its contents and writes them out as a bytecode file.

The compiled bytecode file can be run with execStorage or evalStorage just like a regular script.

**See also:** [Scripts.execStorage](Scripts.md#execstorage) / [Scripts.evalStorage](Scripts.md#evalstorage)

---

### exec

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `script` | `&nbsp;` | Script to execute, as a string. |
| `name` | `''` | File name used in error messages |
| `linesof` | `0` | Line number used in error messages |
| `context` | `global` | Execution context. |

**Return value**

The result of executing the script.

**Description**

Executes a script

Executes the string given in script as a TJS2 script.

Exceptions raised while the script runs are not caught inside this method, so the caller
can catch them.

**See also:** [Scripts.execStorage](Scripts.md#execstorage) / [Scripts.eval](Scripts.md#eval)

---

### eval

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `expression` | `&nbsp;` | Expression to execute, as a string. |
| `name` | `''` | File name used in error messages |
| `linesof` | `0` | Line number used in error messages |
| `context` | `global` | Execution context. |

**Return value**

The result of evaluating the expression.

**Description**

Evaluates an expression

Executes the string given in expression as a TJS2 expression.

Exceptions raised while the script runs are not caught inside this method, so the caller
can catch them.

**See also:** [Scripts.execStorage](Scripts.md#execstorage) / [Scripts.exec](Scripts.md#exec)

---

### dump

Method

**Description**

Dumps contexts

Writes detailed contents of each context in the script blocks currently loaded into TJS2
to a local file. The output is mainly a disassembly of the VM code.

The file is written to the same folder as the Kirikiri executable, and its name is
the executable's file name with .dump.txt appended.

---

### getTraceString

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `limit` | `0` | Maximum call depth to retrieve. If omitted or 0, as much history as possible is retrieved. |

**Return value**

The call history as a string

**Description**

Gets the call stack

Gets the method call history (call stack) as a string, as of the moment this method is called.

To use this method, debug mode must be enabled with the -debug command-line option. If debug mode is disabled, this method returns an empty string.

The returned string looks like 'messagelayer.tjs(1561)[(function) addButton] <-- mainwindow.tjs(4463)[(function expression) (anonymous)] <-- conductor.tjs(427)[(function) onTag] <-- conductor.tjs(95)[(function) timerCallback]'.

---

### setCallMissing

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `missing` | `&nbsp;` | Handler called when a member is not found. |

**Description**

Registers a handler called when a member is not found

Registers a handler that is called when a member is not found.

---

### getClassNames

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `object` | `&nbsp;` | Object whose class names to get. |

**Return value**

Array of class names

**Description**

Gets class names

Gets the class names of an object.

---

### dumpStringHeap

Method

**Description**

Dumps the string heap

Writes the contents of the string heap managed by the TJS2 runtime to the debug output.
Can be called only on an engine built with `TJS_DEBUG_DUMP_STRING` enabled.
Intended solely for debugging, such as investigating memory leaks.

---

## Plugin extension: json

Manual written as pseudo-code

### Members

#### Methods

- [evalJSON](#evaljson)
- [evalJSONStorage](#evaljsonstorage)
- [saveJSON](#savejson)
- [toJSONString](#tojsonstring)

---

### evalJSON

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `jsonText` | `&nbsp;` | Text containing JSON |

**Return value**

Array or Dictionary

**Description**

Parses a JSON string and returns an Array or Dictionary

---

### evalJSONStorage

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `jsonFile` | `&nbsp;` | File name of the text file containing JSON |
| `utf8` | `false` | Input encoding. true for UTF-8, false for the current code page |

**Return value**

Array or Dictionary

**Description**

Parses a JSON file and returns an Array or Dictionary

---

### saveJSON

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `jsonFile` | `&nbsp;` | Destination file |
| `obj` | `&nbsp;` | Object to save |
| `utf8` | `false` | Output encoding. true for UTF-8, false for the current code page |
| `newline` | `0` | Line ending 0:CRLF 1:LF |

**Description**

Saves data in JSON format

---

### toJSONString

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `obj` | `&nbsp;` |  |
| `newline` | `0` | Line ending 0:CRLF 1:LF |

**Return value**

Text in JSON format

**Description**

Converts data to a JSON string

---

## Plugin extension: saveStruct

### Members

#### Methods

- [toStructString](#tostructstring)

---

### toStructString

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `target` | `&nbsp;` | Value to stringify (besides dictionaries and arrays, int/real/string/octet/null/void are also accepted) |
| `newline` | `1` | Line ending 0:CRLF 1:LF |
| `option` | `ssoIndent\|ssoSort` | Formatting options: a combination of sso* (described below) or a numeric value |

**Return value**

A string in the same form as saveStruct produces

**Description**

Note that the default value of option differs from that of Array/Dictionary (intended for debugging).

---

## Plugin extension: scriptsEx

### Members

#### Methods

- [getObjectKeys](#getobjectkeys)
- [getObjectCount](#getobjectcount)
- [getObjectContext](#getobjectcontext)
- [isNullContext](#isnullcontext)
- [equalStruct](#equalstruct)
- [equalStructNumericLoose](#equalstructnumericloose)
- [foreach](#foreach)
- [getMD5HashString](#getmd5hashstring)
- [clone](#clone)
- [rehash](#rehash)
- [propSet](#propset)
- [propGet](#propget)
- [safeEvalStorage](#safeevalstorage)

---

### getObjectKeys

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `obj` | `&nbsp;` | Target object |

**Return value**

Array containing the keys

**Description**

Returns the list of an object's member names

---

### getObjectCount

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `obj` | `&nbsp;` | Target object |

**Return value**

The number of members

**Description**

Returns the number of an object's members

---

### getObjectContext

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `obj` | `&nbsp;` | Target object |

**Return value**

Context object

**Description**

Returns an object's context

---

### isNullContext

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `obj` | `&nbsp;` | Target object |

**Return value**

true if the context is null

**Description**

Checks an object's context

---

### equalStruct

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `obj1` | `&nbsp;` | First object |
| `obj2` | `&nbsp;` | Second object |

**Return value**

true if equal

**Description**

Compares two objects. For dictionaries and arrays, their elements are compared recursively

---

### equalStructNumericLoose

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `obj1` | `&nbsp;` | First object |
| `obj2` | `&nbsp;` | Second object |

**Return value**

true if equal

**Description**

Compares two objects. For dictionaries and arrays, their elements are compared recursively

Numbers are compared loosely (0.0 and 0 are treated as equal).

---

### foreach

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `obj` | `&nbsp;` | Object to process (dictionary or array) |
| `func` | `&nbsp;` | Function to call. It is called as func(key, value, args*).<br>If its context is null, as with an anonymous function, it automatically runs with the this context.<br>If the function returns any value, iteration stops. |
| `args*` | `&nbsp;` |  |

**Return value**

The value returned when iteration was stopped

**Description**

Iterates over all members of an object

---

### getMD5HashString

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `octet` | `&nbsp;` | Target octet |

**Return value**

Hash value (32-character lowercase hexadecimal string)

**Description**

Gets the MD5 hash of an octet

---

### clone

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `obj` | `&nbsp;` | Value to clone<br>void, numbers, strings and octets are returned as is.<br>Dictionary and array objects are deep-copied; nested values are processed recursively.<br>For other objects, the return value of their "clone" method is returned if it exists; otherwise the original value is returned as is. |

**Description**

Returns a clone of a value.

---

### rehash

Method

**Description**

Calls TJSDoRehash()

Sets the flag that rebuilds the hash table size of TJSCustomObject-based objects.
(This covers dictionaries and most class and instance objects.)

Explanation:
The hash table size is determined by the number of elements the object holds.
After the flag is set, the size is recalculated the next time something is written to the object,
and the table is rebuilt only if its size changes. (Size is roughly 2^(bit count of the element count + 2)?)
Normally Kirikiri calls TJSDoRehash() periodically (when idle and at least 1.5 seconds have passed since the last call),
so you usually do not need to worry about it.
However, when adding a large number of elements without any idle time in between,
it may be effective to call this at intervals such as once every few thousand to tens of thousands of additions, using a counter.

---

### propSet

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `obj` | `&nbsp;` | Target object |
| `member` | `&nbsp;` | Member name (if typeof member == "Integer", Prop{Set,Get}ByNum is called) |
| `value` | `&nbsp;` | Value to set (propSet only) |
| `flag` | `Scripts.pfMemberEnsure` | Flags (a combination of Scripts.pf* joined with "\|" (or), or 0)<br>Scripts.pfMemberEnsure    : (set) Specify when adding a new member (without it, only existing members can be rewritten)<br>Scripts.pfMemberMustExist : (get) Error if the member does not exist (undefined dictionary entries also raise an error instead of returning void)<br>Scripts.pfIgnoreProp      : (get/set) Ignore property behavior (same as the & specifier in TJS)<br>Scripts.pfHiddenMember    : (set) Hidden member (ignored by EnumMembers-based processing such as assignStruct/saveStruct)<br>Scripts.pfStaticMember    : (set) Static member (used for class objects and the like) |

**Return value**

The retrieved value (propGet only; void for set)

**Description**

Calls PropSet/PropGet on the specified object

---

### propGet

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `obj` | `&nbsp;` |  |
| `member` | `&nbsp;` |  |
| `flag` | `Scripts.pfMemberMustExist` |  |

---

### safeEvalStorage

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `storage` | `&nbsp;` | Storage to evaluate (bytecode binaries are not allowed; intended for dictionaries/arrays saved by saveStruct with (const)) |
| `mode` | `&nbsp;` | Mode string |
| `context` | `&nbsp;` | Execution context |

**Return value**

The evaluated data

**Description**

Safely evaluates a dictionary/array marked (const)

---

## Plugin extension: windowEx

Scripts extensions

### Members

#### Methods

- [setEvalErrorLog](#setevalerrorlog)

---

### setEvalErrorLog

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `enabled` | `&nbsp;` | Whether logging is allowed |

**Return value**

The previous value

**Description**

Suppresses error logging from Scripts.eval

Setting enabled to false makes Scripts.eval evaluate through
TVPExecuteExpression, so no log is written when an exception occurs.
Note that this behavior may change in future versions of Kirikiri.

---
