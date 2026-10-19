---
source_hash: e04dbe809717
---

# File Formats

This page describes the file formats supported by Kirikiri Z.

### Contents

[File formats](#fileformat)

## File formats { #fileformat }

| Kind | Format | Extension | Description |
| --- | --- | --- | --- |
| Still image | Windows bitmap (Bitmap) | .bmp | Only uncompressed files are supported. |
| Still image | JPEG | .jpg | The decoding precision can be specified.<br>The value is one of 'high', 'normal', or 'low'.<br>The default is 'normal'.<br>low: fixed-point (integer) AAN IDCT, no chroma upsampling interpolation.<br>normal: fixed-point (integer) LLM IDCT, with chroma upsampling interpolation.<br>high: floating-point AAN IDCT, with chroma upsampling interpolation.<br>For how to specify it, see [command-line option -jpegdec (JPEG decoding precision)](../guide/CommandLine.md). |
| Still image | Portable Network Graphic (PNG) | .png | Supports alpha channels and a transparent color. |
| Still image | Entis Rasterized Image format (ERI) | .eri | A lossless compression format proposed by L.Entis.<br>Images with an alpha channel can also be read. |
| Still image | TLG5 | .tlg | Kirikiri's own format.<br>Notable for fast decoding (about 4x as fast as PNG).<br>Can be converted with the [image format converter](../guide/TPC.md). |
| Still image | TLG6 | .tlg | Kirikiri's own format.<br>Compresses better than PNG or TLG5, but takes about twice as long as TLG5 to decode.<br>Even so, it is still about twice as fast as PNG.<br>Can be converted with the [image format converter](../guide/TPC.md). |
| Still image | Others | .* | Can be extended with Susie plugins. |
| Sound | WAVE | .wav | Uncompressed WAVE is supported. |
| Sound | Ogg Vorbis | .ogg | Built into the engine (no extra DLL needed). |
| Sound | Opus | .opus | Built into the engine (no extra DLL needed). |
| Sound | Others | .* | Can be extended with plugins. |
| Movie | WebM | .webm | VP8 / VP9. Supports movies with alpha (transparency). The movie playback mechanism is built into the engine (no extra DLL needed). |
| Movie | MPEG-1 | .mpg<br>.mpeg<br>.mpv<br>.m1v<br>.dat | Only MPEG-1 is supported (MPEG-2 and later are not). Decoded with the built-in pl_mpeg. |
| Movie | MP4 | .mp4<br>.m4v<br>.mov | H.264 / HEVC. Decoded with Media Foundation (hardware decoding by default). |
| Movie | Windows Media Video (WMV) | .wmv<br>.asf | Decoded with Media Foundation. The playback machine needs the Windows Media components. |
| Movie | AVI | .avi | Unofficially supported. Plays only if the internal codec can be handled by Media Foundation (not officially supported). |
| Animation | ASD file | .asd | Kirikiri's own animation definition format.<br>See the comments in AnimationLayer.tjs. |
| Archive | XP3 | .xp3 | Kirikiri's own format.<br>Created with the [xp3 archive tool](../guide/Xp3Tool.md). |
| Archive | PEXP3 | .exe | Kirikiri's own format.<br>Combines the Kirikiri executable (krkr.eXe) with an XP3 archive.<br>Deprecated.<br>The xp3 is appended to the end of the executable (can be created with the [Releaser](../guide/Releaser.md)). |
| Archive | Others | .* | Can be extended with plugins. |
| Font | Pre-rendered font | .tft | Kirikiri's own format.<br>Generated with the tftSave plugin ([Creating pre-rendered font data](../guide/FontMaker.md)). |
| Font | TrueType/OpenType font | .ttf<br>.otf | Unofficially supported.<br>Can be used without installing the font on the system.<br>Requires [addFont.dll](https://github.com/wamsoft/addFont). Windows only. |
