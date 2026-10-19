# MenuItem

This class is extended by several plugins.

## Plugin extension: menu

### Members

#### Constructors

- [MenuItem](#menuitem)

#### Properties

- [HMENU](#hmenu)
- [caption](#caption)
- [checked](#checked)
- [children](#children)
- [enabled](#enabled)
- [group](#group)
- [index](#index)
- [parent](#parent)
- [radio](#radio)
- [root](#root)
- [shortcut](#shortcut)
- [visible](#visible)
- [window](#window)

#### Methods

- [add](#add)
- [insert](#insert)
- [popup](#popup)
- [remove](#remove)
- [onClick](#onclick)

---

### MenuItem

Constructor

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `window` | `Window` | `&nbsp;` | Window in which to create this menu item. |
| `caption` | `string` | `""` | Caption (displayed text) of the menu item.<br>Can be set and read with the MenuItem.caption property. |

**Description**

Constructs a MenuItem object

Constructs an object of the MenuItem class.
To add the created menu item to a parent menu item, use the parent's MenuItem.add method.

---

### HMENU

Property \ Access: `r`

**Description**

HMENU menu item handle

The menu item handle of type HMENU in the Windows API.
Use this property when a plugin or the like needs direct access to the menu item.
Accessing it from TJS2 is meaningless.
The value is an integer; when using it in a plugin, cast it to HMENU.

---

### caption

Property \ Access: `r/w`

**Description**

Caption

The caption (displayed text). Can also be set.
Specifying '-' (a hyphen) displays a separator.

---

### checked

Property \ Access: `r/w`

**Description**

Whether to show a check mark

Whether a check mark is shown next to the menu item. Can also be set.
true shows the check mark.
If the MenuItem.radio property is true, a filled circle is shown instead of a check mark.
Among menu items that have the same group number in MenuItem.group, the same parent, and the MenuItem.radio property set to true, no more than one can have this property true at a time. When this property becomes true on one menu item, it is automatically set to false on any other menu item that had it true.

---

### children

Property \ Access: `r`

**Description**

Child menu items

An array object listing the child menu items.
Writing values to this array, or removing or adding entries, is not reflected in the actual menu items. Treat it as read-only.

---

### enabled

Property \ Access: `r/w`

**Description**

Whether the item can be selected

Whether the menu item can be selected. Can also be set.
true makes the menu item selectable; false makes it unselectable.

---

### group

Property \ Access: `r/w`

**Description**

Group number

The group number. Can also be set.
Among menu items that have the same group number, the same parent, and the MenuItem.radio property set to true, no more than one can have the MenuItem.checked property true at a time.

---

### index

Property \ Access: `r/w`

**Description**

Order

A zero or positive integer giving the order among menu items with the same parent.
0 means the first.
Useful for getting or changing the current position.
Setting a value moves the menu item to that position.

---

### parent

Property \ Access: `r`

**Description**

Parent menu item

The parent menu item.

---

### radio

Property \ Access: `r/w`

**Description**

Whether this is a radio item

Whether this is a radio item. Can also be set.
See the MenuItem.checked property for the behavior when this is true.

---

### root

Property \ Access: `r`

**Description**

Root menu item

The root (topmost) menu item (an instance of the MenuItem class).

---

### shortcut

Property \ Access: `r/w`

**Description**

Shortcut key

The shortcut key. Can also be set.
The shortcut key is given as a string combining modifier keys and the target key name. Case is ignored. Examples of valid shortcut keys:

"Shift+Esc"
"Ctrl+S"
"Shift+Alt+E"
"Alt+Enter"
"Ctrl+F1"
"T" (modifier keys can be omitted)

An invalid combination or "" (an empty string) disables the shortcut key.
In the current version, some keys whose use is predefined by the system or Kirikiri, such as Tab or Shift+F1, and some keys (such as Shift by itself) do not respond.
Once a shortcut key is set, events such as onKeyDown are no longer raised for that key; the event is raised only on the menu item that has the shortcut key.

---

### visible

Property \ Access: `r/w`

**Description**

Whether the item is visible

Whether the menu item is visible. Can also be set.
true shows it; false hides it.

---

### window

Property \ Access: `r`

**Description**

Owner window

The owner window (an object of the Window class) that holds this menu item.

---

### add

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `item` | `MenuItem` | `&nbsp;` | Child menu item to add.<br>It is added after the existing child menu items. |

**Description**

Adds a child menu item

Adds a child menu item.
Once a menu item becomes a child of another menu item, it is invalidated automatically when its parent is invalidated.
It also becomes the parent's child in the menu hierarchy.

---

### insert

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `item` | `MenuItem` | `&nbsp;` | Child menu item to insert. |
| `index` | `int` | `&nbsp;` | Position to insert at. 0 inserts at the beginning. |

**Description**

Inserts a child menu item

Inserts a child menu item at the given position.

---

### popup

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `flags` | `int` | `&nbsp;` | Flags describing the menu behavior. Specify a bitwise OR of the following values:<br>tpmLeftButton<br>tpmRightButton<br>tpmLeftAlign<br>tpmCenterAlign<br>tpmRightAlign<br>tpmTopAlign<br>tpmVCenterAlign<br>tpmBottomAlign<br>tpmHorizontal<br>tpmVertical<br>tpmNoNotify<br>tpmReturnCmd<br>tpmRecurse<br>tpmHorPosAnimation<br>tpmHorNegAnimation<br>tpmVerPosAnimation<br>tpmVerNegAnimation<br>tpmNoAnimation<br>See the corresponding MSDN page for details on these flags. |
| `x` | `int` | `&nbsp;` | X position in the window's client coordinates. |
| `y` | `int` | `&nbsp;` | Y position in the window's client coordinates. |

**Return value**

If tpmReturnCmd is given in flags, the ID of the selected menu item as an integer (however, the current version provides no way to set this ID from Kirikiri, so specifying tpmReturnCmd in flags is meaningless).
Returns 0 if the menu is canceled without a selection.

**Description**

Shows the menu item as a pop-up

Shows the menu item as a pop-up menu. This method does not return until the menu is closed.
Note that other asynchronous events may occur while the menu is open.
Window.menu itself cannot be shown as a pop-up.
Hidden menu items cannot be shown as a pop-up.
Menus that are not children of Window.menu cannot be shown as a pop-up.

---

### remove

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `item` | `MenuItem` | `&nbsp;` | Child menu item to remove. |

**Description**

Removes a child menu item

Removes the given child menu item from the list.

---

### onClick

Method

**Description**

The menu item was selected

Raised when the menu item is selected (clicked or the Enter key is pressed).

---

## Plugin extension: windowEx

MenuItem extensions

### Members

#### Properties

- [rightJustify](#rightjustify)
- [bmpChecked](#bmpchecked)
- [bmpUnchecked](#bmpunchecked)

#### Methods

- [popupEx](#popupex)

#### Constants

- [biSystem](#bisystem)
- [biRestore](#birestore)
- [biMinimize](#biminimize)
- [biClose](#biclose)
- [biCloseDisabled](#biclosedisabled)
- [biMinimizeDisabled](#biminimizedisabled)
- [biPopupClose](#bipopupclose)
- [biPopupRestore](#bipopuprestore)
- [biPopupMaximize](#bipopupmaximize)
- [biPopupMinimize](#bipopupminimize)

---

### rightJustify

Property \ Access: `r/w`

**Description**

Right-aligns items on the menu bar

If true, this item and the items after it are pushed to the right edge.
Note: does not work correctly unless the item is directly under Window.menu and visible.

---

### bmpChecked

Property \ Access: `r/w`

**Description**

Icon when checked (0 for the default)

Use the MenuItem.bi* constants, or pass a layer object.
Note: this has no effect unless the item is a child of Window.menu and visible at the time the value is set.
Also note that pull-down menus are not displayed unless extended events are registered with Window.registerExEvent().

---

### bmpUnchecked

Property \ Access: `r/w`

**Description**

Icon when unchecked (0 for the default)

The values and notes are the same as for bmpChecked.

---

### popupEx

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `flags` | `&nbsp;` |  |
| `x` | `cursorX` | Display position X (screen coordinates; the mouse cursor position if omitted). |
| `y` | `cursorY` | Display position Y (screen coordinates; the mouse cursor position if omitted). |
| `hwnd` | `this.root.window` | Owner window (the window the instance belongs to if omitted). |
| `rect` | `&nbsp;` | Area the menu must not overlap (%[ x, y, w, h ]; no restriction if omitted). |
| `menulist` | `this.children` | Array of menu entries (they need not be MenuItem instances; dictionaries are fine). |

**Return value**

The selected object.

**Description**

Shows a pop-up menu

Unlike MenuItem.popup, the item does not need to belong to a window menu, and the list can be given as, for example, an array of dictionaries.
Note that icons set with the bmp* properties are not shown in pop-ups opened by this function.

---

### biSystem

Constant

**Description**

HBMMENU_SYSTEM

---

### biRestore

Constant

**Description**

HBMMENU_MBAR_RESTORE

---

### biMinimize

Constant

**Description**

HBMMENU_MBAR_MINIMIZE

---

### biClose

Constant

**Description**

HBMMENU_MBAR_CLOSE

---

### biCloseDisabled

Constant

**Description**

HBMMENU_MBAR_CLOSE_D

---

### biMinimizeDisabled

Constant

**Description**

HBMMENU_MBAR_MINIMIZE_D

---

### biPopupClose

Constant

**Description**

HBMMENU_POPUP_CLOSE

---

### biPopupRestore

Constant

**Description**

HBMMENU_POPUP_RESTORE

---

### biPopupMaximize

Constant

**Description**

HBMMENU_POPUP_MAXIMIZE

---

### biPopupMinimize

Constant

**Description**

HBMMENU_POPUP_MINIMIZE

---
