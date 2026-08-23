# Wamsoft 派生版で削除/追加された機能

このページは、Wamsoft Ltd. Partnership がメンテナンスしている派生版 ( [wamsoft/krkrz_dev](https://github.com/wamsoft/krkrz_dev) ) で、上流の吉里吉里Z / 吉里吉里2 から **削除されたレガシー機能** と **新規に追加された機能** の概要をまとめたものです。

個々の TJS API の削除については [吉里吉里Zで削除された機能](deleted.md) も参照してください。

## 削除されたレガシー機能

主に Windows レガシー API 依存やクロスプラットフォーム化の障害となる実装が置き換え・撤去されています。

| 削除されたもの | 置き換え / 現状 |
| --- | --- |
| DirectSound ( 音声出力 ) | **miniaudio** ( 全ビルド共通の音声エンジン。WASAPI 共有モード、マルチチャンネル対応 ) |
| DirectShow / EVR ベースの動画再生 ( `dsmovie` / `dslayerd` 等 ) | CPU デコード ( webm=movie-player / MPEG-1=pl_mpeg / それ以外=Media Foundation SourceReader ) + **Direct3D 11 合成**に統一 |
| krmovie のプラグイン境界 ( tp_stub / V2Link DLL 境界 ) | krmovie を **exe へ直接組み込み** ( エンジンシンボルを直接呼び出し ) |
| krflash / `.swf` ( Flash 動画 ) | 撤去 |
| Direct3D 9 / DirectDraw による表示 ( 排他フルスクリーン等 ) | **Direct3D 11 / DXGI** ( flip-model スワップチェイン、ボーダレスフルスクリーン ) |
| DirectInput ( ゲームパッド / マウス ) | ゲームパッドは **XInput**、マウスホイールは `WM_MOUSEWHEEL` ( 共有 `tTVPPadManager` によるマルチパッド対応 ) |
| TLG6 の NASM アセンブラ最適化 | C リファレンス実装 ( `tvpgl.c` )。SSE2/AVX2/NEON の SIMD 実装は別途あり |
| JPEG XR ( `.jxr` ) ローダ | 撤去 ( 代替なし ) |
| `timeBeginPeriod` / `timeGetTime` タイマ | **QueryPerformanceCounter** + 高分解能待機タイマ |
| 各種レガシー Win32 互換シム ( XP/Vista/7/8 フォールバック ) | Windows 10 以降を最小ターゲットとして直接リンク |
| Perl 製の各種生成器 ( `makestub.pl` / `gentext*.pl` 等 ) | **Python** 製生成器 ( 出力はバイト一致 ) |

### コアから削除された主な TJS クラス / API

以下は本体コアから削除され、同梱の **Krkr2Compat** や個別プラグインで補完される要素です ( 詳細は [削除された機能](deleted.md) )。

- `KAGParser` クラス → `KAGParser.dll` プラグインをリンクして利用
- `Menu` クラス → `menu.dll`
- `Console` クラス / デバッグコンソール窓 ( `Debug.console` ) → Krkr2Compat
- `Font.doUserSelect` ( フォント選択ダイアログ ) / `System.inputString` ( 1行入力 ) → Krkr2Compat
- `Layer.hint`、および `affineBlend` / `affinePile` / `blendRect` / `pileRect` / `stretchBlend` / `stretchPile` 等の obsolete メソッド → `operateAffine` / `operateRect` / `operateStretch` で TJS 再実装可能

## 新規に追加された機能

クロスプラットフォーム化 ( SDL3 ) と、GPU 描画・開発支援・音声機能の拡張が中心です。

| 追加された機能 | 概要 |
| --- | --- |
| SDL3 クロスプラットフォームビルド | Windows / Linux / macOS / Android / Emscripten(web) 対応の generic ビルド、および静的ライブラリ形態の LIB ビルド |
| OpenGL ES 描画パス | 遅延初期化される GPU 描画デバイス [OGLDrawDevice](../../reference/OGLDrawDevice.md) と、[Canvas](../../reference/Canvas.md) / [Texture](../../reference/Texture.md) / [ShaderProgram](../../reference/ShaderProgram.md) / [Offscreen](../../reference/Offscreen.md) / VertexBuffer / Matrix32 / Matrix44 等の GL クラス群 |
| GLCompositor | 非 GL 描画デバイス下でも裏で OpenGL ES オフスクリーン合成し Layer へ書き戻すクラス ( [GLCompositor](../../reference/GLCompositor.md) ) |
| Canvas トランジション描画 | `Canvas.drawTransition` による GPU ベースの画面遷移描画 |
| Elements ベースの汎用ダイアログ | JSON / Dictionary 定義のクロスプラットフォーム UI ( [Dialog](../../reference/Dialog.md) クラス。詳細は [ダイアログ](../../guide/Dialog.md) ) |
| REPL ( 対話型 TJS シェル ) | `-repl` / `-replfile` によるスクリプト評価・検証 ( [REPL](../core/repl.md) ) |
| WebServer | 組み込み HTTP + SSE サーバ ( `-replweb` )。TJS からエンドポイントを登録可能 ( [WebServer](../../reference/WebServer.md) ) |
| Agent | 入力注入・画面キャプチャ・ダイアログ操作の自動化駆動 API ( [Agent](../../reference/Agent.md) ) |
| FreeType カラー絵文字フォント | CBDT/COLR カラー絵文字のラスタライズ ( `Font.emojiMode` ) |
| フォントメタデータと遅延ロード | `fonts.json` で宣言し初回使用時に実ファイルをロード ( 実行ファイルサイズ削減 ) |
| ゲームパッド マルチパッド再設計 | 複数パッド対応 ( 論理パッド 0 = 最後に操作されたパッド )、共有 `tTVPPadManager` |
| 音声 3D 定位 ( spatializer ) | miniaudio ベースの位置/距離/ドップラー/指向性 ( [WaveSoundBuffer](../../reference/WaveSoundBuffer.md) の `use3D` 系、[SoundListener](../../reference/SoundListener.md) ) |
| リップシンク / 音声解析 API | `getSoundLevel` / `getSoundSpectrum` / `getVowel` / `getVisBuffer` |
| 3D / エフェクトプラグイン | threepp ( three.js 移植 ) / Effekseer / Live2D / GLES ヘルパ |
| Media Foundation HW 動画 | `IMFMediaEngine` によるハードウェアデコード ( mp4/wmv 既定、`-mediaengine=no` で無効 ) |
| オンスクリーンデバッグ表示 | ゲームパッド状態 ( PadOverlay )、メモリ観測、描画スレッド利用率 ( DrawStats ) |
| DPI 対応 / ボーダレスフルスクリーン / 長いパス | PerMonitorV2 DPI 認識 ( 拡大率の異なるモニタへ移動しても描画領域のピクセルサイズは維持し、枠だけ描き直す )、`\\?\` 拡張パス対応 |
| ゲーム画面の表示画角制御 ( ビューポート ) | 外側ウインドウの中に内側ゲーム画面を fit / zoom / align / offset で配置し、余白を背景色や壁紙で埋める ( [ビューポート](../core/viewport.md) ) |
| 起動ディスプレイの指定 | マルチディスプレイ環境で最初に表示するモニタを番号 / 名前で選ぶ `-display` ( [コマンドラインオプション](../../guide/CommandLine.md) ) |
| 起動時 DrawDevice の選択 | `-drawdevice` で起動時の描画デバイスを選択 ( SDL3 の既定は OpenGL ES ベースの [SDLOGLDrawDevice](../../reference/SDLOGLDrawDevice.md) )。GLES コンテキストの EGL 強制 `-forceegl` も指定可能 |
| メッセージ / 設定 UI の多言語化 | エンジンメッセージとオプション解説 ( `-userconf` ) が OS 言語 ( ja / en / chs / cht ) に追従。`-language` で明示指定 ( [コマンドラインオプション](../../guide/CommandLine.md) ) |
