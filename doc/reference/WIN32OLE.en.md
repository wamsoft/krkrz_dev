# WIN32OLE

Creates an object for controlling OLE.
Methods that the OLE object exposes through IDispatch can be called directly.

## Members

### Constructors

- [WIN32OLE](#win32ole)

### Methods

- [invoke](#invoke)
- [set](#set)
- [get](#get)
- [getConstant](#getconstant)
- [addEvent](#addevent)

---

### WIN32OLE

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

**Description**

Constructor

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

### getConstant

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `obj` | `this` | Stores the constants as properties of the given object.<br>If omitted, they are stored in this object. |

**Description**

Gets constants

---

### addEvent

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `eventName` | `&nbsp;` | Event interface name (e.g. "DWebBrowser2Events2"). |
| `receiver` | `&nbsp;` | Object that receives the events.<br>The method whose name matches the event name is called.<br>If there is no such method, nothing happens. |

**Description**

Registers an event receiver object

---
