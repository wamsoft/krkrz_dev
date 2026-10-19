# BitmapLayerTreeOwner

The BitmapLayerTreeOwner class holds a layer tree and lets you get its rendering result as a Bitmap. (1.1.0 and later)

Pass it instead of a window as the first argument of the Layer constructor, and you can get the rendering result of those layers as an image in a Bitmap.

## Members

### Constructors

- [BitmapLayerTreeOwner](#bitmaplayertreeowner)

### Properties

- [bitmap](#bitmap)
- [dirtyRect](#dirtyrect)
- [focusedLayer](#focusedlayer)
- [height](#height)
- [isUpdated](#isupdated)
- [layerEventTargetInterface](#layereventtargetinterface)
- [layerTreeOwnerInterface](#layertreeownerinterface)
- [primaryLayer](#primarylayer)
- [width](#width)

### Methods

- [clearDirtyRect](#cleardirtyrect)
- [fireClick](#fireclick)
- [fireDisplayRotate](#firedisplayrotate)
- [fireDoubleClick](#firedoubleclick)
- [fireKeyDown](#firekeydown)
- [fireKeyPress](#firekeypress)
- [fireKeyUp](#firekeyup)
- [fireMouseDown](#firemousedown)
- [fireMouseMove](#firemousemove)
- [fireMouseOutOfWindow](#firemouseoutofwindow)
- [fireMouseUp](#firemouseup)
- [fireMouseWheel](#firemousewheel)
- [fireMultiTouch](#firemultitouch)
- [fireRecheckInputState](#firerecheckinputstate)
- [fireReleaseCapture](#firereleasecapture)
- [fireTouchDown](#firetouchdown)
- [fireTouchMove](#firetouchmove)
- [fireTouchRotate](#firetouchrotate)
- [fireTouchScaling](#firetouchscaling)
- [fireTouchUp](#firetouchup)
- [update](#update)

### Events

- [onChangeLayerImage](#onchangelayerimage)
- [onDisableAttentionPoint](#ondisableattentionpoint)
- [onGetCursorPos](#ongetcursorpos)
- [onReleaseMouseCapture](#onreleasemousecapture)
- [onResetImeMode](#onresetimemode)
- [onResizeLayer](#onresizelayer)
- [onSetAttentionPoint](#onsetattentionpoint)
- [onSetCursorPos](#onsetcursorpos)
- [onSetHintText](#onsethinttext)
- [onSetImeMode](#onsetimemode)
- [onSetMouseCursor](#onsetmousecursor)

---

### BitmapLayerTreeOwner

Constructor

**Description**

Constructs a BitmapLayerTreeOwner object

Constructs an object of the BitmapLayerTreeOwner class.

---

### bitmap

Property \ Access: `r/w`

**Description**

Destination Bitmap object

Returns the `Bitmap` object held by this layer tree owner.
The contents of the layer tree are drawn into this Bitmap. Read-only.

**See also:** [BitmapLayerTreeOwner.update](BitmapLayerTreeOwner.md#update)

---

### dirtyRect

Property \ Access: `r/w`

**Description**

Dirty rectangle object

Returns a `Rect` object representing the area updated by the most recent drawing.
Read-only.

---

### focusedLayer

Property \ Access: `r/w`

**Description**

Focused layer

Gets or sets the layer that currently has focus in this tree.
Setting null removes the focus.

**See also:** [Layer.focused](Layer.md#focused)

---

### height

Property \ Access: `r/w`

**Description**

Height (read-only)

---

### isUpdated

Property \ Access: `r/w`

**Description**

Updated flag

Returns whether the layer tree has been updated since the last `update` call.
If true, it needs to be redrawn. Read-only.

---

### layerEventTargetInterface

Property \ Access: `r/w`

**Type**: `Integer`

**Description**

LayerEventTarget interface pointer

Returns the pointer to the C++ interface that layer events are forwarded to ( `tTVPLayerTreeOwner` )
as a 64-bit integer. Use it to access the layer event delivery system from a plugin. Read-only.

---

### layerTreeOwnerInterface

Property \ Access: `r/w`

**Description**

LTO interface, for internal use (read-only)

---

### primaryLayer

Property \ Access: `r/w`

**Description**

Primary layer (read-only)

---

### width

Property \ Access: `r/w`

**Description**

Width (read-only)

---

### clearDirtyRect

Method

**Description**

Clears the updated rectangle information

---

### fireClick

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | x coordinate of the clicked position (client coordinates) |
| `y` | `&nbsp;` | y coordinate of the clicked position (client coordinates) |

**Description**

Notifies layers of a click (not recommended)

---

### fireDisplayRotate

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `orientation` | `&nbsp;` | Display orientation |
| `rotate` | `&nbsp;` | Angle |
| `bpp` | `&nbsp;` | Bits per pixel |
| `hresolution` | `&nbsp;` | Display width |
| `vresolution` | `&nbsp;` | Display height |

**Description**

Notifies layers that the display has been rotated

---

### fireDoubleClick

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | x coordinate of the double-clicked position (client coordinates) |
| `y` | `&nbsp;` | y coordinate of the double-clicked position (client coordinates) |

**Description**

Notifies layers of a double click (not recommended)

---

### fireKeyDown

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `key` | `&nbsp;` | Virtual key code of the pressed key |
| `shift` | `&nbsp;` | State of the shift-type keys and mouse buttons held down when the key was pressed |

**Description**

Notifies layers that a key has been pressed

---

### fireKeyPress

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `key` | `&nbsp;` | Character |

**Description**

Notifies layers that a character has been entered

---

### fireKeyUp

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `key` | `&nbsp;` | Virtual key code of the released key |
| `shift` | `&nbsp;` | State of the shift-type keys and mouse buttons held down when the key was released |

**Description**

Notifies layers that a key has been released

---

### fireMouseDown

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | x coordinate where the mouse button was pressed (client coordinates) |
| `y` | `&nbsp;` | y coordinate where the mouse button was pressed (client coordinates) |
| `mb` | `&nbsp;` | Mouse button that was pressed |
| `flags` | `&nbsp;` |  |

**Description**

Notifies layers of a mouse button press

---

### fireMouseMove

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | x coordinate the mouse moved to (client coordinates) |
| `y` | `&nbsp;` | y coordinate the mouse moved to (client coordinates) |
| `flags` | `&nbsp;` | State of the shift-type keys and mouse buttons held down while the mouse was moving |

**Description**

Notifies layers of mouse movement

---

### fireMouseOutOfWindow

Method

**Description**

Notifies layers that the mouse has left the window

---

### fireMouseUp

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | x coordinate where the mouse button was released (client coordinates) |
| `y` | `&nbsp;` | y coordinate where the mouse button was released (client coordinates) |
| `mb` | `&nbsp;` | Mouse button that was released |
| `flags` | `&nbsp;` | State of the shift-type keys held down when the mouse button was released |

**Description**

Notifies layers of a mouse button release

---

### fireMouseWheel

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `shift` | `&nbsp;` | State of the shift-type keys and mouse buttons held down while the mouse was moving |
| `delta` | `&nbsp;` | Wheel rotation angle |
| `x` | `&nbsp;` | x coordinate where the wheel was rotated (client coordinates) |
| `y` | `&nbsp;` | y coordinate where the wheel was rotated (client coordinates) |

**Description**

Notifies layers of mouse wheel rotation

---

### fireMultiTouch

Method

**Description**

Notifies layers of a multi-touch state change

---

### fireRecheckInputState

Method

**Description**

Call this at 1-second intervals if needed.

Rechecks the mouse position over the current layer, updates the hint, and rechecks the cursor type and layer enter/leave.
Internally it issues a mouse cursor move by 0.

---

### fireReleaseCapture

Method

**Description**

Notifies layers that mouse capture has been released

---

### fireTouchDown

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | x coordinate of the touched position (client coordinates) |
| `y` | `&nbsp;` | y coordinate of the touched position (client coordinates) |
| `cx` | `&nbsp;` | Horizontal contact size of the finger, in pixels |
| `cy` | `&nbsp;` | Vertical contact size of the finger, in pixels |
| `id` | `&nbsp;` | Touch ID |

**Description**

Notifies layers of a touch

---

### fireTouchMove

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | x coordinate of the touch position (client coordinates) |
| `y` | `&nbsp;` | y coordinate of the touch position (client coordinates) |
| `cx` | `&nbsp;` | Horizontal contact size of the finger, in pixels |
| `cy` | `&nbsp;` | Vertical contact size of the finger, in pixels |
| `id` | `&nbsp;` | Touch ID |

**Description**

Notifies layers that a touch has moved

---

### fireTouchRotate

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `startangle` | `&nbsp;` | Angle in radians when the multi-touch began |
| `curangle` | `&nbsp;` | Angle of the touch in radians when the event occurred |
| `dist` | `&nbsp;` | Distance between touches in pixels when the event occurred |
| `cx` | `&nbsp;` | x coordinate of the center (client coordinates) |
| `cy` | `&nbsp;` | y coordinate of the center (client coordinates) |
| `flag` | `&nbsp;` | Multi-touch state flag |

**Description**

Notifies layers of a rotate gesture

---

### fireTouchScaling

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `startdist` | `&nbsp;` | Distance in pixels when the multi-touch began |
| `curdist` | `&nbsp;` | Distance between touches in pixels when the event occurred |
| `cx` | `&nbsp;` | x coordinate of the center (client coordinates) |
| `cy` | `&nbsp;` | y coordinate of the center (client coordinates) |
| `flag` | `&nbsp;` | Multi-touch state flag. |

**Description**

Notifies layers of a zoom gesture

---

### fireTouchUp

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | x coordinate of the released position (client coordinates) |
| `y` | `&nbsp;` | y coordinate of the released position (client coordinates) |
| `cx` | `&nbsp;` | Horizontal contact size of the finger, in pixels |
| `cy` | `&nbsp;` | Vertical contact size of the finger, in pixels |
| `id` | `&nbsp;` | Touch ID |

**Description**

Notifies layers that a touch has been released

---

### update

Method

**Description**

Updates the layer tree rendering

Draws the internal layer tree into the Bitmap referenced by the `bitmap` property,
and reflects the updated area in `dirtyRect`.

**See also:** [BitmapLayerTreeOwner.bitmap](BitmapLayerTreeOwner.md#bitmap) / [BitmapLayerTreeOwner.dirtyRect](BitmapLayerTreeOwner.md#dirtyrect)

---

### onChangeLayerImage

Event

**Description**

A layer image has been updated

---

### onDisableAttentionPoint

Event

**Description**

A layer cleared the attention point

---

### onGetCursorPos

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**Description**

A layer requested the cursor position

Return the cursor position if needed.

---

### onReleaseMouseCapture

Event

**Description**

A layer requested release of mouse capture

Release mouse capture if needed.

---

### onResetImeMode

Event

**Description**

The IME mode has been reset

---

### onResizeLayer

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |

**Description**

The primary layer has been resized

---

### onSetAttentionPoint

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `layer` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**Description**

A layer set the attention point

---

### onSetCursorPos

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**Description**

A layer requested setting the cursor position

Set the cursor position if needed.

---

### onSetHintText

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `sender` | `&nbsp;` |  |
| `hint` | `&nbsp;` |  |

**Description**

A layer requested setting the hint text

Set the hint text if needed.

---

### onSetImeMode

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `mode` | `&nbsp;` |  |

**Description**

The IME mode has been set

---

### onSetMouseCursor

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `cursor` | `&nbsp;` |  |

**Description**

A layer requested setting the cursor

Change the cursor if needed.

---
