# プラグイン一覧資料 (wamsoft ビルド構成)

吉里吉里Z (krkrz_dev) umbrella ビルドに組み込むプラグインの一覧・現状・
Win32 依存の原因をまとめた資料。`wamsoft` ブランチ (worktree
`../krkrz_dev_wamsoft`) の構成を対象とする。

## ソースの所在とビルド枠組み

- **src/plugins/** … umbrella リポジトリ本体のプラグイン submodule 群。
- **../krkrtemplate/plugins_utf8/** … ワムソフト開発作業用プラグイン
  (`TVP_PLUGIN_FOLDERS` に追加)。src/plugins に無いものをここから取り込む。
- 各プラグインは `TVP_PLUGINS` に列挙され、`src/core` が
  `add_subdirectory(${FOLDER}/${PLUGIN})` + `install(TARGETS ${PLUGIN})` で解決。
  → **TVP_PLUGINS 名 = フォルダ名 = ターゲット名** が必須。

### ビルド状況の凡例

| 記号 | 意味 |
|---|---|
| **全** | ポータブル。全バリアント (WIN / SDL / LIB) 共通でビルド |
| **WIN** | `KRKRZ_VARIANT STREQUAL "WIN"` 限定 (Win32 依存または未移植) |
| **utf8** | wamsoft 追加分 (plugins_utf8 由来)。現状 WIN 限定で登録 |
| **除外** | 既定でコメントアウト / 本体機能と重複などで対象外 |

---

## 1. ポータブル プラグイン (src/plugins・全バリアント)

いずれも Win32 固有 API の実利用は無い。`windows.h` の出現は (a) `#ifdef _WIN32`
でガードされた DLL エントリ定型、(b) バンドルされたクロスプラットフォームな
サードパーティ (ThorVG / psdparse) 内部、(c) コンフリクト回避コメントのいずれか。

| プラグイン | 状況 | 機能概要 | 備考 |
|---|---|---|---|
| KAGParserEx | 全 | KAGParser を置換・拡張 (複数行タグ記述など) | 移植可 |
| csvParser | 全 | CSV ファイルパーサ | 移植可 |
| getSample | 全 | WaveSoundBuffer に口パク用サンプル値取得を追加 | 移植可 |
| json | 全 | JSON ファイルパーサ | 移植可 (※WINVERビルドで `<vector>` include 漏れ顕在化 §7) |
| layerExAreaAverage | 全 | Layer に面積平均法の縮小命令を追加 | 移植可 |
| layerExBTOA | 全 | レイヤの α 領域 / Province 操作 (α動画対応など) | 移植可 |
| layerExImage | 全 | Layer への画像処理系拡張 (一部 CxImage 由来) | 移植可 |
| layerExLongExposure | 全 | 長時間露光「風」画像生成 | 移植可 |
| layerExRaster | 全 | Layer にラスター処理風コピー命令を追加 | 移植可 |
| layerExVector | 全 | ThorVG によるベクタ描画拡張 (LayerExDraw のサブセット) | windows.h はThorVG内部のみ |
| lineParser | 全 | 行単位のテキストパーサ | 移植可 |
| minizip | 全 | minizip-ng による zip 入出力 | **要注意**: 排他制御に Win32 `CRITICAL_SECTION`。`#ifdef _WIN32` ガードだが**非Windows フォールバック無**でロックが無効化 → `std::mutex` 化が必要 |
| psdfile | 全 | PSD 読込・レイヤ取得・`psd://` 仮想ストレージ | windows.h は psdparse submodule 内のみ |
| saveStruct | 全 | Array/Dictionary の saveStruct を UTF-8/CP 出力 | 移植可 (※WINVERビルドで include 漏れ顕在化 §7) |
| scriptsEx | 全 | iTJSDispatch2 を直接操作する裏口プラグイン | 移植可 |
| shrinkCopy | 全 | 面積平均法の縮小専用コピーを Layer に追加 | 移植可 |
| krkr_richtext | 全 | ThorVG/minikin によるリッチテキスト描画 | linux/osx/android プリセットあり |
| krkrlua | 除外 | Lua バインド | CMakeLists でコメントアウト |

---

## 2. Win32 専用 プラグイン (src/plugins)

現状 `KRKRZ_VARIANT=="WIN"` 限定。原因を「非移植の核」で示す。★は
**核が Win32 でほぼ移植不可**、△は**付随部分のみ Win32 で移植容易**(→§4)。

| プラグイン | 状況 | 機能概要 | Win32依存の原因 |
|---|---|---|---|
| addFont | WIN ★ | アーカイブ/実ファイルのフォントを private 登録する System.addFont | GDI フォント登録 `AddFontResourceEx`/`AddFontMemResourceEx`/`Remove...`(gdi32) が核。テンポラリ展開に Win32 file API + COM `IStream` |
| binaryStream | WIN △ | バイナリストリーム (read/write/seek/copy/zlib/adler/MD5/XP3フィルタ) | 本体は移植可。核は暗号フィルタ DLL の `LoadLibraryW`/`GetProcAddress`/`__stdcall` ロード。→ dlopen 化で移植可 |
| fpslimit | WIN △ | System.fpslimit で連続コールバックによりフレーム間引き | 待機 `Sleep()` と DLLエントリ `WINAPI` のみ。→ `sleep_for` 化で移植可 |
| memfile | WIN △ | `mem:///` メモリ仮想ファイル/ディレクトリ | バッファに `GlobalAlloc`(HGLOBAL)+COM `CreateStreamOnHGlobal`。→ std::vector 化で移植可 |
| varfile | WIN △ | `./` var ストレージ (TJS octet をファイル化) | memfile 同様 HGLOBAL + 自前 `IStream`。→ 可搬バッファ化で移植可 |
| fstat | WIN ★ | Storages にファイル情報/時刻/属性/列挙/コピー移動/フォルダ選択/MD5 等を追加 | 全面 Win32 file/shell: `CreateFile`/`FindFirstFileEx`/`GetFileAttributes`/`CopyFile`+シェル COM `SHBrowseForFolder`/`IShellFolder`。非移植度最大 |
| gamepad | WIN ★ | ゲームパッド入力 (スティック/トリガー/ボタン/振動) | DirectInput (`IDirectInput8`) + XInput + COM。→ SDL_GameController への全面書換が必要 |
| layerExDraw | WIN ★ | GDI+ でレイヤにテキスト/図形/パス/画像を高品質描画 | 描画エンジンが GDI+ (`Gdiplus::Graphics` 等)。→ Skia/Cairo へ全面置換が必要 (layerExVector が ThorVG 版サブセット) |
| layerExSave | WIN △ | レイヤ画像を PNG/TLG5 で保存 (同期/非同期) | エンコーダ (LodePNG/TLG5) は移植可。核は非同期部の `_beginthread`+`PostMessage(HWND,WM_APP)` 通知 |
| menu | WIN ★ | Window にネイティブメニューバー/ポップアップを構築 | Win32 メニュー `HMENU`/`MENUITEMINFO`/`WM_COMMAND`。OS メニュー機構前提 |
| msgreceiver | WIN ★ | `WM_COPYDATA` 受信 IPC (onCopyData / HWND 保存) | ウィンドウメッセージ IPC `WM_COPYDATA`/`COPYDATASTRUCT` + Window メッセージフック |
| stdio | WIN ★ | 標準入出力 (コンソール) へ UTF-8 で接続 | Windows コンソール API `AllocConsole`/`GetStdHandle`/`SetConsoleOutputCP(CP_UTF8)`。GUI にコンソールを付ける Windows 固有機能 |
| win32dialog | WIN ★ | メモリ上 `DLGTEMPLATE` からネイティブダイアログ生成 | Win32 ダイアログマネージャ `CreateDialogIndirectParam` + commctrl。名称通り Win32 GUI 直結 |
| windowEx | WIN ★ | Window 枠/アイコン/最大最小化ボタン/角丸/タスクバー/デバイス着脱通知 | `HWND` 前提の `GetWindowLong`/`SetWindowPos`/`WM_*` + DWM `DwmSetWindowAttribute`(角丸) + `RegisterDeviceNotification` |
| httprequest | WIN ★ | 非同期 HTTP(S) リクエスト (XMLHttpRequest 風) | WinINet `InternetOpen`/`HttpOpenRequest`/`InternetReadFile` + `_beginthreadex` + `PostMessage` 通知。→ libcurl 置換が必要 |
| shellExecute | WIN ★ | Window に shellExecute / コマンド実行 (標準出力取得) を追加 | `ShellExecuteEx` + `CreateProcessW`+`CreatePipe` + HWND_MESSAGE ウィンドウ `PostMessage` コールバック |
| systemEx | WIN △ | OSバージョン/既知フォルダパス/メッセージボックス等 | `MessageBox`/`RtlGetVersion`/`SHGetKnownFolderPath`。→ 機能ごとに OS API 置換で移植容易 |
| tftSave | WIN ★ | フォントグリフをレンダリングしテクスチャフォント(TFT)生成/保存 | GDI `GetGlyphOutlineW`(HDC/HFONT) + DirectWrite `IDWriteBitmapRenderTarget`。フォントラスタライズが核 |
| process | WIN ★ | Process クラス (子プロセス起動/標準出力取得/シグナル送信) | `CreateProcessW`+`CreatePipe`+`WaitForSingleObject`/`TerminateProcess` + メッセージ専用ウィンドウ `PostMessage` |
| messenger | WIN ★ | ウィンドウ間メッセージ通信 (HWND保存/`WM_COPYDATA`/ユーザメッセージ) | `SendMessage`/`PostMessage`/`WM_COPYDATA`/`RegisterWindowMessage`/`EnumWindows`。Window メッセージ機構が本体 |
| windowExProgress | WIN ★ | ウィンドウ上にネイティブ プログレスバー(+キャンセル)を重ねる | コモンコントロール `PROGRESS_CLASS` を `CreateWindowEx` + `PBM_*` + `FindWindowEx`(描画ウィンドウ TScrollBox の HWND) |
| win32ole | WIN ★ | TJS から COM/OLE オートメーション(IDispatch)を操作 | COM/OLE 全面 (`IDispatch`/`VARIANT`/ATL/`ITypeInfo`/ActiveScript)。Windows 専用技術 |
| sigcheck | WIN △ | 実行ファイル/ファイルの RSA-PSS+SHA256 署名を非同期検証 | 署名検証自体は libtomcrypt で移植可。核は `_beginthread`+`PostMessage(HWND,WM_APP)` 通知のみ |
| resourceRW | 除外 | リソース読み書き | CMakeLists でコメントアウト |
| httpserv | 除外 | 簡易 HTTP サーバ | CMakeLists でコメントアウト |
| steam | 除外 | Steamworks 連携 (`krkrsteam.dll`) | `STEAMWORKS_SDK` 環境変数指定時のみ。既定コメントアウト |

---

## 3. ワムソフト追加 プラグイン (plugins_utf8 由来)

`makeworld_tools_utf8/plugin64*` の DLL のうち、src/plugins に無く plugins_utf8 側に
ソースがあるもの。CMakeLists.txt を新規作成 (6件) または既存流用 (2件)。内訳:
- **textrender / wfstkeff / wfdspfilter** … Win32 非依存化 → **base (全バリアント) リストへ**
  (wf* は windows.h を `#ifdef _WIN32` ガード＋license を非Windows no-op 化。§4-4)。
- **getLangName / lzfs / msdfrender** (3件) … WIN ブロック。
- **k2compat / wvdecoder** … CMakeLists 作成済だが構成からは除外 → §6。

| フォルダ | 出力DLL | 状況 | CMakeLists | 機能概要 | Win32依存の原因 |
|---|---|---|---|---|---|
| getLangName | getLangName.dll | utf8 △ | 既存 | OS/ユーザ UI 言語・ロケール表示名を取得 | NLS API `GetLocaleInfoW`/`GetUserDefaultUILanguage`。`#else` に別実装あり → 各OS言語取得APIへ差替で移植可 |
| ~~k2compat~~ | k2compat.dll | **除外** | 新規(残置) | 吉里吉里2互換のウィンドウ/ダイアログ/タッチ・マウス補助 | 構成から除外 (原則今後不使用) → §6 |
| lzfs | lzfs.dll | utf8 △ | **新規** | LZ4 フレーム圧縮ファイルを透過展開する StorageMedia | LZ4 本体は移植可。核は `CreateStreamOnHGlobal`(HGLOBAL)+自前 `IStream`。→ tTJSBinaryStream 実装置換で移植可 |
| msdfrender | msdfrender.dll | utf8 ★ | **新規** | レイヤ上で MSDF/SDF グリフ生成・カラーテーブル描画 | kzbackport `win32/TVPSysFont.cpp` が GDI (`CreateFontIndirect`/`GetGlyphOutline`) でグリフをラスタライズ → 実 Win32 依存。WIN 継続 |
| textrender | textrender.dll | **全** | 既存 | 矩形内リッチテキスト整形/レイアウト (禁則/ルビ/リンク/時間制御) | **Win32非依存 (base へ移動)**。フォント実測は TJS コールバック委譲。ソースに windows.h 無し、CMakeLists は `.rc` 不参照 |
| ~~wvdecoder~~ | wvdecoder.dll | **除外** | 新規(残置) | 音源(ogg/opus/wav)を生 PCM へ一括デコードする解析用プラグイン | 構成から除外 → §6 |
| wfstkeff | **wfBasicEffect.dll** | **全** | 新規 (OUTPUT_NAME) | オーディオエフェクト (リバーブ/EQ/ディレイ/リミッタ/ボコーダ)。STK 使用 | **移植済→base**。windows.h ガード・license 非Win no-op。STK は OS 別定義 |
| wfdspfilter | **wfTypicalDSP.dll** | **全** | 新規 (OUTPUT_NAME) | 古典 IIR フィルタ (Butterworth/Chebyshev/Elliptic/Bessel/RBJ)。DSPFilters 使用 | **移植済→base**。DSPFilters は純C++。windows.h ガード・license 非Win no-op |

新規 CMakeLists は premake5.lua から移植。同梱ライブラリ: lzfs=lz4(直結) /
wfstkeff=libStk(静的) / wfdspfilter=DSPFilters(静的) / msdfrender=kzbackport(本体へ直結)。
tp_stub/krkrz.cmake は umbrella canonical (`src/plugins/tp_stub`) を利用
(top-level normal var が shadow するため)。v2link は wf*/getLangName/msdfrender とも
`SIMPLEBIND` オプション or 明示追加で umbrella simplebinder を使用。

---

## 4. 「移植可能」だが現状 WIN 扱いのもの (移植候補)

CMakeLists のコメント「WIN32固有機能をつかっていて現時点でWIN専用。要改修」の実体。
以下は **核ロジックは OS 非依存**で、付随部分の置換で SDL/LIB ビルドへ移植できる。

### 4-1. 非同期イベント通知イディオムのみが原因
「ワーカースレッド (`_beginthread`/`_beginthreadex`) + 完了/進捗を
`PostMessage(HWND, WM_APP+n)` で吉里吉里 Window へ通知」という共通イディオムだけが
Win32 依存。`TVPPostWindowMessage`(tp_stub 追加済) + `std::thread` で置換可能。

- **layerExSave** (エンコーダは LodePNG/TLG5 で可搬)
- **sigcheck** (署名検証は libtomcrypt/libtommath で可搬)
- **httprequest** / **shellExecute** / **process** は通知に加えて通信・プロセス
  API 自体も Win32 のため ★ 寄り (通知置換だけでは不足)

### 4-2. メモリバッファを HGLOBAL+IStream で持っているだけ
- **memfile** / **varfile** / **lzfs** … `GlobalAlloc`+`CreateStreamOnHGlobal` を
  可搬バッファ (std::vector / tTJSBinaryStream) に置換すれば移植可能。

### 4-3. 単純な OS 抽象化で済むもの
- **fpslimit** (`Sleep`→`sleep_for`)
- **systemEx** (`MessageBox`/`SHGetKnownFolderPath`→各OS API)
- **getLangName** (NLS→各OS言語取得、既に `#else` 実装あり)
- **binaryStream** (フィルタ DLL ローダを dlopen 化)

### 4-4. Win32 非依存の確認結果 (実ソース検証済 2026-07-01)
「windows.h/.rc が名目的」と当初見立てた4件を実ソースで検証した結果:

- **textrender** … ✅ **非依存を確認 → base (全バリアント) へ移動済**。`.cpp/.h` に
  windows.h 無し、CMakeLists も `.rc` 不参照。
- **wfstkeff / wfdspfilter** … ✅ **移植済 → base へ移動 (2026-07-01)**。
  - 決め手: `wf_common/BasicWaveFilter.cpp` の asm/naked/`__declspec` は
    `#if BWF_USE_K2WRAPPER` 配下で、**x64 では BWF_USE_K2WRAPPER=0**(BasicWaveFilter.hpp)
    のためコンパイル対象外。x64 での実 Win32 依存は `license.cpp` (リソースAPI) のみ。
  - 改修: 各ソースの `#include <windows.h>` を `#ifdef _WIN32` ガード。`license.cpp` は
    `#ifdef _WIN32` 実装 / `#else void ShowLicense(){}` no-op。`license.rc` と
    `V2LINK_NEED_HMODULE` は CMake `if(WIN32)` 限定。v2link は `SIMPLEBIND` オプションへ。
  - ライセンス表示の全プラットフォーム対応は共通 IF 設計待ち (別タスク)。
- **msdfrender** … ❌ 実は Win32 依存。`Plugin.cpp` が無条件 `#include <Windows.h>`、
  kzbackport `win32/TVPSysFont.cpp` が GDI (`CreateFontIndirect`/`GetDC`/`HFONT`) で
  グリフをラスタライズ (MSDF 生成に使用)。移植には font 経路の GDI 置換が必要 → WIN 継続。

### 4-5. 移植困難 (核が Win32) — 全面書換または代替設計が必要
addFont(GDI font) / fstat(file+shell) / gamepad(DirectInput→SDL) /
layerExDraw(GDI+→Skia等) / menu(HMENU) / msgreceiver(WM_COPYDATA) /
stdio(コンソール) / win32dialog(ダイアログ) / windowEx(HWND/DWM) /
tftSave(GDI/DirectWrite) / messenger(WM_COPYDATA) / windowExProgress(comctl) /
win32ole(COM) / k2compat(GUI/WM_TOUCH) / wvdecoder(COM/TSS) / msdfrender(GDI font)

> 補足: minizip はビルド分類上は「全」だが、排他制御が Win32 限定で
> 非Windows ではスレッド安全性が失われる (§1 参照)。実質は移植候補。

---

## 5. ソースが krkrtemplate に無いもの (別リポジトリ・未取得)

`plugin64*` に DLL はあるが src/plugins にも plugins_utf8 にも実ソースが無い。
対象一覧のみ (今回は未対応)。

| DLL | 状況 |
|---|---|
| AlphaMovie / extrans / psbfile / motionplayer | 別リポジトリ (未取得) |
| psd | **除外 (user 判断 2026-09-04)**: `wamsoft_work/libpsd` を近代化して一度取込んだ (2026-07-21) が、今後は使わない方針。§6 参照。PSD 読み込みは `src/plugins/psdfile` (psdparse ベースの `psdfile.dll`) のみ |
| PackinOne | `plugins_utf8/packinone` はあるが `_makefile` が svn switch のみでソース未取得 (`/branches/plugin_PackInOne`) |
| krmovie | 本体側 (`src/core` win32 movie) |
| krkrsteam | `src/plugins/steam` にあり (既定コメントアウト・`STEAMWORKS_SDK` 必須) |

---

## 6. 除外・注意

- **wuopus / wuvorbis** (および `_plain` 版) … 機能は **krkrz 本体に既にある**
  ため対象外 (user 指示)。
- **libpsd (→ psd.dll) … 除外 (user 判断 2026-09-04)**
  - 2026-07-21 に `wamsoft_work/libpsd` を近代化して WIN ゲートへ入れたが
    (TVPCreateStream 化 + x64 ポインタ切り捨て修正 `psd_uintptr`)、
    **今後は使わない方針**。PSD 読み込みは `src/plugins/psdfile`
    (psdparse ベース、全バリアント対応) に一本化する。
  - **除外理由**: 用途が psdfile と重複していること、および
    **libpsd が LGPL-2.0** (`wamsoft_work/libpsd/libpsd/COPYING`) で、
    静的リンクの配布に追加の表記・再リンク条項が付いてくること。
    psdparse は MIT なのでその制約が無い。
  - CMakeLists.txt のプラグイン一覧からは 2026-08-10 (ec14667) の時点で既に
    外れている。ソースは `wamsoft_work/libpsd` に残置 (SVN)。
    ビルド済み `psd.dll` が `bin/*/plugin*/` に残っている場合は消すこと。
- **k2compat … 除外 (user 判断 2026-07-01)**
  - 吉里吉里2互換のウィンドウ/ダイアログ/タッチ・マウス補助プラグイン。生 Win32 GUI
    (`WNDCLASSEXW`/`CreateWindowExW`/`DefWindowProc`) + `WM_TOUCH` サブクラス + comctl32 依存。
  - **除外理由**: 原則今後は使わない方針。CMakeLists.txt は `plugins_utf8/k2compat` に残置。
- **wvdecoder … 除外 (user 判断 2026-07-01)**
  - **正体**: 吉里吉里標準の `WaveSoundBuffer`(再生)を使わず、ogg/opus/wav を
    まるごと生 PCM にデコードするだけの **解析用**プラグイン。`WaveSoundData.F32`
    (float) / `WaveSoundData.S16`(int16) クラスを生やし、`open`/`save`(wav書出)/
    `getSample`/`foreach`/`getLipSync`(リップシンク)/`makeThumbnail`(波形サムネイル)
    等を提供。wav は同梱 dr_libs で独自パース、ogg/opus は `wumtrack` +
    `wuvorbis.dll`/`wuopus.dll` を TSS COM モジュール(`ITSSWaveDecoder`)として
    動的ロードして利用。
  - **除外理由**: ogg/opus 解析は wu*.dll(TSS COM 実体)が前提だが、本体内蔵の
    Vorbis/Opus デコード(再生パス)とは別物で本構成には無い。wav 解析のみなら
    単体動作するが、ツール用途のため本体に載せる必然性が低い。
  - **今後の方針**: 音源解析は **python 等の別ツールで対応**する方向が無難。
  - CMakeLists.txt は `plugins_utf8/wvdecoder` に残置 (将来の単体ビルド用)。

---

## 7. ビルド検証結果 (2026-07-02, VS2022 / vcpkg d:\vcpkg)

両プリセットで configure→build を実施 (worktree の入れ子サブモジュール
richtext/thorvg/psdparse は初期化必須)。

- **x64-windows (SDL/generic): 完全成功** ✅
  base の全プラグイン＋ krkrz64.exe がビルド＆リンク。移植した
  **wfBasicEffect / wfTypicalDSP / textrender** も生成。移植(Win32非依存化)を検証。
- **x64-windows-win (WINVER): 成功** ✅ (wamsoft の6プラグイン
  getLangName / lzfs / msdfrender / wfBasicEffect / wfTypicalDSP / textrender を含む)。

### 今回入れた修正 (modern MSVC + umbrella tp_stub 追従。いずれも wamsoft プラグイン側)
1. **DSPFilters** `Common.h`: `std::tr1`→`std` (VS2015+ で tr1 削除。wfdspfilter)
2. **wf* license.cpp**: `header = (const tjs_char*)head` キャスト
   (umbrella tp_stub の `tjs_char` は `char16_t`、`WCHAR`=wchar_t と別型)
3. **msdfrender**: `UNICODE`/`_UNICODE` 付与 (LOGFONT を wide 化) ＋ kzbackport を
   静的 libでなく**本体へ直接組み込み** (tp_stub/名前空間/define を統一しリンク解決)
4. **msdfrender kzbackport `tvpgl.h`**: `TVPChBlur*` を tp_stub.h へ委譲
   (二重宣言=曖昧呼び出し C2668 を解消)＋ `tvpgl.c` をビルド対象外

### (解決済) WIN 全体ビルドを一時止めていた別要因 = .gitattributes のファイル破壊
初回の WINVER ビルドでは core/既存base側が失敗していたが、**原因は `.gitattributes` の
eol 正規化による checkout 時のファイル破壊**だった (user が特定・修正)。特に:
- `src/core/win32/vcproj/tvpwin32.rc` / `krmovie.rc` … **UTF-16 の .rc** が CRLF 変換で
  バイト列破壊 → rc コンパイラが `unexpected #endif`。
- `src/plugins/json` / `saveStruct` … 破壊で `<vector>` 等が壊れ parse エラー。
→ `.gitattributes` 修正後は **WINVER ビルドも正常** (wamsoft プラグインとは無関係だった)。
