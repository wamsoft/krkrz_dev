# WaveSoundBuffer

The WaveSoundBuffer class manages PCM playback.

The WaveSoundBuffer class can load and process .sli files created with the [Loop Tuner](../guide/LoopTuner.md). See the Loop Tuner documentation for details.

## Members

### Constructors

- [WaveSoundBuffer](#wavesoundbuffer)

### Properties

- [position](#position)
- [paused](#paused)
- [totalTime](#totaltime)
- [looping](#looping)
- [volume](#volume)
- [volume2](#volume2)
- [status](#status)
- [bits](#bits)
- [channels](#channels)
- [filters](#filters)
- [flags](#flags)
- [frequency](#frequency)
- [globalFocusMode](#globalfocusmode)
- [globalVolume](#globalvolume)
- [labels](#labels)
- [pan](#pan)
- [posX](#posx)
- [posY](#posy)
- [posZ](#posz)
- [samplePosition](#sampleposition)
- [useVisBuffer](#usevisbuffer)
- [use3D](#use3d)
- [minDistance](#mindistance)
- [maxDistance](#maxdistance)
- [rolloffFactor](#rollofffactor)
- [dopplerFactor](#dopplerfactor)
- [attenuationModel](#attenuationmodel)

### Methods

- [open](#open)
- [play](#play)
- [stop](#stop)
- [fade](#fade)
- [stopFade](#stopfade)
- [freeDirectSound](#freedirectsound)
- [getVisBuffer](#getvisbuffer)
- [getSoundLevel](#getsoundlevel)
- [getSoundSpectrum](#getsoundspectrum)
- [getVowel](#getvowel)
- [setPos](#setpos)
- [set3DPosition](#set3dposition)
- [set3DVelocity](#set3dvelocity)
- [set3DConeDirection](#set3dconedirection)
- [set3DCone](#set3dcone)
- [setGainQueryCallback](#setgainquerycallback)

### Events

- [onStatusChanged](#onstatuschanged)
- [onFadeCompleted](#onfadecompleted)
- [onLabel](#onlabel)

---

### WaveSoundBuffer

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `owner` | `&nbsp;` | The object that receives events. |

**Description**

Constructs a WaveSoundBuffer object

Constructs an object of the WaveSoundBuffer class.

When an event occurs, the action method of the object specified as owner is called. If owner is null, the action method is not called. Normally an object of the [Window](Window.md) class is specified as owner.

---

### position

Property \ Access: `r/w`

**Description**

Playback position

The playback position in ms. Setting a value moves to that position.

---

### paused

Property \ Access: `r/w`

**Description**

Whether playback is paused

Indicates whether playback is paused. You can also set this value.

True means paused.

---

### totalTime

Property \ Access: `r`

**Description**

Media duration

The total playback time of the media, in ms.

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

Unlike the [WaveSoundBuffer.volume](WaveSoundBuffer.md#volume) property, this property is not changed by the
[WaveSoundBuffer.fade](WaveSoundBuffer.md#fade) method.

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

### bits

Property \ Access: `r`

**Description**

Bits per sample

The bits per sample of the sound currently playing.
For the same bit depth as a CD, this is 16.
It may not return a valid value when no media is open.

---

### channels

Property \ Access: `r`

**Description**

Number of channels

The number of channels of the sound currently playing.
1 for mono, 2 for stereo.
It may not return a valid value when no media is open.

---

### filters

Property \ Access: `r`

**Description**

Filter array

An array (an instance of the Array class) holding insertion filter objects.
By registering filter objects in this array, you can apply various effects to the sound in real time during playback.
Changes to the filter array take effect only when the WaveSoundBuffer.open method is executed.
Until then, changes to this array have no effect.
Example:
```
var buf = new WaveSoundBuffer(window);
(略)
buf.filters.clear();
// clear the filter array
buf.filters.add(new WaveSoundBuffer.PhaseVocoder());
// add a PhaseVocoder filter
buf.filters[0].time = 0.5;
// double-speed playback
```

---

### flags

Property \ Access: `r`

**Description**

Flags

Gets an object representing the flags.
This object has properties 0 to 15, each representing the value of a flag.
The properties can be accessed with the indirect member selection operator (the '[ ]' operator).
You can also set values on these properties.
Values range from 0 to 9999 and cannot go below or above that range.
The count property of this object always returns 16.
This object has a reset method; calling it resets all flags to 0.
If no media is open, setting values on the properties of this object is ignored.
This object may look like an array object, but it is not a TJS array object (an object of the 'Array' class).
All flags are reset to 0 by the WaveSoundBuffer.open method.
Example:

```
var buf = new WaveSoundBuffer(window);
(略)
buf.flags.reset();
// reset all flags to 0
var cnt = buf.flags.count;
// cnt is 16
buf.flags[4] = 34;
// assign 34 to flag 4
```

---

### frequency

Property \ Access: `r/w`

**Description**

Sampling frequency

The sampling frequency of the sound currently playing.
You can also set this value.
For the same sampling frequency as a CD, this is 44100.
It may not return a valid value when no media is open.
Setting a value plays the sound at that frequency.

---

### globalFocusMode

Property \ Access: `r/w`

**Description**

Focus mode

The focus mode.
You can also set this value.
The focus mode controls muting when the application is minimized or becomes inactive.

+ sgfmNeverMute never mutes, whatever the state of the application.
+ sgfmMuteOnMinimize mutes when the application is minimized.
+ sgfmMuteOnDeactivate mutes when the application becomes inactive.

This property exists only on the WaveSoundBuffer class itself (objects created from WaveSoundBuffer do not have it).
Use it as WaveSoundBuffer.globalFocusMode.

---

### globalVolume

Property \ Access: `r/w`

**Description**

Global volume

The global volume (master volume).
You can also set this value.
This volume affects all WaveSoundBuffers.
Specify a number from 0 to 100000, where 0 is fully muted and 100000 is 100% volume.
The default is 100000.
This property exists only on the WaveSoundBuffer class itself (objects created from WaveSoundBuffer do not have it).
Use it as WaveSoundBuffer.globalVolume.

---

### labels

Property \ Access: `r`

**Description**

Labels

Gets an object representing the labels.
This object is a dictionary whose members are named after the labels in the loop information.
Each element is also a dictionary: the name member is the label name, the position member is the label position in milliseconds, and samplePosition is the label position in samples.
Treat this dictionary as read-only.
Assigning values or creating new members has no effect.
Example:

```
var buf = new WaveSoundBuffer(window);
(略)
debug.message(buf.labels['start'].position);
// position of the label named 'start', in milliseconds
debug.message(buf.labels['start'].samplePosition);
// position of the label named 'start', in samples
```

---

### pan

Property \ Access: `r/w`

**Description**

Pan

The pan (stereo position).
You can also set this value.
Specifies the left/right position from which the sound is heard.
Specify a number from -100000 through 0 to 100000, where -100000 is fully left, 0 is center, and 100000 is fully right.

---

### posX

Property \ Access: `r/w`

**Type**: `Real`

**Description**

3D source position (X coordinate)

Gets or sets the X coordinate of the sound source position for 3D sound playback.
You can also set all three axes at once with `WaveSoundBuffer.setPos`.

**See also:** [WaveSoundBuffer.setPos](WaveSoundBuffer.md#setpos)

---

### posY

Property \ Access: `r/w`

**Type**: `Real`

**Description**

3D source position (Y coordinate)

Gets or sets the Y coordinate of the sound source position for 3D sound playback.

**See also:** [WaveSoundBuffer.setPos](WaveSoundBuffer.md#setpos)

---

### posZ

Property \ Access: `r/w`

**Type**: `Real`

**Description**

3D source position (Z coordinate)

Gets or sets the Z coordinate of the sound source position for 3D sound playback.

**See also:** [WaveSoundBuffer.setPos](WaveSoundBuffer.md#setpos)

---

### samplePosition

Property \ Access: `r/w`

**Description**

Playback position

The playback position in samples.
Setting a value moves to that position.

---

### useVisBuffer

Property \ Access: `r/w`

**Description**

Whether to use the visualization buffer

Indicates whether the visualization buffer is used.
You can also set this value.
If true, the visualization buffer becomes available and the WaveSoundBuffer.getVisBuffer method can be used.
The default is false.
Note that true consumes more memory and CPU time than false.

---

### use3D

Property \ Access: `r/w`

**Description**

Enables or disables 3D positioning (spatializer)

Indicates whether miniaudio-based 3D positioning (distance attenuation, panning,
Doppler, directional cone) is enabled for this WaveSoundBuffer. When enabled,
specify the source position with [set3DPosition](#set3dposition) and related methods.

---

### minDistance

Property \ Access: `r/w`

**Description**

Minimum distance

No distance attenuation is applied within this distance (maximum volume).

**See also:** [WaveSoundBuffer.maxDistance](WaveSoundBuffer.md#maxdistance)

---

### maxDistance

Property \ Access: `r/w`

**Description**

Maximum distance

Beyond this distance, distance attenuation stops increasing.

**See also:** [WaveSoundBuffer.minDistance](WaveSoundBuffer.md#mindistance)

---

### rolloffFactor

Property \ Access: `r/w`

**Description**

Strength of distance attenuation

The strength of distance attenuation (rolloff factor). Larger values attenuate more sharply.

---

### dopplerFactor

Property \ Access: `r/w`

**Description**

Strength of the Doppler effect

The strength of the Doppler effect (0 disables it, 1 is standard).

**See also:** [WaveSoundBuffer.set3DVelocity](WaveSoundBuffer.md#set3dvelocity)

---

### attenuationModel

Property \ Access: `r/w`

**Description**

Distance attenuation model

An integer representing the distance attenuation model: 0 = none, 1 = inverse, 2 = linear,
3 = exponential.

---

### open

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `storage` | `&nbsp;` | The storage to play. |

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
| `to` | `&nbsp;` | The target volume.<br>See the [WaveSoundBuffer.volume](WaveSoundBuffer.md#volume) property for how to specify the<br>volume. |
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

Forcibly stops a fade started with the [WaveSoundBuffer.fade](WaveSoundBuffer.md#fade) method.

The volume stays at the value it had when the fade was stopped.

---

### freeDirectSound

Method

**Description**

Releases DirectSound (for compatibility; does nothing)

A method provided for the former DirectSound implementation.
Kirikiri Z's sound output now uses miniaudio (WASAPI shared mode)
and does not use DirectSound, so calling this method does nothing.
It is kept only for compatibility with older scripts.
This method exists only on the WaveSoundBuffer class itself (objects created from WaveSoundBuffer do not have it).
Use it as WaveSoundBuffer.freeDirectSound();.

---

### getVisBuffer

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `buffer` | `&nbsp;` | The buffer to write the output data to.<br>The buffer is an array of 16-bit signed integers and must be large enough to hold the samples specified by the numsamples and channels arguments (at least numsamples * channels elements).<br>If channels is other than 1, the samples of each channel are stored interleaved (for stereo, in the order right, left, right, left, ...).<br>You must pass a pointer to the first element of the array, cast to an integer type. |
| `numsamples` | `&nbsp;` | The number of samples to get. |
| `channel` | `&nbsp;` | The number of channels to get.<br>Specifying 1 gives the data as-is for mono, or downmixed to one channel otherwise.<br>If you specify a number other than 1, it must equal the number of channels of the sound being played.<br>In that case, you get the data as-is. |
| `ahead` | `0` | The number of samples to read ahead.<br>You can get samples starting this many samples ahead of the current playback position.<br>Specifying 0 or omitting this argument gets samples from the current playback position. |

**Return value**

The number of samples obtained.

**Description**

Gets data for visualization

Gets PCM data for visualization.
Reads PCM data from the current playback position and writes it into the array specified by the buffer argument.
Depending on the buffer state and playback format, however, the data may not be read correctly.
This method is intended for use from plugins written in C, C++, and the like, so you cannot, for example, pass a TJS array as the buffer argument.
To use this method, the WaveSoundBuffer.useVisBuffer property must be set to true.

---

### getSoundLevel

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `ahead` | `0` | The number of samples to read ahead (default 0 = current playback position).<br>Use it to shift the mouth movement earlier or later to match drawing latency. |
| `windowSamples` | `0` | The number of samples in the window used to compute the volume (default 0 = engine default). |

**Return value**

A dictionary of the form `%[ rms:RMS value, peak:peak value ]`. Both are 0.0 to 1.0, and
`rms` can be used directly as the mouth opening amount.

**Description**

Gets the sound level (for lip sync)

Gets the volume near the current playback position. Unlike `getVisBuffer`, there is no need to
extract raw PCM and compute on the TJS side; the engine computes it in C++ and returns it.
To use it, `WaveSoundBuffer.useVisBuffer` must be true (if it is not set,
it is enabled automatically and 0 is returned for that call).

**See also:** [WaveSoundBuffer.getVowel](WaveSoundBuffer.md#getvowel) / [WaveSoundBuffer.getSoundSpectrum](WaveSoundBuffer.md#getsoundspectrum)

---

### getSoundSpectrum

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `numbands` | `&nbsp;` | The number of bands to get (1 to 256). |
| `ahead` | `0` | The number of samples to read ahead (default 0). |

**Return value**

An array (numbands elements) containing the energy of each band.
The bands are logarithmically spaced (from low to high frequencies).

**Description**

Gets the spectrum (for lip sync)

Analyzes the spectrum near the current playback position with an FFT and returns it as
logarithmically spaced band energies. Useful for vowel detection, equalizer displays, and so on.
`WaveSoundBuffer.useVisBuffer` must be true.

**See also:** [WaveSoundBuffer.getVowel](WaveSoundBuffer.md#getvowel)

---

### getVowel

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `ahead` | `0` | The number of samples to read ahead (default 0). |

**Return value**

A dictionary of the form `%[ a:, i:, u:, e:, o:, voiced: ]`. a to o are the estimated weights of each vowel
(summing to roughly 1.0); `voiced` is 1 if voiced (there is energy in the vowel bands)
and 0 if silent.

**Description**

Gets a vowel estimate (for lip sync)

Analyzes the spectrum near the current playback position and estimates how closely it matches each of the five Japanese vowels (a, i, u, e, o)
from the energy ratios of the formant bands. The result can be used as blend weights for mouth shapes
(visemes). Note that this is only a simple estimate.
`WaveSoundBuffer.useVisBuffer` must be true.

**See also:** [WaveSoundBuffer.getSoundLevel](WaveSoundBuffer.md#getsoundlevel)

---

### setPos

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | X coordinate. |
| `y` | `&nbsp;` | Y coordinate. |
| `z` | `&nbsp;` | Z coordinate. |

**Description**

Sets the 3D source position at once

Sets the sound source position (X / Y / Z) for 3D sound playback in one call.

**See also:** [WaveSoundBuffer.posX](WaveSoundBuffer.md#posx) / [WaveSoundBuffer.posY](WaveSoundBuffer.md#posy) / [WaveSoundBuffer.posZ](WaveSoundBuffer.md#posz)

---

### set3DPosition

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | X coordinate. |
| `y` | `&nbsp;` | Y coordinate. |
| `z` | `&nbsp;` | Z coordinate. |

**Description**

Sets the 3D source position

Sets the source position for 3D positioning (takes effect when [use3D](#use3d) is enabled).

**See also:** [WaveSoundBuffer.setPos](WaveSoundBuffer.md#setpos)

---

### set3DVelocity

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `vx` | `&nbsp;` | Velocity along X. |
| `vy` | `&nbsp;` | Velocity along Y. |
| `vz` | `&nbsp;` | Velocity along Z. |

**Description**

Sets the velocity vector of the 3D source

Sets the velocity vector of the source used for Doppler calculations.

**See also:** [WaveSoundBuffer.dopplerFactor](WaveSoundBuffer.md#dopplerfactor)

---

### set3DConeDirection

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `dx` | `&nbsp;` | X component of the direction. |
| `dy` | `&nbsp;` | Y component of the direction. |
| `dz` | `&nbsp;` | Z component of the direction. |

**Description**

Sets the direction of the directional cone

Sets the direction vector of the directional cone ([set3DCone](#set3dcone)).

---

### set3DCone

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `innerAngleRad` | `&nbsp;` | Full angle of the inner cone (radians). No attenuation inside it. |
| `outerAngleRad` | `&nbsp;` | Full angle of the outer cone (radians). |
| `outerGain` | `&nbsp;` | Attenuation gain outside the cone (0.0 to 1.0). |

**Description**

Sets the directional cone

Sets the directional cone of the source. Angles are in radians; outside the cone the sound is attenuated
down to the outerGain gain. For omnidirectional output, set inner = outer = 2*PI.

**See also:** [WaveSoundBuffer.set3DConeDirection](WaveSoundBuffer.md#set3dconedirection)

---

### setGainQueryCallback

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `callback` | `&nbsp;` | A function that takes the URL (storage name) as its single argument and returns the additional<br>gain to apply, in dB. Specify null to unregister. |

**Description**

Sets the per-track gain query callback (class method)

Registers a callback function that returns an **additional gain (dB)** to apply to each file
when decoding ogg (Vorbis) / opus files. This is a class
method, and the registration is shared by all WaveSoundBuffers. It integrates the API of the same name from the former wuvorbis /
wuopus plugins into the engine's built-in decoders.
The callback is called once when a file is opened (at open time, on the script thread),
and the returned dB value is applied to the decoded output. Use it, for example, to even out volume across tracks
(loudness normalization).

Example:

`WaveSoundBuffer.setGainQueryCallback(function(url) {`

`  return url.indexOf("loud_") != -1 ? -6.0 : 0.0; // 特定曲だけ -6dB`

`});`

Other gain sources include an overall gain set by a command-line option at startup and
ReplayGain tag support (see "Sound gain" in [command line](../guide/CommandLine.md)).

**Differences between codecs / recommendation**

By specification, opus carries an output gain (R128) in its header, which the decoder applies internally, accurately and
cheaply (the CLI / callback gain is added to it). Vorbis, on the other hand,
has no concept of gain in the format, so the engine scales the output PCM in the float domain
to apply it (there is practically no performance difference). **If you work actively with gain or
loudness, using opus is recommended.**

---

### onStatusChanged

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `status` | `&nbsp;` | The new status.<br>See the [WaveSoundBuffer.status](WaveSoundBuffer.md#status) property. |

**Description**

The status changed

Occurs when the playback status (state) changes.

---

### onFadeCompleted

Event

**Description**

The fade finished

Occurs when a fade started with the [WaveSoundBuffer.fade](WaveSoundBuffer.md#fade) method finishes.

---

### onLabel

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | The name of the label that was passed. |

**Description**

A label was passed

Occurs when the playback position passes a label.

---

## Plugin extension: getSample

Manual in pseudo-code

### Members

#### Properties

- [sampleValue](#samplevalue)
- [sampleCount](#samplecount)
- [sampleAhead](#sampleahead)

#### Methods

- [getSample](#getsample)

---

### sampleValue

Property \ Access: `r`

**Description**

Gets a sample value (new method)

Gets samples with getVisBuffer(buf, sampleCount, 1, sampleAhead) and
returns the maximum of (value/32768)^2 (as a real number from 0 to 1).
Note: reading this property implicitly sets useVisBuffer=true.

---

### sampleCount

Property \ Access: `r/w`

**Description**

Parameter property for buffer retrieval in the new method (see sampleValue)

The default is determined by setDefaultCounts/setDefaultAheads.
Note: reading or writing this property implicitly sets useVisBuffer=true.

---

### sampleAhead

Property \ Access: `r/w`

---

### getSample

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `n` | `&nbsp;` | The number of samples to get. Defaults to 100 if omitted. |

**Return value**

The average value.
Note: set useVisBuffer=true beforehand.

**Description**

Gets a sample value (old method)

Gets the specified number of samples from the current playback position and returns their average.
Negative sample values are ignored.

---
