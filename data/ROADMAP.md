# デモ整備ロードマップ

吉里吉里Z の諸機能を「動くコード + ドキュメント」で確認できるデモ群を、
少しずつ追加して最終的に広範囲をカバーすることを目指す長期計画。

- 進め方: **1 イテレーション = 1〜2 デモ** (実装 → 実機確認 → doc 反映 → commit)。
  バックログは「候補」であり、最初に全部作らない。よさそうなものから順次着手し、
  完了したらこのファイルのチェックを更新する。
- UI 操作系は全体的に **Elements (Dialog クラス)** を利用する (SDL ビルド前提)。
  Elements が無い環境 (WINVER 等) ではパネル無しでも最低限動くようにする。
- **WIN 専用機能系 (menu / win32dialog / windowEx / layerExDraw / win32ole 等) は後回し**。

## 全体アーキテクチャ (3 層 + 束ね機構)

```
① src/core/data/<demo>/        … エンジンコア機能のデモ (core submodule 内)
② src/plugins/<name>/sample/   … 個別プラグインで完結するデモ (各 plugin submodule 内)
③ data/<demo>/                 … 複数プラグイン横断・組み合わせデモ (umbrella 直置き)
                                  例: transition_demo (標準 + extrans + extNagano)
```

これらを `data/startup.tjs` の**サンプルランチャ**が一覧に束ねる:

- ③ は従来どおり `data/samples.tjs` に手書きエントリ。
- ① は core 側に `src/core/data/samples.tjs` を持たせ、ランチャがマージ読込。
  Web (krkrz_web) では `core/` として合成済みなのでそのまま起動可。
- ② は集約スクリプト (`tools/collect_samples.py` 予定) が
  `data/plugins/<name>/` へコピーし `samples_auto.tjs` (生成物) を出力。
  → data/README.md「将来: プラグイン別サンプルの集約」の具体化。
- デスクトップでの起動: `process` プラグインが link できる場合は
  ランチャから krkrz(64).exe を子プロセス起動 (無ければ従来どおりコマンドライン案内)。

### デモ共通規約

data/README.md の構成規約 (1 サンプル = 1 フォルダ、startup.tjs 必須、
readme.txt 推奨、資材自己完結、canLink ガード) に加えて:

- 共通ヘルパ `data/demolib/demo_common.tjs` (①〜③ で共有できるようコピー配布):
  ウィンドウ生成、FPS 表示、Elements 操作パネルの組み立て補助、説明オーバーレイ。
- readme.txt に「対応する doc/reference/*.md」へのポインタを書き、
  doc/ 側 (mkdocs) にはデモ一覧ページを設けて相互リンクする。

## 束ね機構の整備タスク

- [x] core 用 `samples.tjs` 新設 (src/core/data、It.1 2026-07-20)。現 startup.tjs は
      「レガシー一括テスト」として残し、個別デモを作るたびに機能を吸収して
      最終的に置換する方式 (path:"." エントリで一覧に出る)
- [x] umbrella ランチャの core samples.tjs マージ読込 + カテゴリ表示・スクロール +
      `-demotest` ヘッドレステスト対応 (It.1)
- [x] デスクトップ起動: process プラグイン利用の子プロセス起動 (canLink ガード、It.1)。
      ※ process は現状 WIN ビルドのみのため実動作は WINVER 環境で要確認
- [x] `demolib/` 共通ヘルパ整備 (It.1)。SSOT は `src/core/data/demolib/`
      (core 単体でも自己完結)。umbrella 側からは相対パス探索で読む
      (方式は demolib/readme.txt)。**描画は DemoWindow.stage に行う規約**
      (primary 直描き / primary 直下 ltAlpha はエンジン既知問題を踏む)
- [ ] `tools/collect_samples.py` + `make samples`: plugin `sample/` 集約 → `samples_auto.tjs` 生成
- [ ] doc/ にデモ一覧ページ (topics/samples.md 等) 新設、以後デモ追加ごとに更新
- [ ] krkrz_web: ランチャの起動トークンが `core/<demo>` 形式 (スラッシュ入り) に
      なったため、pre.js の ?sample= 対応を krkrz_web 側で確認 (別リポ作業)

## 独立タスク: Elements の非 SDL プラットフォーム対応 (WINVER 含む)

デモ本体とは独立の基盤タスク。WINVER はフェードアウト予定だが当面使い続ける
ため、Elements (Dialog クラス) を WINVER でも利用可能にする。作業は
「WINVER 対応」ではなく **SDL 依存の剥がし**として行う — LIB ビルド等の
非 SDL プラットフォーム全般に効く投資と位置づける。

現状の SDL 癒着点 (調査済 2026-07-20、重い部分 = overlay_session /
iTVPDialogRenderer / OGLDialogRenderer は既に中立):

1. elements_modal のイベント型 (`SDL_BUTTON_*` / `SDL_KMOD_*` 変換) と
   `ELEMENTS_HOST_UI_LIBRARY=sdl` の CMake gating
2. ElementsDialogManager.cpp の SDL_StartTextInput / スクリーンキーボード /
   メイン SDL_Window 取得
3. イベント供給 (sdl3/environ/form.cpp → manager 転送) の WndProc 版
4. モーダル nested pump (SDLElementsModalRunner) の Win32 版
5. 独立ウィンドウ型 `run_modal` は SDL 専用のまま (オーバーレイ経路のみ対応)

- [ ] elements_modal: 中立イベント型導入 + SDL gating 解除 (wamsoft/elements fork 作業)
- [ ] ElementsDialogManager: テキスト入力/ウィンドウ取得を seam 化
- [ ] WINVER: WndProc → manager イベント転送 + IME 接続 + nested pump
- [ ] WINVER: OGLDrawDevice への OGLDialogRenderer 配線 (Elements 使用時は
      OGL デバイス前提と割り切る。BasicDrawDevice (D3D) 用 renderer は作らない)
- [ ] 実機確認: WINVER ビルドで elements_gallery デモが動くこと (完成後の検証を兼ねる)

## デモバックログ (候補カタログ)

「☆」= 優先着手候補。完了したら `[x]` にして一覧 (data/README.md) にも反映。

### ① コア機能 (src/core/data)

- [x] sysinfo — System / Storages の情報表示 (demolib 動作確認を兼ねる最小デモ、It.1)
- [x] elements_gallery — Elements 主要パーツ一覧 (It.2、2026-07-20)。7 ページ
      (基本/値入力/選択/レイアウト/atlas/アニメ/vars) を segmented_picker で切替、
      各ページの定義ソース (TJS Dictionary) を右パネルに併記 (表示=実物、pages.tjs の
      行配列を eval して使用)、onAction イベントログ付き。レイアウトは Dialog.showDict。
      atlas 素材は自作 (gen_assets.tjs で生成)。※ 実装中に elements fork のバグを 1 件
      発見・修正 (button の vars_on_focus が無効 → wamsoft/elements ブランチ
      fix/button-vars-on-focus。core submodule ポインタ更新は要レビュー)
- [x] gl_canvas — OpenGL 基礎 (It.3、2026-07-20)。5 ページ: drawTexture+Matrix32 /
      ShaderProgram (波打ちフラグメント) / Offscreen RTT / ポストエフェクト /
      マスククリップ。素材自作 (gen_assets)。※ カスタム頂点シェーダは a_size +
      ortho 射影が必須 (drawTexture 規約)
      krkrgles 由来の**ポストエフェクト機構は Canvas へ取り込み済み**
      (core 8823a9e2、2026-07-20: beginEffect/endEffect + コマンド列
      gamma/light/lut/grayscale/colorize/modulate/noise/overcolor/
      boxBlur/gaussianBlur、マスク/ステンシルクリップ、doc/CanvasEffect.md)。
      **エフェクト + クリッピングのデモページを含めて作る**
- [x] gl_particles — ステートレス GPU パーティクル (It.3、2026-07-20)。VertexBuffer +
      ポイントスプライトシェーダで数万粒子 (50000 で ~55fps)、加算/通常ブレンド、
      3 エミッタ (噴水/放射/上昇)、Elements パネル + FPS 表示。位置はシェーダが
      時刻からパラメトリック計算 (CPU 更新なし)
- [x] layer_basic — 合成モードと不透明度 (2026-07-20)。operateRect で 9 種の
      合成モード (omOpaque/omAlpha/omAdditive/omSubtractive/omMultiplicative/
      omScreen/omDodge/omDarken/omLighten) を比較、opacity パネル操作。
      ※ 非全画面入れ子レイヤの Layer.type ブレンドが黒くなる挙動を発見
      (回避=operateRect、engine-layer-tree-nested-blend-black メモに記録)
- [ ] image_ops — Bitmap / ImageFunction: adjustGamma・グレースケール・フリップ・
      アフィン copy・saveLayerImage、ピクセル直接操作 (bufferPointer)
- [ ] text_font — Font 列挙・サイズ/装飾・getTextWidth・縦書き・アンチエイリアス比較
- [ ] input — キーボード / マウス / ホイール / タッチ / パッド入力の可視化
      (現 startup.tjs のキーコード表示を発展させて移設)
- [ ] timer_async — Timer / AsyncTrigger / onContinuous のタイミング可視化
- [ ] sound — WaveSoundBuffer: 再生・ループ・ラベル・fade・pan、PhaseVocoder
      (現デモから移設)、SoundBuffer
- [ ] video — VideoOverlay: layer / overlay モード、シーク、ループ
- [ ] storage — Storages / autoPath / アーカイブ / BinaryStream / セーブデータ
      (Web では IDBFS 永続化の確認を兼ねる)
- [ ] ui_flow — Elements 画面遷移 (screens / navigator): 現 flowdemo.jsonc +
      menu/*.json を整理してタイトル→設定→ダイアログの一連フローに
- [ ] system_debug — System 情報 / Debug.console / Scripts.eval / 例外ハンドラ挙動

### ③ 横断デモ (data/、複数プラグイン組み合わせ)

- [x] transition_demo — 標準 + extrans + extNagano トランジション (完成済)
- [x] vector_demo — layerExVector (GdiPlus 互換 API) 横断デモ (It.4、2026-07-20)。
      プリミティブ/グラデ/パス/回転のギャラリー、Elements パネルで線幅/回転/
      グラデ色相/画像効果を操作。layerExImage との組み合わせ (描画結果への
      ブラー/明度/カラー化/ノイズ) を実装。アウトライン文字はフォント未同梱で
      任意 (font/ に .ttf があれば表示)
- [ ] data_parse — json + csvParser + lineParser: データ駆動でシナリオ/表を読み
      画面構築、saveStruct での書き戻し
- [ ] net_demo — httprequest + json: Web API 取得→パース→表示 (Web ビルドでは
      fetch 制約の注意書きを readme に)
- [ ] movie_alpha — AlphaMovie + VideoOverlay: アルファ付き動画を背景+キャラ合成で
- [ ] archive_demo — minizip(Unzip/Zip) + fstat + varfile: アーカイブ読み書き・列挙
- [ ] richtext_demo — krkr_richtext: リッチテキスト組版 + Elements スクロール
- [ ] gl_plugin_mix — gl_particles + layerExVector で「ベクタ描画したスプライトを
      Canvas で大量アニメーション」(①GL 系と ③ベクタ系が揃ってから)
- [ ] kag_mini — KAG3 最小シナリオ (script/KAG3 の動作確認を兼ねる)

### ② 個別プラグイン sample/ (各 plugin repo 内)

集約機構 (collect_samples) が入ってから順次。既存資材の流用元:

- [ ] layerExVector — 既存 data/ (startup.tjs + フォント) を sample/ 規約へ整理
- [ ] gamepad / fpslimit / scriptsEx / shrinkCopy / layerExAreaAverage /
      layerExLongExposure / layerExRaster / layerExBTOA … (小粒なものから)
- [ ] psdfile / psbfile 系は資材ライセンスに注意 (同梱可能な素材を自作する)

### WIN 専用 (後回し)

- [ ] menu / windowEx / win32dialog / layerExDraw / addFont / win32ole —
      SDL 側の代替が固まってから、または要望が出た時点で

## イテレーション計画 (直近)

| It. | 内容 | 主な作業場所 |
|---|---|---|
| 1 ✅ | 基盤: core samples.tjs マージ + demolib + sysinfo デモ + ランチャ改良 (スクロール/カテゴリ/process 起動/-demotest) — 2026-07-20 完了 | src/core (submodule) + data/ |
| 2 ✅ | elements_gallery (Elements 主要パーツ一覧、7 ページ) — 2026-07-20 完了 | src/core/data |
| 3a ✅ | gl_canvas (OpenGL/Canvas 基礎 + エフェクト/クリップ、5 ページ) — 2026-07-20 完了 | src/core/data |
| 3b ✅ | gl_particles (ステートレス GPU パーティクル、50000 粒子) — 2026-07-20 完了 | src/core/data |
| 4 ✅ | vector_demo (layerExVector + layerExImage 横断) — 2026-07-20 完了 | data/ |
| 5 | collect_samples 集約機構 + doc/ デモ一覧ページ | tools/ + doc/ |
| 6〜 | バックログから順次選択 (layer_basic / sound / storage / data_parse …) | — |

※ It.1 の core 側変更は src/core submodule へのコミットになる点に注意
(krkrz_develop.git)。Web (krkrz_web) のステージングは `core/` 合成が
フォルダ構成変更に追従できるか It.1 で確認する。
