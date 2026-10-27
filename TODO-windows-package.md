# Windows 版の配布パッケージ外枠 (krkrz_windows) 設計

**状態: P1〜P5 済み (2026-10-27、リポジトリ = https://github.com/wamsoft/krkrz_windows (public・MIT、2026-10-27 に公開))。§10 の決めどころは同日決定済み。対象は x64 だけ (x86 は扱わない、同日決定)。** 公開ドキュメント = [doc/topics/core/windows_package.md](doc/topics/core/windows_package.md)。設定項目と手順の SSOT は krkrz_windows の README (この文書は設計の経緯と段階の記録)。 索引は [TODO.md](TODO.md)。

吉里吉里Z 本体とタイトルのデータをまとめて、Windows 向けの配布物 (そのまま動くフォルダ / zip /
任意でインストーラ) を作る外枠リポジトリ **krkrz_windows** を新設する。krkrz_linux
(https://github.com/wamsoft/krkrz_linux) と同じ形にする。

- エンジン本体とプラグインのソースは krkrz_dev を `KRKRZ_BASE` 経由で参照する。外枠には Windows 固有の
  ビルド手順とパッケージングだけを置く
- タイトルごとの設定 (`windows-config.json`) と資材は別のフォルダ (プロジェクトフォルダ) に置ける。
  外枠だけでも、同梱のサンプル (krkrz_dev のコアデモ) としてビルドできる
- `cmake` (プラグイン構成) と `assetPack` (資材の取り込み) は他の外枠と共通の書式
  (公開サイトの «外枠リポジトリの共通設定» = `doc/topics/core/platform_config.md`)
- exe の書き換え (アイコン・版情報・埋め込みオプション・セキュリティ設定)・xp3・`.sig` は、標準ツールの
  **リリーサ `krkrrelease`** を呼んで済ませる (外枠で同じ処理を書き直さない)
- 既定は **SDL 版** (他機種と挙動をそろえる)。WINVER 版は従来タイトルを続けて使うための選択肢 (§5)
- 吉里吉里の署名 (`.sig`) を付けたタイトルは、**ファイル破損チェックツール (`krkrcheck`) も一緒に配れる** (§8.1)

Microsoft Store / Xbox 向け (msixvc) は krkrz_gdk の担当なので、ここでは扱わない。

---

## 1. 今あるもの (2026-10-27 確認)

| 部品 | 状態 |
|---|---|
| 汎用のインストーラを作る仕組み | **無い** (TODO-tools.md で «別計画» とだけ書かれていた) |
| リリーサ `krkrrelease` (krkrz_tools、Windows 専用) | 済み。設定は JSON、CLI (`--cli run <release.json>`) あり。exe のコピーと改名 → リソース書き換え (埋め込みオプション: WINVER = TEXT/139、SDL = BINARY/CONFIG.CF、アイコン、版情報) → セキュリティ設定 → データ (`none` / `copy` = 隣に data.xp3 / `bind` = exe に結合。フォルダを渡すと xp3 を作る) → `.sig` (最後)。手順の正本 = krkrz_tools `docs/krkrrelease.md` |
| 署名ツール `krkrsign` / 破損チェック `krkrcheck` | 済み |
| krkrz_dev の Windows の install 成果物 | `krkrz64.exe` / `plugin64/*.dll` / `d3dcompiler_47.dll` / `libEGL.dll` / `libGLESv2.dll` (ANGLE) / SDL 版はさらに `SDL3.dll` / `license.txt` / `licenses/`。CRT と vcpkg のライブラリは静的リンクなので VC++ 再頒布パッケージは要らない |
| 外枠の型 | krkrz_linux (`tools/krkrz_linux.py` の `build` / `stage` / `package`、Makefile、`linux-config.json`) |

---

## 2. 出力

```
<PROJECT_DIR>/build/windows/
  package/<name>/                    そのまま動くフォルダ (Steam のデポ・itch.io・DLsite などはこれをそのまま使う)
    <exeName>.exe                    リリーサで作った exe (アイコン・版情報・埋め込みオプション入り)
    plugin64/*.dll
    SDL3.dll, d3dcompiler_47.dll, libEGL.dll, libGLESv2.dll   (WINVER 版は SDL3.dll なし)
    data.xp3  または  exe に結合 / data/ フォルダ
    *.sig                            署名するとき
    <checkTool.exeName>.exe / .ini   破損チェックツールと公開鍵・文言 (同梱するとき)
    license.txt, licenses/
  dist/<name>-<version>-windows-<arch>.zip
  dist/<name>-<version>-windows-<arch>-setup.exe     (installer を選んだとき)
```

先勝ちの順は «リリーサの出力 (exe / data.xp3 / `.sig`) → 破損チェックツール → エンジン一式 → ANGLE → `assetPack`»。
外枠が置くものを `assetPack` で上書きできない点は krkrz_linux と同じ。

---

## 3. 手順 (`tools/krkrz_windows.py <コマンド>`、Makefile は薄い入口)

| コマンド | 内容 |
|---|---|
| `build` | 外枠の `CMakeLists.txt` (krkrz_dev のトップと同じ手順) を configure / build / install する。`variant` は `-DKRKRZ_VARIANT=SDL/WIN`、triplet は `x64-windows-static`。プラグイン構成は生成ファイル `myapp.cmake` で渡す (他の外枠と同じ)。標準ツール (krkrrelease / krkrsign / krkrcheck) もここでできる |
| `stage` | install 先からエンジン一式を `package/<name>/` に写し、`release.json` を生成してリリーサを呼び、`assetPack` を取り込む |
| `sign` | (任意) Authenticode 署名 → `.sig` の作り直し (§6) |
| `package` | `package.formats` に従って zip / インストーラを作る |
| `all` | `build` → `stage` → `sign` → `package` |

ビルドする PC の前提は krkrz_dev と同じ (Visual Studio 2022 v17.14 と同梱 CMake / Ninja、`VCPKG_ROOT`)。
加えて Python 3 (標準ライブラリのみ)。インストーラを作るときは Inno Setup 6.3 以降 (`ISCC.exe`。7 で確認)、
Authenticode 署名をするときは Windows SDK の `signtool.exe`。

---

## 4. windows-config.json

設計時の案。実装済みの項目の一覧は krkrz_windows の README が SSOT (`checkTool.caption` / `notice`、
`package.installer.dirName` / `icon`、`runtime.angleDir` などを足してある)。

```json
{
  "name": "krkrz-sample",
  "version": "1.0.0",
  "exeName": "krkrz-sample",
  "variant": "sdl",
  "arch": "x64",

  "cmake": {
    "buildType": "Release",
    "options": { "MASTER": "ON" },
    "pluginFolders": [], "plugins": [], "staticPlugins": []
  },

  "release": {
    "icon": "${PROJECT_DIR}/setup/game.ico",
    "versionInfo": { "FileDescription": "", "ProductName": "", "CompanyName": "", "LegalCopyright": "" },
    "options": "; 埋め込みオプション (.cf と同じ書式)\n",
    "security": { "forcedataxp3": 1 },
    "data": { "mode": "copy", "source": "${PROJECT_DIR}/data", "rpf": "" },
    "signKey": ""
  },

  "saveData": { "location": "documents" },

  "checkTool": { "enabled": true, "exeName": "ファイル破損チェック", "publicKey": "${PROJECT_DIR}/setup/public.txt" },

  "assetPack": [ { "type": "mirror", "from": "${PROJECT_DIR}/extra", "to": "" } ],

  "package": {
    "formats": ["dir", "zip"],
    "installer": {
      "appId": "{GUID}",
      "publisher": "", "url": "",
      "installMode": "user",
      "languages": ["japanese", "english"],
      "desktopIcon": true,
      "licenseFile": ""
    }
  }
}
```

| キー | 意味 |
|---|---|
| `name` / `version` | 表示名 / 版 (zip・インストーラの名前、インストーラの版、版情報の FileVersion / ProductVersion) |
| `exeName` | 配る exe の名前 (リリーサの出力名) |
| `variant` | `sdl` (SDL 版の Windows、既定) / `win` (WINVER) (§5) |
| `arch` | `x64` だけ。x86 は扱わない (2026-10-27 決定)。`arm64` は課題 (§11) |
| `cmake.*` / `assetPack` | 外枠共通の書式 |
| `release.*` | リリーサの設定 (`release.json`) にそのまま写す。`version` は `name` / `version` から補う |
| `runtime.angleDir` | ANGLE (`libEGL.dll` / `libGLESv2.dll` / `d3dcompiler_47.dll`) の置き場所。krkrz_dev の install には入らない (手動配置の DLL) ので外枠が取り込む。空なら環境変数 `KRKRZ_ANGLE_DIR`、それも無ければ krkrz_dev の `plugin64/`。見つからなければ警告して続ける |
| `saveData.location` | セーブデータの場所 (§7)。`documents` (既定) / `appdata` / `exe`。`-datapath` を作って埋め込みオプションへ足す |
| `checkTool` | 破損チェックツールの同梱 (§8.1)。`exeName` (配る名前)、`publicKey` (`krkrsign` で作った公開鍵)、任意で画面の文言 |
| `package.formats` | `dir` / `zip` / `installer` |
| `package.installer.*` | Inno Setup の設定 (§8)。`appId` は**タイトルごとに固定の GUID** (変えると別のアプリ扱いになり上書き更新できない) |

秘密の値 (Authenticode の証明書・パスワード、`.sig` の秘密鍵の場所) は JSON に書かず、環境変数で渡す (§6)。

---

## 5. WINVER 版と SDL 版

| | WINVER (`variant: "win"`) | SDL (`variant: "sdl"`) |
|---|---|---|
| 描画 | D3D11 (既定) / OpenGL ES (ANGLE) | OpenGL ES (ネイティブ ES か ANGLE) / SDL_Renderer |
| 文字 | GDI (既定) | FreeType / glyphware |
| Win32 専用プラグイン (windowEx / layerExDraw / win32dialog / addFont / win32ole / menu など) | 使える | 使えない |
| 他機種との挙動の揃い方 | Windows 独自 | Linux / macOS / 機種と同じ経路 |

**既定は SDL 版にする** (2026-10-27 決定)。Linux / Steam Deck / macOS / 機種と描画・文字・挙動をそろえるため。
WINVER 版は基本的に**従来のタイトルを続けて使うため**の選択肢で、Win32 専用プラグインや GDI の文字の見た目に
依存するタイトルが `variant: "win"` を選ぶ。

---

## 6. 署名

2 種類あり、順序が決まっている。

1. **Authenticode** (Windows の «発行元» 表示・SmartScreen 用): `signtool sign /fd sha256 /tr <timestamp> ...` で
   exe・DLL・インストーラに付ける。証明書は環境変数で渡す (`KRKRZ_SIGN_CERT` = 証明書ストアの拇印、または
   `KRKRZ_SIGN_PFX` + `KRKRZ_SIGN_PFX_PASSWORD`、`KRKRZ_SIGN_TIMESTAMP_URL`)。未設定なら `sign` は飛ばす
2. **吉里吉里の `.sig`** (改変検出。`sigcheck` プラグインで検証): exe を Authenticode で書き換えると `.sig` が
   合わなくなるので、**Authenticode の後に `krkrsign --cli sign` で作り直す** (krkrrelease の説明どおり)

順序: リリーサ (exe 書き換え・xp3) → Authenticode (exe / DLL) → `.sig` → zip / インストーラ作成 →
インストーラに Authenticode。

**exe の署名の置き場所に注意** (2026-10-27 に確認): krkrsign は «署名領域を持つ吉里吉里の exe» なら署名を
exe の中へ書き、それ以外は隣の `.sig` に書く。埋め込みの場合、署名のハッシュは PE ヘッダを含む
(オプション領域から先だけを除く) ので Authenticode でヘッダが変わると合わなくなり、逆に Authenticode の後で
埋め込むと今度は Authenticode が壊れる (両立しない)。今の本体の exe (WINVER / SDL とも) は krkrsign が隣の
`.sig` に出すので問題は起きない。将来 exe に署名を埋め込む形に戻すなら、Authenticode を使うタイトルでは
exe の署名を隣の `.sig` に出す必要がある。

---

## 7. セーブデータの場所

本体の Windows の既定は `$(exepath)\savedata` (exe の隣) だが、**書き込めない場所 (Program Files など) に
置くと保存できない**。外枠では**既定をマイドキュメントにする** (2026-10-27 決定)。

| `saveData.location` | 埋め込む `-datapath` | 向き |
|---|---|---|
| `documents` (既定) | `$(personalpath)\<folder>` | 利用者からセーブの場所が見える。zip でもインストーラでも同じ場所 |
| `appdata` | `$(appdatapath)\<folder>` | 利用者に見せたくないとき。Steam Cloud (Windows のルート `WinAppDataRoaming`) |
| `exe` | (足さない = `$(exepath)\savedata`) | 従来のタイトルとの互換 (WINVER で既存のセーブを引き継ぐ場合など) |

- **同じタイトルの zip 版とインストーラ版で場所を変えない** (乗り換えたときにセーブが消えたように見える)。
  タイトルで 1 つに決める
- `installMode: "admin"` と `location: "exe"` の組み合わせは `package` で止める (保存できない構成のため)
- `<folder>` は既定で `name`。変えたいときは `saveData.folder` (`会社名\タイトル名` のような 2 段も可)

---

## 8. インストーラ (Inno Setup)

`windows-config.json` から Inno Setup のスクリプト (`generated/installer/setup.iss`、BOM 付き UTF-8) を生成し、
`ISCC.exe` で作る (テンプレートのファイルは置かず、`tools/krkrz_windows.py` が組み立てる)。
`ISCC.exe` が見つからないときは `installer` を飛ばして警告する (zip までは作る)。

- **既定は管理者権限なしのユーザごとのインストール** (`PrivilegesRequired=lowest`、`{localappdata}\Programs\<name>`)。
  UAC の確認が出ない (2026-10-27 決定)。
  `installMode: "admin"` で Program Files への全ユーザ向けインストール、`"ask"` で利用者に選ばせる
  (`PrivilegesRequiredOverridesAllowed=dialog`)
- 画面の言語は日本語・英語 (Inno Setup 同梱の `Japanese.isl` / `Default.isl`)
- スタートメニューのショートカット、任意でデスクトップのショートカット、アンインストーラ (Windows の «アプリ» 一覧に出る)
- **アンインストールでセーブデータは消さない** (Inno Setup は自分が入れたファイルしか消さないので、既定でそうなる)
- `licenseFile` があれば使用許諾の画面を出す
- 上書きインストールで更新できる (`AppId` が同じなら同じアプリとして扱われる)

### 8.1 破損チェックツールの同梱

`.sig` を付けたタイトルでは、標準ツールの `krkrcheck` を `checkTool.exeName` の名前で同梱できる。
`krkrcheck` は «実行ファイル名.ini» から公開鍵と画面の文言を読み、自分のフォルダ以下を検証するので、
外枠は exe を改名して置き、同じ名前の `.ini` を公開鍵 (`checkTool.publicKey`) と文言から作る。

- フォルダ / zip: パッケージ直下に置く
- インストーラ: 任意のコンポーネント «ファイルの破損チェック» として入れ、スタートメニューにショートカットを作る
  (既定で選択)
- 破損チェックツール自体にも Authenticode 署名を付ける (§6)。`.sig` の対象からは外す (検証する側のため)

### 8.2 採らない形式

NSIS や WiX (MSI) は採らない。NSIS は同等のことができるが利点が少なく、MSI は企業内の一括配布向けで
ゲームの配布には重い。Store 外の MSIX は信頼された証明書が要り、AppData への書き込みが付け替えられて
セーブの場所に影響するため採らない (Store 向けは krkrz_gdk)。

---

## 9. 段階

| 段階 | 内容 |
|---|---|
| ✅ P1 | **2026-10-27 済み**: リポジトリの雛形 (README 日英・LICENSE MIT・Makefile・`tools/krkrz_windows.py`・サンプルの `windows-config.json`)。`build` / `stage` (リリーサ呼び出し・assetPack) / `package` の `dir` と `zip`。サンプルで SDL 版 x64 を確認。**確認**: サンプルを SDL 版 x64 でビルド (本体・プラグイン 26 本・標準ツール) → リリーサで `krkrz-sample.exe` (版情報・`datapath` の埋め込み) → 201 ファイルのフォルダと zip。zip を展開した場所から起動して `-demotest` 全 24 シーン ok、セーブ先がマイドキュメント\krkrz-sample になることを確認。実装中に足したもの: `runtime.angleDir` (ANGLE の取り込み)、umbrella の `cmake/KrkrzTools.cmake` に `KRKRZ_TOOLS_SOURCE_DIR` (外枠から標準ツールをビルドするため)、`tools/docgen/check_readme_en.py` の対象に krkrz_windows |
| ✅ P2 | **2026-10-27 済み**: `saveData` → `-datapath` の埋め込み (P1 で実装済み)、`variant: "win"` (WINVER)、破損チェックツールの同梱 (フォルダ / zip)。**x86 は対象から外した** (2026-10-27 決定。`arch` は x64 だけ)。**確認**: WINVER 版 x64 をビルド〜zip、展開した場所から `-demotest` 全 24 シーン ok、埋め込んだ保存場所 (マイドキュメント)。破損チェックツールを `checkTool.exeName` に改名して同梱し、そのままで全件正常 (終了コード 0)、data.xp3 を 1 バイト変えると «破損» (終了コード 1)。ついでに見つけた本体の不具合: WINVER の `-printdatapath` が日本語のパスを `?` に化けさせていた (`wprintf`) → `TVPWriteStdOutText` に揃えて修正。ほか、`PROJECT_DIR` が深いと FetchContent (HarfBuzz のテスト用ファイル) がパス長の上限で configure に失敗する (README に注意書き)。また、データを xp3 にまとめるとコアデモの webui シーンが例外で止まっていた (`web/` の候補パス `../webui/web/` が xp3 の中では «無い» ではなく例外になる) → 候補を try で調べるよう修正し、xp3 のパッケージから `-demotest` 全 24 シーン ok |
| ✅ P3 | **2026-10-27 済み**: Inno Setup のインストーラ (`package.formats` の `installer`。`generated/installer/setup.iss` を生成して ISCC)。ユーザごと・管理者・選択、日英、スタートメニュー / デスクトップのショートカット、更新インストール (`appId`)、破損チェックツールのコンポーネント。ISCC が無ければ警告して飛ばす。**確認** (Inno Setup 7、WINVER 版): 無人インストールで `%LOCALAPPDATA%\Programs\<name>` に入り、ショートカット 2 つと «アプリ» の一覧への登録、入った先で破損チェックが正常・起動、アンインストールでアプリ・ショートカット・登録が消えセーブの場所は残る |
| ✅ P4 | **2026-10-27 済み**: `sign` コマンド (Authenticode → `.sig` の作り直し、§6)。証明書は `KRKRZ_SIGN_CERT` / `KRKRZ_SIGN_PFX` (+ `_PASSWORD`)、`KRKRZ_SIGN_TIMESTAMP_URL`。信頼された署名が既にあるもの (`d3dcompiler_47.dll`) は飛ばす。インストーラにも署名。stage はハードリンクで置くので、書き換える前にリンクを切る。**確認** (openssl で作った自己署名のテスト証明書): exe・DLL・破損チェックツール・インストーラに署名が付き、install 側の exe と ANGLE の元は書き換わらない、作り直した `.sig` で破損チェックが正常、署名した exe が起動 |
| ✅ P5 | **2026-10-27 済み**: 公開ドキュメント [windows_package.md](doc/topics/core/windows_package.md) (日英)、[platform_config.md](doc/topics/core/platform_config.md) に外枠として追記、linux_package.md の «今後» を更新、mkdocs の nav |

---

## 10. 決めたこと (2026-10-27)

- [x] 既定の `variant` は **SDL 版**。WINVER は従来のタイトルを続けて使うための選択肢 (§5)
- [x] セーブデータの既定は **マイドキュメント** (`$(personalpath)`)。AppData も選べる。exe の隣は互換用 (§7)
- [x] インストーラの既定は **利用者ごとのインストール** (§8)
- [x] **Authenticode 署名を手順に含める** (証明書が無ければ飛ばす) (§6)
- [x] **破損チェックツール (`krkrcheck`) も一緒に配れる**ようにする (§8.1)
- [x] リポジトリ名 `krkrz_windows`、他の外枠と同じく public・MIT
- [x] **対象は x64 だけ**。x86 は扱わない (P2 の途中で決定)

## 11. 課題

- [ ] **arm64**: 本体に `arm64-windows(-win)` の preset はあるが、Windows arm64 の実機で確認できていない
  (`TJS_64BIT_OS` が MSVC arm64 で定義されない件も TODO.md にある)。実機が用意できたら対象に加える
- [x] **GitHub への公開**: 2026-10-27 に https://github.com/wamsoft/krkrz_windows を public で作成・push
- [ ] **まだ確かめていないこと**: 正規のコード署名証明書とタイムスタンプでの署名 (自己署名のテスト証明書だけで確認)、
  インストーラの `installMode: admin` / `ask`、上書きインストールでの更新、SDL 版でのインストーラ・署名
  (処理は変種に依らない)、`release.data.mode: bind` と署名・破損チェックの組み合わせ
