---
source_hash: bca50abf0da0
---

# Sound Playback

This page describes the sound playback features supported by Kirikiri Z.

### Contents

[Overview](#overview)

[Specifications](#spec)

[Supported formats](#format)

[Seamless looping (.sli)](#loop)

[3D positioning (spatializer)](#spatializer)

[Lip-sync/analysis API](#analysis)

[Time stretching/pitch shifting](#phasevocoder)

## Overview { #overview }

The current Kirikiri Z uses **miniaudio** as its single sound engine in all builds (the old DirectSound implementation has been removed).

- **WINVER** — miniaudio owns the output device and outputs to it directly.
- **SDL(GENERIC)** — miniaudio runs with device I/O disabled (no-device mode) to generate PCM, and SDL3 owns the output device.

In both lines, the core of sound processing — decoding, mixing, effects, and 3D positioning — is the same.

## Specifications { #spec }

| &nbsp; | &nbsp; | &nbsp; |
| --- | --- | --- |
| Values | Bit depth | Integer: 8-bit to 32-bit<br>Floating point: 32-bit |
| Values | Channels | 1ch, 2ch, 4ch, 6ch (5.1ch) |
| Values | Sampling rate | Depends on the source (44.1 kHz / 48 kHz, etc.) |
| Settable values | Volume | 0 to 100000<br>0: fully muted<br>100000: 100% |
| Settable values | Balance<br>(panning) | -100000 to 0 to 100000<br>-100000: fully left<br>0: center<br>100000: fully right |
| Settable values | Playback position | Milliseconds, sample number |

## Supported formats { #format }

WaveSoundBuffer supports the following formats out of the box.

| Format | Extension | Notes |
| --- | --- | --- |
| WAV (RIFF PCM) | .wav | Supports WAVE_FORMAT_PCM (8- to 32-bit integer), WAVE_FORMAT_IEEE_FLOAT (32-bit float), and WAVE_FORMAT_EXTENSIBLE (PCM / IEEE_FLOAT subtypes). |
| Ogg Vorbis | .ogg | Vorbis decoding. |
| Opus | .opus | Opus decoding. |

Integer PCM is played as is, without reducing the bit depth (8-bit = unsigned / 16-, 24-, and 32-bit = signed; 24-bit is handled in its packed 3-byte form). With WAVE_FORMAT_EXTENSIBLE, if the number of valid bits is smaller than the container width (for example, 24 bits left-aligned in a 32-bit container), samples are read at the container width.

Decoder allocations go through the TLSF pool of **SoundAllocator**. The pool size can be set with `-soundpoolsize`; the default is 16MB.

Plugins can add support for more formats.

## Seamless looping (.sli) { #loop }

A sound loop information file (`.sli` file) enables seamless loop playback with no audible seams. `.sli` files, which contain the loop point settings, are created with the loop tuner.

## 3D positioning (spatializer) { #spatializer }

A 3D positioning feature based on miniaudio is provided.

- When `WaveSoundBuffer.use3D` is enabled, the buffer is treated as a 3D sound source.
- On the source side, set position, velocity, and directivity with `set3DPosition` / `set3DVelocity` / `set3DCone`, and so on.
- On the listener side, control position, orientation, velocity, and so on with `SoundListener`.

The distance attenuation model can be chosen from the following four.

| Model | Description |
| --- | --- |
| amNone | No distance attenuation |
| amInverse | Inverse attenuation |
| amLinear | Linear attenuation |
| amExponential | Exponential attenuation |

HRTF is not supported, so front and back cannot be distinguished.

## Lip-sync/analysis API { #analysis }

APIs are provided for analyzing the sound being played. They can be used for lip-sync and audio visualization.

| API | Description |
| --- | --- |
| getSoundLevel | Gets the RMS / peak level. |
| getSoundSpectrum | Gets the spectrum per frequency band. |
| getVowel | Gets estimated weights for the five Japanese vowels. |
| getVisBuffer | Gets raw PCM around the playback position. |

## Time stretching/pitch shifting { #phasevocoder }

Time stretching (tempo change) and pitch shifting with a Phase Vocoder are supported. They are applied through `WaveSoundBuffer.filters`.
