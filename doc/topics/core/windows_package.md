# Windows 版の配布パッケージ ( krkrz_windows )

吉里吉里Z 本体と作品のデータをまとめて、Windows 向けの配布物を作る方法です。
道具は外枠リポジトリ krkrz_windows。krkrz_linux / krkrz_android / krkrz_ios / krkrz_web と同じく、
エンジンは `KRKRZ_BASE` 経由で krkrz_dev を参照し、Windows 固有のビルドとパッケージングだけを
受け持ちます。設定項目の一覧とビルド手順は krkrz_windows の README にあります。

Microsoft Store / Xbox 向け ( msixvc ) は krkrz_gdk の担当なので、ここでは扱いません。

## 配布形式と方針

| 形式 | 主な配布先 | krkrz_windows |
|---|---|---|
| フォルダ / zip | Steam のデポ、itch.io、DLsite、自前サイト | ✅ 出力する |
| インストーラ ( Inno Setup ) | 自前サイト、パッケージ版 | ✅ 出力する ( 任意 ) |
| MSI / MSIX | — | 採らない ( MSI は企業内の一括配布向けで重い。Store 外の MSIX は信頼された証明書が要り、AppData への書き込みが付け替えられてセーブの場所に影響する ) |

Linux 版と同じく、**「そのまま動くフォルダ」を正式な成果物とし、zip とインストーラはその包み直し**
という方針です。Steam が受け取るのはフォルダそのものです。

- 対象は **x64** です ( x86 は扱いません。arm64 は実機で確かめられるまで保留 )
- 既定は **SDL 版** です。Linux / macOS / 機種と描画・文字・挙動がそろいます。Win32 専用プラグイン
  ( windowEx / layerExDraw / win32dialog など ) や GDI の文字の見た目に頼る従来のタイトルは、
  `variant: "win"` で WINVER 版を選べます
- MSVC のランタイムと vcpkg のライブラリは静的リンクなので、VC++ 再頒布パッケージは要りません

## 使い方

Visual Studio 2022 の開発者用シェル ( x64 ) から実行します。

```bat
set KRKRZ_BASE=D:\work                    & rem krkrz_dev のある親フォルダ
cd D:\work\krkrz_windows
python tools\krkrz_windows.py all         & rem サンプル ( コアデモ )
set PROJECT_DIR=D:\work\mygame
python tools\krkrz_windows.py all         & rem 自分の作品
```

`all` は `build` ( 本体・プラグイン・標準ツール ) → `stage` ( リリーサで exe を作り、パッケージフォルダを
組み立てる ) → `sign` ( 署名 ) → `package` ( zip / インストーラ ) の順に行います。出力は
`${PROJECT_DIR}/build/windows/` の下です。

- `package/<exeName>/` … そのまま動くフォルダ
- `dist/<exeName>-<version>-windows-x64.zip`
- `dist/<exeName>-<version>-windows-x64-setup.exe` ( `package.formats` に `installer` を入れたとき )

作品の定義は `${PROJECT_DIR}/windows-config.json` です。`cmake` ( プラグイン構成 ) と `assetPack`
( 資材の取り込み ) は他の外枠と同じ書式です ( [外枠リポジトリの共通設定](platform_config.md) )。

!!! note "プロジェクトフォルダは浅い場所に"
    ビルドで取得するライブラリにはテスト用の長い名前のファイルがあり、プロジェクトフォルダが深い場所だと
    Windows のパス長の上限に当たって configure が失敗します。`D:\work\mygame` のような浅い場所に置いてください。

## exe はリリーサで作る

配る exe は、標準ツールのリリーサ ( `krkrrelease` ) で作ります。外枠は `windows-config.json` の
`release` からリリーサの設定を作って呼ぶだけで、同じ処理を書き直しません。

- アイコン・版情報 ( FileVersion / ProductVersion は `version` から )・埋め込みオプション・セキュリティ設定
- データは `none` ( `assetPack` で `data/` などを置く ) / `copy` ( exe の隣に data.xp3 ) / `bind` ( exe に結合 )。
  フォルダを渡すと xp3 を作ります
- 秘密鍵を指定すると、exe と xp3 に吉里吉里の署名 ( `.sig` ) を付けます

## セーブデータの場所

本体の Windows の既定は exe の隣の `savedata` ですが、書き込めない場所 ( Program Files など ) に置くと
保存できません。外枠は `saveData` から `-datapath` を作って exe に埋め込み、**既定をマイドキュメントにします**。

| `saveData.location` | 保存場所 | 向き |
|---|---|---|
| `documents` ( 既定 ) | マイドキュメント\\`<folder>` | 利用者からセーブの場所が見える。zip でもインストーラでも同じ場所 |
| `appdata` | AppData\\Roaming\\`<folder>` | 利用者に見せたくないとき。Steam Cloud の Windows のルート `WinAppDataRoaming` |
| `exe` | exe の隣の `savedata` | 従来のタイトルとの互換用 |

- 同じタイトルの zip 版とインストーラ版で場所を変えないでください ( 乗り換えたときにセーブが消えたように見えます )
- 埋め込まれた場所は、配る exe に `-printdatapath` を付けて起動すると確かめられます
  ( WINVER 版・SDL 版とも。SDL 版は起動ログの後の最終行です )

## インストーラ

Inno Setup ( 6.3 以降。7 で確認 ) でインストーラを作ります。Inno Setup が無い環境では、インストーラだけ飛ばして
警告します ( zip までは作ります )。

- **既定は利用者ごとのインストール**です。管理者権限が要らず、UAC の確認も出ません
  ( `%LOCALAPPDATA%\Programs\<name>` )。`installMode` で全ユーザ向け ( Program Files ) や、
  インストール時に選ばせる形にもできます
- 画面は日本語・英語。スタートメニューのショートカット、任意でデスクトップのショートカット、
  アンインストーラ ( Windows の «アプリ» の一覧に出ます ) が入ります
- **アンインストールしてもセーブデータは消えません** ( Inno Setup は自分が入れたファイルしか消さないため )
- `appId` ( GUID ) が同じなら同じアプリとして扱われ、新しい版を上書きで入れて更新できます。
  **`appId` はタイトルごとに一度決めたら変えないでください**
- 全ユーザ向けのインストールと「exe の隣に保存」の組み合わせは保存できないので、外枠が止めます

## 署名とファイル破損チェック

署名は 2 種類あります。

| 署名 | 目的 | 付け方 |
|---|---|---|
| Authenticode | Windows の «発行元» の表示、SmartScreen の警告を減らす | コード署名証明書。外枠の `sign` が `signtool` で付けます。証明書は環境変数で渡します |
| 吉里吉里の `.sig` | ファイルの改変・破損の検出 ( sigcheck プラグイン、ファイル破損チェックツール ) | `krkrsign` で作った鍵。リリーサが付けます |

Authenticode は exe を書き換えるので、**Authenticode → `.sig` の作り直し**の順に行います。
外枠の `sign` がこの順序を守ります。配布元がもう署名している DLL ( `d3dcompiler_47.dll` など ) には
署名し直しません。タイムスタンプのサーバを指定しないと、証明書の期限が切れたときに署名が無効になるので、
本番では指定してください。

`.sig` を付けたタイトルは、標準ツールのファイル破損チェックツール ( `krkrcheck` ) を好きな名前に改名して
同梱できます。公開鍵と画面の文言は同じ名前の .ini に入り、利用者はツールを起動するだけで自分のフォルダの
ファイルが壊れていないかを確かめられます ( 吉里吉里2 の «ファイル破損チェックツール» と同じ使い方です )。
インストーラでは選べる部品 «ファイルの破損チェック» になります。

## 確認済みのこと ( 2026-10-27 )

- SDL 版・WINVER 版 ( x64 ) とも、サンプル ( コアデモ ) をビルドして zip まで作り、zip を展開した場所から
  `-demotest` の全 24 シーンが ok。保存場所がマイドキュメントになること
- インストーラ ( WINVER 版で確認 ): 利用者ごとのインストール、スタートメニューのショートカット、«アプリ» の一覧への登録、
  インストール先での起動と破損チェック、アンインストールでアプリが消えてセーブデータが残ること
- 破損チェックツール: そのままで «すべて正常»、data.xp3 を 1 バイト変えると «破損» になること
- 署名 ( テスト用の証明書 ): exe・DLL・破損チェックツール・インストーラに Authenticode が付き、作り直した `.sig` で
  破損チェックが正常のまま、署名した exe が起動すること

## 関連

- [外枠リポジトリの共通設定](platform_config.md) — `cmake` / `assetPack` / `${...}` 展開の書式
- [Linux 版の配布パッケージ](linux_package.md) — krkrz_linux
- [コマンドラインオプション](../../guide/CommandLine.md) — `-datapath` / `-printdatapath`
- [吉里吉里Z固有のクラッキング対策](anti_cracking.md)
