# WIN32Dialog

A class for working with native Windows dialogs.
It is little more than an API wrapper and therefore very awkward to use,
but WIN32DialogEX, written in TJS and described later, makes life much easier.

## Members

### Constructors

- [WIN32Dialog](#win32dialog)

### Properties

- [left](#left)
- [top](#top)
- [width](#width)
- [height](#height)
- [modeless](#modeless)
- [HWND](#hwnd)
- [icon](#icon)
- [isValid](#isvalid)
- [propsheet](#propsheet)
- [progress](#progress)
- [progressValue](#progressvalue)
- [progressCanceled](#progresscanceled)

### Methods

- [loadResource](#loadresource)
- [makeTemplate](#maketemplate)
- [open](#open)
- [close](#close)
- [getItem](#getitem)
- [getItemID](#getitemid)
- [getItemClassName](#getitemclassname)
- [setItemInt](#setitemint)
- [getItemInt](#getitemint)
- [setItemText](#setitemtext)
- [getItemText](#getitemtext)
- [setItemEnabled](#setitemenabled)
- [getItemEnabled](#getitemenabled)
- [setItemFocus](#setitemfocus)
- [setItemPos](#setitempos)
- [setItemSize](#setitemsize)
- [getItemLeft](#getitemleft)
- [getItemTop](#getitemtop)
- [getItemWidth](#getitemwidth)
- [getItemHeight](#getitemheight)
- [setItemBitmap](#setitembitmap)
- [sendItemMessage](#senditemmessage)
- [getBaseUnits](#getbaseunits)
- [mapRect](#maprect)
- [invalidateRect](#invalidaterect)
- [setPos](#setpos)
- [setSize](#setsize)
- [setActive](#setactive)
- [onInit](#oninit)
- [onCommand](#oncommand)
- [onHScroll](#onhscroll)
- [onVScroll](#onvscroll)
- [onNotify](#onnotify)
- [onKeyDown](#onkeydown)
- [onKeyUp](#onkeyup)
- [messageBox](#messagebox)
- [chooseColor](#choosecolor)
- [show](#show)
- [InitCommonControls](#initcommoncontrols)
- [InitCommonControlsEx](#initcommoncontrolsex)
- [openPropertySheet](#openpropertysheet)
- [propSheetMessage](#propsheetmessage)
- [setMessageResult](#setmessageresult)
- [openProgress](#openprogress)
- [closeProgress](#closeprogress)
- [insertTab](#inserttab)
- [deleteTab](#deletetab)
- [deleteAllTab](#deletealltab)
- [getCurSel](#getcursel)
- [selectTab](#selecttab)
- [setScrollInfo](#setscrollinfo)
- [getScrollInfo](#getscrollinfo)

---

### WIN32Dialog

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `owner` | `&nbsp;` | Owner that receives event callbacks. null or this sends them to this object. |

**Description**

Constructor

---

### left

Property \ Access: `r`

**Description**

Left position of the dialog

Read-only. Use setPos to change the position and setSize to change the size.

---

### top

Property \ Access: `r`

**Description**

Top position of the dialog (read-only)

---

### width

Property \ Access: `r`

**Description**

Width of the dialog (read-only)

---

### height

Property \ Access: `r`

**Description**

Height of the dialog (read-only)

---

### modeless

Property \ Access: `r/w`

**Description**

Flag for modeless dialogs

If true, the dialog is opened modeless.
Note that in modeless mode, unless WS_VISIBLE is set in the dialog style,
the dialog is not shown automatically by open().

---

### HWND

Property \ Access: `r`

**Description**

Window handle of the dialog

---

### icon

Property \ Access: `r/w`

**Description**

Icon image of the dialog

An instance of the WIN32Dialog.Bitmap class: that image
null: the executable's icon
void: no icon

---

### isValid

Property \ Access: `r`

**Description**

Whether the dialog is open

---

### propsheet

Property \ Access: `r`

**Description**

Whether the dialog is shown as a property sheet

---

### progress

Property \ Access: `r`

**Description**

Whether a progress dialog is active

---

### progressValue

Property \ Access: `r/w`

**Description**

Updates the progress bar (a number from 0 to 100, or a negative value for the marquee speed)

---

### progressCanceled

Property \ Access: `r/w`

**Description**

Whether the progress was canceled (the target button is always IDCANCEL)

---

### loadResource

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `dllfile` | `&nbsp;` | DLL file (in local storage format). |
| `resource` | `&nbsp;` | Dialog resource name. |

**Description**

Loads a dialog resource

---

### makeTemplate

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `header` | `&nbsp;` | Dialog template header (must be an instance of the WIN32Dialog.Header class). |
| `items*` | `&nbsp;` | Dialog template items (must be instances of the WIN32Dialog.Items class). |

**Description**

Creates a dialog template

---

### open

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `window` | `&nbsp;` | Parent window (a Kirikiri Window object). No parent if omitted or void. |

**Description**

Opens the dialog

A dialog template must have been created with makeTemplate beforehand,
or a dialog resource loaded with loadResource.
Note that data from loadResource takes precedence over makeTemplate.

---

### close

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `result` | `&nbsp;` | Result value passed to the EndDialog API. |

**Description**

Closes the dialog

---

### getItem

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` | ID of the dialog item. |

**Return value**

HWND of the dialog item.

**Description**

Wrapper for GetDlgItem

---

### getItemID

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `hwnd` | `&nbsp;` | HWND of the dialog item. |

**Return value**

ID of the dialog item.

**Description**

Wrapper for GetDlgCtrlID

---

### getItemClassName

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` | ID of the dialog item. |

**Return value**

Class name of the dialog item.

**Description**

Wrapper for GetClassName

---

### setItemInt

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` | ID of the dialog item. |
| `value` | `&nbsp;` | Value to set (set only). |

**Return value**

The value obtained (get only).

**Description**

Wrappers for Get/SetDlgItemInt/Text

---

### getItemInt

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` |  |

---

### setItemText

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` |  |
| `value` | `&nbsp;` |  |

---

### getItemText

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` |  |

---

### setItemEnabled

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` | ID of the dialog item. |
| `value` | `&nbsp;` | Enabled / disabled (set only). |

**Return value**

The value obtained (get only).

**Description**

Sets or gets whether an item is enabled

---

### getItemEnabled

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` |  |

---

### setItemFocus

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` | ID of the dialog item. |

**Description**

Sets the focus to an item

---

### setItemPos

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` | ID of the dialog item. |
| `x` | `&nbsp;` | X coordinate of the dialog item. |
| `y` | `&nbsp;` | Y coordinate of the dialog item. |

**Description**

Changes or gets the position and size of an item

---

### setItemSize

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |

---

### getItemLeft

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` |  |

---

### getItemTop

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` |  |

---

### getItemWidth

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` |  |

---

### getItemHeight

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` |  |

---

### setItemBitmap

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` | ID of the dialog item. |
| `bmp` | `&nbsp;` | WIN32Dialog.Bitmap instance to set as the bitmap.<br>WIN32DialogEX also accepts a Layer instance. |

**Description**

Sets a bitmap on an item

---

### sendItemMessage

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` | ID of the dialog item. |
| `msg` | `&nbsp;` | Message to send. |
| `wparam` | `&nbsp;` | wparam to send. |
| `lparam` | `&nbsp;` | lparam to send. |

**Return value**

LRESULT

**Description**

Wrapper for SendDlgItemMessage

---

### getBaseUnits

Method

**Return value**

Result dictionary (%[ h: horizontal unit, v: vertical unit ]).

**Description**

Wrapper for GetDialogBaseUnit

---

### mapRect

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `rect` | `&nbsp;` | Rectangle dictionary (%[ left, top, right, bottom ]). |

**Return value**

Result dictionary (%[ left, top, right, bottom ]).

**Description**

Wrapper for MapDialogRect

---

### invalidateRect

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `rect` | `&nbsp;` | Rectangle dictionary (%[ left, top, right, bottom ]). |
| `erase` | `&nbsp;` | Whether to erase the background. |

**Return value**

true on success.

**Description**

Wrapper for InvalidateRect

---

### setPos

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | X coordinate. |
| `y` | `&nbsp;` | Y coordinate.<br>Note that this raises an error unless the dialog is shown. Change the position in onInit or later. |

**Description**

Sets the dialog position

---

### setSize

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `w` | `&nbsp;` | width |
| `h` | `&nbsp;` | height<br>Note that this raises an error unless the dialog is shown. |

**Description**

Sets the dialog size

---

### setActive

Method

**Description**

Activates the dialog

Note that versions before this method was added had a problem where setPos/setSize activated the dialog (they no longer do).

---

### onInit

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `msg` | `&nbsp;` | DlgProc message == WM_INITDIALOG. |
| `wparam` | `&nbsp;` | DlgProc WPARAM. |
| `lparam` | `&nbsp;` | DlgProc LPARAM. |

**Description**

Callback for WM_INITDIALOG

Note that the callback is called on owner.
If owner.onInit is not defined, nothing happens.

---

### onCommand

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `msg` | `&nbsp;` | DlgProc message == WM_COMMAND. |
| `wparam` | `&nbsp;` | DlgProc WPARAM. |
| `lparam` | `&nbsp;` | DlgProc LPARAM. |

**Description**

Callback for WM_COMMAND

Note that the callback is called on owner.
If owner.onCommand is not defined, nothing happens.

---

### onHScroll

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `msg` | `&nbsp;` | DlgProc message == WM_HSCROLL. |
| `wparam` | `&nbsp;` | DlgProc WPARAM. |
| `lparam` | `&nbsp;` | DlgProc LPARAM. |

**Description**

Callback for WM_HSCROLL

---

### onVScroll

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `msg` | `&nbsp;` | DlgProc message == WM_VSCROLL. |
| `wparam` | `&nbsp;` | DlgProc WPARAM. |
| `lparam` | `&nbsp;` | DlgProc LPARAM. |

**Description**

Callback for WM_VSCROLL

---

### onNotify

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `msg` | `&nbsp;` |  |
| `wparam` | `&nbsp;` | DlgProc WPARAM. |
| `lparam` | `&nbsp;` |  |

**Description**

Callback for WM_NOTIFY

---

### onKeyDown

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `wparam` | `&nbsp;` | DlgProc WPARAM. |
| `lparam` | `&nbsp;` | DlgProc LPARAM. |

**Description**

Callback for WM_KEYDOWN

---

### onKeyUp

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `wparam` | `&nbsp;` | DlgProc WPARAM. |
| `lparam` | `&nbsp;` | DlgProc LPARAM. |

**Description**

Callback for WM_KEYUP

---

### messageBox

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `window` | `&nbsp;` | Owner window (pass null if none). |
| `text` | `&nbsp;` | Message text. |
| `caption` | `&nbsp;` | Caption of the dialog box. |
| `type` | `&nbsp;` | Combination of flags for the buttons and icon to show. |

**Return value**

ID of the button pressed.
Setting the custom flag MB_OWNER_CENTER in type tries to center the box on the owner window
(but if the dialog would go off screen, it is centered on the desktop).

**Description**

Wrapper for MessageBox

---

### chooseColor

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `window` | `&nbsp;` | Owner window (pass null if none). |
| `elm` | `&nbsp;` | Options (a dictionary; optional).<br>%[ color: initially selected color, palette: [ palette color 1, ... , palette color 16 ],<br>disableCustomColor: disables custom colors, openCustomColor: opens the custom color section initially ] |

**Return value**

The selected color (0xRRGGBB), or void if canceled.
If elm.palette is given, its contents are updated as well.

**Description**

Wrapper for ChooseColor

---

### show

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `nCmdShow` | `&nbsp;` | SW_* flag. |

**Description**

Wrapper for ShowWindow

Mainly for modeless dialogs.

---

### InitCommonControls

Method

**Return value**

Whether it succeeded (Ex only).

**Description**

Wrapper for InitCommonControls and InitCommonControlsEx

---

### InitCommonControlsEx

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `icc` | `&nbsp;` |  |

---

### openPropertySheet

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `window` | `&nbsp;` | Owner window (pass null if none). |
| `sheets` | `&nbsp;` | Sheet information (an array of WIN32Dialog instances). |
| `elm` | `&nbsp;` | Options (a dictionary; optional).<br>%[ caption: property sheet title, page: initial page number, icon: icon ] |

**Return value**

Return value of ::PropertySheet.

**Description**

Shows a property sheet (always modal; modeless is not implemented)

---

### propSheetMessage

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `msg` | `&nbsp;` |  |
| `wparam` | `&nbsp;` |  |
| `lparam` | `&nbsp;` |  |

**Description**

Sends a PSM_* message to the property sheet window

---

### setMessageResult

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `value` | `&nbsp;` |  |

**Description**

Sets the DWL_MSGRESULT value

---

### openProgress

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` | Dialog item ID of the progress bar (the target updated by the progressValue property). |
| `window` | `&nbsp;` | [optional] Owner window (void = no owner, null = Application). |
| `dsapp` | `(typeof window!="Object")` | [optional] Whether to disable the application windows while progress is shown. |
| `breathe` | `(typeof window=="Object")` | [optional] Whether the progressValue setter calls breathe. |
| `activate` | `true` | [optional] Whether to activate the dialog when it is shown. |

**Return value**

true on success.

**Description**

Shows a progress dialog

Do not set WS_VISIBLE in the progress dialog's style.
Always close it with closeProgress().
Note that while showing progress, no callbacks other than onInit are delivered.

---

### closeProgress

Method

**Description**

Closes the progress dialog

---

### insertTab

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `tab_id` | `&nbsp;` |  |
| `pos` | `&nbsp;` |  |
| `label` | `&nbsp;` |  |

**Description**

Works with tab controls

The usage is still under consideration.
insertTab(IDC_TAB, 0, "基本"); // add a tab
// deleteTab(IDC_TAB, 0); // delete a tab
// deleteAllTab(IDC_TAB); // delete all tabs
var dlg = new WIN32Dialog(); dlg.loadResource("resource.dll", "INNER"); // a dialog with Border=None, Style=Child
selectTab(IDC_TAB, dlg); // show it
insertTab(IDC_TAB, 1, "拡張");
var dlg2 = new WIN32Dialog(); dlg2.loadResource("resource.dll", "INNER2");
dlg.show(SW_HIDE);
selectTab(IDC_TAB, dlg2); // switch
// In onNotify, notify->code == TCN_SELCHANGE and notify->idFrom == IDC_TAB means the user switched tabs
// Get the tab index with getCurSel(tab_id), then SW_SHOW the corresponding dialog and SW_HIDE the others
// Keep track of which dialog corresponds to each tab index yourself
Note: dlg and dlg2 are opened when selectTab is called, so check with isValid that a dialog is open before calling show(SW_HIDE) on it.

---

### deleteTab

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `tab_id` | `&nbsp;` |  |
| `pos` | `&nbsp;` |  |

---

### deleteAllTab

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `tab_id` | `&nbsp;` |  |

---

### getCurSel

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `tab_id` | `&nbsp;` |  |

---

### selectTab

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `tab_id` | `&nbsp;` |  |
| `dialog` | `&nbsp;` |  |

---

### setScrollInfo

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` | Dialog item ID of the scroll bar. |
| `pos` | `&nbsp;` | Slider position. |
| `min` | `&nbsp;` | Minimum value. |
| `max` | `&nbsp;` | Maximum value. |
| `page` | `&nbsp;` | Page value. |

**Description**

Sets the ScrollInfo

---

### getScrollInfo

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` | Dialog item ID of the scroll bar. |

**Return value**

%[pos, min, max, page]

**Description**

Gets the ScrollInfo

---
