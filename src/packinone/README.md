# packinone 再構築 (調査と実装範囲)

status: **土台まで実装 (2026-09-27)**。10 個取り込み済み / 残りは下記
置き場: `src/packinone` (`src/plugins` とは別枠。ここが統合プラグインの唯一の置き場)

## これは何か

`PackinOne.dll` は**旧プラグイン 14 個を 1 つの DLL に詰め合わせたもの**で、
`Plugins.link` を自前で差し替えて「同梱済みのプラグイン名は無視する」ハックで動いている。
案件はこれ 1 つを置けば済むので配備が楽、という運用上の資産。

旧ソースは `krkrtemplate/plugins/packinone` (Shift_JIS)。**旧版メンテ用なので触らない。**
ここで作るのは**現行ツリーの個別プラグインを取り込んで作り直した別物**。

## なぜ作り直すのか

旧 `PackinOne.dll` は **generic (SDL / CS) ビルドで即死する**。
本体が Win32 専用 API を「戻り値の無い空関数」としてプラグインへ渡していたのが直接の原因で、
そちらは本体側で直した (nullptr を返すスタブへ。`doc/GenericPluginLoading.md`)。

ただし**それは落ちなくなるだけ**で、Win32 専用 API に依存した機能は generic では動かない。
旧ソースは現行の tp_stub (名前空間化済み) でもそのままではビルドが通らない (実測 177 エラー)。

## 方針

| | |
|---|---|
| `packinone` | **全機種で動くもの**だけを詰める |
| `packinoneWin32` | **WINVER 専用**の機能を分ける (Win32 の UI / ウィンドウ / COM に触るもの) |

- 中身は**現行ツリーの個別プラグインのソースをそのまま取り込む** (`src/plugins/*`)。
  同じ実装を二重管理しない
- ファイルストリームは **`TVPCreateIStream` (COM) を使わない**。
  `TVPCreateStream` → `tTJSBinaryStream` に統一する。旧実装の IStream 利用は
  「ストレージのファイルを開く」以上のことをしていないので機械的に置き換えられる

## 構成要素の棚卸し

| 旧 PackinOne の中身 | 現行ツリーのソース | Win32 依存 | 新 packinone での扱い |
|---|---|---|---|
| `csvParser` | `src/plugins/csvParser` | 無し | ✅ 取り込み済み |
| `saveStruct` | `src/plugins/saveStruct` | 無し | ✅ 取り込み済み |
| `scriptsEx` | `src/plugins/scriptsEx` | 無し | ✅ 取り込み済み |
| `shrinkCopy` | `src/plugins/shrinkCopy` | 無し | ✅ 取り込み済み |
| `layerExBTOA` | `src/plugins/layerExBTOA` | 無し | ✅ 取り込み済み |
| `layerExImage` | `src/plugins/layerExImage` | 無し | ✅ 取り込み済み |
| `layerExRaster` | `src/plugins/layerExRaster` | 無し | ✅ 取り込み済み |
| `tjsDataPack` | `krkrtemplate/plugins_utf8/tjsDataPack` | 無し | ✅ 取り込み済み |
| `fstat` | `src/plugins/fstat` | `TVPCreateIStream` (ファイルを開くだけ) | ⚠ ストリームを `TVPCreateStream` へ置換 |
| `addFont` | `src/plugins/addFont` | `TVPCreateIStream` (フォントを読むだけ) | ⚠ 同上。**本体に `System.addFont` があるので要否から再検討** |
| `proxyfs` | `krkrtemplate/plugins_utf8/proxyfs` | IStream でストリームを**提供**している | ⚠ 作り直しが要る (本体のストレージメディア API へ) |
| `tlgSliceLoader` | `krkrtemplate/plugins_utf8/tlgSliceLoader` | 3 ファイル | ⚠ 要調査 |
| `systemEx` | `src/plugins/systemEx` | `TVPGetApplicationWindowHandle` (メッセージボックスの親) / ntdll の `RtlGetVersion` / `SetDefaultDllDirectories` | ⚠ **分割**。移植可能な部分だけ packinone へ、残りは packinoneWin32 |
| `process` | `src/plugins/process` | メッセージ専用ウィンドウを `CreateWindowExW` で作る | ❌ **packinoneWin32 へ** |
| FileSelector / selfile | (旧 packinone のみ) | ファイル選択ダイアログ | ❌ **不要**。本体に `Storages.selectFile` / `selectDirectory` がある (WINVER / generic 両方) |
| DpiIconManager | (旧 packinone のみ) | ウィンドウアイコン / DPI | ❌ **packinoneWin32 へ** (または廃止。[windowEx 廃止で落とした機能] と同じ扱い) |
| pemachinetype | (旧 packinone のみ) → `src/plugins/pemachinetype` | PE ヘッダを読んで x86/x64 判定 | ✅ 取り込み済み (ストリームを置換して起こし直し) |
| TriBinPairString | (旧 packinone のみ) → `src/plugins/TriBinPairString` | 文字列ユーティリティ | ✅ 取り込み済み (計算のみ。UTF-8 化して起こし直し) |

## 本体が既に持っているので実装しなくてよいもの

| 機能 | 本体 API | 備考 |
|---|---|---|
| ファイル / フォルダ選択ダイアログ | `Storages.selectFile` / `Storages.selectDirectory` | **WINVER / generic の両方にある** (`*/base/StorageImpl.cpp`) |
| フォント追加 | `System.addFont` / `Font.addFont` | `common/visual/LayerIntf.cpp` / `generic/base/SystemImpl.cpp` |
| プログラム起動 | `TVPExecuteProgram` (generic にもある) / `System.shellExecute` (WINVER) | `process` の「起動するだけ」の用途はこれで足りる |
| MD5 | `TVP_md5_init` / `append` / `finish` をプラグインへ export 済み | ⚠ `__WINVER__` ガードが**無い**ので全機種で使える |

## 実装範囲 (絞り込み結果)

1. ✅ **そのまま取り込むだけ**: csvParser / saveStruct / scriptsEx / shrinkCopy /
   layerExBTOA / layerExImage / layerExRaster / tjsDataPack (8 個) — **完了**
2. ✅ **ストリームの置き換えだけ**: pemachinetype / TriBinPairString — **完了**
   (どちらも旧 PackinOne にしか無かったので、`src/plugins/` に個別プラグインとして
    起こし直してから取り込んだ。 単体 DLL は作っていない = `TVP_PLUGINS` に入れていない)
3. **要否から再検討**: addFont (本体に同等機能あり)
4. **作り直し**: proxyfs (ストリームを提供する側なので設計から)、tlgSliceLoader (要調査)
5. **packinoneWin32 へ**: process / DpiIconManager / systemEx の Win32 部分
6. **作らない**: FileSelector / selfile (本体のダイアログを使う)

## 実装した仕組み (動作確認済み)

### 取り込み方: 静的プラグイン機構に寄せた

各プラグインのソースを **per-source の define 付きでそのままコンパイル**する。

```cmake
packinone_absorb(scriptsEx NCBIND SOURCES Main.cpp)
# → TVP_STATIC_PLUGIN / TVP_PLUGIN_NAME=scriptsEx /
#    V2Link=V2Link_scriptsEx / V2Unlink=... / DllEntryPoint=... を付けてコンパイル

packinone_absorb(tjsDataPack SIMPLEBIND      # simplebinder を使うものは SIMPLEBIND
    DIR      <ツリー外のパス>                 # 既定は ../plugins/<名前>
    INCLUDES lz4 xxHash                      # DIR からの相対 (絶対も可)
    SOURCES  Main.cpp …)
```

- `TVP_STATIC_PLUGIN` を付けると **バインダの自動登録リストがプラグインごとに別名**になり
  (`ncbind.hpp` / `simplebinder.hpp` が `TVP_PLUGIN_NAME` で改名する)、同じ DLL に同居できる
- 同時に `krkrz_plugin_<名前>()` という登録エントリが生える
- ⚠ **バインダ本体 (`ncbind.cpp` / simplebinder の `v2link.cpp`) に V2Link と登録エントリが
  入っている**ので、**プラグインごとに別コンパイル**する必要がある
  (生成した 1 行のラッパ `#include "…/<バインダ>.cpp"` を per-source define 付きで積む)
- ⚠ `V2Link` / `V2Unlink` / `DllEntryPoint` は各プラグインが定義するので、
  define で改名しないと重複定義になる
- ⚠ 取り込むプラグイン自身のディレクトリを **include 順の先頭**に置く
  (`krkrtemplate/plugins` に転がっている古い `tp_stub.h` を拾わないため)

### 束ね役 (packinone.cpp)

`krkrz_plugin_<名前>()` は本体の `TVPRegisterPlugin()` を呼ぶが、**DLL からは本体の
それを呼べない** (ヘッダに宣言があるだけ)。そこで **packinone 自身が
`TVPRegisterPlugin` を定義して横取り**し、集めた `link` を自分の `V2Link` から順に呼ぶ。

### 本体の口: `TVPRegisterBundledPlugin`

```cpp
TVPRegisterBundledPlugin(ttstr(p->name) + TJS_W(".dll"));
```

これを呼ぶと本体が「その名前は同梱済み」と覚え、以後

- `Plugins.link("csvParser.dll")` … **何もせず成功**
- `Plugins.canLink("csvParser.dll")` … **true**

になる。名前はファイル名部分だけを見て大小文字を無視するので
`tools/plugin64/CSVPARSER.DLL` でも一致する。
旧 PackinOne が `Plugins.link` を自前で差し替えてやっていたことの置き換え。

### 実測 (SDL ビルド)

```
(info) Bundled Plugin:csvparser.dll / savestruct.dll / scriptsex.dll / shrinkcopy.dll /
       layerexbtoa.dll / layerexraster.dll / layereximage.dll / tjsdatapack.dll
PROBE CSVParser = Object / Scripts.getObjectKeys = Object / Layer.doBoxBlur = Object
PROBE Layer.gaussianBlur / colorize / modulate = Object            (layerExImage)
PROBE Scripts.saveDataPack / loadDataPack / makeDataPackDigest = Object
PROBE saveDataPack→loadDataPack 往復 OK / makeDataPackDigest = 3492451245
PROBE canLink(csvParser.dll) = 1 / canLink(notexist.dll) = 0
PROBE link(layerExImage.dll) は素通り OK / 大小文字・パス違いも OK
```

## 取り込み状況

| | |
|---|---|
| ✅ 取り込み済み (10) | csvParser / saveStruct / scriptsEx / shrinkCopy / layerExBTOA / layerExRaster / layerExImage / tjsDataPack / pemachinetype / TriBinPairString |
| ⬜ 次 | fstat — ⚠ **見積もり誤り。下記参照** |
| ⬜ 要否再検討 | addFont (本体に `System.addFont` あり) |
| ⬜ 作り直し | proxyfs / tlgSliceLoader |
| ⬜ packinoneWin32 へ | process / DpiIconManager / systemEx の Win32 部分 |

⚠ **取り込んだものは `TVP_PLUGINS` から外す** (同じクラスの二重登録を避けるため)。
外し忘れると個別 DLL と両方ビルドされる。

⚠ **外した分は単体 DLL が作られなくなる。** とくに `tjsDataPack.dll` は
既存プロジェクトが単体で配置して使っている。 このツリーの成果物を配るときは
`PackinOne.dll` を一緒に置くこと (単体で要るなら、その置き場の
`krkrtemplate/plugins_utf8/tjsDataPack` を直接ビルドする)。

⚠ `tjsDataPack` だけは現行ツリーの外 (`krkrtemplate/plugins_utf8`) にある。
`PACKINONE_TJSDATAPACK_DIR` で差せる。 無い場合は警告を出して**その 1 個だけ落とす**
(`PACKINONE_HAS_TJSDATAPACK` で packinone.cpp 側も連動する)。

## ⚠ fstat は「ストリームの置き換えだけ」では済まない (見積もり誤り)

当初「`TVPCreateIStream` を `TVPCreateStream` に替えるだけ」と見積もったが、実際に
中身を見たら **ファイルシステム API を直接叩いている部分が本体**だった。

```
CreateFile ×3 / GetFileAttributes ×5 / SetFileAttributes ×2 / GetFileTime ×2 /
SetFileTime ×2 / FindFirstFile・FindNextFile ×2 / CreateDirectory ×2 /
RemoveDirectory / MoveFile / CopyFile / DeleteFile / SearchPath
```

生えるメソッドも `Storages.dirlist` / `createDirectory` / `moveFile` /
`copyFile` / `setFileAttributes` / `changeDirectory` … と、ほぼ全部が
ローカルファイルシステム操作。 IStream を使っているのは
`fstat` / `exportFile` / `getMD5HashString` の 3 箇所だけ。

**選択肢**:

| | |
|---|---|
| A. `std::filesystem` で書き直す | packinone は C++17 なので通る。全機種で動く。手は入る |
| B. `packinoneWin32` へ送る | 現状維持。 generic では使えないまま |

⬜ **未決**。 generic (SDL / CS) で `Storages.dirlist` 等が要るかどうかで決まる。

## ⚠ ビルド構成の未決事項

- ✅ 二重登録 → 取り込んだものは `TVP_PLUGINS` から外す (決定・実施済み)
- ✅ 取り込み方 → 静的プラグイン機構に寄せた (上記)
- ✅ `Plugins.link` の乗っ取り → 本体に `TVPRegisterBundledPlugin` の口を作った
- ⬜ fstat を std::filesystem で書き直すか packinoneWin32 へ送るか (上記)
- ⬜ `packinoneWin32` の切り出し (WINVER 専用機能)
- ⬜ 案件への配備をどうするか (いまの案件は旧 PackinOne.dll をそのまま使っている)

## 参考

- `doc/GenericPluginLoading.md` — generic のプラグイン解決と Win32 専用 API スタブの話
- 旧ソース: `krkrtemplate/plugins/packinone` (Shift_JIS、**触らない**)
