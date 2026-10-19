# Console

Debug.console extensions

Note: these fail unless the console window has been created at least once after startup by setting visible=true.

## Members

### Methods

- [restoreMaximize](#restoremaximize)
- [maximize](#maximize)
- [getRect](#getrect)
- [setPos](#setpos)
- [getPlacement](#getplacement)
- [setPlacement](#setplacement)
- [bringAfter](#bringafter)

---

### restoreMaximize

Method

**Description**

Restores the window from the maximized state (works around the window size being wrong on the next launch if the program exits while maximized)

---

### maximize

Method

**Description**

Maximizes the window

---

### getRect

Method

**Description**

Gets the position and size

---

### setPos

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |

**Description**

Sets the position and size

---

### getPlacement

Method

**Description**

Gets the WindowPlacement

---

### setPlacement

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `dict` | `&nbsp;` |  |

**Description**

Sets the WindowPlacement

---

### bringAfter

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `win` | `&nbsp;` |  |

**Description**

Changes the z-order

---
