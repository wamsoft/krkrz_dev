# EffekseerDevice

Draw device

Create one per OpenGL (ES) context.

## Members

### Constructors

- [EffekseerDevice](#effekseerdevice)

### Properties

- [instanceMax](#instancemax)
- [squareMaxCount](#squaremaxcount)
- [premultipliedAlpha](#premultipliedalpha)
- [projectionMode](#projectionmode)
- [frameRate](#framerate)
- [restorationOfStates](#restorationofstates)
- [clearDepth](#cleardepth)
- [verbose](#verbose)
- [surfaceWidth](#surfacewidth)
- [surfaceHeight](#surfaceheight)
- [totalInstanceCount](#totalinstancecount)
- [drawCallCount](#drawcallcount)
- [drawVertexCount](#drawvertexcount)
- [deviceInfo](#deviceinfo)

### Methods

- [onBeginScene](#onbeginscene)
- [onEndScene](#onendscene)
- [update](#update)
- [beginUpdate](#beginupdate)
- [endUpdate](#endupdate)
- [onLostDevice](#onlostdevice)
- [onResetDevice](#onresetdevice)
- [stopAll](#stopall)
- [setCapacity](#setcapacity)
- [setPerspective](#setperspective)
- [setOrthographic](#setorthographic)
- [setCamera](#setcamera)
- [resetCamera](#resetcamera)
- [getGLError](#getglerror)

---

### EffekseerDevice

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `oglbase` | `&nbsp;` | Object that holds GLGetProcAddress (the GetProcAddress provider).<br>One of the following can be specified:<br>- The GLESAdaptor of the krkrgles plugin<br>- A Window (when using the engine's built-in OpenGL rendering, i.e. OGLDrawDevice)<br>Note: the implementation simply reads the GLGetProcAddress property of the given object.<br>OGLDrawDevice itself does not have this property, so pass the Window instead<br>(the same object you would pass to threepp's GLRenderer).<br>The device is initialized for the current OpenGL ES context.<br>Note: create it while the context is current. |

**Description**

Constructor

---

### instanceMax

Property \ Access: `r/w`

**Description**

Read-only

---

### squareMaxCount

Property \ Access: `r/w`

**Description**

Read-only

---

### premultipliedAlpha

Property \ Access: `r/w`

**Description**

Whether to draw with premultiplied alpha (default false).

Changing it recreates the manager/renderer (same caveat as setCapacity).

---

### projectionMode

Property \ Access: `r/w`

**Description**

Projection mode

EffekseerDevice.EffekseerProjectionOrthographic … orthographic projection (default)
EffekseerDevice.EffekseerProjectionPerspective  … perspective projection

---

### frameRate

Property \ Access: `r/w`

**Description**

Base frame rate for advancing effects (default 60).

Used to convert the milliseconds passed to progress(tick) / update(tick) into frames.

---

### restorationOfStates

Property \ Access: `r/w`

**Description**

Whether to save/restore GL state around drawing (default true).

Keep this true when mixing with GL rendering from Kirikiri or other plugins.

---

### clearDepth

Property \ Access: `r/w`

**Description**

Whether onBeginScene clears the depth buffer (default true)

When depth testing (ZTest) is enabled on an effect node, it is compared against the
depth values of the render target. Offscreen buffers prepared by Kirikiri may have
uninitialized depth (krkrgles's capture clears only color and stencil),
in which case the effect would not appear at all.
By default the depth is reset to 1.0 every frame. Set this to false only
when the caller manages depth itself.

---

### verbose

Property \ Access: `r/w`

**Description**

Writes asset-open results and detailed Effekseer logs to the Kirikiri log (default false)

Useful for diagnosing problems such as missing textures.

---

### surfaceWidth

Property \ Access: `r/w`

**Description**

Read-only: width from the last onBeginScene

---

### surfaceHeight

Property \ Access: `r/w`

**Description**

Read-only: height from the last onBeginScene

---

### totalInstanceCount

Property \ Access: `r/w`

**Description**

Read-only: total number of particles

---

### drawCallCount

Property \ Access: `r/w`

**Description**

Read-only: number of draw calls in the last frame

---

### drawVertexCount

Property \ Access: `r/w`

**Description**

Read-only: number of vertices in the last frame

---

### deviceInfo

Property \ Access: `r/w`

**Description**

Read-only: all settings (dictionary)

---

### onBeginScene

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `width` | `&nbsp;` | Width of the render target (pixels) |
| `height` | `&nbsp;` | Height of the render target (pixels)<br>Note: call this in the context the device was created in. |

**Description**

Begins drawing. Updates the projection matrix and starts Effekseer rendering.

---

### onEndScene

Method

**Description**

Ends drawing.

---

### update

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `tick` | `&nbsp;` | Elapsed time (milliseconds)<br>Not needed if you call progress() on each player individually. |

**Description**

Advances all effects at once.

---

### beginUpdate

Method

**Description**

Batches per-player updates

When calling EffekseerPlayer.progress() on many players, wrapping the calls in beginUpdate() ... endUpdate()
lets the internal buffers be swapped only once.
device.beginUpdate();
for (...) players[i].progress(tick);
device.endUpdate();

---

### endUpdate

Method

---

### onLostDevice

Method

**Description**

Releases / rebuilds GL resources (for handling context loss)

---

### onResetDevice

Method

---

### stopAll

Method

**Description**

Stops all playing effects

---

### setCapacity

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `instanceMax` | `&nbsp;` | Maximum number of particles that can exist at once (default 4000) |
| `squareMaxCount` | `&nbsp;` | Maximum number of sprites per draw (default 8192) |

**Description**

Sets the internal buffer capacities.

This recreates the internal manager/renderer, so existing EffekseerEffect / EffekseerPlayer objects are invalidated.
Note: call this before loading effects and before creating players.
Does nothing if the values are the same as the current ones. Values of 0 or less throw an exception.

---

### setPerspective

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `fovDegree` | `&nbsp;` | Vertical field of view (degrees), default 45 |
| `znear` | `&nbsp;` | Near clip plane, default 1 |
| `zfar` | `&nbsp;` | Far clip plane, default 10000<br>The camera is automatically placed at the distance where 1 world unit = 1 pixel on the Z=0 plane. |

**Description**

Switches to perspective projection and sets its parameters

---

### setOrthographic

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `znear` | `&nbsp;` | Near clip plane |
| `zfar` | `&nbsp;` | Far clip plane |

**Description**

Switches to orthographic projection and sets the depth range

---

### setCamera

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `px` | `&nbsp;` |  |
| `py` | `&nbsp;` |  |
| `pz` | `&nbsp;` |  |
| `tx` | `&nbsp;` |  |
| `ty` | `&nbsp;` |  |
| `tz` | `&nbsp;` |  |

**Description**

Places the camera manually (in the same screen-center-origin pixel coordinates as positioning)

By default the camera is placed automatically so that it faces the origin (screen center) head-on.

---

### resetCamera

Method

**Description**

Restores automatic camera placement

---

### getGLError

Method

**Description**

Gets the most recent GL error code (cleared on read; 0 means no error)

---
