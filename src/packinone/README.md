# packinone 再構築 (調査と実装範囲)

status: **実装中 (2026-09-28)**。packinone 11 個 + packinoneWin32 4 個 / 残りは proxyfs のみ
置き場: `src/packinone` / `src/packinoneWin32` (`src/plugins` とは別枠)

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
| `packinoneWin32` | **WINVER 専用**の機能を分ける (Win32 の UI / ウィンドウ / COM / ローカル FS に触るもの)。`KRKRZ_VARIANT=WIN` のときだけターゲットを作る |

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
| `fstat` | `src/plugins/fstat` | ローカル FS 操作そのもの | ✅ **大半は本体へ移した**。Win32 専用の残りだけ packinoneWin32 |
| `addFont` | `src/plugins/addFont` | `AddFontResourceEx` / テンポラリ展開 | ❌ **不要**。本体の `System.addFont` に寄せた (下記) |
| `proxyfs` | `krkrtemplate/plugins_utf8/proxyfs` | IStream でストリームを**提供**している | ⚠ 作り直しが要る (本体のストレージメディア API へ) |
| `tlgSliceLoader` | `krkrtemplate/plugins_utf8/tlgSliceLoader` | 無し | ✅ 取り込み済み (Win32 依存は無かった) |
| `systemEx` | `src/plugins/systemEx` | レジストリ / DPI / OS バージョン / 既知フォルダ / DLL 検索パス | ✅ **分割済み**。環境変数と URL エンコードは本体へ、残りは packinoneWin32 |
| `process` | `src/plugins/process` | メッセージ専用ウィンドウを `CreateWindowExW` で作る | ✅ **packinoneWin32 へ取り込み済み** |
| FileSelector / selfile | (旧 packinone のみ) | ファイル選択ダイアログ | ❌ **不要**。本体に `Storages.selectFile` / `selectDirectory` がある (WINVER / generic 両方) |
| DpiIconManager | (旧 packinone のみ) → `src/plugins/dpiicon` | ウィンドウアイコン / DPI | ✅ **packinoneWin32 へ取り込み済み** (UTF-8 化して起こし直し) |
| pemachinetype | (旧 packinone のみ) → `src/plugins/pemachinetype` | PE ヘッダを読んで x86/x64 判定 | ✅ 取り込み済み (ストリームを置換して起こし直し) |
| TriBinPairString | (旧 packinone のみ) → `src/plugins/TriBinPairString` | 文字列ユーティリティ | ✅ 取り込み済み (計算のみ。UTF-8 化して起こし直し) |

## 本体が既に持っているので実装しなくてよいもの

| 機能 | 本体 API | 備考 |
|---|---|---|
| ファイル / フォルダ選択ダイアログ | `Storages.selectFile` / `Storages.selectDirectory` | **WINVER / generic の両方にある** (`*/base/StorageImpl.cpp`) |
| ローカルファイル操作 | `Storages.fstat` / `dirlist` / `dirlistEx` / `dirtree` / `isExistentDirectory` / `createDirectory` / `removeDirectory` / `moveFile` / `deleteFile` / `copyFile` / `exportFile` / `truncateFile` / `getMD5HashString` / `getTemporaryName` / `clearStorageCaches` | **2026-09 に fstat から本体へ移した** (`common/base/StorageIntf.cpp`)。WINVER / generic 共通 |
| フォント追加 | `System.addFont` / `Font.addFont` | `*/base/SystemImpl.cpp` / `common/visual/LayerIntf.cpp`。**WINVER に `System.addFont` が無かったので足した** |
| プログラム起動 | `TVPExecuteProgram` (generic にもある) / `System.shellExecute` (WINVER) | `process` の「起動するだけ」の用途はこれで足りる |
| MD5 | `TVP_md5_init` / `append` / `finish` をプラグインへ export 済み | ⚠ `__WINVER__` ガードが**無い**ので全機種で使える |

## 実装範囲 (絞り込み結果)

1. ✅ **そのまま取り込むだけ**: csvParser / saveStruct / scriptsEx / shrinkCopy /
   layerExBTOA / layerExImage / layerExRaster / tjsDataPack (8 個) — **完了**
2. ✅ **ストリームの置き換えだけ**: pemachinetype / TriBinPairString — **完了**
   (どちらも旧 PackinOne にしか無かったので、`src/plugins/` に個別プラグインとして
    起こし直してから取り込んだ。 単体 DLL は作っていない = `TVP_PLUGINS` に入れていない)
3. ✅ **要否から再検討**: addFont — **取り込まない** (下記)
4. **作り直し**: proxyfs (ストリームを提供する側なので設計から)。
   tlgSliceLoader は ✅ **調査の結果そのまま入った** (下記)
5. ✅ **packinoneWin32 へ**: fstat / systemEx (Win32 部分) / process / dpiicon — **完了**
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
| ✅ 取り込み済み (11) | csvParser / saveStruct / scriptsEx / shrinkCopy / layerExBTOA / layerExRaster / layerExImage / tjsDataPack / pemachinetype / TriBinPairString / tlgSliceLoader |
| ✅ packinoneWin32 (4) | fstat / systemEx (どちらも本体へ移した分を除く) / process / dpiicon |
| ⬜ 作り直し | proxyfs (ストリームを提供する側なので設計から) |

⚠ **取り込んだものは `TVP_PLUGINS` から外す** (同じクラスの二重登録を避けるため)。
外し忘れると個別 DLL と両方ビルドされる。

⚠ **外した分は単体 DLL が作られなくなる。** とくに `tjsDataPack.dll` は
既存プロジェクトが単体で配置して使っている。 このツリーの成果物を配るときは
`PackinOne.dll` を一緒に置くこと (単体で要るなら、その置き場の
`krkrtemplate/plugins_utf8/tjsDataPack` を直接ビルドする)。

⚠ `tjsDataPack` だけは現行ツリーの外 (`krkrtemplate/plugins_utf8`) にある。
`PACKINONE_TJSDATAPACK_DIR` で差せる。 無い場合は警告を出して**その 1 個だけ落とす**
(`PACKINONE_HAS_TJSDATAPACK` で packinone.cpp 側も連動する)。

## addFont は取り込まない (本体へ寄せた)

旧 `addFont` プラグインは `System.addFont(file, extract)` を生やし、
`AddFontResourceEx` / テンポラリ展開という **Win32 の作りそのもの**だった。

本体には既に同じことをする口があるので、そちらへ寄せた。

| | 旧プラグイン | 本体 |
|---|---|---|
| 置き場 | `System.addFont(file, extract)` | `Font.addFont(storage)` / `System.addFont(storage)` |
| アーカイブ内 | `extract` でテンポラリ展開が要る | ストレージが面倒を見るので不要 |
| 戻り値 | 登録できたフォント数 | 実 face 名の配列 |

やったこと:

- **WINVER の本体に `System.addFont` を足した** (generic には既にあった)。
  中身は `Font.addFont` と同じ `FontSystem::AddExtraFont`
- generic の `System.addFont` も face 名の配列を返すようにして戻り値をそろえた

実測:

```
SDL    : System.addFont("roboto-regular.ttf") -> ["Roboto Regular"]
WINVER : System.addFont("roboto-regular.ttf") -> []       ← 下記
両方   : 存在しないファイルは「ストレージ … を開くことができません」
```

⚠ **WINVER で face 名が返らないのは本体側の既存の穴**で、この変更とは別件。
`GDIFontRasterizer::AddFont` が `AddFontMemResourceEx` を呼ぶだけで
`faces` を埋めていない (`Font.addFont` も同じく空配列が返る)。
埋めるにはフォントの name テーブルを自前で読む必要がある。

## fstat は大半を本体へ移し、Win32 専用の残りだけ packinoneWin32 へ

当初「`TVPCreateIStream` を `TVPCreateStream` に替えるだけ」と見積もったが、実体は
**ファイルシステム API の直叩き**だった (`CreateFile` ×3 / `GetFileAttributes` ×5 /
`FindFirstFile` / `CopyFile` / `MoveFile` / `SetFileTime` / `SearchPath` …)。
IStream を使っているのは `fstat` / `exportFile` / `getMD5HashString` の 3 箇所だけ。

### 本体の `Storages` は WINVER と generic で品揃えが違う

| | WINVER の本体 | generic の本体 |
|---|---|---|
| `getLocalName` / `searchCD` / `selectFile` / `selectDirectory` / `getLastModifiedFileTime` | ✅ | ✅ |
| `dirlist` / `dirtree` / `isExistentDirectory` / `moveFile` / `deleteFile` | ❌ | ✅ |
| `commitSavedata` / `rollbackSavedata` | ❌ | ✅ |

つまり**重要どころは generic の本体が既に持っていて、WINVER の本体だけが持っていない**。

### やったこと: 下回りが両方にあるものは本体へ移した

本体には **WINVER / generic の両方にある**ローカルファイル操作の下回りが揃っている:

```
TVPCreateStream / TVPMoveStorage / TVPRemoveStorage / TVPCreateFolders /
TVPRemoveFolder / TVPFileSize / TVPLastModifiedFileTime /
TVPCheckExistentLocalFile / TVPCheckExistentLocalFolder / TVPGetTemporaryName
```

足りなかったのは「ディレクトリかどうかを付けた列挙」だけだったので、
`TVPGetLocalFolderListAt()` を 1 本足した (generic は
`iTVPLocalFileSystem::GetListAt`、WINVER は `FindFirstFileW` に落ちる)。

これで fstat のメソッドの大半は**本体 (`common/base/StorageIntf.cpp`) に
1 つの実装**で置ける。 移したのは 16 個:

```
clearStorageCaches / fstat / dirlist / dirlistEx / dirtree /
isExistentDirectory / isExistentStorageNoSearchNoNormalize /
createDirectory / removeDirectory / moveFile / deleteFile /
copyFile / exportFile / truncateFile / getMD5HashString / getTemporaryName
```

generic 本体が持っていた `dirlist` / `dirtree` / `isExistentDirectory` /
`moveFile` / `deleteFile` は common へ引き上げたので、**generic からは消してある**
(二重登録を避けるため)。

### プラグインに残るもの (Win32 専用 = 下回りが本体に無い)

```
getTime / setTime / setLastModifiedFileTime      ← ctime/atime と時刻の書き込み
setFileAttributes / resetFileAttributes / getFileAttributes  ← Win32 の属性ビット
searchPath                                        ← SearchPath
getDisplayName                                    ← シェルの表示名
changeDirectory / currentPath                     ← プロセスのカレント
createDirectoryNoNormalize / copyFileNoNormalize  ← 正規化なし版
TemporaryFiles クラス                             ← DELETE_ON_CLOSE ハンドル
```

本体へ移した 16 個はプラグイン側も `IF_MISSING` で登録してあるので、
**本体がある環境では登録されない** (古い本体と組み合わせたときだけ補完する)。

### 実測 (WINVER / generic で結果が一致)

```
[本体のみ] 生えていないもの: なし
[本体のみ] Win32 専用のうち生えているもの: なし (想定どおり)
dirlist("./") / dirlistEx("./") (name + isDirectory) / isExistentDirectory("./")=1
fstat(startup.tjs) size / mtime>0
getMD5HashString = 3ec457795713f439efee25c3c2ef75d3   ← 両機種で同値
createDirectory("probedir/a/b/")=1 → dirtree("probedir",true) = a/,a/b/
  → removeDirectory=1 → 消えたか OK
copyFile=1 (サイズ一致) / failIfExist の 2 回目=0
exportFile → truncateFile(…,100) → サイズ=100
moveFile=1 → deleteFile=1 → 存在=0

[WINVER] PackinOneWin32.dll を link する前後:
  前: Win32 専用 11 個は生えていない / currentPath, TemporaryFiles も無い
  後: 11 個 + currentPath + TemporaryFiles が生える。
      本体側の dirlist / fstat / getMD5HashString は上書きされず同じ値のまま
      getFileAttributes(startup.tjs)=32 / getTime は mtime,ctime,atime とも取れる
[SDL] canLink(fstat.dll)=0 (packinoneWin32 は作られない)
```

### ついでに直した本体側のバグ 2 件

- **generic の `TVPRemoveFolder` が極性を間違えていた** (`0==RemoveDirectory(...)`)。
  実際には削除できているのに false が返っていた
- **`deleteFile` / `moveFile` の後も `isExistentStorage` が true を返すことがあった**。
  `TVPGetPlacedPath` は「渡された名前」をキーにキャッシュするので、
  正規化名だけ落としても素の名前で引いた結果が残る。両方落とすようにした
- `truncateFile` は `iTJSBinaryStream::SetEndOfStorage` では generic の実ファイルが
  縮まない (論理位置を覚えるだけ) ため、`std::filesystem::resize_file` を使う

## tlgSliceLoader は Win32 依存が無かった (そのまま入った)

「作り直しが要る」と見積もっていたが、実際に見たら **`StreamWrapper.hpp` は
どこからも include されていない死にコード**だった。 これは古い tp_stub に
`tTJSBinaryStream` が無かった頃の名残で、`tTJSBinaryStream` を IStream の
ラッパとして自前定義し `TVPCreateStream` をマクロで乗っ取るもの。
現行のソースは本体の `iTJSBinaryStream` / `TVPCreateStream` を直接使っている。

`lz4` は tjsDataPack のものを共用する (同じ DLL なので `lz4.c` は 1 本で足りる)。
`tjsDataPack` が無い構成では `tlgSliceLoader` も落とす。

実測 (SDL):

```
(info) Bundled Plugin:tlgsliceloader.dll / canLink(tlgSliceLoader.dll)=1
SliceLayer.SliceLoader.{loadSlicedImage,fetchPartialInfo,loadPartialImage,loadNormalImage}
Layer.fetchImageSize が png / tlg6 / bmp とも [32,24,4] を返す
```

⚠ `Layer.fetchImageSize` の戻りは **`[幅, 高さ, 成分数]` の配列**
(`width` / `height` を持つ辞書ではない)。

## systemEx も同じ手で分けた

| | |
|---|---|
| 本体へ移した | `getAboutString` / `readEnvValue` / `writeEnvValue` / `expandEnvString` / `urlencode` / `urldecode` |
| packinoneWin32 に残す | `writeRegValue` / `waitForAppLock` / `setDpiAwareness` (+`dac*` 定数) / `getOSVersion` / `getKnownFolderPath` / `processApplicationMessages` / `handleApplicationMessage` / `setDefaultDllDirectories` (+`lls*` 定数) / `addDllDirectory` / `removeDllDirectory` |

環境変数は CRT 経由 (`_wgetenv` / `_wputenv_s`、POSIX は `getenv` / `setenv`)、
`expandEnvString` の `%NAME%` 展開は自前で書いたので generic でも動く。
`urlencode` は**旧実装に二重 delete があった**ので直してある。

実測 (WINVER / generic で結果が一致):

```
[本体のみ] 生えていないもの: なし / Win32 専用のうち生えているもの: なし
PATH が読める / 未設定は void / writeEnvValue は以前の値を返す / 空文字列で消える
expandEnvString("[%KRKRZ_PROBE_VAR%]") = [second]
expandEnvString 未設定はそのまま = [%KRKRZ_NO_SUCH_VAR_XYZ%] / "%%" → "%"
urlencode("a b&c=d") = a%20b%26c%3Dd / "あいう" = %E3%81%82%E3%81%84%E3%81%86
utf8=0 の往復も OK / 不正な %XX は例外
[WINVER] link 後に Win32 専用 10 個 + dac*/lls* 定数 + Process + DpiIcon が生え、
         本体側の urlencode / readEnvValue / getAboutString は上書きされない
         getOSVersion major=10 build=26200 / getKnownFolderPath も取れる
         DpiIcon: getDpi(win)=192 / calcSize(24,192)=48 / setIcon=1
```

⚠ **`DpiIcon` はウィンドウアイコンの唯一の口**になっている。
windowEx 廃止で `setWindowIcon` が落ちたままなので、これが無いと
engine はアイコン設定を黙って飛ばす (`typeof global.DpiIcon` で分岐している)。

## ⚠ ビルド構成の未決事項

- ✅ 二重登録 → 取り込んだものは `TVP_PLUGINS` から外す (決定・実施済み)
- ✅ 取り込み方 → 静的プラグイン機構に寄せた (上記)
- ✅ `Plugins.link` の乗っ取り → 本体に `TVPRegisterBundledPlugin` の口を作った
- ✅ fstat → 16 個を本体へ移し、Win32 専用の残りだけ packinoneWin32 へ
- ✅ `packinoneWin32` の残り (systemEx / process / dpiicon) も取り込み済み
- ⬜ proxyfs の作り直し (IStream 前提の 1400 行。下記)
- ⬜ 案件への配備をどうするか (いまの案件は旧 PackinOne.dll をそのまま使っている)

## 参考

- `doc/GenericPluginLoading.md` — generic のプラグイン解決と Win32 専用 API スタブの話
- 旧ソース: `krkrtemplate/plugins/packinone` (Shift_JIS、**触らない**)
