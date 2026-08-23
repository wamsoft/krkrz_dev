# SDLOGLDrawDevice

SDLOGLDrawDevice クラスは、このインスタンスを [Window.drawDevice](Window.md#drawdevice) に登録して使用するための DrawDevice で、SDL3 ビルドで OpenGL ES を直接使ってレイヤ合成結果を画面へ描画します。SDL3 ビルド (KRKRZ_VARIANT=SDL) 専用で、WINVER ビルドには含まれません。

OpenGL 有効ビルド ( 既定構成 ) の SDL3 では**起動時の既定 DrawDevice** として最初から登録されているため、通常は意識する必要はありません。起動オプション `-drawdevice=sdlogl` で明示することもできます ( [コマンドラインオプション](../guide/CommandLine.md) )。

[SDLDrawDevice](SDLDrawDevice.md) ( `SDL_Renderer` 経由 ) との違いは、SDL のレンダラ抽象を介さず OpenGL ES へ直接テクスチャ更新・描画を行う点です。[OGLDrawDevice](OGLDrawDevice.md) ( [Canvas](Canvas.md) / [Texture](Texture.md) / [ShaderProgram](ShaderProgram.md) 等の TJS 公開 GL クラス群を持つフル機能版 ) から、それら TJS 公開ロジックを除いた「レイヤ描画 + 動画再生」のシンプル版にあたります。GL コンテキストは OGLDrawDevice と共有可能で、Canvas 等を使いたくなったら Window.drawDevice へ [OGLDrawDevice](OGLDrawDevice.md) をセットして切り替えられます。

利用には OpenGL ES が使える環境が必要です ( OS の OpenGL ドライバの ES プロファイル、または ANGLE の `libEGL.dll` / `libGLESv2.dll`。`-forceegl` で EGL 強制も可能 )。

## メンバー一覧

### コンストラクタ

- [SDLOGLDrawDevice](#sdlogldrawdevice)

### プロパティ

- [interface](#interface)
- [window](#window)
- [glVideoPresenterHost](#glvideopresenterhost)
- [dialogRendererHost](#dialogrendererhost)
- [viewportBackgroundHost](#viewportbackgroundhost)

---

### SDLOGLDrawDevice

コンストラクタ

**解説**

SDLOGLDrawDevice オブジェクトの構築

SDLOGLDrawDevice クラスのオブジェクトを構築します。

OpenGL 有効ビルドの SDL3 では起動時の既定 DrawDevice として最初から Window.drawDevice に登録されているので、新たに登録する必要はありません。

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
