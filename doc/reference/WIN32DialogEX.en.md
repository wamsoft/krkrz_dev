# WIN32DialogEX

A wrapper that makes WIN32Dialog a little easier to use from Kirikiri.
Load it with Scripts.execStorage("win32dialog.tjs").
See that source file and the samples for details.

Extends: [WIN32Dialog](WIN32Dialog.md)

## Members

### Methods

- [store](#store)
- [setInitParams](#setinitparams)
- [open](#open)
- [setCenterPosition](#setcenterposition)
- [loadResource](#loadresource)
- [DefPushButton](#defpushbutton)
- [PushButton](#pushbutton)
- [AutoCheckBox](#autocheckbox)
- [CheckBox](#checkbox)
- [AutoRadioButton](#autoradiobutton)
- [RadioButton](#radiobutton)
- [GroupBox](#groupbox)
- [LText](#ltext)
- [CText](#ctext)
- [RText](#rtext)
- [Icon](#icon)
- [EditText](#edittext)
- [ListBox](#listbox)
- [ComboBox](#combobox)

---

### store

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `elm` | `&nbsp;` | Template dictionary.<br>elm = %[ helpID, exStyle, style, x, y, cx, cy, menu, windowClass, title, pointSize, weight, italic, charset, typeFace,<br>items: [ control1, control2, ... ] ]; |

**Description**

Loads a template

For controls, call the control creation functions.

---

### setInitParams

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `elm` | `&nbsp;` | Parameter dictionary. |

**Description**

Sets the initialization parameters of the items

Always call this after store(). See win32dialog.tjs and testscript.tjs for the parameters.

---

### open

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `parent` | `&nbsp;` |  |

**Return value**

%[ result: the nResult value passed to EndDialog, items: dictionary of item states ];

**Description**

Shows the dialog

Note that the return value differs from WIN32Dialog.open.

---

### setCenterPosition

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `win` | `parent` | Window (if omitted, the window passed to open is used).<br>Passing null centers the dialog on the screen. |

**Description**

Centers the dialog on the given window

---

### loadResource

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `dllfile` | `&nbsp;` | DLL file (Storages.getPlacedPath/getLocalName are applied automatically). |
| `resource` | `&nbsp;` | Dialog resource name. |

**Description**

Loads a dialog resource (override)

---

### DefPushButton

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `text` | `&nbsp;` | Text. |
| `id` | `&nbsp;` | Control ID. |
| `x` | `&nbsp;` | X coordinate (in dialog units). |
| `y` | `&nbsp;` | Y coordinate (in dialog units). |
| `w` | `&nbsp;` | Width (in dialog units). |
| `h` | `&nbsp;` | Height (in dialog units). |
| `style` | `&nbsp;` | Style. |
| `ex` | `&nbsp;` | Extended style. |

**Description**

Functions for creating the various controls

---

### PushButton

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `text` | `&nbsp;` |  |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---

### AutoCheckBox

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `text` | `&nbsp;` |  |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---

### CheckBox

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `text` | `&nbsp;` |  |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---

### AutoRadioButton

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `text` | `&nbsp;` |  |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---

### RadioButton

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `text` | `&nbsp;` |  |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---

### GroupBox

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `text` | `&nbsp;` |  |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---

### LText

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `text` | `&nbsp;` |  |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---

### CText

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `text` | `&nbsp;` |  |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---

### RText

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `text` | `&nbsp;` |  |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---

### Icon

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `text` | `&nbsp;` |  |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---

### EditText

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---

### ListBox

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---

### ComboBox

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---
