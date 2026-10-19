---
source_hash: 5eb8a20c6392
---

# Steam Deck hardware check (pre-release check)

This is the procedure for building a native Linux binary intended for Steam
distribution and verifying it on actual Steam Deck hardware, entirely from the
command line. Use it as **one item of the pre-release checklist**.

The tool is [steamdev](https://github.com/wamsoft/steamdev) (a headless Steam Deck
control CLI + sniper cross-build environment). `deckproject.toml` at the umbrella
root defines how krkrz is built, staged, and launched.

- The build environment and the **pass criteria for binaries** are described in
  [LinuxBuild.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/LinuxBuild.md)
  (the engine-side SSOT)
- For steamdev details, see `docs/WORKFLOW.md` / `docs/DECKPROJECT.md` /
  `deckbuild/README.md`
- Packaging a title into a distributable folder / tar.gz is covered in
  [Linux distribution package (krkrz_linux)](linux_package.md). Its output can be
  sent to the Deck and checked with the same procedure

---

## 0. Preparation (once per environment)

| Requirement | Check command |
|---|---|
| steamdev CLI (editable install) | `steamdev --version` |
| WSL2 + docker + sniper build image | `wsl -e docker images \| grep deckbuild-sniper` |
| Paired with the Deck (devkit key) | `steamdev discover` → `steamdev -d <ip> status` |

If anything is missing, follow "Initial setup" in the steamdev README
(creating the image downloads several GB, first time only).

Differences **when using a Linux host** (no WSL):

- Install steamdev with `uv tool install --editable <steamdev> --with zeroconf`
  (uv works even on Debian / Ubuntu without python3-venv). Build the image with
  `bash <steamdev>/deckbuild/deckbuild.sh image`
- The devkit key is `~/.config/steamos-devkit/devkit_rsa`. Even if you have paired via
  the official Windows client, this host needs its own pairing. **Open
  "Settings → Developer → Pair new host" on the Deck first**, then run
  `steamdev -d <ip> register` (without it open you get HTTP 403)
- `~/devkit-utils` on the Deck comes from the official client. A Linux host has no
  bundled utils, so if they have ever been transferred from Windows, `sync-utils`
  is unnecessary
- The Deck can also be found with `avahi-browse -rpt _steamos-devkit._tcp`
- The container runs as root, so on a Linux host `bin/x64-linux/` ends up owned by
  root (see LinuxBuild.md for how to restore it)

You can fix the Deck's IP instead of typing it every time.

```powershell
$env:STEAMDEV_DEVICE = "192.168.x.x"
```

---

## 1. Check procedure

### 1-1. Linux build (sniper container)

```bash
steamdev project -p . build linux
```

This builds in a container of Valve's official Steam Linux Runtime 3.0 "sniper" SDK
(Debian 11 / glibc 2.31 / gcc-14). **This is the pass/fail criterion for Linux
builds**; a successful direct build on WSL Ubuntu or the like does not count as
confirmation (its glibc is too new to run on target systems).

Artifacts are installed to `bin/x64-linux/Release/`.

### 1-2. Binary pass criteria

```bash
wsl -e bash -lc "cd /mnt/d/.../bin/x64-linux/Release && \
  objdump -T krkrz | grep -o 'GLIBC_[0-9.]*' | sort -uV | tail -1 && \
  objdump -T krkrz | grep -c GLIBCXX"
# Linux ホストなら wsl -e を外してそのまま
readelf -d bin/x64-linux/Release/krkrz | grep RPATH     # (RPATH) [$ORIGIN]
```

- The highest required glibc is **2.31 or lower**
- **Zero GLIBCXX dependencies** (libstdc++ is statically linked)
- The executable has an **RPATH of `$ORIGIN`** (to reliably load the bundled SDL3;
  plugins use `$ORIGIN:$ORIGIN/..`)

### 1-3. Transfer and launch

```bash
steamdev project -p . stage linux            # 資材構築 (.deckstage/linux)
steamdev project -p . deploy linux --start   # 転送 + Steam 登録 + 起動
# 1-1〜1-3 をまとめて: steamdev project -p . ship linux
```

### 1-4. Confirm launch by both "process + screen"

```bash
steamdev exec -- "pgrep -a krkrz"
steamdev screenshot -o deck.png
```

A running process is not necessarily in the foreground (gamescope brings the most
recently launched one to the front). **Always check the screenshot too**. Right after
`run-game`, Steam takes several to a dozen-plus seconds to process, so wait before
checking.

### 1-4b. Display check of all core demo scenes (recommended)

Running `-demotest -demotestcap` on the Deck with replaced launch arguments cycles
through every demo scene, captures each to PNG, and exits on its own when done. Use
`steamdev deploy` to temporarily replace the launch command (arguments are baked in
at registration time, so restore them afterward with
`steamdev project -p . deploy linux`).

```bash
steamdev project -p . stage linux
steamdev deploy --gameid krkrz_linux --dir .deckstage/linux --clean --start \
    --command "./krkrz data -demotest -demotestcap=/home/deck/krkrz_demotest -loglevel=info"
# 終了待ち: steamdev exec -- "pgrep -x krkrz" が空になるまで
steamdev exec -- "ls /home/deck/krkrz_demotest | wc -l"     # シーン数
steamdev exec -- "grep -a '@demotest:' ~/.local/share/Steam/logs/console-linux.txt | tail -2"
steamdev ssh-command      # 表示された ssh のオプションで rsync -e "ssh ..." すればキャプチャを回収できる
steamdev project -p . deploy linux                            # 起動コマンドを戻す
```

Standard output of apps launched from Steam goes to
`~/.local/share/Steam/logs/console-linux.txt` on the Deck (it contains binary data,
so use `grep -a`). Loaded .so files can be checked via `/proc/$(pgrep -x krkrz)/maps`.

### 1-5. Inspecting internals with the REPL (optional)

The launch command in `deckproject.toml` includes `-replweb`, so a REPL server runs
on 127.0.0.1:8899 on the Deck. It is bound to localhost, so a tunnel is required.

```bash
steamdev tunnel -L 18899:8899        # 別ターミナルで開いたまま
# (deckproject.toml で -replwebidle=no にしてあるので、ブラウザを閉じても落ちない)
curl -s http://127.0.0.1:18899/state                       # コントローラ
curl -s -X POST -d 'System.getTickCount()' http://127.0.0.1:18899/pad/exec
curl -s -X POST -d 'op=add&expr=System.osName' http://127.0.0.1:18899/watch
```

Opening `http://127.0.0.1:18899/` in a browser gives you the Console / Watch / Pad UI
as-is. See [REPL](repl.md) for details.

### 1-6. Cleanup (always do this)

```bash
steamdev exec -- "pgrep -a krkrz"     # PID を確認
steamdev exec -- "kill -9 <PID>"      # 先に止める (下記の注意)
steamdev delete krkrz_linux
steamdev exec -- "ls ~/devkit-game/"  # 残骸が無いか確認
```

---

## 2. Windows (Proton) target

The same mechanism lets you check a Windows build running under Proton.

```bash
steamdev project -p . ship windows
```

`compat_tool` must specify **a Proton version installed on the Deck**
(`deckproject.toml` uses `proton-stable`). Specifying one that is not installed, such
as `proton-experimental`, **fails to launch silently**.
The first Proton launch normally takes tens of seconds to create the prefix.

---

## 3. Pitfalls (observed)

| Symptom | Cause and fix |
|---|---|
| **The app keeps running after `steamdev delete`** | delete only removes the files and the shortcut; it **does not stop the process**. Kill it first |
| `pkill -f krkrz_linux` does nothing / kills itself | The pattern also matches your own remote shell. Even brackets (`krkrz_[l]inux`) sometimes miss, so **check the PID with `pgrep -a` and `kill -9 <PID>`** reliably |
| Linux binary dies immediately / bundled SDL3 is not used | Resolution of bundled `.so` files relies on the exe's `$ORIGIN` (DT_RPATH) and the installed soname link `libSDL3.so.0`. An older build without `(RPATH) [$ORIGIN]` in `readelf -d krkrz` loads SteamOS's SDL3 from `/usr/lib`, which is on Steam's `LD_LIBRARY_PATH` (check loaded .so files in `/proc/<pid>/maps`) |
| Changed launch arguments are not reflected | Arguments are baked into Steam when the shortcut is registered. Editing `<gameid>-argv.json` on the device is pointless; **a redeploy is required** |
| The `+` in curl `-d 'expr=a+b'` becomes a space | That is how form-urlencoded works. Write `+` as **`%2B`** |
| Build fails with `_mm256_*` undefined | The sniper SDK's default gcc-10 is too old. deckbuild defaults to gcc-14 |
| `deckbuild.sh image` fails with apt 404 | With the end of Debian 11 LTS, `bullseye-security` was removed from deb.debian.org. The Dockerfile in steamdev `adc1343` and later points to archive.debian.org |
| SDL initialization segfaults when launched under Wayland on the host | The display (compositor) was asleep. It is not a build problem; wake the display and run again |
| An environment variable you removed keeps taking effect | The Deck-side devkit-utils does not delete `~/devkit-game/<gameid>-env.json` when env is empty. `deploy` in steamdev `e39d1d9` and later deletes it when env is empty (titles registered with an older steamdev get it removed on redeploy) |
| deploy fails with `invalid gameid` | gameid may contain only alphanumerics, `_`, and `.` (no hyphens) |
| Save data cannot be found | Since 2026-10, the default save location for the Linux version is `~/.local/share/<orgname>/<appname>/` (`/home/deck/.local/share/…` on the Deck). The `deckproject.toml` setup has no `.cf`, so it is `wamsoft/krkrz` |

### Notes on using `-replweb` (since 2026-09-06)

`-replwebidle` is now **enabled by default (5 seconds)**. Left as-is, **opening
`http://127.0.0.1:18899/` in a browser and then closing it also quits the app on the
Deck** (it arms only after at least one connection arrives, so checking with curl
alone does not trigger an exit).

Hardware checks involve repeatedly looking, closing, and looking again, so the launch
command in `deckproject.toml` **includes `-replwebidle=no`**. Remove it only when you
want the app to exit when the browser is closed.

---

## 4. Verified runs

The whole procedure was run end-to-end on 2026-09-06 (SteamOS 3.8.16 / actual Deck).

- Linux build succeeded in the sniper container, GLIBC ≤ 2.30 / no GLIBCXX dependencies
- Staged → transferred → launched 183 files, confirmed the demo launcher via screenshot
- Through the tunnel, `/state` `/watch` `/pad/exec` `/` (browser UI) all responded
- Completed through cleanup

Re-verified on 2026-10-06 from a Linux host (no WSL) (SteamOS 3.8.16).

- sniper build: GLIBC ≤ 2.30 (plugins also ≤ 2.31) / no GLIBCXX dependencies
- All 24 scenes ok with `-demotest -demotestcap`
- Confirmed via `/proc/<pid>/maps` that the bundled SDL3 (3.4.0) is loaded through RPATH
  (before RPATH support, SteamOS's `/usr/lib/libSDL3.so.0` (3.2.18) was loaded)
- The krkrz_linux sample project package (`krkrz-sample`) also passed all 24 scenes.
  Its save location follows `orgname` / `appname` in the `.cf`:
  `/home/deck/.local/share/wamsoft/krkrz-sample/`

## Related

- [REPL (interactive TJS shell)](repl.md) — the `-replweb` HTTP API and browser UI
- [LinuxBuild.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/LinuxBuild.md)
  — contents of the sniper build environment and pass criteria (engine-side SSOT)
- [Linux distribution package (krkrz_linux)](linux_package.md) — packaging a title for distribution
- `deckproject.toml` at the umbrella root — build / staging / launch definitions
