# packinone 再構築 (調査と実装範囲)

status: **土台まで実装 (2026-09-27)**。6 個取り込み済み / 残りは下記
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
| `csvParser` | `src/plugins/csvParser` | 無し | ✅ そのまま取り込む |
| `saveStruct` | `src/plugins/saveStruct` | 無し | ✅ そのまま |
| `scriptsEx` | `src/plugins/scriptsEx` | 無し | ✅ そのまま |
| `shrinkCopy` | `src/plugins/shrinkCopy` | 無し | ✅ そのまま |
| `layerExBTOA` | `src/plugins/layerExBTOA` | 無し | ✅ そのまま |
| `layerExImage` | `src/plugins/layerExImage` | 無し | ✅ そのまま |
| `layerExRaster` | `src/plugins/layerExRaster` | 無し | ✅ そのまま |
| `tjsDataPack` | `krkrtemplate/plugins_utf8/tjsDataPack` | 無し | ✅ そのまま |
| `fstat` | `src/plugins/fstat` | `TVPCreateIStream` (ファイルを開くだけ) | ⚠ ストリームを `TVPCreateStream` へ置換 |
| `addFont` | `src/plugins/addFont` | `TVPCreateIStream` (フォントを読むだけ) | ⚠ 同上。**本体に `System.addFont` があるので要否から再検討** |
| `proxyfs` | `krkrtemplate/plugins_utf8/proxyfs` | IStream でストリームを**提供**している | ⚠ 作り直しが要る (本体のストレージメディア API へ) |
| `tlgSliceLoader` | `krkrtemplate/plugins_utf8/tlgSliceLoader` | 3 ファイル | ⚠ 要調査 |
| `systemEx` | `src/plugins/systemEx` | `TVPGetApplicationWindowHandle` (メッセージボックスの親) / ntdll の `RtlGetVersion` / `SetDefaultDllDirectories` | ⚠ **分割**。移植可能な部分だけ packinone へ、残りは packinoneWin32 |
| `process` | `src/plugins/process` | メッセージ専用ウィンドウを `CreateWindowExW` で作る | ❌ **packinoneWin32 へ** |
| FileSelector / selfile | (旧 packinone のみ) | ファイル選択ダイアログ | ❌ **不要**。本体に `Storages.selectFile` / `selectDirectory` がある (WINVER / generic 両方) |
| DpiIconManager | (旧 packinone のみ) | ウィンドウアイコン / DPI | ❌ **packinoneWin32 へ** (または廃止。[windowEx 廃止で落とした機能] と同じ扱い) |
| pemachinetype | (旧 packinone のみ) | PE ヘッダを読んで x86/x64 判定 | ✅ ファイルを読むだけなので移植可能 |
| TriBinPairString | (旧 packinone のみ) | 文字列ユーティリティ | ✅ 移植可能 |

## 本体が既に持っているので実装しなくてよいもの

| 機能 | 本体 API | 備考 |
|---|---|---|
| ファイル / フォルダ選択ダイアログ | `Storages.selectFile` / `Storages.selectDirectory` | **WINVER / generic の両方にある** (`*/base/StorageImpl.cpp`) |
| フォント追加 | `System.addFont` / `Font.addFont` | `common/visual/LayerIntf.cpp` / `generic/base/SystemImpl.cpp` |
| プログラム起動 | `TVPExecuteProgram` (generic にもある) / `System.shellExecute` (WINVER) | `process` の「起動するだけ」の用途はこれで足りる |
| MD5 | `TVP_md5_init` / `append` / `finish` をプラグインへ export 済み | ⚠ `__WINVER__` ガードが**無い**ので全機種で使える |

## 実装範囲 (絞り込み結果)

1. **そのまま取り込むだけ**: csvParser / saveStruct / scriptsEx / shrinkCopy /
   layerExBTOA / layerExImage / layerExRaster / tjsDataPack (8 個)
2. **ストリームの置き換えだけ**: fstat / pemachinetype / TriBinPairString
3. **要否から再検討**: addFont (本体に同等機能あり)
4. **作り直し**: proxyfs (ストリームを提供する側なので設計から)、tlgSliceLoader (要調査)
5. **packinoneWin32 へ**: process / DpiIconManager / systemEx の Win32 部分
6. **作らない**: FileSelector / selfile (本体のダイアログを使う)

## 実装した仕組み (動作確認済み)

### 取り込み方: 静的プラグイン機構に寄せた

各プラグインのソースを **per-source の define 付きでそのままコンパイル**する。

```cmake
packinone_absorb(scriptsEx NCBIND Main.cpp)
# → TVP_STATIC_PLUGIN / TVP_PLUGIN_NAME=scriptsEx /
#    V2Link=V2Link_scriptsEx / V2Unlink=... / DllEntryPoint=... を付けてコンパイル
```

- `TVP_STATIC_PLUGIN` を付けると **ncbind の自動登録リストがプラグインごとに別名**になり
  (`ncbind.hpp` が `TVP_PLUGIN_NAME` で改名する)、同じ DLL に同居できる
- 同時に `krkrz_plugin_<名前>()` という登録エントリが生える
- ⚠ **ncbind を使うプラグインは V2Link も登録エントリも `ncbind.cpp` 側にある**ので、
  **プラグインごとに ncbind.cpp を別コンパイル**する必要がある
  (生成した 1 行のラッパ `#include "…/ncbind.cpp"` を per-source define 付きで積む)
- ⚠ `V2Link` / `V2Unlink` / `DllEntryPoint` は各プラグインが定義するので、
  define で改名しないと重複定義になる

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
(info) Bundled Plugin:csvparser.dll / savestruct.dll / scriptsex.dll /
       shrinkcopy.dll / layerexbtoa.dll / layerexraster.dll
PROBE CSVParser = Object / Scripts.getObjectKeys = Object / Layer.doBoxBlur = Object
PROBE canLink(csvParser.dll) = 1 / canLink(notexist.dll) = 0
PROBE link(csvParser.dll) は素通り OK / 大小文字・パス違いも OK
```

## 取り込み状況

| | |
|---|---|
| ✅ 取り込み済み (6) | csvParser / saveStruct / scriptsEx / shrinkCopy / layerExBTOA / layerExRaster |
| ⬜ 次 (そのまま入るはず) | layerExImage (LicensesGen.cpp つき) / tjsDataPack |
| ⬜ ストリーム置換が要る | fstat / pemachinetype / TriBinPairString |
| ⬜ 要否再検討 | addFont (本体に `System.addFont` あり) |
| ⬜ 作り直し | proxyfs / tlgSliceLoader |
| ⬜ packinoneWin32 へ | process / DpiIconManager / systemEx の Win32 部分 |

⚠ **取り込んだものは `TVP_PLUGINS` から外す** (同じクラスの二重登録を避けるため)。
外し忘れると個別 DLL と両方ビルドされる。

## ⚠ ビルド構成の未決事項

- ✅ 二重登録 → 取り込んだものは `TVP_PLUGINS` から外す (決定・実施済み)
- ✅ 取り込み方 → 静的プラグイン機構に寄せた (上記)
- ✅ `Plugins.link` の乗っ取り → 本体に `TVPRegisterBundledPlugin` の口を作った
- ⬜ `packinoneWin32` の切り出し (WINVER 専用機能)
- ⬜ 案件への配備をどうするか (いまの案件は旧 PackinOne.dll をそのまま使っている)

## 参考

- `doc/GenericPluginLoading.md` — generic のプラグイン解決と Win32 専用 API スタブの話
- 旧ソース: `krkrtemplate/plugins/packinone` (Shift_JIS、**触らない**)
