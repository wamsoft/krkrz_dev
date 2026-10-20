# krkrz_dev — 吉里吉里Z 統合開発リポジトリ

日本語 | [English](README_en.md)

吉里吉里Z (Kirikiri Z) の開発用の統合リポジトリです。エンジン本体・プラグイン・TJS2 スクリプト
ライブラリ・標準ツールを git の submodule として束ね、1 つの CMake ビルドにまとめています。
Windows / Linux / macOS のデスクトップ版はこのリポジトリでビルドします。

- **ドキュメント**: [公開サイト](https://wamsoft.github.io/krkrz_dev/) (日本語 / English)。
  ソースはこのリポジトリの `doc/` です
- **ブランチ**: `develop` が開発の主軸、`master` がリリース用です (エンジン `src/core` の参照先も
  ブランチで違います。master は公開エンジン [krkrz](https://github.com/wamsoft/krkrz))
- ブラウザ / Android / iOS / Linux の配布パッケージ / Microsoft GDK 向けは、このリポジトリを
  エンジンのソースとして参照する別の「外枠」リポジトリでビルドします ([下記](#外枠リポジトリ))

## リポジトリの構成

| フォルダ | 中身 |
|---|---|
| `src/core` | エンジン本体 (submodule)。ビルドの詳細・内部構造は [src/core/README.md](src/core/README.md) |
| `src/plugins/*` | プラグイン (それぞれ submodule)。一覧は公開サイトの [プラグイン](https://wamsoft.github.io/krkrz_dev/guide/Plugins/) |
| `src/tools/krkrz_tools` | 標準ツール (submodule、[krkrz_tools](https://github.com/wamsoft/krkrz_tools)) |
| `script/*` | TJS2 スクリプトライブラリ (KAG3 / Krkr2Compat / サンプル / テスト。それぞれ submodule) |
| `data/` | プラグイン / 機能のサンプル集と、統合デモギャラリー (直下の `startup.tjs`)。エンジンのコア機能のデモは `src/core/data/` |
| `doc/` | 公開サイトのソース (mkdocs)。生成の仕組みは [tools/docgen/README.md](tools/docgen/README.md) |
| `tools/` | ドキュメント生成・Claude Code 用スキルなどの補助ツール |

各 submodule はそれぞれ独立したリポジトリです。中身を直すときのコミットは、その submodule の
リポジトリへ行います。未対応の課題の一覧は [TODO.md](TODO.md) にあります。

## 外枠リポジトリ

| リポジトリ | 対象 | 設定ファイル |
|---|---|---|
| [krkrz_web](https://github.com/wamsoft/krkrz_web) | ブラウザ (Emscripten / wasm32) | `web-config.json` |
| [krkrz_android](https://github.com/wamsoft/krkrz_android) | Android (Gradle + NDK) | `app-config.json` |
| [krkrz_ios](https://github.com/wamsoft/krkrz_ios) | iOS / iPadOS (CMake の Xcode ジェネレータ) | `ios-config.json` |
| [krkrz_linux](https://github.com/wamsoft/krkrz_linux) | Linux の配布パッケージ (Steam Linux Runtime の SDK コンテナでビルド) | `linux-config.json` |
| [krkrz_gdk](https://github.com/wamsoft/krkrz_gdk) | Microsoft GDK (PC / Xbox) | `gdk-config.json` |

- どれもこのリポジトリと同じフォルダに clone し、環境変数 `KRKRZ_BASE` にその親フォルダを指定します
  (`KRKRZ_BASE/krkrz_dev` と `KRKRZ_BASE/krkrz_android` などが並ぶ形)
- エンジン本体とプラグインには手を入れず、機種ごとのビルド定義とパッケージングだけを持ちます
- タイトルの設定と資材は別のフォルダ (プロジェクトフォルダ) に置けます。設定のうち `cmake`
  (プラグイン構成) と `assetPack` (資材の取り込み) は共通の書式で、1 つのプロジェクトフォルダに各機種の
  設定を並べて同じデータを使い回せます。書式は公開サイトの
  [外枠リポジトリの共通設定](https://wamsoft.github.io/krkrz_dev/topics/core/platform_config/) を参照してください

各機種の詳細はそれぞれの README にあります。

## 必要なもの

- **Windows**: Visual Studio 2022 (v17.14) と、それに同梱の CMake / Ninja。これ以外の版・ツールチェーンは
  確かめていません
- **Linux**: 確認の基準は [steamdev](https://github.com/wamsoft/steamdev) の `deckbuild/` で作る Docker の
  ビルド環境 (Steam Linux Runtime 3.0 "sniper" SDK、Debian 11 / glibc 2.31) です ([下記](#linux-でのビルド))
- **macOS**: プリセット `x64-osx` / `arm64-osx` でビルドします (手順の文書は整備中です)
- [vcpkg](https://github.com/microsoft/vcpkg) — 環境変数 `VCPKG_ROOT` に導入先を指定します

  ```
  export VCPKG_ROOT=d:/vcpkg
  ```

- make を使う場合は、cygwin や msys2 などの make が使える環境 (下記の Makefile を使えます)

## ソースの取得

```
git clone --recursive https://github.com/wamsoft/krkrz_dev.git
```

submodule もすべて再帰的に取得してください。あとから取得する場合は
`git submodule update --init --recursive` です。

## ビルド

CMake のプリセット (`src/core/CMakePresets.json`) を使います。ビルドフォルダは `build/<プリセット名>` です。
プリセットの一覧と主なビルドオプションは [src/core/README.md](src/core/README.md) にあります。

```
cmake --preset=x64-windows                                      # ビルドの準備
cmake --build build/x64-windows --config Release                # ビルド
cmake --install build/x64-windows --config Release --prefix bin # インストール
```

Makefile からも同じことができます。

```
make prebuild     # cmake --preset
make              # cmake --build
make install      # bin/<プリセット>/<ビルドタイプ> へインストール
make run          # (Windows) ビルドしてデモを起動
```

| 種類 | 名前 | 説明 |
|---|---|---|
| 環境変数 | `PRESET` | CMake のプリセット名 (未指定なら OS から自動で選ぶ) |
| | `BUILD_TYPE` | `Debug` / `RelWithDebInfo` / `Release` (既定 `Release`) |
| | `CMAKEOPT` | CMake に渡す追加のオプション |

```
# 32bit (SJIS 対応) 版
export PRESET=x86-windows
export CMAKEOPT="-DKRKRZ_USE_SJIS=ON"
make prebuild && make && make install
```

32bit 版を作るときは、Visual Studio の x86 用コマンドプロンプトから作業してください。x86 用の設定に
なっていないと vcpkg が誤動作します。

### OpenGL 用 ANGLE DLL の配置 (Windows)

エンジンの OpenGL (GLES) の機能を Windows で使うには、ANGLE の `libEGL.dll` / `libGLESv2.dll` が要ります
(WINVER 版では必須。SDL3 版では OpenGL ドライバの ES プロファイルが使えない環境のための予備)。
リポジトリには含まれないので、リポジトリ直下の `plugin/` (32bit) / `plugin64/` (64bit) に置いてください。
`make run` がビルド出力へコピーします。入手先は [mmozeiko/build-angle](https://github.com/mmozeiko/build-angle)
の Releases が手軽です。注意点は [src/core/README.md](src/core/README.md) の「OpenGL ES の実行環境」にあります。

### Linux でのビルド

steamdev の `deckbuild/` で作る Docker のビルド環境 (Valve の Steam Linux Runtime 3.0 "sniper" SDK) で
ビルドします。ここでビルドしたものは SteamOS・Steam Linux Runtime のコンテナ・glibc 2.31 以降の
一般的なディストリビューションで動きます。

```bash
# WSL2 の docker で。最初の 1 回だけイメージを作る
<steamdev>/deckbuild/deckbuild.sh image

# ビルド (configure + build + install → bin/x64-linux/Release/)
<steamdev>/deckbuild/deckbuild.sh -s /mnt/d/work/kirikiri/krkrz_dev all
```

リポジトリ直下の `deckproject.toml` は steamdev の CLI 用のプロジェクト定義で、ビルドから Steam Deck への
転送・起動までを一度に行えます (`steamdev -d <deck> project -p . ship linux`)。互換性の考え方とバイナリの
合格基準 (要求する glibc のシンボルが 2.31 以下など) は [src/core/doc/LinuxBuild.md](src/core/doc/LinuxBuild.md)
にあります。

## 標準ツール (krkrz_tools)

`src/tools/krkrz_tools` のツール (破損チェック・署名・xp3・音声 / 画像のコンバータ・ループチューナ・
リリーサ) も一緒にビルドし、`make install` で `<インストール先>/tools/` に置きます。

- ツールは exe 1 本で配れるよう静的リンク (`x64-windows-static` など) で作るので、本体とは別のビルドです
  (`build/<preset>/krkrz_tools`、常に Release。`cmake/KrkrzTools.cmake`)
- 最初は、ツール用の vcpkg のライブラリ (静的版) のビルドに時間がかかります
- デスクトップ (Windows / Linux / macOS) では既定で有効です。`CMAKEOPT='-DKRKRZ_BUILD_TOOLS=OFF'` で外せます

各ツールの使い方は [krkrz_tools の README](src/tools/krkrz_tools/README.md) にあります。

## プラグインの選び方

ビルドするプラグインはトップの `CMakeLists.txt` の `TVP_PLUGINS` (フォルダ名のリスト) で決まります。
`TVP_PLUGINS_STATIC` に書いたものは実行ファイルに静的リンクされます。CMake のリストなので `;` で区切ります。

```
CMAKEOPT='-DKRKRZ_USE_SJIS=ON -DTVP_PLUGINS_STATIC="json;csvParser"' make prebuild
make
make install
```

プラグインが外部のライブラリを使う場合は、そのプラグインのフォルダに `vcpkg.json` を置きます。
そのプラグインがビルドの対象に入ったときだけ、依存が自動でマージされます (リポジトリ直下に
`vcpkg.json` は置かず、CMake が本体と各プラグインの `vcpkg.json` をまとめてビルドフォルダに作ります)。
マージの規則と除外の指定は [src/core/cmake/MergeVcpkgManifest.cmake](src/core/cmake/MergeVcpkgManifest.cmake)
の先頭にあります。

```json
{
  "name": "minizip",
  "version": "0.0.1",
  "dependencies": [ "minizip-ng" ]
}
```

## Claude Code 用スキル

吉里吉里Z の開発向けの [Claude Code](https://claude.com/claude-code) 用スキルを同梱しています。Claude に
「TJS2 の書き方」「Layer の API」「REPL での確かめ方」を毎回説明しなくて済むようにするためのものです。

| スキル | 内容 |
|---|---|
| `krkrz` | 本体のクラスの API (Layer / Window / Bitmap / Storages / DrawDevice / OpenGL の描画 / サウンド / 主なプラグイン) |
| `tjs2` | TJS2 の言語仕様と組み込みクラス。JavaScript との違いを中心に |
| `elements` | Elements を使ったダイアログ / 画面 UI の作り方 |
| `krkrz-repl` | `-repl` / `-replfile` でのエージェントからの操作、Agent API、画面のキャプチャ |
| `krkrz-webui` | `-replweb` の HTTP + SSE サーバにブラウザの UI を載せる方法 |

正本は `.claude/skills/` にあり、**このリポジトリで作業している間はそのまま有効**です。他のリポジトリで
使う場合のインストール (`bash tools/skills/install.sh --user` など) と更新・編集の注意は
[tools/skills/README.md](tools/skills/README.md) にあります。

## ライセンス

このリポジトリは構成要素を submodule で束ねたもので、ライセンスはそれぞれの構成要素で決まっています。
エンジン本体は [src/core/LICENSE](src/core/LICENSE)、プラグインは各フォルダの LICENSE / README を
参照してください。まとめは [LICENSE.md](LICENSE.md) にあります。配布物に載る第三者のコンポーネントの
一覧は公開サイトの [同梱ライセンス一覧](https://wamsoft.github.io/krkrz_dev/guide/BundledLicenses/) です。
