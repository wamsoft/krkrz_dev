# data — プラグイン/機能サンプル集

吉里吉里Z (umbrella) の**サンプル置き場**です。各プラグインや機能の
使い方を、実際に動く最小構成で示します。今後プラグインごとにサンプルを
追加していく前提で、以下の規約で構成します。

このフォルダ自体も 1 つのプロジェクトで、直下の `startup.tjs` は
**サンプルランチャ** (カテゴリ付き一覧表示 + 起動) です。一覧は 2 系統を
マージして表示します:

- **コア機能デモ** — `src/core/data/samples.tjs` で定義 (各デモは
  `src/core/data/<demo>/`)。Web ビルド (krkrz_web) ではステージング時に
  `core/` として合成され、デスクトップでは `../src/core/data/` を直接読む。
- **横断デモ・サンプル** — この `samples.tjs` (手書き) と
  `samples_auto.tjs` (プラグイン別サンプルの自動集約分・生成物、予定)。

ランチャはヘッドレステストに対応しています:
`krkrz64.exe data -demotest` で一覧構築結果 (`@demotest:entry ...`) を
出力して即終了します。また `process` プラグインが link できる環境
(現状 WIN ビルドのみ) では、選択したサンプルを子プロセスとして直接
起動します (無い環境ではコマンドラインを案内)。

## 構成規約

- **1 サンプル = 1 サブフォルダ**。サブフォルダ自体が「実行可能な data
  ディレクトリ」になります (エンジンは data dir 直下の `startup.tjs` を
  起動スクリプトとして評価する)。
- 各サンプルフォルダの構成:
  ```
  data/<sample_name>/
    startup.tjs      … エントリポイント (必須)
    readme.txt       … そのサンプルの説明・実行方法・操作 (推奨)
    image/ 等        … そのサンプル専用の資材 (必要なら)
  ```
  資材はサンプルフォルダ内に閉じて持たせ、`Storages.addAutoPath("image/")`
  等でサブディレクトリを検索パスに登録して参照します (他サンプルや
  src/core/data と共有しない = 自己完結)。
- 依存プラグインは `startup.tjs` の中で `Plugins.canLink` → `Plugins.link`
  し、**無い場合はその機能をスキップ**して落ちないようにします
  (サンプルは環境依存で欠けても最低限動くのが望ましい)。
- **デモ共通ヘルパ demolib** — `src/core/data/demolib/demo_common.tjs`
  (SSOT) に DemoWindow (FPS 表示 / 説明帯 / Elements パネル自動リトライ /
  `-demotest` ヘッドレステスト) 等の共通機能があります。読み込みブロックと
  API は [src/core/data/demolib/readme.txt](../src/core/data/demolib/readme.txt)
  を参照。
- **描画は primary レイヤに直接行わない** — フルサイズの opaque 子レイヤ
  (demolib では `DemoWindow.stage`) に描きます。primary への直接 drawText と
  primary 直下の半透明 ltAlpha レイヤは、現行エンジンの既知の描画問題を
  踏みます (2026-07-20 時点)。

## 実行方法

`make install` 済みの実行ファイルに、サンプルフォルダのパスを渡します。

```
bin/<preset>/<config>/krkrz64.exe  data/<sample_name>
```

例 (umbrella ルートから):
```
bin/x64-windows/Release/krkrz64.exe  data/transition_demo
```

- プラグイン DLL は実行ファイルと同じフォルダ、または実行ファイル配下の
  `plugin64/` (32bit は `plugin/`) にあれば読まれます。`make install` した
  `bin/` 以下には各プラグインが揃います。
- Elements UI (`Dialog` クラス) を使うサンプルは **SDL3 ビルド +
  KRKRZ_USE_ELEMENTS=ON** (既定 ON) が必要です (WINVER ビルドでは Dialog
  クラスが登録されません)。→ プリセット `x64-windows` (SDL) を使用。

### Web (krkrz_web) での実行

krkrz_web を既定構成 (`KRKRZ_WEB_DATA_DIR` 未指定) でビルドすると、
この data/ 一式 + core サンプルがパックされ、ブラウザでランチャが
起動します。ランチャでサンプルを選ぶと `?sample=<name>` 付きで
リロードされ、そのフォルダがプロジェクトとして起動します
(URL で直接 `krkrz.html?sample=transition_demo` と指定も可能)。

## サンプル一覧

| サンプル | 概要 | 主な対象 | 要 SDL/Elements |
|---|---|---|---|
| core (実体は [src/core/data](../src/core/data/)) | 入力・サウンド再生 (PhaseVocoder)・セーブ・ビデオ・UI 等の一括動作確認 (レガシー、順次個別デモへ分割予定) | エンジンコア全般 | ○ |
| core/sysinfo | System / Storages の情報表示。demolib の動作確認を兼ねる | System / Storages / demolib | パネルのみ |
| [transition_demo](transition_demo/) | 標準 + extrans + extNagano のトランジションを Elements UI パネルで選択・パラメータ設定・実行 | トランジション全般 / extrans / extNagano / Dialog | ○ |

コア機能デモの追加は `src/core/data/samples.tjs` へ、横断デモの追加は
この `samples.tjs` へ (手順は下記)。

*(今後の追加計画・バックログは [ROADMAP.md](ROADMAP.md) を参照)*

## 新しいサンプルの追加手順

1. `data/<new_sample>/` を作成し、`startup.tjs` を置く。
2. 専用資材は同フォルダ内 (`image/` 等) に置き、`addAutoPath` で登録。
3. 依存プラグインは `canLink` ガード付きで `link`。
4. `readme.txt` に概要・実行方法・操作を記述。
5. `samples.tjs` にエントリ (path/title/desc) を追加
   (ランチャは startup.tjs が実在するエントリだけを表示するので、
   環境によって欠けるサンプルがあっても安全)。
6. この `README.md` の「サンプル一覧」に 1 行追加。

## 将来: プラグイン別サンプルの集約

プラグインリポジトリ側に `sample/` (startup.tjs + 資材) を持たせ、
集約スクリプトで `data/plugins/<plugin_name>/` へコピーした上で
`samples_auto.tjs` (生成物) にエントリを出力する構成を予定しています。
ランチャは `samples.tjs` に加えて `samples_auto.tjs` があれば自動で
読み込みます。

---

※ `data/` 直下の `startup.tjs` / `bg_*.png` は旧来の動作確認用スクラッチで、
サンプル集とは独立です (サンプルは各サブフォルダを data dir として起動します)。
