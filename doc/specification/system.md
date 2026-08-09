# システム構成

吉里吉里Z (Wamsoft 派生実装) のシステム構成について記載します。

## 概要

現行の吉里吉里Z には、大きく分けて 2 つのビルド系統があります。

- **WINVER** — Windows ネイティブ実装。描画は Direct3D 11、ウィンドウ/入力は Win32 API を用います。Windows 上での実行に特化した系統です。
- **SDL(GENERIC)** — SDL3 を基盤としたクロスプラットフォーム実装で、こちらが既定の系統です。ウィンドウ/入力/表示を SDL3 に委ね、描画は OpenGL ES を基本とします。Windows / Linux / macOS / Android / Emscripten(web) を対象とします。

このほか、GENERIC 系統を静的ライブラリとしてまとめた **LIB** 形態があります。実行ファイルではなくライブラリとして他のアプリケーションへ組み込むための構成で、内部コンポーネントは SDL(GENERIC) と共通です。

いずれの系統も、TJS2 言語ランタイム・レイヤ/Bitmap の画像処理・OpenGL 描画クラス群・miniaudio 音声・プラグイン ABI といった中核部分を共有しており、系統の違いは主にウィンドウ/描画/入力/動画/音声の各プラットフォーム結合部分に現れます。

## WINVER の主要コンポーネント

| 機能 | 実装 | 備考 |
| --- | --- | --- |
| 描画/表示 | Direct3D 11 / DXGI (BasicDrawDevice) | 既定の描画デバイス。flip-model スワップチェインを用います (`d3d11` / `dxgi` / `d3dcompiler`)。 |
| ウィンドウ/入力 | Win32 API | ウィンドウ生成・メッセージ処理・キーボード/マウス入力。 |
| ゲームパッド | XInput | 旧 DirectInput 実装は廃止されています。 |
| 動画 | Media Foundation ほか | Media Foundation SourceReader + IMFMediaEngine による HW デコード、webm は movie-player、MPEG-1 は pl_mpeg。krmovie は exe に直結され、旧 DirectShow/EVR/プラグイン境界は撤去されています。 |
| 音声 | miniaudio (WASAPI) | miniaudio が出力デバイスを所有します。旧 DirectSound 実装は撤去されています。 |
| OpenGL ES パス (任意) | ANGLE / EGL | `libEGL.dll` / `libGLESv2.dll`。drawDevice を OpenGL 系へ切り替えた場合に用いられます。 |

## SDL(GENERIC) の主要コンポーネント

| 機能 | 実装 | 備考 |
| --- | --- | --- |
| ウィンドウ/入力/表示 | SDL3 | ウィンドウ生成・入力・タイミングなどを担います。 |
| 描画デバイス | OpenGL ES ベース (SDLOGLDrawDevice) / SDL_Renderer ベース (SDLDrawDevice) | 既定は OpenGL ES ベースの SDLOGLDrawDevice。SDL_Renderer ベースの SDLDrawDevice も選択できます。 |
| OpenGL ES | glad + プラットフォームの GLES/EGL | Windows 上では ANGLE へ透過的にフォールバックします。 |
| 動画 | movie-player(webm) + pl_mpeg(MPEG-1) | Emscripten(web) ではブラウザの `<video>` を用いる WebMoviePlayer になります。 |
| 音声 | miniaudio (no-device モード) | miniaudio はデバイス I/O 無効モードで PCM を生成し、出力デバイスは SDL3 が所有します。 |

対応プラットフォームは Windows / Linux / macOS / Android / Emscripten(web) です。

## 共有コンポーネント

両系統は以下のコンポーネントを共有します。

- **TJS2 言語ランタイム** (`common/tjs2`) — スクリプト言語 TJS2 のコンパイラ/実行系。
- **レイヤ/Bitmap 画像処理** — CPU 側 32bpp BGRA の合成面に対するブレンド/リサンプル等。SIMD 実装 (SSE2 / AVX2 / NEON) と C リファレンス実装 (`tvpgl.c`) を持ちます。
- **OGLDrawDevice と GL クラス群** — Canvas / Texture / ShaderProgram / Offscreen などの OpenGL ES 描画クラス群。両系統で同じ GL コードを共有します。
- **miniaudio 音声** — 全ビルドで単一の音声エンジンとして用いられます。
- **プラグイン ABI** — `tp_stub` を介したプラグインとのバイナリインタフェース。

## 起動時の既定描画デバイス

| 系統 | 起動時の既定描画デバイス |
| --- | --- |
| WINVER | BasicDrawDevice (Direct3D 11) |
| SDL(GENERIC) | OpenGL ES ベース (SDLOGLDrawDevice) |

OGLDrawDevice は、TJS スクリプトから `drawDevice` を切り替えた時点で遅延初期化されます。どちらの系統でも同じ GL 描画コードを共有するため、切り替え後の挙動は共通です。
