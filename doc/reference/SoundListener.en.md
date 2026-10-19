# SoundListener

The SoundListener class controls the "listener" for 3D sound positioning. You cannot create objects of this class. As with System, call its members directly, as in `SoundListener.setPosition(...)`.

This class controls the listener shared by the engine (listener 0) for the miniaudio-based 3D sound positioning. Sound sources are configured on the WaveSoundBuffer side with [use3D](WaveSoundBuffer.md#use3d), set3DPosition, and so on.

The coordinate system follows miniaudio (right-handed, Y up, arbitrary units; by default forward = -Z and up = +Y; cone angles are in radians).

HRTF is not supported. On stereo output, front and back cannot be distinguished; only L/R panning and distance attenuation are applied.

## Members

### Properties

- [enabled](#enabled)

### Methods

- [setPosition](#setposition)
- [setDirection](#setdirection)
- [setWorldUp](#setworldup)
- [setVelocity](#setvelocity)
- [setCone](#setcone)

---

### enabled

Property \ Access: `r/w`

**Description**

Whether the listener (3D positioning) is enabled

Indicates whether the listener (3D positioning) is enabled. You can also set this value.

**See also:** [WaveSoundBuffer.use3D](WaveSoundBuffer.md#use3d)

---

### setPosition

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | X component of the position. |
| `y` | `&nbsp;` | Y component of the position. |
| `z` | `&nbsp;` | Z component of the position. |

**Description**

Sets the listener position

Sets the position of the listener.

---

### setDirection

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | X component of the forward vector. |
| `y` | `&nbsp;` | Y component of the forward vector. |
| `z` | `&nbsp;` | Z component of the forward vector. |

**Description**

Sets the listener direction

Sets the direction of the listener (the forward vector).

---

### setWorldUp

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | X component of the up vector. |
| `y` | `&nbsp;` | Y component of the up vector. |
| `z` | `&nbsp;` | Z component of the up vector. |

**Description**

Sets the world up vector

Sets the world up vector.

---

### setVelocity

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | X component of the velocity. |
| `y` | `&nbsp;` | Y component of the velocity. |
| `z` | `&nbsp;` | Z component of the velocity. |

**Description**

Sets the listener velocity

Sets the listener velocity used for Doppler calculations.

---

### setCone

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `innerAngleRad` | `&nbsp;` | Inner angle of the cone, in radians. |
| `outerAngleRad` | `&nbsp;` | Outer angle of the cone, in radians. |
| `outerGain` | `&nbsp;` | Gain outside the cone (0 to 1). |

**Description**

Sets the listener's directional cone

Sets the directional cone of the listener. Angles are in radians.

---
