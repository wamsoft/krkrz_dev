# Linux 版の配布パッケージ ( krkrz_linux )

吉里吉里Z 本体と作品のデータをまとめて、Linux 向けの配布物を作る方法です。
道具は外枠リポジトリ [krkrz_linux](https://github.com/wamsoft/krkrz_linux)。
krkrz_android / krkrz_ios / krkrz_web と同じく、エンジンは `KRKRZ_BASE` 経由で
krkrz_dev を参照し、Linux 固有のビルドとパッケージングだけを受け持ちます。

## Linux の配布形式と方針

Linux には Android の APK のような「これ一つ」というアプリ形式がなく、配布先ごとに
形式が分かれます。ただ、どれも「そのまま動くフォルダ」に freedesktop の
メタデータ ( `.desktop` / アイコン / AppStream ) を添えて包み直したものです。

| 形式 | 主な配布先 | krkrz_linux |
|---|---|---|
| フォルダ / tar.gz | Steam のデポ、itch.io、GOG、Humble | ✅ 出力する |
| AppImage | 自前サイト、itch.io | 未実装 ( 同じフォルダから作れる。`.desktop` とアイコンは生成済み ) |
| Flatpak | Flathub | 未定 ( AppStream メタデータとマニフェストが要る ) |

ゲームで重要な Steam が受け取るのはフォルダそのものなので、**フォルダを正式な
成果物とし、他の形式はその包み直し**という方針です。

## ビルド環境

Valve の **Steam Linux Runtime 3.0 "sniper" SDK** ( Debian 11 / glibc 2.31 ) の
コンテナでビルドします。SteamOS ネイティブ、Steam Linux Runtime、glibc 2.31 以降の
一般的なディストリビューションで動くバイナリになります。イメージは
[steamdev](https://github.com/wamsoft/steamdev) の `deckbuild/deckbuild.sh image`
で作る `deckbuild-sniper` を使います。合格基準 ( 要求 glibc ≤ 2.31 /
GLIBCXX 依存なし ) は engine 側の `src/core/doc/LinuxBuild.md` が SSOT です。

## 使い方

```bash
export KRKRZ_BASE=~/kirikiri                 # krkrz_dev のある親フォルダ
cd ~/kirikiri/krkrz_linux
make all                                     # サンプル案件 (コアデモ)
PROJECT_DIR=/path/to/mygame make all         # 自分の案件
```

出力は `${PROJECT_DIR}/build/linux/` の下です。

- `package/<exeName>/` … そのまま動くフォルダ
- `dist/<exeName>-<version>-linux-x86_64.tar.gz` … それを固めたもの

案件の定義は `${PROJECT_DIR}/linux-config.json` です。`cmake` ( プラグイン構成 ) と
`assetPack` ( 資材の取り込み、先勝ち ) は krkrz_android の `app-config.json` と同じ
書式なので、案件フォルダの資材定義を共有できます。項目の一覧は krkrz_linux の
README を参照してください。

## パッケージの中身

```
mygame/
  mygame                 実行ファイル ( KRKRZ_EXE_NAME )
  libSDL3.so.0 ( .x.y )  同梱 SDL3
  plugin/*.so            プラグイン
  mygame.cf              orgname / appname ほか ( 生成 )
  <id>.desktop, <id>.svg freedesktop のメタデータ ( 生成 )
  license.txt, licenses/
  data/ または data.xp3  引数なしで起動すると自動検出される
```

### 同梱 .so の解決 ( RPATH )

実行ファイルには `$ORIGIN`、`krkrz_plugin()` で作ったプラグインには
`$ORIGIN:$ORIGIN/..` を **DT_RPATH** で埋め込んでいます。同梱の SDL3 や、
プラグインが依存する .so ( `plugin/` か実行ファイルのフォルダに置く ) は、
`LD_LIBRARY_PATH` も起動スクリプトもなしで読まれます。

Steam から起動すると `LD_LIBRARY_PATH` の先頭に Steam ランタイムと `/usr/lib` が
入るため、RUNPATH ( 新しいリンカの既定 ) や `LD_LIBRARY_PATH=.` では SteamOS 側の
同名 .so が先に読まれてしまいます。DT_RPATH はそれより先に探されるので、
同梱版が確実に使われます。独自の CMake で RPATH を付けるプラグインは
`--disable-new-dtags` を使ってください ( RUNPATH を持つと実行ファイル側の
DT_RPATH も効かなくなります )。

## セーブデータの場所 ( 2026-10〜 )

!!! warning "重要 (2026-10 の変更)"
    Linux 版の既定のデータ保存場所 ( `-datapath` 未指定時 ) は、実行ファイルの隣の
    `savedata` から **`~/.local/share/<orgname>/<appname>/`** ( `$XDG_DATA_HOME`
    があればその下 ) に変わりました。詳細は
    [コマンドラインオプション の -datapath](../../guide/CommandLine.md) を参照してください。

- **`orgname` / `appname` は案件の設定から取って `<exeName>.cf` に書き込む**のが
  決まりです。krkrz_linux は `linux-config.json` の `orgName` / `appName` から
  自動で書き込みます。これで作品ごとに別のフォルダになります
- 実行ファイルの隣に書かないので、読み取り専用の場所 ( AppImage、Flatpak、
  `/opt` など ) に置いても動きます
- `System.dataPath` はローカルパス ( `file://./home/…` ) なので、
  `Storages.getLocalName()` も使えます
- 実際の保存場所は起動ログの `datapath (Linux default, …)` の行で確認できます

### Steam Cloud

Steamworks の Auto-Cloud を使う場合は、Linux のルートを `LinuxXdgDataHome`
( = `~/.local/share` )、サブディレクトリを `<orgname>/<appname>` にします。
Windows 版とは保存場所が違うので、両方を配布するときは「ルートの上書き」で
OS ごとに指定してください ( ルート種別の名前は Steamworks の設定画面で確認 )。

## Steam Deck で確かめる

krkrz_linux の出力フォルダは steamdev でそのまま Deck に送れます。

```bash
steamdev -d <deck> deploy --gameid mygame_linux \
    --dir build/linux/package/mygame --command "./mygame" --start
```

手順全体とハマりどころは [Steam Deck 実機確認](steamdeck.md) を参照してください。

## 今後

- AppImage 出力 ( `AppRun` を足して `appimagetool` で固める )
- xp3 アーカイブの作成 ( 今は `archive/*.xp3` を取り込むだけ )
- Flatpak は需要が出てから
- macOS ( .app ) / Windows / Xbox も、`*-config.json` の `cmake` / `assetPack`
  書式を共通にした外枠で揃える方向で調査中

## 関連

- [krkrz_linux](https://github.com/wamsoft/krkrz_linux) — README に設定項目の一覧
- [Steam Deck 実機確認 ( リリース前チェック )](steamdeck.md)
- [コマンドラインオプション](../../guide/CommandLine.md) — `-datapath` / `-orgname` / `-appname` と `.cf` の書式
