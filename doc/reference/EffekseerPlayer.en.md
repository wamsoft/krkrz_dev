# EffekseerPlayer

Playback player

Handles playback, positioning, and drawing of a single effect instance.

## Members

### Constructors

- [EffekseerPlayer](#effekseerplayer)

### Properties

- [device](#device)
- [effect](#effect)
- [loaded](#loaded)
- [playing](#playing)
- [instanceCount](#instancecount)
- [renderScale](#renderscale)
- [left](#left)
- [top](#top)
- [z](#z)
- [zoomX](#zoomx)
- [zoomY](#zoomy)
- [angle](#angle)
- [speed](#speed)
- [color](#color)
- [paused](#paused)
- [shown](#shown)
- [spawnDisabled](#spawndisabled)
- [layer](#layer)
- [meta](#meta)

### Methods

- [load](#load)
- [loadEffect](#loadeffect)
- [clear](#clear)
- [play](#play)
- [stop](#stop)
- [stopRoot](#stoproot)
- [progress](#progress)
- [moveToFrame](#movetoframe)
- [render](#render)
- [setRenderMatrix](#setrendermatrix)
- [getRenderMatrix](#getrendermatrix)
- [setRenderScale](#setrenderscale)
- [getRenderScale](#getrenderscale)
- [setCoord](#setcoord)
- [getCoord](#getcoord)
- [setZoom](#setzoom)
- [getZoom](#getzoom)
- [setAngleDeg](#setangledeg)
- [getAngleDeg](#getangledeg)
- [setAngleRad](#setanglerad)
- [getAngleRad](#getanglerad)
- [setRotate](#setrotate)
- [getRotate](#getrotate)
- [setSpeed](#setspeed)
- [getSpeed](#getspeed)
- [setTargetLocation](#settargetlocation)
- [setRandomSeed](#setrandomseed)
- [setDynamicInput](#setdynamicinput)
- [setDynamicInputByName](#setdynamicinputbyname)
- [getDynamicInputByName](#getdynamicinputbyname)
- [findDynamicInput](#finddynamicinput)
- [readMeta](#readmeta)
- [getDynamicInput](#getdynamicinput)
- [sendTrigger](#sendtrigger)

---

### EffekseerPlayer

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `device` | `&nbsp;` | EffekseerDevice instance |

**Description**

Constructor

---

### device

Property \ Access: `r/w`

**Description**

Read-only

---

### effect

Property \ Access: `r/w`

**Description**

Read-only: the EffekseerEffect assigned with loadEffect()

---

### loaded

Property \ Access: `r/w`

**Description**

Read-only

---

### playing

Property \ Access: `r/w`

**Description**

Read-only: whether it is playing

---

### instanceCount

Property \ Access: `r/w`

**Description**

Read-only: number of particles in this effect

---

### renderScale

Property \ Access: `r/w`

---

### left

Property \ Access: `r/w`

---

### top

Property \ Access: `r/w`

---

### z

Property \ Access: `r/w`

---

### zoomX

Property \ Access: `r/w`

---

### zoomY

Property \ Access: `r/w`

---

### angle

Property \ Access: `r/w`

**Description**

Degrees

---

### speed

Property \ Access: `r/w`

---

### color

Property \ Access: `r/w`

**Description**

Overall color 0xAARRGGBB (default 0xFFFFFFFF). Multiplied over the whole effect.

---

### paused

Property \ Access: `r/w`

**Description**

Paused

---

### shown

Property \ Access: `r/w`

**Description**

Visible / hidden

---

### spawnDisabled

Property \ Access: `r/w`

**Description**

Stops spawning new particles

---

### layer

Property \ Access: `r/w`

**Description**

Layer the effect belongs to (0-31)

---

### meta

Property \ Access: `r/w`

**Description**

Supplementary information of the playing asset (same as EffekseerEffect.meta)

Bridged so that it is also available when loaded via player.load().

---

### load

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `&nbsp;` | Storage name (.efkzip / .efkefc / .efk) |
| `magnification` | `&nbsp;` | Magnification at load time (1.0 if omitted) |
| `entry` | `&nbsp;` | Effect file name inside the .efkzip (optional) |

**Description**

Loads an effect file (dedicated to this player)

Arguments are the same as EffekseerEffect.load (.efkzip supported)

---

### loadEffect

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `effect` | `&nbsp;` | EffekseerEffect instance |

**Description**

Assigns a loaded EffekseerEffect

---

### clear

Method

**Description**

Unassigns the effect (stops it if playing)

---

### play

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `startFrame` | `&nbsp;` | Start frame (0 if omitted) |

**Description**

Starts playback. If already playing, stops and restarts.

---

### stop

Method

**Description**

Stops immediately (particles disappear as well)

---

### stopRoot

Method

**Description**

Stops only the root. No new particles are spawned and the remaining ones fade out naturally.

Use this to end an effect cleanly.

---

### progress

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `tick` | `&nbsp;` | Elapsed time (milliseconds)<br>Apply positioning settings before calling progress(). |

**Description**

Advances playback

---

### moveToFrame

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `frame` | `&nbsp;` | Frame number (based on 60 fps) |

**Description**

Moves to the given frame (slow, since it recomputes from the start)

---

### render

Method

**Description**

Draws the effect. Call it on the OpenGL context, between device.onBeginScene() and onEndScene().

---

### setRenderMatrix

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `m11` | `&nbsp;` |  |
| `m12` | `&nbsp;` |  |
| `m13` | `&nbsp;` |  |
| `m21` | `&nbsp;` |  |
| `m22` | `&nbsp;` |  |
| `m23` | `&nbsp;` |  |

**Description**

Sets the render matrix (outer affine transform)

X' = m11*x + m12*y + m13
Y' = m21*x + m22*y + m23

---

### getRenderMatrix

Method

**Description**

%[ m11:, m12:, m13:, m21:, m22:, m23: ]

---

### setRenderScale

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `scale` | `&nbsp;` |  |

**Description**

Scale factor applied to the linear part of the render matrix (default 1.0)

---

### getRenderScale

Method

---

### setCoord

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**Description**

Display position (pixel offset from the screen center)

---

### getCoord

Method

**Description**

%[ x:, y:, z: ]

---

### setZoom

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `zx` | `&nbsp;` |  |
| `zy` | `&nbsp;` |  |

**Description**

Scaling (default 1.0)

---

### getZoom

Method

**Description**

%[ x:, y: ]

---

### setAngleDeg

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `degree` | `&nbsp;` |  |

**Description**

In-screen rotation. Positive angles rotate clockwise on screen.

---

### getAngleDeg

Method

---

### setAngleRad

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `radian` | `&nbsp;` |  |

---

### getAngleRad

Method

---

### setRotate

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**Description**

Three-axis rotation (degrees). z is the same in-screen rotation as setAngleDeg.

x / y tilt the effect in depth; the result is easiest to see with perspective projection.

---

### getRotate

Method

**Description**

%[ x:, y:, z: ]

---

### setSpeed

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `speed` | `&nbsp;` |  |

**Description**

Playback speed (1.0 is normal speed)

---

### getSpeed

Method

---

### setTargetLocation

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**Description**

Target location (when the effect uses target-dependent settings)

Coordinates are screen-center-origin pixel coordinates, the same as positioning.

---

### setRandomSeed

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `seed` | `&nbsp;` |  |

**Description**

Fixes the random seed

---

### setDynamicInput

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` | Index of the dynamic input defined in the effect (0-based)<br>Out-of-range indices are ignored (getting returns 0). |
| `value` | `&nbsp;` |  |

**Description**

Dynamic parameter (Dynamic Input in the Effekseer editor)

---

### setDynamicInputByName

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` |  |
| `value` | `&nbsp;` |  |

**Description**

Sets / gets a dynamic parameter by name

The mapping comes automatically from effect.json in the .efkzip
(it can also be replaced with EffekseerEffect.setDynamicInputNames()).
Passing an unknown name throws an exception.

player.setDynamicInputByName("emitter.x", 120);

---

### getDynamicInputByName

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

---

### findDynamicInput

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

**Description**

Checks whether a name can be set. Returns -1 if unknown

---

### readMeta

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

---

### getDynamicInput

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` |  |

---

### sendTrigger

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` | Index of the trigger defined in the effect (0-based) |

**Description**

Sends a trigger (Trigger in the Effekseer editor)

---
