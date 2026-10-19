# JScriptHost

Host for running JScript. Uses IActiveScript to evaluate JScript expressions and get their results.
Example:
var js = new JScriptHost();
var r = js.eval("1+2"); // -> 3
js.addGlobal("tvp", global); // expose the TJS global object to JScript
var v = js.eval("tvp.version");

## Members

### Constructors

- [JScriptHost](#jscripthost)

### Methods

- [eval](#eval)
- [addGlobal](#addglobal)
- [reset](#reset)
- [invoke](#invoke)
- [set](#set)
- [get](#get)
- [missing](#missing)

---

### JScriptHost

Constructor

**Description**

Constructor

Creates and connects a JScript engine.

---

### eval

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `code` | `&nbsp;` | JScript expression to evaluate, as a string. |

**Return value**

The result (number, string, bool, wrapped IDispatch, etc.).

**Description**

Evaluates an expression

---

### addGlobal

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Name used to refer to it from JScript. |
| `obj` | `&nbsp;` | Object to add (a TJS object, exposed as IDispatch). |

**Description**

Adds a global object (registers it in JScript's list of named objects)

---

### reset

Method

**Description**

Reinitializes the engine

Resets the script state.

---

### invoke

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Method name. |
| `...` | `&nbsp;` | Arguments to pass. |

**Description**

Invokes a method

---

### set

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Property name. |
| `value` | `&nbsp;` |  |

**Description**

Sets a property

---

### get

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Property name. |

**Return value**

The property value.

**Description**

Gets a property

---

### missing

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `...` | `&nbsp;` |  |

**Description**

TJS missing handler. Unregistered names are tried as set/get/invoke as-is

---
