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

---

## 0. 準備 ( 環境ごとに 1 回 )

| 要件 | 確認コマンド |
|---|---|
| steamdev CLI ( editable インストール ) | `steamdev --version` |
| WSL2 + docker + sniper ビルドイメージ | `wsl -e docker images \| grep deckbuild-sniper` |
| Deck とペアリング済み ( devkit 鍵 ) | `steamdev discover` → `steamdev -d <ip> status` |

未整備なら steamdev の README「初期セットアップ」に従います
( イメージ作成は数 GB ダウンロードで初回のみ )。

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
```

- 要求 glibc の最大が **2.31 以下**
- **GLIBCXX 依存が 0** ( libstdc++ は静的リンク )

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

### 1-5. REPL で中身を確認する ( 任意 )

`deckproject.toml` の起動コマンドに `-replweb` が入っているので、Deck 上の
127.0.0.1:8899 に REPL サーバが立ちます。localhost バインドなのでトンネル必須。

```bash
steamdev tunnel -L 18899:8899        # 別ターミナルで開いたまま
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
| Linux バイナリが即死 | 同梱 `.so` の soname 欠落 / RPATH 無し。`deckproject.toml` の stage script が `libSDL3.so.0` を補完し、`LD_LIBRARY_PATH=.` で起動している |
| 起動引数を変えたのに反映されない | 引数はショートカット登録時に Steam 側へ焼き込まれる。デバイス上の `<gameid>-argv.json` を書き換えても無駄で、**再デプロイが必要** |
| curl `-d 'expr=a+b'` の `+` が空白になる | form-urlencoded の仕様。`+` は **`%2B`** と書く |
| ビルドが `_mm256_*` 未定義で失敗 | sniper SDK 既定の gcc-10 が古い。deckbuild は gcc-14 を既定にしている |

### `-replweb` を使うときの注意 ( 2026-09-06〜 )

`-replwebidle` が**既定で有効 ( 5 秒 )** になりました。**ブラウザで
`http://127.0.0.1:18899/` を開いて閉じると、Deck 上のアプリも終了します**
( 一度でも接続が来てから武装するので、curl だけの確認では終了しません )。

- 「ブラウザを閉じたら終わる」で都合がよければそのまま
- 検証中に落としたくなければ、`deckproject.toml` の起動コマンドへ
  `-replwebidle=no` を足す

---

## 4. 確認済みの実績

2026-09-06 に本手順を通しで実測 ( SteamOS 3.8.16 / Deck 実機 )。

- sniper コンテナで Linux ビルド成功、GLIBC ≤ 2.30 / GLIBCXX 依存なし
- 183 ファイルを stage → 転送 → 起動、デモランチャの表示をスクリーンショットで確認
- トンネル経由で `/state` `/watch` `/pad/exec` `/` ( ブラウザ UI ) すべて応答
- 後片付けまで完了

## 関連

- [REPL ( 対話型 TJS シェル )](repl.md) — `-replweb` の HTTP API とブラウザ UI
- [LinuxBuild.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/LinuxBuild.md)
  — sniper ビルド環境の中身と合格基準 ( engine 側 SSOT )
- umbrella ルートの `deckproject.toml` — ビルド / 資材 / 起動の定義
