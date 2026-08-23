# OGLDrawDevice

OGLDrawDevice クラスは、このインスタンスを [Window.drawDevice](Window.md#drawdevice) に登録して使用するための DrawDevice で、OpenGL ES (glad / ANGLE / EGL) を用いた描画機能を提供します。

起動時の既定 DrawDevice ではなく、TJS スクリプトで明示的に Window.drawDevice にセットしたタイミングで内部の OpenGL コンテキストが生成され、以降のすべての描画が GL パスを通るようになります。起動オプション `-drawdevice=ogl` で起動時からこのデバイスを選ぶこともできます ( [コマンドラインオプション](../guide/CommandLine.md) )。

利用には OpenGL ES が使える環境が必要です。WINVER ビルドは常に EGL ( ANGLE の `libEGL.dll` / `libGLESv2.dll` ) 経由なので DLL の同梱が必須です。SDL3 ビルドでは OS の OpenGL ドライバの ES プロファイルが優先され、使えない場合に同じ ANGLE DLL へフォールバックします ( `-forceegl` で EGL 強制も可能 )。また SDL3 ビルドを `-drawdevice=sdl` で起動した場合は、実行中にこのデバイスへ切り替えることはできません。

このデバイスがアクティブな間のみ、TJS 公開クラス [Canvas](Canvas.md) / [Texture](Texture.md) / [ShaderProgram](ShaderProgram.md) / [Offscreen](Offscreen.md) / [Matrix32](Matrix32.md) / [VertexBuffer](VertexBuffer.md) / [VertexBinder](VertexBinder.md) が機能します。

## メンバー一覧

### コンストラクタ

- [OGLDrawDevice](#ogldrawdevice)

### プロパティ

- [interface](#interface)
- [window](#window)
- [canvas](#canvas)
- [texture](#texture)
- [matrix](#matrix)
- [glVideoPresenterHost](#glvideopresenterhost)
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

### OGLDrawDevice

コンストラクタ

**解説**

OGLDrawDevice オブジェクトの構築

OGLDrawDevice クラスのオブジェクトを構築します。

構築直後はまだ OpenGL コンテキストは生成されません。Window.drawDevice にセットしたときに初期化されます。

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

テクスチャ管理オブジェクトを取得

このデバイスが管理している [Texture](Texture.md) オブジェクトを返します。

---

### matrix

プロパティ \ アクセス: `r`

**解説**

行列オブジェクトを取得

このデバイスが管理している [Matrix32](Matrix32.md) オブジェクトを返します。
描画時の座標変換に使用します。

---

### glVideoPresenterHost

プロパティ \ アクセス: `r`

**解説**

オーバーレイ動画 presenter 登録口 (ポインタ値)

オーバーレイ動画側がこの GL デバイスへ pull 型で合成するために読み取る presenter host
へのポインタ値です (WINVER の [videoPresenterHost](Window.BasicDrawDevice.md#videopresenterhost) /
SDL の [sdlVideoPresenterHost](SDLDrawDevice.md#sdlvideopresenterhost) と同じ規約)。
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
`iTVPViewportBackgroundHost` へのポインタ値です。 Window はこのプロパティが非 0 の
ときだけ余白設定を反映します ( プロパティを持たない描画デバイスでは余白の塗り分けは
効かず、そのデバイス既定の塗りつぶしのままになります )。 通常はエンジン内部/プラグインが
使用します。

---

### recreate

メソッド

**解説**

内部デバイス再生成

内部デバイスの再生成を行います。

通常使用することはありません。

---

### createCanvas

メソッド

**解説**

Canvas オブジェクトを生成

このデバイスに紐づく [Canvas](Canvas.md) オブジェクトの生成を要求します。
生成された Canvas は [canvas](#canvas) プロパティから取得できます。

---

### resumeOnDraw

メソッド

**解説**

自動停止した onDraw の発火を再開

onDraw ハンドラが毎フレーム例外を投げ続けて連続例外の上限
( コマンドラインオプション `-eventexceptionlimit`、既定 10 ) に達すると、
onDraw の発火は自動停止します ( 画面クリア等の描画サイクル自体は継続 )。
このメソッドを呼ぶと発火を再開します。

---

### onInit

イベント

**解説**

GL コンテキスト初期化時に呼び出されるイベント

このデバイスが Window.drawDevice にセットされ、内部の OpenGL ES コンテキストの生成と初期化が完了した直後に発火します。

シェーダ・テクスチャ等の初期リソース確保はここで行います。

**関連:** [OGLDrawDevice.onDone](OGLDrawDevice.md#ondone)

---

### onDone

イベント

**解説**

GL コンテキスト破棄前に呼び出されるイベント

このデバイスが切り離される、もしくはコンテキストが破棄される直前に発火します。

onInit で確保したリソースの解放はここで行います。

**関連:** [OGLDrawDevice.onInit](OGLDrawDevice.md#oninit)

---

### onDraw

イベント

**解説**

画面描画時に呼び出されるイベント

描画サイクルごとに発火します。Canvas が割り当てられている場合、内部で BeginDrawing 〜 EndDrawing で挟まれた状態で呼ばれるため、ハンドラ内で [canvas](#canvas) プロパティ経由で描画コマンドを発行できます。

---
