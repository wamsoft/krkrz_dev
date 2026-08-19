# 吉里吉里Z 統合リポジトリ 開発用

本体のソースコード、プラグインのソースコード、各種TJS2スクリプト、
ドキュメント等開発関係のもの全てが入ったリポジトリ。
各種ファイルはサブモジュールで参照されています。

## 他プラットフォーム向けの外枠リポジトリ (ブラウザ / Android)

Win32 や各種デスクトップ向けのビルドは本リポジトリ (umbrella) で完結するが、
**ブラウザ (wasm) と Android** はそれぞれ別の「外枠」リポジトリでビルドする。
どちらも本リポジトリをエンジンソースとして参照し (環境変数 `KRKRZ_BASE` に
本リポジトリの親フォルダを指定)、エンジン本体・プラグインには手を入れず、
各プラットフォーム固有のビルド定義・パッケージングだけを持つ。本リポジトリと
同じ場所に clone しておく (`KRKRZ_BASE/krkrz_dev` と `KRKRZ_BASE/krkrz_web` /
`KRKRZ_BASE/krkrz_android` が並ぶ構成)。

- **krkrz_web** — ブラウザ (Emscripten / wasm32, SDL3 ベース) 版。
  https://github.com/wamsoft/krkrz_web
  共有バイナリ (案件非依存) を一度ビルドし、案件のデータ・リソース・起動設定は
  「配信サイドカー」として差し替える方式。案件データはバラファイルを `web://` で
  オンデマンド fetch (+ OPFS キャッシュ) する。案件構成は `web-config.json`
  (`assetPack.sources` で複数ソースをマージ) で定義し、
  `make PROJECT_DIR=<案件> run` でステージング + ローカル起動する。
  SharedArrayBuffer/pthread + JSPI 対応ブラウザ (Chrome / Edge) が必要。

- **krkrz_android** — Android 版 (Gradle + NDK/CMake, SDL3 ベース)。
  https://github.com/wamsoft/krkrz_android
  案件構成は `app-config.json` (`assetPack.sources` で資材をマージ、`padPacks`
  で Play Asset Delivery の分割配信) で定義し、`PROJECT_DIR` を指定してビルドする。

各リポジトリ固有の詳細はそれぞれの README を参照。

## ビルド手順

Win32 版を作成する場合は、Visual Studio のコマンドラインの x86 版を
起動してそのコンソールから作業するようにしてください。x86 用の設定に
なってないと vcpkg が誤動作します

cygwin や msys2 などを導入して make が利用可能な場合は、定義済み Makefile が利用できます

### 前準備

vcpkg を導入して外部ライブラリ参照を準備します

https://github.com/microsoft/vcpkg
https://learn.microsoft.com/vcpkg/get_started/get-started

環境変数 VCPKG_ROOT に vcpkg 導入先フォルダを設定してください

例:
```
export VCPKG_ROOT=d:/vcpkg
```

### ソース取得

```
git clone --recursive https://github.com/wamsoft/krkrz_dev.git
```

サブモジュールもすべて再帰的に取得してください

### cmake によるビルド

cmake による構築になります。

環境別定義は、CMakePresets.json にあらかじめ定義されているので、
それを利用してビルドできます。

※build/プリセット名 がビルドフォルダ設定されています

```
# ビルドの準備
cmake --preset=x64-windows

# ビルド
cmake --build build/x64-windows

# ビルドタイプ指定してビルド
cmake --build build/x64-windows --config Debug

# インストール処理
cmake --install build/x64-windows --config Release --prefix bin
```

| 種類         | 名前         | 説明                                      |
|--------------|--------------|-------------------------------------------|
| 環境変数     | PRESET       | cmake のプリセット名を指定                |
|              | BUILD_TYPE   | ビルド対象の config 指定<br>Debug/RelWithDebInfo/Release |
| ビルドルール | prebuild     | cmake の構築呼び出し                      |
|              | build        | cmake のビルド呼び出し                    |
|              | install      | cmake のインストール呼び出し              |

win32版（SJIS対応）で作成する

```
export PRESET=x86-windows
export CMAKEOPT="-DUSESJIS=ON"
make prebuild
make
make install
```

win64版で作成する

```
export PRESET=x64-windows
make prebuild
make
make install
```

### プラグイン作成

TVP_PLUGIN_FOLDERS から、TVP_PLUGINS で定義された名称の
プラグインがあわせてビルドされます。それぞれリストです

TVP_PLUGINS_STATIC が定義されている場合は、それに含まれる
プラグインは実行ファイル中に静的にビルトインされます

CMake のリストとして定義するので ;　区切りで必要なものを列挙します

```
CMAKEOPT='-DUSESJIS=ON -DTVP_PLUGINS_STATIC="json;csvParser"' make prebuild
make
make install
```

### vcpkg マニフェストの統合

このリポジトリ直下に `vcpkg.json` は **置きません**。代わりに、トップの
`CMakeLists.txt` が `project()` 呼び出し前に複数の `vcpkg.json` を
マージして `${CMAKE_BINARY_DIR}/vcpkg.json` を生成し、`VCPKG_MANIFEST_DIR`
をビルドフォルダに向けることで vcpkg manifest install にそれを読ませます。
仕組み (`krkrz_merge_vcpkg_manifest`) は `src/core/cmake/MergeVcpkgManifest.cmake`
にあり、umbrella と `src/core` 単独ビルドの両方が同じものを共有します。

マージ対象は次の通り:

- **BASE**: `src/core/vcpkg.json` — エンジン本体の共通依存と
  `builtin-baseline` / `vcpkg-configuration` を提供
- **SUBDIRS**:
  - `src/core/external/movie-player/vcpkg.json` (動画再生)
  - `TVP_PLUGINS` × `TVP_PLUGIN_FOLDERS` で解決した各プラグインフォルダ
    直下の `vcpkg.json`

依存は `name` 単位で重複排除されます (BASE 側を優先)。
`builtin-baseline` / `overrides` / `vcpkg-configuration` は BASE のみ採用。

**プラグイン側の vcpkg.json**

各プラグインは独自に外部ライブラリを必要とすることがあるため、
`<plugin_folder>/<plugin_name>/vcpkg.json` を置いておけば、その依存が
`TVP_PLUGINS` でビルド対象に入ったときだけ自動でマージされます。
本体や他プラグインの設定を触る必要はなく、また有効化されていない
プラグインの依存が混入することもありません。

例: `src/plugins/minizip/vcpkg.json` (minizip プラグインを有効にしたときだけ
`minizip-ng` が引かれる)

```json
{
  "name": "minizip",
  "version": "0.0.1",
  "dependencies": [
    "minizip-ng"
  ]
}
```

サブの `vcpkg.json` を変更すると `cmake --preset` の再走で再マージが
走ります (`CMAKE_CONFIGURE_DEPENDS` 登録済み)。

特定の依存だけ取り込みたくない場合は umbrella 側 `CMakeLists.txt` の
`krkrz_merge_vcpkg_manifest(... EXCLUDE ...)` に追記します。指定形式:

- `"<dep>"` — どこから来ても除外 (グローバル)
- `"<basename>:<dep>"` — そのフォルダ末尾名のサブからのみ除外

(現在は `movie-player:glew` / `movie-player:glfw3` をサンプル用として除外)

## Claude Code 用スキル

このリポジトリには吉里吉里Z 開発向けの [Claude Code](https://claude.com/claude-code)
スキルが同梱されています。Claude に「TJS2 の書き方」「Layer の API」「REPL でどう
検証するか」を毎回説明しなくても済むようにするためのリファレンス群です。

| スキル | 内容 |
|---|---|
| `krkrz` | 本体クラス API (Layer / Window / Bitmap / Storages / DrawDevice / OpenGL 描画 / サウンド / 主要プラグイン) |
| `tjs2` | TJS2 言語仕様と組み込みクラス。JS との差異にフォーカス |
| `elements` | Elements ベースのダイアログ / 画面 UI の作り方 |
| `krkrz-repl` | `-repl` / `-replfile` によるエージェント駆動、Agent API、画面キャプチャ |
| `krkrz-webui` | `-replweb` HTTP+SSE サーバにブラウザ UI を載せる方法論 |

正本は `.claude/skills/` にあります。**このリポジトリで作業している間は追加の
セットアップなしでそのまま有効**です (Claude Code がプロジェクトスキルとして
自動的に読み込みます)。

### 他の場所でも使う (インストール)

`krkrz` / `tjs2` の SKILL.md は詳細リファレンスを `doc/reference/`、`doc/tjs2/`
といった**このリポジトリ相対のパス**で参照しています。そのため他のリポジトリへ
そのままコピーしても参照が解決しません。

`tools/skills/install.sh` が、参照ドキュメントをスキル内 `references/` へ同梱し、
SKILL.md 内のパスを書き換えて、**どこに置いても壊れない自己完結形**に組み立てます。
実行には bash が必要です (msys2 / Git Bash)。

**自分用にインストールする** — 以降どのリポジトリで作業していても有効になります。
案件のリポジトリで TJS2 を書くときにも使いたい場合はこちら。

```
bash tools/skills/install.sh --user
```

`~/.claude/skills/` へ配置されます。既存の同名スキルがある場合は確認を求めます
(`--force` で確認なし)。**このスクリプトが触るのは上記 5 スキルだけ**で、
そこにある他のスキルには手を出しません。

**案件リポジトリにインストールする** — その案件で作業する人全員に配りたい場合。

```
bash tools/skills/install.sh --project /path/to/project
```

`<project>/.claude/skills/` へ配置されます。案件リポジトリに commit すれば、
clone した人はセットアップなしで使えます。案件側の `.gitignore` が `.claude` を
無視していることが多いので、その場合は本リポジトリと同様に

```
.claude/*
!.claude/skills/
```

としてください。

**配布用に書き出す** — krkrz_dev を持っていない人へ配る場合。

```
bash tools/skills/install.sh --dist /path/to/dist-repo
```

プラグイン構造 (`.claude-plugin/marketplace.json` + `plugins/krkrz-skills/`) で
出力します。これを git リポジトリとして push すると、受け取る側は次で導入できます。

```
/plugin marketplace add <owner>/<repo>
/plugin install krkrz-skills@krkrz-skills
```

`--dry-run` を付けると、何をどこへ書くかだけ表示して終了します。

### 更新

スキルやリファレンスを更新したら、インストール済みの環境では
`install.sh` を同じオプションで再実行してください (`--force` 推奨)。
同梱されるリファレンスは実行時点のリポジトリの内容です。

### スキルを編集するとき

- 編集するのは `.claude/skills/` の**正本**です。インストール先を直接直しても
  次の `install.sh` で上書きされます。
- リファレンスはリポジトリ相対パス (`doc/reference/<Name>.md` 等) で参照します。
  同梱時のパス書き換えは `install.sh` の `BUNDLE` テーブルが担当するので、
  新しい参照先ディレクトリを増やしたときはそこに 1 行足してください。
- **案件固有の情報 (取引先名・案件リポジトリのパス・案件の設定値) は書かない**こと。
  スキルは案件をまたいで配布されます。
