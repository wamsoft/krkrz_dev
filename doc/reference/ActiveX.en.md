# ActiveX

Creates an object for controlling an ActiveX control.
Methods that the ActiveX control exposes through IDispatch can be called directly.

Extends: [WIN32OLE](WIN32OLE.md)

## Members

### Constructors

- [ActiveX](#activex)

### Properties

- [isValidWindow](#isvalidwindow)
- [left](#left)
- [top](#top)
- [width](#width)
- [height](#height)
- [visible](#visible)

### Methods

- [setPos](#setpos)
- [setSize](#setsize)
- [setExternalUI](#setexternalui)
- [onCreate](#oncreate)
- [onDestroy](#ondestroy)

---

### ActiveX

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | ProgID or CLSID, as a string. Note that the CLSID format differs from WIN32OLE: it uses the CAxWindow::CreateControl format. |
| `win` | `null` | If given, the control is created on that window. If omitted, it becomes a standalone window. |
| `left` | `0` | Display position. If a window is given and this is omitted, the top-left of the window's client area. |
| `top` | `0` | Display position. If a window is given and this is omitted, the top-left of the window's client area. |
| `width` | `100` | Display size. If a window is given and this is omitted, the size of the parent window's client area. |
| `height` | `100` | Display size. If a window is given and this is omitted, the size of the parent window's client area. |

**Description**

Constructor

---

### isValidWindow

Property \ Access: `r`

**Description**

Whether the window is valid (read-only)

---

### left

Property \ Access: `r/w`

**Description**

Left edge coordinate

---

### top

Property \ Access: `r/w`

**Description**

Top edge coordinate

---

### width

Property \ Access: `r/w`

**Description**

Width

---

### height

Property \ Access: `r/w`

**Description**

Height

---

### visible

Property \ Access: `r/w`

**Description**

Visibility

---

### setPos

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `left` | `&nbsp;` | Left edge coordinate. |
| `top` | `&nbsp;` | Top edge coordinate. |

**Description**

Sets the position

---

### setSize

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `width` | `&nbsp;` | Width. |
| `height` | `&nbsp;` | Height. |

**Description**

Sets the size

---

### setExternalUI

Method

**Description**

Enables the external UI

Only meaningful for the IE component. In the current version, calling this
suppresses the context menu.

---

### onCreate

Method

**Description**

Event called after the window has been created

Called after the window is created, for example on initial creation or when switching to full screen.
After re-creation, all registered events are discarded and various other state is
reset, so re-apply whatever you need inside this event.

---

### onDestroy

Method

**Description**

Event called before the window is destroyed

Called before the window is destroyed, for example when switching to full screen or when the object is destroyed.

---
