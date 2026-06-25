# 吉里吉里Z 統合リポジトリ 開発用

本体のソースコード、プラグインのソースコード、各種TJS2スクリプト、
ドキュメント等開発関係のもの全てが入ったリポジトリ。
各種ファイルはサブモジュールで参照されています。

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