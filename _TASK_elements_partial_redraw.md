# 作業指示: Elements overlay 部分再描画 (ダーティ矩形化)

2026-08-12 起票。**2026-08-13 第一段実装・完了 (push 済)。**
前段の「ダーティフラグ化 (パネル単位の全か無かスキップ)」は実装・push 済み
(_TASK_elements_dirty_flag.md、elements 1dc47e6e / src/core 096793f2)。

## ✅ 実装済み (2026-08-13, elements 14d9a631 / src/core 4a0d733e)

矩形が特定できるダーティ (= view の `refresh(rect)` 経由 = 実質キャレット
点滅) を矩形限定で描き直す経路を通した。 それ以外の契機 (入力 / focus・
hover / 演出 tick / setVar) は**全面へ昇格**させて正しさを担保している。

- elements: `base_view` が refresh(rect) を device 座標で蓄積 →
  `overlay_session::render_to_buffer_partial()` が矩形クリア +
  **`view::draw_bounds` で矩形外の子要素をカリング** + ThorVG
  `Canvas::viewport` でラスタ範囲限定 → 書換矩形を返す
- core: `iTVPDialogRenderer::ReleaseBufferRect` (SDL / OGL 実装、
  既定実装は全面フォールバックなので D3D11 も安全) で部分転送。
  `Dialog.partialRedraw` (既定 true) / `renderStats.partials`
- **Windows 実測: キャレット点滅のラスタ 1 回 3505us → 1700us (-52%)**。
  効いているのは主にカリング (viewport だけだと -21%)。全面描画との
  ピクセル差は AA 境界の数 px のみ
- NX 実測: 上記シナリオ以外 (counter / anim / multi) は矩形が特定
  できないため数値不変 = **回帰なし**を確認 (下表)

## ✅ 第二段も完了 (2026-08-13, elements 45bd5362 相当)

矩形化の対象を広げた。 **setVar / vars_on_focus による要素更新**と
**focus/hover 変化**を、 該当要素の矩形だけの再描画にした。

- 変数: subscriber に「見た目が変わる要素」を持たせて通知
  (`set_var_change_notifier`)。 複数要素が変わる購読 (slider+gauge) や
  位置が変わるもの (`at_var`) は通知せず全面フォールバック
- focus/hover: 変化した新旧 id を `id_map` から引いて両方の矩形を積む
- ⚠ 要素は bounds をはみ出して描くので、 矩形は
  「bounds ∪ 自然サイズ(`limits().min`)」で求め、 変数変化は**変更前後の
  2 回**積む (縮んだときの消し残り防止)。 `view::element_bounds()` を新設
  (refresh を横取りして同期的に矩形を得る)
- 「範囲不明なら全面」を update 冒頭のヒューリスティックでやっていたのを
  やめ、 **契機側で明示的に全面ダーティを立てる**設計へ変更

**NX 実測**: counter 8747→5882us (-33%、 share 54.5%→36.9%) /
複合 8748→5873us (-33%、 54.9%→37.5%)。 Windows も -36〜38%。
全面再描画とのピクセル差なし。

## ✅ 第三段 (演出 animate) も完了 (2026-08-13, elements e38f65b8 相当)

**設計を変えて解決した**。 前回は「毎フレーム要素ツリーを走査して bounds を
求める」方式で +1.9ms/frame の純損 + 残像だったため取り下げていた。 今回は
**変換 proxy が描画時に既に受け取っている `ctx.bounds` を `xform_state` へ
控える**方式:

- `xform_state` に subject の未変換矩形 (`bl/bt/br/bb` + `bounds_valid`) を
  追加し、 `xform_base::prepare_subject` が毎フレーム記録 (コスト = 代入のみ)
- `transformed_bounds()` が「記録矩形 + 変換量」から実描画矩形を算出。
  適用順を prepare_subject と同一に保つので**原理的に残像が出ない**
- `overlay_session` は tick 前後で集めて両方をダーティに。 走査ゼロなので
  update コストは 9〜29us で据え置き (旧方式は 1923us)
- 検証: 有限アニメ (移動+拡縮+回転) 完走後の画素比較で全面再描画と**完全一致**

**NX 実測**: アニメ小 12688→9108us (78.2%→56.4%) / アニメ広域
16317→11904us (93.9%→74.5%、 **54.5fps→60fps でフレーム落ち解消**) /
counter 8747→5949us (54.5%→37.3%) / 複合 8748→5935us (54.9%→37.9%)。

### 残タスク

1. **シーンの保持 (retained 化)** — 部分再描画で「描く範囲」は絞れたが、
   範囲内の要素は毎フレーム Shape を作り直している。 変化のない要素の
   Shape を保持できれば更に下がる。 ThorVG の damage 機構 (`TVG_PARTIAL`)
   もこれとセットで初めて使える。 **ここが次の本丸**。
   (テキストについては 2026-08-13 の run ビットマップキャッシュで先行して
   解決済み = ラスタ -38%。 doc/ElementsDialog.md 参照)
2. Windows の upload 経路 (`SDL_UpdateTexture` が 12〜15ms/回、 矩形サイズ
   非依存)。 NX は 0.1〜0.8ms なので Windows 固有。
3. D3D11 (WINVER) の `ReleaseBufferRect` 実装。
4. 全画面パネルの密度上限 (`Dialog.renderScale` は authored 相対なので
   扱いにくい。 「buffer 高さの上限」型の指定を足すと docked 1080p を
   720p 相当で描けて面積比で約半分になる)。
5. NX でのキャレット部分再描画の実測 — テキスト欄 focus は
   ソフトウェアキーボードを開くため自動計測不可。 名前入力画面のような
   実画面での目視/手動計測で確認する。
   (NX の計測は `bash tools/nxctl.sh install && bash tools/nxctl.sh
   bench-inst` で無操作実行できる)

## ✅ NX 実測結果 (2026-08-13, EDEV / Release / -benchauto, generic krkrz_nx)

- renderCache は決定的に有効: idle 1 パネルで OFF=raster 29.6ms/回・fps 32・
  share 96.5% ⇔ ON=share 0.6%・60fps。
- **NX の支配項は raster (ThorVG CPU)**。upload は 0.1〜0.8ms/frame と軽い
  (Windows の upload スパイクとは逆傾向)。
- renderCache が効かない毎フレーム更新系が重い:
  counter (小パネル・数値1個) = raster 8.9ms/f・share 55% /
  anim小 12.8ms・79% / anim広域 16.4ms・**fps 54 に低下**・94% /
  複合 (3枚, cache OFF) = **fps 17**。
- → 本タスクの主眼は **ラスタの矩形限定** (NX に効く)。upload 部分化
  (ReleaseBufferRect) は Windows のスパイク対策として併記 (優先度は下)。
- 再計測手順: krkrz_nx で
  `make run PRESET=arm64-nx BUILD_TYPE=Release VCPKG_ROOT=d:/vcpkg
   NSDK_ROOT=<SDK> TARGET_ID=<devkit_id> PWD_ABS=<krkrz_nx絶対パス>
   DATA_FOLDER=krkrz/data/elements_bench
   RUNOPT="-readencoding=UTF-8 -benchauto -loglevel=info"`
  (この環境の make は env 変数を拾えないため全部コマンドライン渡し。
   結果は RunOnTarget 出力の @bench 行。TJS のみの変更なら再ビルド不要 =
   data は host マウント)。sg8bit 実画面での確認は別途。

## 発動条件 (これを満たしたら着手)

NX 実機 (krkrz_nx_sg8bit を 096793f2 + elements 1dc47e6e に追従させた状態) で
renderCache 有効でもまだ重い画面が残っている場合。特に疑わしいのは:

- タイトル入力画面: テキスト欄 focus 中はキャレット点滅で 500ms ごとに
  **パネル全面** (docked 1080p / 携帯 720p) を再ラスタライズする。
- animate ループ (明滅等の無限 yoyo) やアニメカーソルを持つ画面:
  再生中は毎フレーム全面再描画。
- HUD の数値 1 個だけが頻繁に変わる常駐パネル。

アイドル画面 (変化なし) は前段対応で既にゼロコストなので対象外。
判断材料: **`Dialog.renderStats` (2026-08-12 新設) + ベンチ画面
`src/core/data/elements_bench/`** を使う。renderStats は描画パイプラインの
区間計測 (update/raster/acquire/upload/present の累積 us + 回数、
renderStatsReset() でクリア)。ベンチ画面は更新パターン別シナリオ
(静的/キャレット点滅/毎フレーム setVar/アニメ小/広域/複合) + renderCache A/B
トグル + 500ms ごとの内訳表示を備え、NX でもそのまま動く (core データ)。
NX の重さ比較はモード固定で行うこと (docked=1080p / 携帯=720p、2.25 倍差)。

⚠ Windows SDL での実測知見 (2026-08-12, -benchauto スイープで精査):
- raster (ThorVG) は 1 回 1.6〜5.2ms (内容/サイズ依存) で安定 = 定常の支配項。
- upload (ReleaseBuffer) は **~40〜240us の組と ~15ms/frame に張り付く組が
  混在** (実行順依存・スパイク時はサイズ非依存、acquire は常に 0)。SDL
  レンダラのテクスチャ同期起因と推定、原因は要調査。
→ 部分化は「ラスタ矩形限定」(定常 raster 削減) が基本線で正しいが、
  upload スパイク対策 (ReleaseBufferRect / streaming テクスチャ二重化) も
  併せて検討。NX での傾向は -benchauto (RunOnTarget ログ回収) で実測する。

## 現状 (前段の到達点と限界)

- ダーティは overlay_session 単位の **bool 1 個**。ボタン 1 個の hover 変化でも
  そのフレームは「バッファ全クリア → ThorVG で全ウィジェット再ラスタ →
  テクスチャ全面アップロード」が走る (変化フレームのコストは従来と同じ)。
- 領域情報は**半分ある**が捨てている:
  - elements の `view::refresh(element&)` / `refresh(rect)` は要素 bounds を
    rect 付きで `base_view::refresh(rect area)` まで伝搬してくる。 前段で足した
    `base_view::take_refresh_request()` (lib/include/elements/base_view.hpp)
    は**これを bool に潰している**。
  - rect 無しの契機も多い: 引数なし `base_view::refresh()` 直呼び
    (focus 変化 / fire_shortcut 後 = view.cpp の qualified call)、
    入力イベント起因のダーティ、animator tick 起因のダーティ。
- ThorVG SW エンジンには damage/partial 機構 (`TVG_PARTIAL=ON`) があるが、
  elements canvas 層が即時モード (毎フレーム全 Shape 生成→remove、
  lib/src/support/canvas.cpp の flush_shapes) なのでフレーム間差分は取らせ
  られない。使えるのは「この矩形にクリップして描かせる」方向のみ。
  (ThorVG GlCanvas 化は調査済みで非推奨 — メモリ
  reference_thorvg_gl_feasibility 参照。本タスクは SW のまま部分化する。)

## 実装方針

「dirty rects の集約 → 矩形限定クリア + クリップ付きラスタ → 部分アップロード」。
まずは複数矩形を**合併 1 矩形**に潰す実装で開始 (十分効くはず。分割管理は次)。

1. **elements 側: ダーティを bool → 矩形蓄積に拡張**
   - `base_view`: `_refresh_requested` (bool) に加えて蓄積矩形
     (`_refresh_rect`、無効値 = 全面) を持たせ、`refresh(rect)` 実装
     (lib/host/windows/base_view.cpp / lib/host/sdl/base_view.cpp) で合併。
     引数なし `refresh()` は全面マーク。`take_refresh_request()` を
     「矩形 or 全面」を返す形に拡張 (bool 版は互換のため残してよい)。
     ※ rect は device 座標で来る (view.cpp が user_to_device してから渡す)。
   - `overlay_session`: `needs_render_` と並べて dirty 矩形 (view local
     論理座標) を蓄積。契機別:
     - view の refresh 矩形 → そのまま合併
     - 入力イベント / focus・hover 変化 / set_var 等、位置が特定できない
       契機 → **全面フォールバック** (正しさ優先。改善は後から
       「focused/hovered id の element bounds を id_map から引く」等で漸進)
     - animator: 対象要素 id を持っているので id_map から bounds を引けるが、
       xform (move/scale/rotate) は**変換前と変換後の合併矩形**が必要。
       tick 前後の xform_state から算出するか、初期実装では
       「anim がアクティブな間は全面」でもよい (キャレット点滅の主目的には
       効かないが、実装を段階化できる)。
     - キャレット点滅: view.cpp / text.cpp の caret timer は
       `refresh(caret_bounds)` を rect 付きで呼んでいる (text.cpp の
       draw_caret → view.post(500ms, ... refresh(caret_bounds)))。
       → 経路 1 で自然に矩形が取れる。**本命ユースケース**。
   - `render_to_buffer` (または新 API `render_to_buffer_partial`):
     dirty 矩形 (全面でなければ) を受けて
     - クリアを矩形内に限定 (`std::fill_n` → 行ループの矩形 fill)
     - ThorVG に矩形クリップを掛けて draw (canvas 層にクリップ矩形を渡す
       口を追加: cnv.clip() / tvg の Canvas::viewport() 相当。
       canvas.cpp / view::draw の dirty 版。elements の view::draw(canvas&)
       は ctx 全体を描くので、クリップはラスタ側で効かせるのが素直)
     - out_rect / last_rect の計算は従来どおり (配置は不変)
     - 呼出側へ「今回書き換えた buffer 内矩形 (ピクセル座標)」を返す
2. **core 側 (ElementsDialogManager / レンダラ): 部分アップロード**
   - dirty 矩形は view 論理座標 → buffer ピクセル座標へ density
     (= buffer_w / view_w) を掛けて変換。丸めは外側に 1px 膨らませる。
   - `iTVPDialogRenderer` に部分アップロード API を追加
     (例 `ReleaseBufferRect(layer, x, y, w, h)`。既存 ReleaseBuffer は
     全面版として残し、未対応レンダラのフォールバックにする):
     - SDL: `SDL_UpdateTexture(tex, &rect, staging+offset, pitch)` —
       staging は全面保持のままなので pitch = w*4 でポインタをずらすだけ。
     - OGL: `GLTexture::UpdateTexture(x, y, w, h, writer)` が
       **既に部分矩形対応** (OGLDialogRenderer.cpp の全面転送を矩形化)。
     - D3D11: presenter (tTVPVideoPresenterD3D::Render) が present 時に
       staging **全面**を DYNAMIC テクスチャへ書く作り。部分化するには
       presenter にテクスチャ保持 + 部分 UpdateSubresource の口が要る
       (WINVER のみ。NX に関係ないので**後回しでよい**。当面は D3D11 だけ
       全面アップロード継続で正しさは保たれる)。
3. **遷移スナップ (last_frame) との整合**
   - nav フローの last_frame 複製は「buffer = 常に完全な最新絵」前提。
     部分更新は in-place なのでこの前提は保たれるが、**クリアを矩形限定に
     する変更を全面描画パスに波及させない**こと (全面描画時は従来どおり
     全クリア)。last_frame の複製コスト自体も大きい (全面 memcpy /
     毎フレーム) ので、部分更新時は「dirty 矩形だけ last_frame へも複製」
     にすると一石二鳥。
4. **切替フラグ**: `Dialog.renderCache` と同様に逃げ道を用意
   (例 `Dialog.partialRedraw = true/false`、既定 true)。renderCount と並べて
   「部分更新だった回数 / 全面だった回数」のカウンタがあると A/B が楽。

### 注意点 (ハマりそうなところ)

- ThorVG のクリップ描画で**クリップ境界の AA 継ぎ目**が出ないか要確認
  (境界 1px を膨らませて重ね描きすれば消えるはず)。
- oversized present (authored > surface) では buffer が縮小密度。矩形変換の
  丸め落ちで 1px 欠けが出やすい — 必ず外側丸め。
- 半透明パネル (background alpha < 255) は「クリア → 再描画」を矩形内で
  完結させないと二重合成で濃くなる。矩形内は必ず 0 クリアしてから描く。
- `refresh(rect)` の device 座標は view の scale (canvas scale) 適用後。
  render_scale (buffer/view_w 導出) と同じ空間かは実装時に要確認
  (embedded では scale=1 の view local のはず)。
- 複数インスタンス: dirty 矩形は per-instance (session が持つので自然に分離)。

## 検証

1. Windows SDL で elements_gallery の入力タブ (キャレット点滅) を表示し、
   部分更新時のアップロード矩形がキャレット周辺のみになることをログで確認。
   点滅で絵が壊れない (継ぎ目 / 残像なし) ことを captureScreen で目視。
2. sg8bit SYSMENU / CONFIG / LOAD で従来どおりの描画・操作
   (前段タスクの検証手順を流用。ゲームを汎用 exe で動かす手順・落とし穴は
   メモリ project_elements_dirty_flag 参照:
   -nostartup + 手動 Plugins.link + ui/_skiplauncher、SYSMENU は
   global.openSysMenu()、クラス名は ElementsDialog)。
3. `Dialog.renderCache` on/off × partialRedraw on/off の 4 通りで表示一致。
4. NX 実機: タイトル入力画面のフレーム時間を前段 (全面再描画) と比較。

## リポ運用 (前段と同じ)

- elements は d:/test/elements (develop) で編集 → push → submodule pull。
  submodule 内で直接コミットしない。ビルドで submodule がリセットされる
  ことがあるので、elements push + core ポインタコミットは必ずセットで。
- core (krkrz_develop, ブランチ master) → krkrz_dev ポインタ更新の順。
- D3D11 部分アップロードを後回しにした場合は TODO をコード内コメントでなく
  このファイル (または後続メモ) に残すこと。
