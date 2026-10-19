---
source_hash: c2bc1160a597
---

# Audio Format Converter

## About the audio format converter

The audio format converter (`krkraudio`) converts the format of sound files played in Kirikiri and evens out their volume. It is one of the [standard tools](Tools.md).

- Converts between WAV, Ogg Vorbis, and Ogg Opus
- Can change the volume during conversion, or bring the loudness (perceived volume) to a specified value
- If loop information (a .sli file) exists, writes it out for the converted file as well
- Can measure the loudness and peak of sounds
- Can write out the volume at fixed intervals for lip sync

Converted sounds and .sli files have been confirmed to open in the Kirikiri engine.

## Supported formats

| Format | Read | Write |
|---|---|---|
| WAV | Integer PCM 8 / 16 / 24 / 32-bit, floating point 32 / 64-bit (WAVE_FORMAT_EXTENSIBLE is also supported) | 16-bit / 24-bit / 32-bit float |
| Ogg Vorbis (.ogg) | Yes | Specify quality (VBR) |
| Ogg Opus (.opus) | Yes | Specify bitrate (automatic by default) |

- The format is determined by the file contents (the extension does not matter)
- The output file name is the source file name with its extension replaced by `.ogg` / `.opus` / `.wav`
- The sample rate and number of channels are kept. However, **Ogg Opus is always 48 kHz** (converting from Opus to WAV / Vorbis also stays at 48 kHz)
- Ogg Vorbis / Ogg Opus comments (tags) are carried over to the output (except ENCODER and ReplayGain / R128 related tags). Converting to WAV drops the tags
- When writing 16-bit / 24-bit WAV, any portion that exceeds ±1.0 after raising the volume is clipped (causing distortion). 32-bit float is not clipped

## Carrying over loop information (.sli)

If the source has a «filename.sli» (loop information created with the [loop tuner](LoopTuner.md)), a «output filename.sli» is written for the output as well.

Positions in .sli are in samples, so when the sample rate changes (when converting to Opus), link and label positions are converted to the new sample rate (rounded to the nearest sample). For example, position 44100 in a 44.1 kHz sound becomes 48000 in Opus.

> **Note:**
> Because the conversion can introduce errors of less than one sample, and lossy compression slightly alters the waveform, the seam may sound different. For important loops, open the converted file in the loop tuner to check. You can also use `krkrloop --cli check` to check whether the .sli positions are within the range of the sound.

If the .sli is in a format the engine cannot read, the file is converted without writing the .sli.

## Volume handling

### How the Kirikiri engine handles volume

The Kirikiri engine applies the following gains when decoding compressed sound (see «サウンドのゲイン» (sound gain) in [command-line options](CommandLine.md) for details).

- **Ogg Opus header gain** (output gain)  
  The gain written in the header of an Opus file is **always** applied by the engine. This lets you change the volume without rewriting the waveform.
- **Ogg Vorbis ReplayGain tags**  
  The `replaygain_track_gain` / `replaygain_album_gain` tags are applied only when the engine is launched with `-ogg_rg=track` (or `album`). By default (`none`), they are not used.

### Changing the volume (--gain)

Changes the volume by the specified number of dB (positive values make it louder, negative values quieter).

- **When converting to Opus**: written to the header gain. The waveform is not changed
- **When converting to Vorbis / WAV**: baked into the waveform

When converting Opus to anything other than Opus, the original Opus header gain is baked into the waveform (so the volume stays as it sounded in the engine). When converting Opus to Opus, the original header gain plus the specified gain becomes the new header gain.

### Normalizing loudness (--normalize)

Measures the integrated loudness of the sound (EBU R128) and determines a gain that brings it to the specified value (LUFS). For example, `--normalize=-18` normalizes to -18 LUFS. Use this to even out the perceived volume of multiple BGM tracks or voice files.

The gain is applied the same way as `--gain` (header gain for Opus, baked in for the others). If specified together with `--gain`, that value is added as well.

> **Note:**
> Normalizing loudness can push peaks above 1.0 (no limiter is applied). When raising the volume substantially, check the peak with «音量の測定» (Measure loudness) after conversion.

### ReplayGain tags (--replaygain)

When converting to Ogg Vorbis, writes the `REPLAYGAIN_TRACK_GAIN` (the gain to match the ReplayGain 2.0 reference of -18 LUFS) and `REPLAYGAIN_TRACK_PEAK` (peak) tags. The values are computed from the sound after `--gain` / `--normalize` have been applied.

These tags take effect only when the engine is launched with `-ogg_rg=track`. Use them when you want to enable volume correction through a command-line option without changing the waveform or the header. They are ignored when converting to anything other than Vorbis.

> **Note:**
> If you work actively with gain and loudness, we recommend Ogg Opus, whose header gain the engine always applies.

## Using the GUI

```
krkraudio                    画面を開く
krkraudio <ファイル>...       画面を開き、ファイルを一覧に入れる
```

The GUI opens in a browser window (see [Standard Tools](Tools.md) for launching and other common points).

The top of the screen is the list of files to process. «追加…» (Add...) adds files, and «クリア» (Clear) empties the list. The list shows the format, sample rate, number of channels, length (seconds), gain (Opus header gain or Vorbis ReplayGain tag), and whether a .sli exists.

Below it are three tabs.

### 変換 (Convert)

Converts all files in the list.

- **変換先 (Output format)**: Ogg Vorbis / Ogg Opus / WAV
- **品質 (Quality)** (Ogg Vorbis): -0.1 to 1.0 (default 0.4). Higher values give better quality and larger files
- **ビットレート (Bitrate)** (Ogg Opus): in kbps. 0 means automatic
- **ビット数 (Bit depth)** (WAV): 16 / 24 / 32 (float)
- **音量 (Volume)**: in dB (same as `--gain`)
- **ラウドネスを ○○ LUFS に揃える (Normalize loudness to ○○ LUFS)**: when checked, does the same as `--normalize` (default -18)
- **ReplayGain タグを書く (Write ReplayGain tags)** (Ogg Vorbis): does the same as `--replaygain`
- **出力フォルダ (Output folder)**: when empty, output goes to the same folder as the source file. You can choose it with «参照…» (Browse...)
- **上書き (Overwrite)**: when unchecked, existing output files are not overwritten and the conversion fails

«変換する» (Convert) starts the conversion, and «中断» (Abort) stops it. The result list shows, for each file, the output destination, whether a .sli was written (and the sample rate if positions were converted), and the ReplayGain value written.

### 音量の測定 (Measure loudness)

For every file in the list, measures and shows the integrated loudness (EBU R128, LUFS), the peak (0 to 1), and the gain needed to reach -18 LUFS. The values represent the volume as played by the engine (including the header gain for Opus).

### 口パク用の音量 (Lip-sync volume)

For the **first file** in the list, writes out the volume at fixed intervals. Use it for things like how wide a character's mouth opens in lip sync.

- **1 秒あたり (Per second)**: the number of values per second (default 30)
- **形式 (Format)**: JSON / CSV
- **保存先 (Save to)**: if you specify a file name, the data is saved there. When empty, it is only shown on screen

For the output format, see "Lip-sync volume format" below.

## Using the command line

With `--cli`, the tool processes without opening the GUI.

```
krkraudio --cli info     <ファイル>...
krkraudio --cli convert  <ファイル>... --to=ogg|opus|wav [--out=DIR]
                         [--quality=Q] [--bitrate=KBPS] [--bits=16|24|32]
                         [--gain=DB] [--normalize=LUFS] [--replaygain] [--force]
krkraudio --cli loudness <ファイル>...
krkraudio --cli lipsync  <ファイル> [--fps=30] [--format=json|csv] [--out=FILE]
```

| Option | Meaning |
|---|---|
| `--to=ogg\|opus\|wav` | Output format (required for convert) |
| `--out=DIR` | convert: output folder (created if missing; defaults to the source file's folder)<br>lipsync: output file (defaults to standard output) |
| `--quality=Q` | Ogg Vorbis quality, -0.1 to 1.0 (default 0.4) |
| `--bitrate=KBPS` | Ogg Opus bitrate (default: automatic) |
| `--bits=16\|24\|32` | WAV bit depth (default 16; 32 is float) |
| `--gain=DB` | Changes the volume (header gain for Opus, baked into the waveform for the others) |
| `--normalize=LUFS` | Normalizes the integrated loudness to this value (e.g. `-18`) |
| `--replaygain` | Writes `REPLAYGAIN_TRACK_GAIN` / `PEAK` to Ogg Vorbis |
| `--force` | Overwrites the output even if it already exists |
| `--fps=N` | lipsync: number of values per second (default 30) |
| `--format=json\|csv` | lipsync: output format (default json) |
| `--json` | Outputs info / convert / loudness results as JSON |
| `--quiet` | Does not show progress |

If the output would be the same file as the input (for example, converting WAV to WAV in the same folder), the file is not converted. Specify a different folder with `--out`.

### Examples

```
> krkraudio --cli info bgm.wav out/bgm.opus
bgm.wav: wav 44100 Hz 2 ch 3.000 秒 (132300 サンプル) 16bit
out/bgm.opus: opus 48000 Hz 2 ch 3.000 秒 (144000 サンプル) ヘッダゲイン -6.00 dB
    ENCODER=krkrz_tools
```

Convert WAV to Opus (the .sli is converted to 48 kHz):

```
> krkraudio --cli convert bgm.wav --to=opus --out=out
変換	bgm.wav	→ out/bgm.opus	(.sli 44100 → 48000 Hz)
```

Convert a batch of BGM to Ogg Vorbis, normalized to -18 LUFS:

```
krkraudio --cli convert bgm/*.wav --to=ogg --quality=0.5 --normalize=-18 --out=data/bgm
```

Convert voice files to Opus, lowering them 6 dB with the header gain:

```
krkraudio --cli convert voice/*.wav --to=opus --gain=-6 --out=data/voice
```

Measure loudness:

```
> krkraudio --cli loudness bgm.wav out/bgm.opus
bgm.wav: -11.14 LUFS / ピーク 0.3000 / ReplayGain -6.86 dB
out/bgm.opus: -17.10 LUFS / ピーク 0.1535 / ReplayGain -0.90 dB
```

«ReplayGain» is the gain needed to reach -18 LUFS.

### Exit codes

| Code | Meaning |
|---|---|
| 0 | Success |
| 2 | Failure (a file could not be read, the output already exists, and so on) |

When processing multiple files, the remaining files are still processed even if some fail.

## Lip-sync volume format

> **Note:**
> This output format is provisional. It may change when features such as vowel estimation are added.

The sound is divided into intervals of «1 / fps» seconds, and for each interval the RMS (root mean square) and the peak (maximum absolute value) of the sound with all channels mixed are output as values from 0 to 1. For Opus, the volume is computed with the header gain applied.

JSON:

```
{"source":"voice.wav","fps":10,"frames":10,"rms":[0.35353,0.35353,...],"peak":[0.49997,0.49997,...]}
```

| Member | Content |
|---|---|
| `source` | File name of the sound |
| `fps` | Number of values per second |
| `frames` | Number of values |
| `rms` | Array of RMS values per interval |
| `peak` | Array of peak values per interval |

CSV:

```
frame,time,rms,peak
0,0.0000,0.35353,0.49997
1,0.1000,0.35353,0.49997
...
```

`frame` is the interval number, and `time` is the start time of the interval (seconds).

To get the volume during playback in real time, you can also use the engine's [WaveSoundBuffer.getSoundLevel](../reference/WaveSoundBuffer.md#getsoundlevel) and similar.
