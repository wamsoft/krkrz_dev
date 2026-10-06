# Steam Deck 実機確認 ( リリース前チェック )

Steam 配布を想定した Linux ネイティブビルドと、Steam Deck 実機での動作確認を
コマンドラインだけで回す手順です。**リリース前チェックの一項目**として使います。

道具は [steamdev](https://github.com/wamsoft/steamdev) ( ヘッドレス Steam Deck
制御 CLI + sniper クロスビルド環境 )。umbrella ルートの `deckproject.toml` が
krkrz のビルド・資材構築・起動の定義です。

- ビルド環境の中身と**バイナリの合格基準**は
  [LinuxBuild.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/LinuxBuild.md)
  ( engine 側 SSOT )
- steamdev 側の詳細は `docs/WORKFLOW.md` / `docs/DECKPROJECT.md` /
  `deckbuild/README.md`
- 作品を配布用のフォルダ / tar.gz にまとめるのは
  [Linux 版の配布パッケージ ( krkrz_linux )](linux_package.md)。その出力も
  同じ手順で Deck に送って確かめられる

---

## 0. 準備 ( 環境ごとに 1 回 )

| 要件 | 確認コマンド |
|---|---|
| steamdev CLI ( editable インストール ) | `steamdev --version` |
| WSL2 + docker + sniper ビルドイメージ | `wsl -e docker images \| grep deckbuild-sniper` |
| Deck とペアリング済み ( devkit 鍵 ) | `steamdev discover` → `steamdev -d <ip> status` |

未整備なら steamdev の README「初期セットアップ」に従います
( イメージ作成は数 GB ダウンロードで初回のみ )。

**Linux ホストから使う場合** ( WSL を使わない ) の違い:

- steamdev は `uv tool install --editable <steamdev> --with zeroconf` で入れる
  ( Debian / Ubuntu 系で python3-venv が無くても uv なら入る )。イメージは
  `bash <steamdev>/deckbuild/deckbuild.sh image`
- devkit 鍵は `~/.config/steamos-devkit/devkit_rsa`。Windows の公式クライアントで
  ペアリング済みでも、このホストは別にペアリングが要る。**Deck 側で
  「設定 → 開発者 → Pair new host」を開いてから** `steamdev -d <ip> register`
  ( 開いていないと HTTP 403 )
- Deck の `~/devkit-utils` は公式クライアント由来。Linux ホストには同梱の utils が
  無いので、一度でも Windows から転送済みなら `sync-utils` は不要
- Deck は `avahi-browse -rpt _steamos-devkit._tcp` でも見つかる
- コンテナは root で動くので、Linux ホストでは `bin/x64-linux/` が root 所有になる
  ( 戻し方は LinuxBuild.md )

Deck の IP は毎回打たずに固定できます。

```powershell
$env:STEAMDEV_DEVICE = "192.168.x.x"
```

---

## 1. チェック手順

### 1-1. Linux ビルド ( sniper コンテナ )

```bash
steamdev project -p . build linux
```

Valve 公式 Steam Linux Runtime 3.0 "sniper" SDK ( Debian 11 / glibc 2.31 /
gcc-14 ) のコンテナでビルドします。**これが Linux ビルドの合否判定基準**で、
WSL の Ubuntu などで直接ビルドが通っても確認したことにはなりません
( glibc が新しすぎて配布先で動かないため )。

成果物は `bin/x64-linux/Release/` に install されます。

### 1-2. バイナリの合格基準

```bash
wsl -e bash -lc "cd /mnt/d/.../bin/x64-linux/Release && \
  objdump -T krkrz | grep -o 'GLIBC_[0-9.]*' | sort -uV | tail -1 && \
  objdump -T krkrz | grep -c GLIBCXX"
# Linux ホストなら wsl -e を外してそのまま
readelf -d bin/x64-linux/Release/krkrz | grep RPATH     # (RPATH) [$ORIGIN]
```

- 要求 glibc の最大が **2.31 以下**
- **GLIBCXX 依存が 0** ( libstdc++ は静的リンク )
- 実行ファイルに **`$ORIGIN` の RPATH** ( 同梱 SDL3 を確実に読むため。プラグインは
  `$ORIGIN:$ORIGIN/..` )

### 1-3. 転送と起動

```bash
steamdev project -p . stage linux            # 資材構築 (.deckstage/linux)
steamdev project -p . deploy linux --start   # 転送 + Steam 登録 + 起動
# 1-1〜1-3 をまとめて: steamdev project -p . ship linux
```

### 1-4. 起動確認は「プロセス + 画面」の 2 点で

```bash
steamdev exec -- "pgrep -a krkrz"
steamdev screenshot -o deck.png
```

プロセスが居ても前面とは限りません ( gamescope は最後に起動したものを前面化 )。
**必ずスクリーンショットまで見ます**。`run-game` 直後は Steam 側の処理に
数秒〜十数秒のラグがあるので、待ってから確認します。

### 1-4b. コアデモ全シーンの表示確認 ( 推奨 )

起動引数を差し替えて `-demotest -demotestcap` を Deck 上で回すと、デモの全シーンを
巡回して PNG に撮り、終わると自分で終了します。`steamdev deploy` で起動コマンドを
一時的に差し替えます ( 引数は登録時に焼き込まれるので、終わったら
`steamdev project -p . deploy linux` で元に戻す )。

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

Steam から起動したアプリの標準出力は Deck の
`~/.local/share/Steam/logs/console-linux.txt` に入ります ( バイナリが混ざるので
`grep -a` )。読み込まれた .so は `/proc/$(pgrep -x krkrz)/maps` で確かめられます。

### 1-5. REPL で中身を確認する ( 任意 )

`deckproject.toml` の起動コマンドに `-replweb` が入っているので、Deck 上の
127.0.0.1:8899 に REPL サーバが立ちます。localhost バインドなのでトンネル必須。

```bash
steamdev tunnel -L 18899:8899        # 別ターミナルで開いたまま
# (deckproject.toml で -replwebidle=no にしてあるので、ブラウザを閉じても落ちない)
curl -s http://127.0.0.1:18899/state                       # コントローラ
curl -s -X POST -d 'System.getTickCount()' http://127.0.0.1:18899/pad/exec
curl -s -X POST -d 'op=add&expr=System.osName' http://127.0.0.1:18899/watch
```

ブラウザで `http://127.0.0.1:18899/` を開けば Console / Watch / Pad の UI が
そのまま使えます。詳細は [REPL](repl.md)。

### 1-6. 後片付け ( 必ずやる )

```bash
steamdev exec -- "pgrep -a krkrz"     # PID を確認
steamdev exec -- "kill -9 <PID>"      # 先に止める (下記の注意)
steamdev delete krkrz_linux
steamdev exec -- "ls ~/devkit-game/"  # 残骸が無いか確認
```

---

## 2. Windows ( Proton ) ターゲット

同じ仕組みで、Windows ビルドを Proton 実行して確認できます。

```bash
steamdev project -p . ship windows
```

`compat_tool` は **Deck にインストール済みの Proton** を指定します
( `deckproject.toml` は `proton-stable` )。未インストールの
`proton-experimental` 等を指定すると**無言で起動失敗**します。
Proton の初回起動は prefix 生成で数十秒かかるのが正常です。

---

## 3. ハマりどころ ( 実測 )

| 症状 | 原因と対処 |
|---|---|
| **`steamdev delete` してもアプリが動き続ける** | delete は資材とショートカットを消すだけで**プロセスは止めない**。先に kill する |
| `pkill -f krkrz_linux` が効かない / 自爆する | パターンが自分のリモートシェルにもマッチする。ブラケット ( `krkrz_[l]inux` ) でも外すことがあるので、**`pgrep -a` で PID を見て `kill -9 <PID>`** が確実 |
| Linux バイナリが即死 / 同梱 SDL3 が使われない | 同梱 `.so` の解決は exe の `$ORIGIN` (DT_RPATH) と install される soname リンク `libSDL3.so.0` に任せている。`readelf -d krkrz` に `(RPATH) [$ORIGIN]` が無い古いビルドだと、Steam の `LD_LIBRARY_PATH` に入る `/usr/lib` の SteamOS 版 SDL3 が読まれる (読まれた .so は `/proc/<pid>/maps` で確認) |
| 起動引数を変えたのに反映されない | 引数はショートカット登録時に Steam 側へ焼き込まれる。デバイス上の `<gameid>-argv.json` を書き換えても無駄で、**再デプロイが必要** |
| curl `-d 'expr=a+b'` の `+` が空白になる | form-urlencoded の仕様。`+` は **`%2B`** と書く |
| ビルドが `_mm256_*` 未定義で失敗 | sniper SDK 既定の gcc-10 が古い。deckbuild は gcc-14 を既定にしている |
| `deckbuild.sh image` が apt の 404 で失敗 | Debian 11 の LTS 終了で `bullseye-security` が deb.debian.org から消えた。steamdev `adc1343` 以降の Dockerfile は archive.debian.org に向け直している |
| ホストで Wayland 起動すると SDL の初期化で segfault | 画面 ( コンポジタ ) がスリープ中だった。ビルドの問題ではないので、画面を復帰させてから実行する |
| 外したはずの環境変数が効き続ける | Deck 側の devkit-utils は env が空だと `~/devkit-game/<gameid>-env.json` を消さない。steamdev `e39d1d9` 以降の `deploy` は env が空なら消す ( 古い steamdev で登録した title は再デプロイで消える ) |
| `invalid gameid` で deploy が失敗 | gameid は英数字・`_`・`.` だけ ( ハイフン不可 ) |
| セーブデータが見当たらない | 2026-10 から Linux 版の既定の保存場所は `~/.local/share/<orgname>/<appname>/` ( Deck なら `/home/deck/.local/share/…` )。`deckproject.toml` の構成は `.cf` が無いので `wamsoft/krkrz` |

### `-replweb` を使うときの注意 ( 2026-09-06〜 )

`-replwebidle` が**既定で有効 ( 5 秒 )** になりました。素のままだと**ブラウザで
`http://127.0.0.1:18899/` を開いて閉じた時点で、Deck 上のアプリも終了します**
( 一度でも接続が来てから武装するので、curl だけの確認では終了しません )。

実機確認は「見て閉じてまた見る」を繰り返すので、`deckproject.toml` の起動
コマンドには **`-replwebidle=no` を入れてあります**。ブラウザを閉じたら
終わってほしい使い方をするときだけ外してください。

---

## 4. 確認済みの実績

2026-09-06 に本手順を通しで実測 ( SteamOS 3.8.16 / Deck 実機 )。

- sniper コンテナで Linux ビルド成功、GLIBC ≤ 2.30 / GLIBCXX 依存なし
- 183 ファイルを stage → 転送 → 起動、デモランチャの表示をスクリーンショットで確認
- トンネル経由で `/state` `/watch` `/pad/exec` `/` ( ブラウザ UI ) すべて応答
- 後片付けまで完了

2026-10-06 に Linux ホスト ( WSL なし ) から再確認 ( SteamOS 3.8.16 )。

- sniper ビルド: GLIBC ≤ 2.30 ( プラグインも ≤ 2.31 ) / GLIBCXX 依存なし
- `-demotest -demotestcap` で全 24 シーン ok
- 同梱 SDL3 ( 3.4.0 ) が RPATH で読まれることを `/proc/<pid>/maps` で確認
  ( RPATH 対応前は SteamOS の `/usr/lib/libSDL3.so.0` ( 3.2.18 ) が読まれていた )
- krkrz_linux のサンプル案件のパッケージ ( `krkrz-sample` ) も同様に全 24 シーン ok。
  保存場所は `.cf` の `orgname` / `appname` どおり `/home/deck/.local/share/wamsoft/krkrz-sample/`

## 関連

- [REPL ( 対話型 TJS シェル )](repl.md) — `-replweb` の HTTP API とブラウザ UI
- [LinuxBuild.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/LinuxBuild.md)
  — sniper ビルド環境の中身と合格基準 ( engine 側 SSOT )
- [Linux 版の配布パッケージ ( krkrz_linux )](linux_package.md) — 作品を配布用にまとめる
- umbrella ルートの `deckproject.toml` — ビルド / 資材 / 起動の定義
