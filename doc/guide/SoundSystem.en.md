---
source_hash: 8a41e4c215b2
---

# Sound System

## About the Sound System

The Kirikiri sound system can play Wave (PCM) audio.

Multiple Wave sounds can play at the same time, and streaming playback (playing a long sound while loading it a little at a time) is supported. With a sound loop information file (.sli file), you can also get seamless loop playback with no audible joint (sound loop information files are created with Loop Tuner).

## Formats Playable by WaveSoundBuffer

By default, [WaveSoundBuffer](../reference/WaveSoundBuffer.md) can play the uncompressed RIFF Wave format ( extension .wav, the standard Windows format ). The accepted formats are:

- WAVE_FORMAT_PCM, integer PCM from 8 bit to 32 bit, with 1 (mono), 2 (stereo), 4 (quadraphonic), or 6 (5.1ch) channels
- WAVE_FORMAT_IEEE_FLOAT, 32-bit floating-point PCM, with 1 (mono), 2 (stereo), 4 (quadraphonic), or 6 (5.1ch) channels
- WAVE_FORMAT_EXTENSIBLE with subtype KSDATAFORMAT_SUBTYPE_PCM, integer PCM from 8 bit to 32 bit
- WAVE_FORMAT_EXTENSIBLE with subtype KSDATAFORMAT_SUBTYPE_IEEE_FLOAT, 32-bit floating-point PCM

Plugins can extend the formats WaveSoundBuffer can play.

## Handling of 4ch and 6ch in WaveSoundBuffer

WAVE_FORMAT_EXTENSIBLE carries information in the data about which channel is assigned to which speaker, but WAVE_FORMAT_PCM and WAVE_FORMAT_IEEE_FLOAT do not. When Kirikiri handles 4ch or 6ch data in WAVE_FORMAT_PCM or WAVE_FORMAT_IEEE_FLOAT, it interprets the channels as follows.

- **4ch**  
  Starting from the first channel, the data is treated as front left, front right, rear left, and rear right speaker data
- **6ch**  
  Starting from the first channel, the data is treated as front left, front center, front right, rear left, rear right, and low-frequency (LFE) speaker data

The same rule also applies when playing 4ch or 6ch sounds in Ogg Vorbis.
