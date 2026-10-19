# SoundBuffer

The class manages MIDI playback, PCM playback, and CD-DA playback.

The WaveSoundBuffer class can load and process .sli files created with the [Loop Tuner](../guide/LoopTuner.md). See the Loop Tuner documentation for details.

## Members

### Constructors

- [SoundBuffer](#soundbuffer)

### Properties

- [position](#position)
- [paused](#paused)
- [totalTime](#totaltime)
- [looping](#looping)
- [volume](#volume)
- [volume2](#volume2)
- [status](#status)

### Methods

- [open](#open)
- [play](#play)
- [stop](#stop)
- [fade](#fade)
- [stopFade](#stopfade)

### Events

- [onStatusChanged](#onstatuschanged)
- [onFadeCompleted](#onfadecompleted)

---

### SoundBuffer

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `owner` | `&nbsp;` | The object that receives events. |

**Description**

Constructs the object

Constructs an object of the class.

When an event occurs, the action method of the object specified as owner is called. If owner is null, the action method is not called. Normally an object of the [Window](Window.md) class is specified as owner.

---

### position

Property \ Access: `r/w`

**Description**

Playback position

The playback position in ms. Setting a value moves to that position.

Not implemented in the current version.

Not implemented in the current version.

---

### paused

Property \ Access: `r/w`

**Description**

Whether playback is paused

Indicates whether playback is paused. You can also set this value.

True means paused.

Not implemented in the current version.

Not implemented in the current version.

---

### totalTime

Property \ Access: `r`

**Description**

Media duration

The total playback time of the media, in ms.

Not implemented in the current version.

Not implemented in the current version.

---

### looping

Property \ Access: `r/w`

**Description**

Whether to loop playback

Indicates whether playback loops. You can also set this value.

If true, playback loops.

Even if false, loop information is used if the media being played contains it.

---

### volume

Property \ Access: `r/w`

**Description**

Volume

The playback volume. You can also set this value.

Specify a number from 0 to 100000, where 0 is fully muted and 100000 is 100% volume.

---

### volume2

Property \ Access: `r/w`

**Description**

Secondary volume

The playback volume. You can set this value.

Unlike the .volume property, this property is not
changed by the .fade method.

The final volume is the product of the volume property and this property. If the volume property is
100000 (100%) and the volume2 property is also 100000 (100%), playback is at 100% x 100% = 100%
volume. If the volume property is 50000 (50%) and the volume2 property is 75000 (75%),
playback is at 50% x 75% = 37.5% volume.

---

### status

Property \ Access: `r`

**Description**

Status

The current state.

The state is a string and takes one of the following values.

`"**unload**"   : ` no media is open

`"**play**"     : ` the media is playing

`"**stop**"     : ` the media is stopped

---

### open

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `storage` | `&nbsp;` | The storage to play.<br>The storage to play.<br>The track to play.<br>If you specify a number, that track is played. If you specify a string of the form "drive letter:track number",<br>the specified track number on that drive is played (for example, "e:5"). |

**Description**

Opens media

Opens the specified media. This method does not start playback.

If a file named after the specified storage with .sli appended exists, it is loaded as sound loop information.

---

### play

Method

**Description**

Plays the media

Starts playing the media.

---

### stop

Method

**Description**

Stops the media

Stops the media.

---

### fade

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `to` | `&nbsp;` | The target volume.<br>See the .volume property for how to specify the<br>volume. |
| `time` | `&nbsp;` | Duration of the fade, in ms. |
| `delay` | `0` | Delay before the fade starts, in ms. |

**Description**

Starts a fade

Starts a fade (a continuous change in volume).

---

### stopFade

Method

**Description**

Stops the fade

Forcibly stops a fade started with the .fade method.

The volume stays at the value it had when the fade was stopped.

---

### onStatusChanged

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `status` | `&nbsp;` | The new status.<br>See the .status property. |

**Description**

The status changed

Occurs when the playback status (state) changes.

---

### onFadeCompleted

Event

**Description**

The fade finished

Occurs when a fade started with the .fade method finishes.

---
