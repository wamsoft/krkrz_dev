---
source_hash: e60a5fb508b3
---

# File Corruption Check Tool

## About the file corruption check tool

Data can become **corrupted** during installation, or afterwards through computer malfunctions and the like.

The file corruption check tool (`krkrcheck`) detects such corrupted files. It is meant to be run on the end user's machine to check whether the distributed files are intact.

To detect file corruption, you must first sign the distribution files with the [key and signing tool](SignTool.md).

The file corruption check tool also verifies the validity of these **digital signatures** (files whose signature cannot be validated are treated as "corrupted" by this tool). Signatures made with a different key and damaged signature files are also reported as "corrupted".

By default, the files checked are those in and under the folder where the tool itself is placed (subfolders are searched as well). For this reason, place the tool in the installation folder.

The tool checks only signed files, that is, files with a signature file named «filename.sig» next to them. Unsigned files are not checked.

> **Note:**
> The Kirikiri Z engine executable has no "area for embedding a signature inside the exe" as in Kirikiri 2. The engine executable is signed with «filename.sig» just like any other file, so **be sure to sign the engine executable as well**. An unsigned engine executable is not checked.
>
> An exe with an embedded signature, such as a Kirikiri 2 engine executable, is checked using that embedded signature even without a .sig.

> **Note:**
> The file corruption check tool can detect corrupted files, but cannot by itself detect that a file is missing.
>
> If you suspect missing files are causing an error, the tool's 「結果をコピー」 (Copy results) button copies to the clipboard both the list of files the tool checked and the list of all files in the target folder. Ask the end user to send it to you for investigation.

## Getting the tool

The file corruption check tool is one of the Kirikiri Z [standard tools](Tools.md).

- When you build the engine in krkrz_dev, it is built along with it, and `make install` places `krkrcheck` (`krkrcheck.exe` on Windows) in the `tools/` folder of the install destination
- The source is in the [krkrz_tools](https://github.com/wamsoft/krkrz_tools) repository, and it can also be built on its own

The tool runs as a single executable (Windows / Linux / macOS). When distributing it to end users, ship this executable together with the settings file (.ini) described below.

## Settings file

The tool reads «executable name.ini» as its settings file: `krkrcheck.ini` for `krkrcheck.exe`, or 「ファイル破損チェックツール.ini」 if you renamed the executable to 「ファイル破損チェックツール.exe」. Place the settings file in the same folder as the executable.

This file holds the tool's settings and must be distributed together with the tool. Without the settings file there is no public key, so no check can be performed.

> **Note:**
> If you rename the executable, rename the settings file to match. For example, if you rename it to 「署名確認ツール.exe」, name the settings file 「署名確認ツール.ini」.

The settings file format is the same as Kirikiri 2's 「ファイル破損チェックツール.ini」, so an ini you used with Kirikiri 2 works as is. The character encoding may be either Shift_JIS or UTF-8.

> **Note:**
> Only the Windows version reads a Shift_JIS ini correctly. When using the tool on Linux / macOS, write the file in UTF-8.

The available settings are described below.

- **[message] section - notice**  
  Specifies the message shown at the top of the screen.
  
  A line starting with notice= must be written on a single line (without line breaks), but you can insert a line break by writing [cr].
- **[message] section - caption**  
  Specifies the string shown as the window title and the screen heading. If omitted, it is 「ファイル破損チェックツール」 (File Corruption Check Tool).
- **[key] section - publickey**  
  Specifies the **public key** used to verify the digital signatures.
  
  Paste the public key here directly (without writing anything like 'name='). The tool searches the whole ini for the part from `-----BEGIN PUBLIC KEY-----` to `-----END PUBLIC KEY-----` and reads it as the public key.

Here is an example settings file.

```
[message]
notice=ファイルが破損していないかをチェックします。[cr]「チェック」ボタンを押してください。
caption=ファイル破損チェックツール

[key]
-----BEGIN PUBLIC KEY-----
MIGJAoGBAK0XoW5bq0F/8RpO/+n1IP0bYFGuJRdLqdZpUpyKzhfas4sq884DUHdT
rB1D84VUAnEER797Jo8Ck82GTtKIdMqpO4rinNVbpIzvxA6Qgi/s8u5+YtEv5pEc
V3WIF2zEufQ6SJ2LNbv3nXOy8zVOYG7fpS2PLmaCgXkZVX1AuB1RAgMBAAE=
-----END PUBLIC KEY-----
```

## Usage

Launching the tool's executable opens the check screen in a browser window (the screen is embedded in the executable, so no internet connection is needed).

The screen heading shows the caption from the settings file, and the notice message appears below it.

- **対象フォルダ (Target folder)**  
  The folder to check. Initially it contains the executable's folder (or the folder specified at launch). You can choose a different folder with the 「参照…」 (Browse...) button.
- **チェック (Check)**  
  Starts the check. The tool searches the target folder and checks each signed file in turn.
  
  Checking large files takes time. Progress is shown in the progress bar.
- **中断 (Abort)**  
  Aborts the running check.
- **Result list**  
  Shows the list of checked files with their file name, status, size, and modification time.
  
  The status column shows 「正常」 (OK), 「破損」 (Corrupted), or 「エラー」 (Error). A corrupted file is shown as 「破損」. A file that could not be checked, for example because it could not be read, is shown as 「エラー」 along with the reason.
  
  The number of OK, corrupted, and error files is shown above the list.
- **結果をコピー (Copy results)**  
  Copies the results to the clipboard.
  
  This is convenient when asking end users to send you their check results.
  
  It becomes enabled (clickable) once the check completes.
  
  The results are tab-separated data with, from left to right: file name, file date, file size, and check result.
  
  The list of all files and folders in the target folder is copied as well. If unexpected files may be present, you can check this output for them.

Closing the screen also exits the tool.

> **Note:**
> Files and folders whose names start with `.` are not searched. Signature files (.sig) themselves are not checked.

## Using the command line

With `--cli`, the tool performs the check on the command line without opening the screen, prints the results, and exits. This is useful for checks before distribution and for build automation.

```
krkrcheck                           画面を開く (対象 = 実行ファイルのフォルダ)
krkrcheck <フォルダ>                 画面を開く (対象フォルダを指定)
krkrcheck --cli [<フォルダ>] [--key=<ini または公開鍵>] [--json | --tsv] [--quiet]
```

If the folder is omitted, the executable's folder is checked.

The options are as follows. Options that take a value are written as `--name=value`.

- **--key=file**  
  Specifies the file to read the public key from. It can be a settings file (.ini) or a public key file created with the [key and signing tool](SignTool.md). If omitted, «executable name.ini» is read.
- **--json**  
  Outputs the results as JSON.
- **--tsv**  
  Outputs the results in the same tab-separated format as 「結果をコピー」 (Copy results).
- **--quiet**  
  Suppresses progress and per-file results (on standard error).

For example, to check the distribution folder release with the local public key public.txt:

```
krkrcheck --cli release --key=public.txt
```

Per-file results are shown on standard error, and when neither `--json` nor `--tsv` is given, a summary is printed to standard output at the end.

```
破損	b.dat
正常	data/a.txt
正常	krkrz64.exe
正常 2 / 破損 1 / エラー 0 (対象 3 / 全ファイル 7)
```

The `--json` output contains the summary (`ok` / `broken` / `error`) and an `entries` array whose items have `path` / `status` (`ok` / `broken` / `error`) / `label` / `message` / `size` / `mtime` for each file.

The exit codes are as follows.

| Exit code | Meaning |
|---|---|
| 0 | All files are OK |
| 1 | Some files are corrupted |
| 2 | Some files could not be checked, or the check failed (for example, no public key) |

For options common to all tools (`--help` and others), see [Standard Tools](Tools.md).
