---
source_hash: 47c76d4e23d3
---

# xp3 Archive Tool

## About the xp3 archive tool

The xp3 archive tool ( `krkrxp3` ) packs the contents of a folder into an xp3 archive (Kirikiri's standard archive format). It can also list, extract, and verify the contents of archives it creates.

It succeeds the archive-creation part of the Kirikiri 2 Releaser ( krkrrel.exe ). The format is the same, and so is the default handling of each extension. It also reads Releaser profiles (.rpf) as is.

Like the other [standard tools](Tools.md), it opens its GUI in a browser window when launched. It can also be used on the command line without opening the GUI (see "Using the command line" below).

> **Note:**
> This tool does not bind archives to executables (exe) or set an exe's options or icon (see [Releaser](Releaser.md)).

## Files included in the archive

The files in the specified folder (including subfolders) are included. File names inside the archive are paths relative to that folder ( / separated).

> **Note:**
> Files and folders whose names start with . (dot) (UNIX-style hidden files, Subversion / Git metadata folders, and so on) are ignored. Folders named "CVS" (CVS metadata folders) are ignored as well.

> **Note:**
> When files with exactly the same content are found, they are stored only once, even if their names differ, and take up the space of a single file.

## Handling by extension

For each extension, you can choose whether files are "compressed", "included but not compressed (stored only)", or "not included in the archive". Normally the default classification is fine. The default classification is the same as the Kirikiri 2 Releaser.

| Handling | Extensions in this category by default |
|---|---|
| Compress | .wav .dll .tpi .spi .txt .mid .smf .swf .ks .tjs .ma .asq .asd .ttf .ttc .bmp .tft .cks |
| Exclude | .xpk .xp3 .exe .bat .tmp .db .sue .vix .ico .aul .aue .rpf .bak .log .kep .cf .cfu, files without an extension, and extensions starting with .~ (editor backups and the like) |
| Store only | Everything else (.png .jpg .tlg .ogg .opus and so on) |

Extensions are case-insensitive. Also, if the archive file being created is itself inside the folder, it is not included in the archive.

Files classified as "compress" are compressed (zlib), which makes them smaller. It also means their contents cannot easily be read by peeking with a text or binary editor. On the other hand, compression costs time when the files are decompressed. PNG, JPEG, TLG, Ogg Vorbis and similar formats are already compressed, so classifying them as "compress" gains little and makes decompression take longer; compressing them is not recommended.

Even when a file is classified as "compress", it is stored uncompressed if compression does not make it smaller.

## Options

- **Do not compress large files**  
  Even if a file is classified as "compress", it is not compressed if it is at least the specified size (default 1024 KB) (enabled by default). Because of how Kirikiri works, compressed files must be decompressed into memory, so compressing large files makes them expensive at run time.
- **Compress the index**  
  Compresses the archive's internal index (the list of stored files) to save space (enabled by default).
- **Extraction protection**  
  Adds an "extraction protection" attribute to each file in the archive's internal index. This signals to archive extraction tools that "the author does not want these files extracted" (disabled by default).
  
  When extraction protection is specified, the archive gets a warning entry at its beginning, as with the Kirikiri 2 Releaser (an entry whose name starts with "$$$ This is a protected archive. $$$ …" and consists of wording asking not to extract it).
  
  This tool does not extract protected files or the warning entry (listing and verification still work).

> **Note:**
> Specifying extraction protection **does not encrypt anything or actually prevent extraction**. It only signals the author's intent. The Kirikiri engine reads protected archives normally. If you write an archive extraction tool (should anyone do so), please take this extraction protection flag into account (for example, by refusing to extract or warning before extracting when the flag is set).

## Profiles (.rpf)

The settings for creating an archive (handling by extension, the options above, and the output file name) can be saved in a profile (.rpf). Profiles use the same format as the Kirikiri 2 Releaser, and profiles created with the Releaser can be read as is.

- If the target folder contains **default.rpf**, its settings are read when creating the archive (on the command line, you can specify a different profile with `--rpf`).
- Extensions not listed in the profile are handled by the default classification.
- If the profile records an output file name (one with the .xp3 extension), it becomes the default output file name.
- In the GUI, checking 「設定を default.rpf に保存」 (Save settings to default.rpf) saves the settings to default.rpf in the target folder when creating. On the command line, specify the destination with `--save-rpf`.
- .rpf is classified as "exclude" by default, so default.rpf never ends up in the archive.

A profile is an INI-format file like the following.

```
[Output]
Executable=0
OutputFileName=data.xp3
[Extensions]
Compress=.asd,.asq,.bmp,.cks,.dll,.ks,.ma,.mid,.smf,.spi,.swf,.tft,.tjs,.tpi,.ttc,.ttf,.txt,.wav
Store=
Discard="",.aue,.aul,.bak,.bat,.cf,.cfu,.db,.exe,.ico,.kep,.log,.rpf,.sue,.tmp,.vix,.xp3,.xpk
[Options]
DoCompressSizeLimit=1
CompressSizeLimit=1024
Protect=0
OVBookShare=0
CompressIndex=1
```

`""` stands for files without an extension. `OVBookShare` (Ogg Vorbis codebook sharing) is not used by this tool (it always writes 0 when saving).

## Compatibility

- Archives created with this tool can be read by the Kirikiri Z engine. The format is the same as archives created by the Kirikiri 2 Releaser.
- Archives created with the Kirikiri 2 Releaser, and archives bound to Kirikiri 2 executables (exe), can also be listed, extracted, and verified.

> **Note:**
> The following are not currently supported.
>
> - Encryption (creating or reading archives encrypted with the Kirikiri 2 Releaser's encryption plugin `xp3enc.dll`)
> - Codebook sharing for Ogg Vorbis files (the Releaser's 「OggVorbisコードブック共有化」 (share Ogg Vorbis codebooks) option)

## Using the GUI

Launching `krkrxp3` shows the GUI in a browser window. If you pass a folder as an argument at launch, it opens in the 「作成」 (Create) screen; if you pass an xp3 file (or .exe), it opens in the 「中身を見る」 (View contents) screen.

### 「作成」 (Create) tab

- **「元のフォルダ」 (Source folder)**  
  Specifies the folder to pack into the archive. You can also choose it with 「参照…」 (Browse...).
  
  When a folder is specified, the number of files, total size, and handling (compress / store only / exclude) are listed for each extension found in the folder. You can change the handling of each extension here. If the folder has default.rpf, the screen indicates that its settings were loaded.
- **「出力ファイル」 (Output file)**  
  Specifies the xp3 file to write. By default it is written as "folder name.xp3" in the same location as the source folder (if the profile has an output file name, that is used).
- **Options**  
  Specifies 「○ KB 以上のファイルは圧縮しない」 (Do not compress files of ○ KB or larger), 「インデックスを圧縮する」 (Compress the index), 「展開プロテクト」 (Extraction protection), and 「設定を default.rpf に保存」 (Save settings to default.rpf) (see "Options" and "Profiles (.rpf)" above).
- **「作成する」 (Create)**  
  Creates the archive. While it is running, you can stop it with 「中断」 (Abort).
  
  When finished, it shows the number of files stored (of which how many were compressed, shared because their content was identical, or excluded), and the original total size → the archive size.

### 「中身を見る」 (View contents) tab

- **「xp3 ファイル」 (xp3 file)**  
  Specify the archive to view and click 「開く」 (Open) (if you choose it with 「参照…」 (Browse...), it opens immediately).
  
  The stored files are listed with their name, size, stored size, whether they are compressed, and whether they are protected. For an archive bound to an executable, its position is shown as well.
- **「検証」 (Verify)**  
  Reads every stored file and checks that the data is not corrupted (that it can be decompressed and the checksum matches).
- **「展開」 (Extract)**  
  Extracts the files into the folder specified in 「展開先」 (Destination). The default destination is a folder named after the xp3 file (without the extension), in the same location as the xp3 file. Protected files are not extracted.

## Using the command line

With `--cli`, the tool processes on the command line without opening the GUI and then exits.

```
krkrxp3 --cli pack    <フォルダ> [--out=FILE] [--rpf=FILE] [--protect]
                      [--no-compress-index] [--size-limit=KB | --no-size-limit] [--save-rpf=FILE]
krkrxp3 --cli list    <xp3> [--json]
krkrxp3 --cli extract <xp3> [--out=DIR]
krkrxp3 --cli verify  <xp3>
```

- **pack**  
  Creates an archive from the contents of a folder. If the folder has default.rpf (and `--rpf` is not given), its settings are read, and command-line options override them.
  
  Specify the output file with `--out`. If omitted, the profile's output file name (one ending in .xp3) is used, or, failing that, "folder name.xp3" in the same location as the folder.
- **list**  
  Lists the stored files. Each line shows "original size", "stored size", "flags", and "name". The first flag character is `Z` if the file is compressed, and the second is `P` if it is protected.
- **extract**  
  Extracts the files. Specify the destination with `--out`. If omitted, it is a folder named after the xp3 file (without the extension), in the same location as the xp3 file. Protected files are not extracted.
- **verify**  
  Reads every stored file and checks that it is not corrupted. Corrupted files are shown as 「破損」 (corrupted).

| Option | Description |
|---|---|
| `--out=PATH` | Output destination (pack: xp3 file / extract: folder) |
| `--rpf=FILE` | Profile to read (default: default.rpf in the target folder) |
| `--save-rpf=FILE` | Saves the settings used as a profile |
| `--protect` | Adds extraction protection |
| `--no-compress-index` | Does not compress the index |
| `--size-limit=KB` | Does not compress files of this size or larger (default 1024) |
| `--no-size-limit` | Compresses files with compressible extensions regardless of size |
| `--json` | Outputs the results as JSON |
| `--quiet` | Does not show progress |

For example:

```
# project フォルダを ../release/data.xp3 にまとめる
krkrxp3 --cli pack project --out=../release/data.xp3

# 展開プロテクトを付けて作り、設定を default.rpf に保存する
krkrxp3 --cli pack project --protect --save-rpf=project/default.rpf

# 中身の一覧と検証
krkrxp3 --cli list data.xp3
krkrxp3 --cli verify data.xp3
```

### Exit codes

| Value | Meaning |
|---|---|
| 0 | Success |
| 1 | verify found corrupted files |
| 2 | Failure (the archive could not be opened, the profile does not exist, some files failed to extract, the operation was aborted, and so on) |
