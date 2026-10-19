# WaveSoundBuffer.PhaseVocoder

WaveSoundBuffer.PhaseVocoder is a filter that you register in [WaveSoundBuffer.filters](WaveSoundBuffer.md#filters); it provides a phase vocoder.

A phase vocoder can change pitch while keeping the playback speed (pitch shifting) and change playback speed while keeping the pitch (time stretching).

## Members

### Constructors

- [PhaseVocoder](#phasevocoder)

### Properties

- [interface](#interface)
- [time](#time)
- [pitch](#pitch)
- [window](#window)
- [overlap](#overlap)

---

### PhaseVocoder

Constructor

**Description**

Constructs a PhaseVocoder object

Constructs an object of the WaveSoundBuffer.PhaseVocoder class.

Register the created instance with a WaveSoundBuffer instance through
[WaveSoundBuffer.filters](WaveSoundBuffer.md#filters).

---

### interface

Property \ Access: `r/w`

**Description**

Gets the interface object

Used internally. Do not use it from scripts.

---

### time

Property \ Access: `r/w`

**Description**

Time-axis scale

The scale along the time axis. You can also set this value.

Any real number greater than 0 can be specified. However, very small values increase CPU load and, in the worst case, may make playback impossible. Also, sound quality degrades above about 1.95, and increasing overlap may not improve it (due to the characteristics of the internal algorithm).

Specifying 1.0 leaves the time-axis scale unchanged (the playback speed does not change).

For example, specifying 1.5 scales the time axis by 1.5, so playback is slower (it takes 1.5 times as long).

For example, specifying 0.5 scales the time axis by 0.5, so playback is faster (double speed).
Even when both the time and pitch properties are 1, the phase vocoder filter still runs, slightly degrading sound quality and consuming CPU time. If you keep both at 1, it is better to remove this filter from the filter array.

Changes to this property take effect in real time, but because of buffering it takes about 2 seconds before they are actually heard. Noise may also occur at the switch.

---

### pitch

Property \ Access: `r/w`

**Description**

Frequency-axis scale

The scale along the frequency axis. You can also set this value.

Any number greater than 0.0 can be specified.

Specifying 1.0 leaves the frequency-axis scale unchanged (the pitch does not change).

For example, specifying 1.0594630943593 raises the pitch by a semitone.

For example, specifying 0.9438743126817 lowers the pitch by a semitone.

Even when both the time and pitch properties are 1, the phase vocoder filter still runs, slightly degrading sound quality and consuming CPU time. If you keep both at 1, it is better to remove this filter from the filter array.

Changes to this property take effect in real time, but because of buffering it takes about 2 seconds before they are actually heard.

---

### window

Property \ Access: `r/w`

**Description**

Window size

The window size (frame size) of the FFT (fast Fourier transform) used inside PhaseVocoder.
Specify a power of two between 64 and 32768. The default is 4096.

Increasing this value raises frequency resolution (pitch is less likely to drift) but lowers time resolution (attacks become duller).

Larger values use more CPU. Look for the smallest value that does not degrade sound quality.

For speech at 44.1 kHz, a window size of about 256 works well. For music, a window size of about 4096 works well.

Changes to this property take effect when the [WaveSoundBuffer.open](WaveSoundBuffer.md#open) method is executed.

---

### overlap

Property \ Access: `r/w`

**Description**

Overlap count

The overlap count (oversampling factor).

Specify 0 or a power of two between 2 and 32. The default is 0.

With 0, an appropriate value is chosen according to the current value of the time property.

Increasing this value raises time resolution. It is a good idea to specify a larger value especially when slowing down playback.

Larger values use more CPU.

Changes to this property take effect in real time, but because of buffering it takes about 2 seconds before they are actually heard. Noise may also occur at the switch.

---
