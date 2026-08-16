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
- [x] 再起動なしシーン切替 (2026-07-20)。demolib に DemoShell/DemoScene を追加し、
      ベース Window を共有して各デモをシーンとして束ね、PgUp/PgDn で切替。各デモは
      scene.tjs (DemoScene) + 薄い startup.tjs (単体起動) に分離。`gallery` デモが
      **8 シーン** (sysinfo/text_font/image_ops/layer_basic/input/timer_async/
      gl_canvas/gl_particles) を統合。GL シーンは drawDevice 差し替え + ツリー透過 +
      GL 終了時のツリー再構築で対応 (shell の enableGL / GL モード)。
- [x] **トップ data/ ランチャの hub 化** (2026-07-20)。旧 `data/startup.tjs`
      (samples.tjs + process.dll で子プロセス起動 = 再起動方式) を廃し、コア 8 シーン
      + 横断 2 シーン (vector_demo/transition_demo) を **1 プロセスに集約**する
      hub-and-spoke ランチャに全面組み直し。`runDemoHub` で先頭に MenuScene を挿し、
      メニュー ⇄ 各デモを **クリック/Enter で起動・ESC でメニューへ戻る**。GL デモ
      往復・Elements パネル付きデモからの ESC 復帰 (grabFocus=false パススルー) を
      実画面キャプチャで検証済 (menu→vector→ESC→GL particles 60fps→transition 実行 A⇔B)。
      横断デモも scene.tjs + 薄い startup.tjs に分離 (単体起動と hub でシーン共有)。
- [x] **elements_gallery のシーン化** (2026-07-20)。最後まで残っていたコアデモを
      DemoScene 化し gallery/hub に統合。**コア 9 + 横断 2 = 全 11 シーン**が 1 プロセス
      集約に。atlas ページの画像参照を getFullPath→自動検索パス名参照に変更し hub でも
      解決 (実機で atlas 全ウィジェット描画確認)。メニュー見出しの「(再起動なしで
      切り替わります)」表記は削除。
- [x] **GL デモ (OGLDrawDevice) でも Elements パネルが出るよう修正** (2026-07-20)。
      主因は demolib のパネル再試行自壊バグ (shellClosePanel が pending を消す)、
      副次でエンジンの host 解決を提示中デバイス追従に改善 (core b143beaa)。GPU
      パーティクルでパネル表示+クリック操作 (粒子数変更) を実機確認。
- [x] **elements_flow (Elements 画面遷移) 追加** (2026-08-08)。Dialog フロー
      (startFlow) の画面切替エフェクト (`transitions` の `effect: fade / universal` +
      rule 画像 + vague) と退場 (exit) 演出を確認するコアデモ
      (`src/core/data/elements_flow/`)。斜めワイプ (vague 大小) / サークル
      (開閉、反転 rule) / クロスフェードの 3 系統。core gallery / data hub /
      単体起動の 3 経路に登録。実機キャプチャ検証済。
- [x] **text_glyphware シーンをシェイピング API 刷新へ追従** (2026-08-12)。
      `drawShapedText` 系改名 (旧 drawGlyphwareText) + Font オブジェクト渡しを
      反映し、`drawShapedTextArea` の矩形内折り返し (禁則/align) と
      `shapedTextCount` + count 制限の**自動再生タイプライタ** (RTL 混在文が
      論理順で 1 クラスタずつ現れる) を追加。実機キャプチャ検証済。
      ※ doc 埋め込み wasm デモ (doc/_assets/demo) への反映は krkrz_web
      再ビルドが必要 (別リポ作業)。**2026-08-16 に再ビルド・再ステージング済**。
- [x] **elements_bench (Elements 負荷計測) 追加** (2026-08-12)。
      `Dialog.renderStats` (描画パイプラインの区間計測: update/raster/
      acquire/upload/present の累積時間+回数) を新設し、更新パターン別
      シナリオ (静的/キャレット点滅/毎フレーム setVar/アニメ小/広域/複合) と
      renderCache A/B トグル付きのベンチ画面を core デモに追加
      (`src/core/data/elements_bench/`)。NX 実測・部分再描画の before/after
      確認用。実測で Windows SDL は再ラスタ時の upload (テクスチャ転送) が
      サイズ非依存 ~10ms 級で支配的と判明 (ElementsDialog.md に記録)。
- [x] doc/ にデモ一覧ページ新設 (2026-08-16)。`doc/demos.md` = ブラウザ実行 (wasm)
      埋め込み + デモ一覧。mkdocs nav に登録済。以後デモ追加ごとに更新すること
      (デモを増やしたら krkrz_web の再ビルド → `tools/stage_docs.py` で
      `doc/_assets/demo` を差し替え)
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
      発見・修正 (button の vars_on_focus が無効) → wamsoft/elements develop に取込・
      push 済み、core submodule ポインタも更新済み
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
- [x] image_ops — 画像処理 (2026-07-20)。doGrayScale/adjustGamma(明暗)/flipLR/
      flipUD/doBoxBlur/affineCopy(回転)/colorRect を 3x3 で before-after 比較。
      ※ ラベルは不透明面に濃い下地バー+白文字 (ltAlpha オーバーレイだと文字が
      薄く合成され暗背景で読めない問題を修正、layer_basic も同様に対応)
- [x] text_font — フォントと文字描画 (2026-07-20)。サイズ/装飾 (bold/italic/
      underline/strikeout)/アンチエイリアス/影/getTextWidth 計測/Font.getList 一覧。
      drawText の色 24bit 仕様の実演も含む
- [x] input — キーボード / マウス / ホイール / パッド入力の可視化 (2026-07-20)。
      VK 名+コード+修飾キー+履歴、マウス座標/ボタン/ホイール/ドラッグ軌跡、
      パッド軸 (System.padAxis*)。postInputEvent で demotest 注入
- [x] timer_async — Timer/AsyncTrigger/連続ハンドラのタイミング可視化 (2026-07-20)
- [x] pad_advanced — ゲームパッド (多パッド / 軸 / 振動) (2026-08-16)。論理番号
      (0=最後に操作したパッド / 1..N)、getPadAxis のスティック升目 + トリガバー
      可視化、VK_PAD* のイベント + getKeyState マトリクス、rumblePad (弱/強/両方
      + 時間)、padEnabled、setPadOverlay、onJoypadChange。資材不要 (実パッドは要)。
      ※ Elements パネル表示中は VK_PAD* がパネルに消費されるため、
        Dialog.registerHotKey で全ボタンを確保してバイパスさせている
        (パネルのチェックで ON/OFF を切り替えて挙動差を確認できる)
- [x] layer_tree — レイヤツリー / ヒットテスト / フォーカス (2026-08-16)。
      htMask + hitThreshold の 3 帯、htProvince (領域画像をコード生成した円)、
      onHitTest による最終判定、親の visible/enabled が子の nodeVisible/
      nodeEnabled に伝わる様子、bringToFront/bringToBack と Tab フォーカス連鎖。
      資材不要。※ hitType は htMask / htProvince の 2 値で htRect は無い
      (矩形全面は hitThreshold = 0)
- [x] window_multi — 複数ウィンドウ / モーダル / 画面情報 (2026-08-16)。
      サブウィンドウ生成、showModal のブロッキング時間計測、borderStyle /
      stayOnTop / setZoom / fullScreen、screen 解像度と displayDensity、
      System.captureScreen による PNG 保存。資材不要。
      ※ 作成中に engine 側 3 件を修正: SDL のウィンドウ位置/サイズ/枠/最前面/
      全画面/zoom が未実装だったのを実装、2 枚目の Window を閉じるとメイン画面が
      更新されなくなる GL コンテキスト問題、サブウィンドウ提示で Elements
      overlay が移設され閉じると消える問題。
      ※ WINVER の setZoom は windowed で見た目が変わらない (TODO.md に記載)
- [x] perf_stats — 転送コストとメモリ計測 (2026-08-16)。System.renderStats の
      差分で提示フレーム/転送回数/転送量/転送率を 500ms ごとに表示し、負荷
      パターン (なし / 小矩形多数 / 全面塗り / 動いた所だけ更新) で比較する。
      texUploadUsePBO の A/B、getSystemAllocatorInfo、doCompact /
      clearGraphicCache / resetMemoryPeak / setMemoryOverlay。資材不要。
      ※ 実測: 全面塗り = 転送率 92.8% に対し、動いた矩形だけ update なら 3.2%
      ※ WINVER は本画面を毎フレーム全画面転送する実装 (TODO.md に記録)
- [ ] sound — WaveSoundBuffer: 再生・ループ・ラベル・fade・pan、PhaseVocoder
      (現デモから移設)、SoundBuffer、**ゲインコントロール** (setGainQueryCallback で
      曲別 dB / CLI 全体ゲイン -opus_gain・-ogg_gain / ReplayGain -*_rg の効果を実聴。
      ゲイン用途は opus 推奨。詳細 [[project_sound_gain_extension]] / doc CommandLine.md)
- [ ] sound_3d — WaveSoundBuffer 3D 定位 (miniaudio spatializer): フライバイ/周回、
      距離減衰/ドップラー/減衰モデル。現 startup.tjs のホットキー実装を専用シーン化
      (前/後/左/右の離散位置サンプルも)。詳細は project_wavesound_3d_spatializer
- [ ] video — VideoOverlay: layer / overlay モード、シーク、ループ
- [x] softkey_ime — 文字入力 / 仮想キーボード / IME (2026-08-16)。onKeyPress で
      文字を受ける自前入力欄、Layer.imeMode + setAttentionPoint、内蔵仮想
      キーボード (Dialog.virtualKeyboard の auto/always/never と
      hasPhysicalKeyboard)、System.inputString、Clipboard。資材不要。
      ※ 作成中に SDL のクリップボードが空実装だったのを SDL3 API で実装
      ※ demolib に onKeyPress フックを追加
      ※ doc の ElementsDialog.md が ElementsDialog.virtualKeyboard と誤記
        (正しくは Dialog.virtualKeyboard) → 修正
- [ ] storage — Storages / autoPath / アーカイブ / BinaryStream / セーブデータ
      (Web では IDBFS 永続化の確認を兼ねる)
- [x] webui — ブラウザ UI (WebServer) (2026-08-16)。内蔵 HTTP + SSE サーバで
      ブラウザ側にツール UI を置く最小構成。静的配信 (serveStatic で同梱
      web/index.html)、動的エンドポイント (GET /api/state / POST /api/message /
      /api/color / /api/bump?by=N)、ゲーム → ブラウザ push (broadcast + SSE)。
      -replweb 稼働中は相乗り、単体なら 8900 で start。資材不要 (HTML 自作)。
      ※ マルチバイトの値は body で受ける (System.urldecode は Windows 拡張)
      ※ TJS の文字取り出しは s[i]。s[i,1] はカンマ式になり常に s[1] を返す
- [ ] ui_flow — Elements 画面遷移 (screens / navigator): 現 flowdemo.jsonc +
      menu/*.json を整理してタイトル→設定→ダイアログの一連フローに
- [x] system_debug — デバッグ支援 (2026-08-16)。Scripts.eval + Debug.prettyPrint
      で式をその場評価、例外オブジェクト (message / trace) を種類別に確認、
      System.exceptionHandler を差し替えて未捕捉例外を自前処理 (true を返して
      既定動作を抑止)、Debug.addLoggingHandler でエンジンのログを画面へ。
      資材不要。※ TJS2 の組込例外クラスは Exception のみ / e.trace は -debug
      起動時のみ中身が入る

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
