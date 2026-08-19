# 課題一覧 (索引)

krkrz_dev 全体の未対応課題をここに集約する。**詳細な SSOT が別にあるものはリンクのみ**に
留め、内容を二重管理しない。

| 領域 | 詳細 SSOT |
|---|---|
| バージョン番号の扱い | [src/core/doc/Versioning.md](src/core/doc/Versioning.md) |
| 画面転送コスト (計測・読み方) | [src/core/doc/ScreenTransfer.md](src/core/doc/ScreenTransfer.md) |
| Elements (レイアウト/ダイアログ) の要修正 | [TODO-elements.md](TODO-elements.md) |
| デモ整備 | [data/ROADMAP.md](data/ROADMAP.md) |
| Window のサイズ/位置/ズーム/ビューポート仕様 | [src/core/doc/WindowGeometry.md](src/core/doc/WindowGeometry.md) |
| Layer / Bitmap / ImageFunction の統合 | [src/core/doc/ImageBufferUnification.md](src/core/doc/ImageBufferUnification.md) |
| WINVER モダン化 | [src/core/doc/ModernizationRoadmap.md](src/core/doc/ModernizationRoadmap.md) |
| 動画 (Media Foundation 移行) | [src/core/doc/MovieMFMigration.md](src/core/doc/MovieMFMigration.md) |
| リファレンスとコードの差分 | [doc/_missing.md](doc/_missing.md) (生成物。現在 0 件) |
| Claude Code スキルの配布形 (install.sh) | [tools/skills/TODO-skills.md](tools/skills/TODO-skills.md) |

対応したら項目に ✅ と対応コミットを書き、**消さずに残す** (再発防止の記録)。

---

## 予定・未着手

| 優先 | 課題 | 内容 |
|---|---|---|
| 中 | リリースのバージョン運用を確定する | 番号の供給元は一本化済み ([Versioning.md](src/core/doc/Versioning.md))。`v2.0.0` は core (krkrz.git) / umbrella (master) 双方に打鍵済み。残りは **再パッケージ時のタグ規則の確定**: core 無変更でプラグインだけ更新する場合に `v2.0.0-2` 等のサフィックスを使うか。既存タグは `1.4.0` (v 無し) と `v1.0.0` (v 有り) が混在しているので、以後は `v` 付きで統一する |
| 中 | 全生成器の Perl 撤去 → Python 統一 | 残 = syntax 後処理 5 本 と `gengl.pl` (7519 行 = 最大の山)。バイト一致の差分ゲート方式。他作業と独立に実施可 |
| 中 | 固定長パスバッファ (`MAX_PATH`) の全体点検 | `common/utils/DebugIntf.cpp:533` に `tjs_char filename[MAX_PATH]` へ `Application->ExePath()` を長さ検査なしで `TJS_strcpy` している箇所がある (`TVPTJS2StartDump`)。Windows のパスは `MAX_PATH` を超えうるので、**同種の固定長バッファ + 無検査コピーが他にどれだけあるかを全体で洗い出し**、`tjs_string` / `ttstr` 化するか長さチェックを入れる。2026-08-19 の設定ファイル調査中に発見 (この件自体は今回の変更とは無関係の既存コード) |
| 中 | DrawDevice overlay 描画口の汎用開放 | `PostRenderCallback` の tp_stub 公開 + WINVER 対応 (小) / dialog renderer の painter リスト化 (大) |
| 中 | Layer / Bitmap / ImageFunction の統合 | ImageFunction の API 二重化と、プラグインが Bitmap を扱えない問題 (Layer 参照 26 ファイル) の再整理。**方針決定済 = P1 (tp_stub 共通アクセス口) → P2 (Bitmap へメソッド追加・ImageFunction は shim 化) → P3 (プラグイン対応) → P4 で共通基底 `ImageBuffer` の要否を判断**。B案はプロトタイプ実測済み (パッチ同梱)。着手は後日。SSOT = [ImageBufferUnification.md](src/core/doc/ImageBufferUnification.md) |
| ✅ | Window ジオメトリ仕様の統一 **P1** | DestRect 算出を `TVPCalcViewportDestRect` 共通計算へ + viewport の配置 API を全バリアント公開 + WINVER 入力座標の DestRect オフセット対応。等価変換で**挙動不変を実測確認済**。SSOT = [WindowGeometry.md](src/core/doc/WindowGeometry.md) |
| ✅ | 同 **P2** | WINVER `setZoom` が `SetInnerSize(layer×zoom)` を行うようになり (旧 WIN / SDL と同じ意味論)、既定 align も両バリアント中央に統一。倍率・入力座標・フルスクリーン往復・KAG3 相当の呼び方を実測確認済 |
| ✅ | 同 **P3** (基準面を inner へ統一) | SDL の `innerWidth` 実値化 (+ min/max getter が 0 固定だったのを修正) / WINVER の min/max を inner 基準へ / WINVER `borderStyle` 変更を inner 維持へ / SDL `displayDensity` を実 DPI へ / WINVER `SetClientSize` を `AdjustWindowRectExForDpi` へ / `frameWidth`・`frameHeight` 追加。**サイズ挙動マトリクスは生成直後を除き全項目で両バリアント一致**。残る差 = キャプション付きウィンドウの Windows 由来の最小幅 (内側 ~116 論理px 未満) のみ、既知の差として記載 |
| ✅ | 同 **P4** (DPI ポリシー = inner の物理ピクセルサイズ維持) | WINVER の `WM_DPICHANGED` を「client 物理サイズ維持 + 位置だけ提案矩形へ」に変更 / SDL は `TVPSDLSetWindowPositionKeepingSize()` を新設してプログラム移動を全て経由させた。200%⇔100% 往復で inner 320x240 維持・枠だけ 26x71⇔16x39 を両バリアントで実測確認 |
| ✅ | 同 **P5** (余白塗りを全バリアントへ) | `viewportBgColor` / `setViewportWallpaper` / `clearViewportWallpaper` を全バリアントで有効化。**`iTVPDrawDevice` には載せず `iTVPViewportBackgroundHost` を新設し、対応デバイスが TJS プロパティ `viewportBackgroundHost` でポインタを公開する実行時検出方式** (動画の `videoPresenterHost` と同じ規約) にしたので、**`iTVPDrawDevice` の vtable は不変 = プラグインの再ビルド不要**。`BasicDrawDevice` に D3D11 実装 (背景色クリア + 壁紙クアッド) を追加、`OGLDrawDevice` の既存実装も開放 |
| 低 | プラグイン横断のリソース消費収集 IF | 命名規約 `getResourceUsage()` の策定から。ライセンス収集 IF と同じ枠組み |
| 低 | プラグイン向けログレベル個別 IF | `TVPLogMsg` を tp_stub に収録するだけ。important = WARNING は維持 |
| 低 | レイヤ系プラグインの Bitmap 両対応 | `Bitmap` に Layer 同名の read-only プロパティ 5 件を追加済みなので、プラグイン側の対象判定 (`IsInstanceOf`) を Layer 限定から Layer/Bitmap 両対応にしたい。事前調査済 (障害は `hasImage` の有無 / class dispatch 経路 / Layer 専用メンバの使用の 3 点)。プラグインごとに要否が分かれるので、対応する価値のあるものから個別に |
| — | ~~WINVER の `Window.setZoom` が事実上効かない~~ | 上の **P2** に統合。調査の結果、旧来の契約は「`setZoom` は倍率を覚えるだけで `inner == layer×zoom` はスクリプトが維持する」(KAG3 `YesNoDialog.tjs:51-59` が実例) であり、この不変条件が守られていれば現 WINVER も 1:1 で正しく出る。差が出るのは `setInnerSize` を伴わず `setZoom` だけ呼んだ場合。詳細 = [WindowGeometry.md](src/core/doc/WindowGeometry.md) §3 |

## 将来課題

| 優先 | 課題 | 内容 |
|---|---|---|
| 中〜高 | WaveSoundBuffer 3D 定位 API (F-1) | miniaudio の spatializer で全バリアント横断の 3D 定位 API を新設 |
| 中 | Elements を WINVER のネイティブ経路へ | 中立イベント型の導入 / manager のテキスト入力・ウィンドウ取得の seam 化 / WndProc → manager 転送 + IME / OGLDrawDevice への renderer 配線 / elements_gallery の実機確認。[data/ROADMAP.md](data/ROADMAP.md) 参照 |
| 中 | SDL ビルドの SEH 捕捉 | ゼロ除算・アクセス違反でログを残さず即死する。WINVER は translator + minidump あり |
| 低 | WINVER モダン化の残 | F-3 (入力)、HW mixer の直描画 |
| 低 | macOS (Retina) の point / pixel の使い分け | `SDL3WindowForm::GetSurfaceSize` が `SDL_GetWindowSize` (macOS では **point**) を使っているため、Retina では描画解像度が半分になる可能性がある。`SDL_GetWindowSizeInPixels` との使い分けを整理する必要あり。**未検証 (macOS 実機確認が前提)**。サイズ API の単位定義とあわせて判断する → [WindowGeometry.md](src/core/doc/WindowGeometry.md) §8 |
| 低 | generic フラグの 3 種区別 | `kirikiriz_generic` が導入当時「CS (コンシューマ) 版」の意味だったため、案件スクリプトは generic = プラグイン静的リンク前提で分岐している。PC の SDL ビルドは CS でも WINVER でもない第 3 の形態なのに区別する手段が無い。案件側スクリプトにも影響するため改定は慎重に |

## 未修正の既知バグ (回避策で運用中)

いずれもレイヤ合成系。回避規約を敷いて運用しているので実害は出ていないが、
**エンジン側のバグの可能性が高く未調査**。直したら回避規約を外せる。

| 課題 | 症状と回避 |
|---|---|
| primary レイヤ直描き / primary 直下の非全画面レイヤ | primary へ直接 `drawText` するとグリフが崩れ、primary 直下の半透明 `ltAlpha` レイヤが白帯化する。`Layer.type` を明示設定した後の `drawText` も崩れる。CPU フラグ (`-cpuavx2=no` / `-cpusimd=no`) で症状が変わるが SIMD パリティテストは全合格なので、レイヤ種別ごとの関数選択・dispatch 経路が疑わしい。DrawDevice 非依存。**回避**: 描画は必ず「primary の全画面 opaque 子レイヤ (demolib の `base`/`stage`)」以下で行う。デモ全体に適用済み (`data/demolib/readme.txt` / `data/README.md` に注意書き) |
| 非全画面の入れ子レイヤの `Layer.type` ブレンド | primary→stage→bg→sp のような**非全画面の孫レイヤ**に `Layer.type` でブレンドを設定すると、多くの型 (`ltOpaque` / `ltAlpha` / `ltMultiplicative` / `ltDodge` / `ltDarken` / `ltLighten`) でそのセルが真っ黒になる (`ltAdditive` / `ltSubtractive` / `ltScreen` は正常)。上と同じ合成器系統の別 facet の可能性。**回避**: ブレンド比較はレイヤツリー合成ではなく `Layer.operateRect` (CPU 合成) を使う。`layer_basic` デモはこの方式 |

## 低優先・保留

- MF SourceReader の WINVER YUV 対応
- web REPL の modal 転送 / 重複プラグインの削除
- Elements WINVER 展開のクリーンアップ
- ゲームパッド実機での最終確認
- glyphware: ThorVG 系のバイト共有最適化 / `fonts.json` スキーマ拡張 (✅ richtext 統合は完了 — 本体 `FontServiceIntf` をバックエンド注入し、richtext から thorvg 依存も除去)
- krkreffekseer の macOS (GLES3) 実機確認 (⏸ ビルド対応済)
- tjsDataPack のライセンス収集 IF 対応 (保留)
- リップシンクの母音判定精度向上とデモ
- Elements 遷移エフェクト Phase C (GPU present 拡張・optional)

## デモ整備

[data/ROADMAP.md](data/ROADMAP.md) 参照。未着手デモは
`sound` / `sound_3d` / `video` / `storage` / `ui_flow` /
`data_parse` / `net_demo` / `movie_alpha` / `archive_demo` / `richtext_demo` の 10 本
(多くは資材待ち。資材一覧は [data/DEMO-ASSETS.md](data/DEMO-ASSETS.md))。
資材不要のデモは全て実装済み (残りは資材待ち)。
ほかに krkrz_web のランチャ起動トークン (スラッシュ入り) 対応が残っている。
doc のデモ一覧ページ ([doc/demos.md](doc/demos.md)) と wasm 再ビルド・再ステージングは
✅ 2026-08-16 に完了 (デモを増やしたら krkrz_web を再ビルドして
`tools/stage_docs.py` で `doc/_assets/demo` を差し替えること)。

---

## 最近クローズしたもの

- ✅ 設定ファイル (`.cf` / `.cfu`) の行正規化と、デスクトップ SDL の探索規約を
  WINVER へ統一 (src/core `7dc9aed0`)
  行末の改行が値に混入していた (win32 = `fgets` で LF が残る / generic =
  `getline` で CRLF の CR が残る)。素の値の比較が静かに失敗し、値省略行は
  参照不能だった。`common/base/ConfigLine.h` で解釈直前に改行・前後の空白・BOM を
  落とすようにした。あわせて generic のデスクトップを WINVER と同じ規約にし
  (`<exe名>.cfu` > `<exe名>.cf` > `config.cf` > 埋め込み)、無効化されていた `.cfu`
  読み込みを有効化 (sdl3 の `-userconf` は書いていたのに誰も読んでいなかった)。
  sdl3 の `ExePath` が固定文字列 `"krkrz.exe"` だったのも実パス解決に修正。
  非デスクトップ (Android/iOS/wasm/組込み機) は挙動を変えていない。
  仕様 = [doc/guide/CommandLine.md](doc/guide/CommandLine.md)
- ✅ `System.screenWidth` / `screenHeight` の仕様を WINVER / SDL で揃えた
  SDL/generic は常にプライマリディスプレイを返していて、リファレンスの記述
  「メインウィンドウのあるディスプレイを対象」と食い違っていた。
  **メインウィンドウのあるディスプレイ → `-display` 指定 → プライマリ** の順で
  解決する規則に統一 (SDL = `SDL3Application::BaseDisplayID()` /
  WINVER = `TVPGetBaseMonitorInfo()`。WINVER は `desktop*` 系も同じ経路)。
  リファレンスにも `-display` 時の扱いを追記
- ✅ 起動するディスプレイの指定 `-display` (src/core `94c67f6b` / umbrella `35a9353`)
  マルチディスプレイ環境で最初に表示するモニタを番号 (1 origin) / モニタ名の
  部分一致 / `primary` で指定できる (`-display=list` で一覧をログ出力)。
  WINVER / SDL3 両対応。テスト時にメインディスプレイを占有しないための口。
  仕様 = [doc/guide/CommandLine.md](doc/guide/CommandLine.md)。
  ※落とし穴: WINVER は `TTVPWindowForm` コンストラクタ**途中**で `SetWindowPos`
  すると WM_MOVE/WM_SIZE ハンドラが未初期化の `TJSNativeInstance` を触って即死する

- ✅ 「SDL3 ビルド限定」表記の全体精査 (src/core `a9bf9de4` / umbrella 側 doc)
  memoverlay / padoverlay は「ビルド限定」ではなく**描画デバイス依存**だった
  (OGL 系 DrawDevice と SDLDrawDevice が描く / WINVER 既定の D3D11 は描かない。
  WINVER でも OGL へ切り替えれば出る)。 併せて PadOverlayGL の WINVER stub を
  撤去し、WINVER でも実パッドの名前・ボタン・軸が出るようにした。
  CommandLine.md / System リファレンス / MemoryGuide / DrawStats / PadOverlay /
  REPL ヘルプ文言 / 各 SystemImpl のコメントを修正。
  ※ `-drawdevice` `-renderer` は実装が sdl3/ のみなので「SDL3 限定」のまま、
  `-drawstatslog` は generic 実装なので「SDL3・LIB」に補正。
- ✅ WINVER 本画面転送の差分更新化 (src/core `5597496d`)
  `BasicDrawDevice` がダーティ矩形単位で `UpdateSubresource` するようになり、
  静止画面 421.9MB/秒 → 1.8MB/秒 (転送率 5.0% → 0.0%)、動きのある画面でも
  -87〜-98%。詳細 = [src/core/doc/D3D11Migration.md](src/core/doc/D3D11Migration.md) 追補節

- ✅ WINVER のモーダルウィンドウがマウス操作を受け付けない (src/core `49fdd011`)
  D3D9 → D3D11 移行の回帰。vblank 待ちをメインスレッドから VSync タイミング
  スレッドへ移動。詳細 = [src/core/doc/D3D11Migration.md](src/core/doc/D3D11Migration.md) 追補節
- ✅ SDL / generic の `Window.showModal` 実装 + generic で `onClick` が発火しない欠落
  (src/core `f6aa5900`) 詳細 = [src/core/doc/ModalWindow.md](src/core/doc/ModalWindow.md)
- ✅ モーダル表示中にタイマーが完全停止する / wake 投函失敗でタイマーが永久停止する
  / WINVER の Agent 入力がモーダルへ届かない (src/core `90698ee1`)
  詳細 = [src/core/doc/ModalWindow.md](src/core/doc/ModalWindow.md)
- ✅ Elements の複数行テキストがレイアウトで壊れる (elements `c98276e1` / src/core `c5e156fa`)
  `default_label_styler` の limits / draw を改行対応に。`text_area` の高さ (1-b) は
  報告後の修正で解決済みだったことを実機確認、dialog の `size` (1-c) は仕様どおりで
  README 記載済み、DSL の lint (1-d) は不要になった。詳細 = [TODO-elements.md](TODO-elements.md)
