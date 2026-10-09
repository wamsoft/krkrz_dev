# GPUDrawDevice

GPUDrawDevice クラスは、このインスタンスを [Window.drawDevice](Window.md#drawdevice) に登録して使用するための DrawDevice で、SDL3 の GPU API ( SDL_GPU ) を用いて [Canvas](Canvas.md) 系クラスを動かします。**開発中の機能** で、Canvas を SDL_GPU で動かすビルド ( CMake オプション `KRKRZ_CANVAS_GPU=ON`、SDL3 ビルドのみ・OpenGL 版とは排他 ) にだけ含まれます。

このビルドでは起動時の既定 DrawDevice がこのクラスになります ( `-drawdevice=gpu`。`-drawdevice=sdl` で [SDLDrawDevice](SDLDrawDevice.md) に戻せます。 [コマンドラインオプション](../guide/CommandLine.md) )。SDL_GPU のドライバは自動選択で、`-gpudriver` で明示できます ( Windows では SPIR-V を受け付ける `vulkan` が選ばれます )。

OpenGL 版の無いビルドでは、このクラスは `Window.OGLDrawDevice` の名前でも登録されます。[OGLDrawDevice](OGLDrawDevice.md) を使う既存のスクリプト ( 派生クラスの `super.OGLDrawDevice()` を含む ) は、そのままこのクラスで動きます。

このデバイスがアクティブな間、[Canvas](Canvas.md) / [Texture](Texture.md) / [ShaderProgram](ShaderProgram.md) / [Offscreen](Offscreen.md) / [Matrix32](Matrix32.md) / [VertexBuffer](VertexBuffer.md) / [VertexBinder](VertexBinder.md) が SDL_GPU の上で機能します。OpenGL ES 版との主な違いは次のとおりです。

- シェーダーは実行時にコンパイルせず、事前に変換したパック ( `canvas_shaders.kzgs` ) から引きます。パックに無いシェーダーを使うと例外になります ( `-gpushadercollect` で書き出して変換します。`-gpushaderpack` でパックを指定できます )
- ポストエフェクト ( beginEffect / endEffect )・マスクやステンシルによるクリッピング・drawText・GLCompositor・TextureLayerTreeOwner・動画テクスチャは未対応です
- [Texture.nativeHandle](Texture.md#nativehandle) は GL のテクスチャ番号ではなく、SDL_GPU のテクスチャになります
- [matrix](OGLDrawDevice.md#matrix) / [glVideoPresenterHost](OGLDrawDevice.md#glvideopresenterhost) プロパティはありません

画面への出し方は [SDLDrawDevice](SDLDrawDevice.md) と同じで、SDL_Renderer を Canvas と同じ GPU デバイスの上で動かし、Canvas が描いた画面をプライマリレイヤーの画像と同じ矩形へ出します。Canvas の座標系はプライマリレイヤーと同じ大きさです。

## メンバー一覧

### コンストラクタ

- [GPUDrawDevice](#gpudrawdevice)

### プロパティ

- [interface](#interface)
- [window](#window)
- [canvas](#canvas)
- [texture](#texture)
- [sdlVideoPresenterHost](#sdlvideopresenterhost)
- [dialogRendererHost](#dialogrendererhost)
- [viewportBackgroundHost](#viewportbackgroundhost)

### メソッド

- [recreate](#recreate)
- [createCanvas](#createcanvas)
- [resumeOnDraw](#resumeondraw)

### イベント

- [onInit](#oninit)
- [onDone](#ondone)
- [onDraw](#ondraw)

---

### GPUDrawDevice

コンストラクタ

**解説**

GPUDrawDevice オブジェクトの構築

GPUDrawDevice クラスのオブジェクトを構築します。

このクラスが起動時の既定の場合、Window.drawDevice には最初からこのクラスのインスタンスが登録されているので、新たに登録する必要はありません。Canvas を使うには [createCanvas](#createcanvas) を呼びます。

---

### interface

プロパティ \ アクセス: `r`

**解説**

インターフェースオブジェクトを取得

プラグインなどで DrawDevice オブジェクトを利用するためにあります。

---

### window

プロパティ \ アクセス: `r`

**解説**

関連付けられた Window オブジェクトを取得

この DrawDevice をセットしている Window オブジェクトを返します。

---

### canvas

プロパティ \ アクセス: `r`

**解説**

描画用 Canvas オブジェクトを取得

このデバイスが管理している [Canvas](Canvas.md) オブジェクトを返します。
onDraw 内などからアクセスして描画コマンドを発行します。

---

### texture

プロパティ \ アクセス: `r`

**解説**

プライマリレイヤーのテクスチャを取得

プライマリレイヤーの画像を保持している [Texture](Texture.md) オブジェクトを返します。
onDraw 内で Canvas に描くことで、レイヤーの画面を Canvas の描画に取り込めます。

---

### sdlVideoPresenterHost

プロパティ \ アクセス: `r`

**解説**

オーバーレイ動画 presenter 登録口 (ポインタ値)

オーバーレイ動画側がこのデバイスへ pull 型で合成するために読み取る presenter host
へのポインタ値です ( [SDLDrawDevice.sdlVideoPresenterHost](SDLDrawDevice.md#sdlvideopresenterhost) と同じ規約 )。
通常はエンジン内部/プラグインが使用します。

---

### dialogRendererHost

プロパティ \ アクセス: `r`

**解説**

Elements ダイアログ renderer host (ポインタ値)

Elements のオーバーレイ描画アダプタを取得するための host へのポインタ値です。
通常はエンジン内部/プラグインが使用します。

---

### viewportBackgroundHost

プロパティ \ アクセス: `r`

**解説**

ビューポート余白塗り登録口 (ポインタ値)

ゲーム画面が描画領域全体を覆わないときの余白 ( [Window.viewportBgColor](Window.md#viewportbgcolor) /
[Window.setViewportWallpaper](Window.md#setviewportwallpaper) ) を受け取る
`iTVPViewportBackgroundHost` へのポインタ値です。 通常はエンジン内部/プラグインが使用します。

---

### recreate

メソッド

**解説**

内部デバイス再生成

[OGLDrawDevice](OGLDrawDevice.md) との互換のためにあります。このクラスでは何もしません。

---

### createCanvas

メソッド

**解説**

Canvas オブジェクトを生成

このデバイスに紐づく [Canvas](Canvas.md) オブジェクトの生成を要求します。
生成された Canvas は [canvas](#canvas) プロパティから取得できます。

GPU デバイスがまだ準備できていない場合は、準備ができたとき ( [onInit](#oninit) の直前 ) に生成されます。

---

### resumeOnDraw

メソッド

**解説**

自動停止した onDraw の発火を再開

onDraw ハンドラが毎フレーム例外を投げ続けて連続例外の上限
( コマンドラインオプション `-eventexceptionlimit`、既定 10 ) に達すると、
onDraw の発火は自動停止します ( 画面の表示自体は継続 )。
このメソッドを呼ぶと発火を再開します。

---

### onInit

イベント

**解説**

GPU デバイス準備時に呼び出されるイベント

このデバイスの描画先 ( SDL_Renderer ) が GPU デバイスの上に作られ、Canvas を使える状態になった直後に発火します。

シェーダ・テクスチャ等の初期リソース確保はここで行います。GPU デバイスが使えない環境では発火せず、Canvas も使えません ( ログに `GPU device is not available` が出ます )。

**関連:** [GPUDrawDevice.onDone](GPUDrawDevice.md#ondone)

---

### onDone

イベント

**解説**

描画先の破棄前に呼び出されるイベント

このデバイスの描画先が破棄される直前に発火します。

onInit で確保したリソースの解放はここで行います。

**関連:** [GPUDrawDevice.onInit](GPUDrawDevice.md#oninit)

---

### onDraw

イベント

**解説**

画面描画時に呼び出されるイベント

Canvas がある間、描画サイクルごとに発火します。内部で Canvas の BeginDrawing 〜 EndDrawing で挟まれた状態で呼ばれるため、ハンドラ内で [canvas](#canvas) プロパティ経由で描画コマンドを発行できます。

オーバーレイ動画を再生している間は発火しません。

---
