# data — プラグイン/機能サンプル集

吉里吉里Z (umbrella) の**サンプル置き場**です。各プラグインや機能の
使い方を、実際に動く最小構成で示します。今後プラグインごとにサンプルを
追加していく前提で、以下の規約で構成します。

このフォルダ自体も 1 つのプロジェクトで、直下の `startup.tjs` は
**統合デモギャラリー (hub)** です。コア機能デモ (`src/core/data/<demo>/`)
と横断デモ (`data/<demo>/`) を **1 つのプロセスに束ねて**メニュー表示し、
選んだデモへ **再起動なしで移動**、**ESC でメニューへ戻る** 構成です
(hub-and-spoke)。GL デモは切替時に DrawDevice を差し替え/復帰します。

各デモは共通基底 **`DemoScene`** (demolib) のサブクラスとして
`<demo>/scene.tjs` に実装し、hub の `data/startup.tjs` がそれらを読み込んで
1 つの `DemoShell` に集約します。各フォルダの `startup.tjs` は「そのデモ 1 つ
だけを単体起動する薄いランチャ」で、`scene.tjs` を読み込んで `runDemoShell`
に渡すだけです (単体起動と hub 起動でシーン本体を共有)。

- **コア機能デモ** — `src/core/data/<demo>/scene.tjs`。Web ビルド
  (krkrz_web) ではステージング時に `core/` として合成され、デスクトップでは
  `../src/core/data/` を直接読む。コア単体の一括ギャラリーは
  `src/core/data/gallery/` にもあります。
- **横断デモ** — `data/<demo>/scene.tjs` (複数プラグインをまたぐデモ)。

ランチャはヘッドレステストに対応しています:
`krkrz64.exe data -demotest` で全シーンを巡回して各デモの検証出力
(`@demotest:scene ...`) を行い、最後に `@demotest:ok` で終了します。

## 構成規約

- **1 サンプル = 1 サブフォルダ**。サブフォルダ自体が「実行可能な data
  ディレクトリ」になります (エンジンは data dir 直下の `startup.tjs` を
  起動スクリプトとして評価する)。
- 各サンプルフォルダの構成:
  ```
  data/<sample_name>/
    scene.tjs        … デモ本体 (DemoScene サブクラス、hub/単体で共有)
    startup.tjs      … 単体起動用の薄いランチャ (demolib+scene 読込→runDemoShell)
    readme.txt       … そのサンプルの説明・実行方法・操作 (推奨)
    image/ 等        … そのサンプル専用の資材 (必要なら)
  ```
  資材はサンプルフォルダ内に閉じて持たせ、`Storages.addAutoPath("image/")`
  等でサブディレクトリを検索パスに登録して参照します。単体起動では
  project=そのフォルダなので `"image/"` で解決でき、hub 起動 (project=data/)
  では `data/startup.tjs` がサブフォルダ込みのパス
  (`"<sample_name>/image/"`) を追加で登録します。
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
| [vector_demo](vector_demo/) | layerExVector でベクタ描画 (プリミティブ/グラデ/パス) し layerExImage で加工 (ブラー/明度/カラー化/ノイズ) | layerExVector / layerExImage / Dialog | ○ |
| [transition_demo](transition_demo/) | 標準 + extrans + extNagano のトランジションを Elements UI パネルで選択・パラメータ設定・実行 | トランジション全般 / extrans / extNagano / Dialog | ○ |

横断デモを hub に載せるには、`data/<demo>/scene.tjs` を作り、
`data/startup.tjs` の `tryScene(...)` に 1 行追加します (手順は下記)。

*(今後の追加計画・バックログは [ROADMAP.md](ROADMAP.md) を参照)*

## 新しいサンプルの追加手順

1. `data/<new_sample>/scene.tjs` を作成し、`DemoScene` を継承したシーン
   クラス (`create()` / `onDemoFrame()` / `onPanelAction()` / `onKeyDown()`
   / `onDemoTest()` 等を override) を実装する。ヘルパやグローバルは hub で
   他シーンと同一プロセスに同居するため、**グローバル名の衝突を避け**、
   定数・ヘルパはクラス内メンバにする。
2. `data/<new_sample>/startup.tjs` (単体起動用の薄いランチャ) を置く。
   demolib と `scene.tjs` を読み込み `runDemoShell([new XxxScene()], "…")`
   を呼ぶだけ (既存の `vector_demo/startup.tjs` を雛形に)。
3. 専用資材は同フォルダ内 (`image/` 等) に置き、`addAutoPath("image/")` で
   登録。hub 起動でも解決できるよう `data/startup.tjs` にサブフォルダ込みの
   `addAutoPath("<new_sample>/image/")` を追加する。
4. 依存プラグインは `create()` 内で `tryPlugin("xxx.dll")` (demolib、canLink
   ガード付き)。**無い場合はその機能をスキップ**して落ちないようにする。
5. `data/startup.tjs` の横断デモ節に
   `tryScene("<new_sample>/scene.tjs", function() { return new XxxScene(); });`
   を 1 行追加する (`Storages.isExistentStorage` で存在確認するので、
   環境によって欠けても安全)。
6. `readme.txt` に概要・実行方法・操作を記述し、この `README.md` の
   「サンプル一覧」に 1 行追加。

## 将来: プラグイン別サンプルの集約

プラグインリポジトリ側に `sample/` (scene.tjs + 資材) を持たせ、
集約スクリプトで `data/plugins/<plugin_name>/` へコピーした上で hub
(`data/startup.tjs`) の `tryScene` 群へ自動登録する構成を検討しています。

---

※ `data/` 直下の `samples.tjs` は旧来の一覧ベースランチャ (子プロセス起動)
の定義ファイルで、現行の hub からは参照していません (横断デモの一覧メモ
として当面残置)。hub 化以前の子プロセス方式ランチャは
`git log data/startup.tjs` で辿れます。
