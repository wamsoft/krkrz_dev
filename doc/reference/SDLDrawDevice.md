# SDLDrawDevice

SDLDrawDevice クラスは、このインスタンスを [Window.drawDevice](Window.md#drawdevice) に登録して使用するための DrawDevice で、SDL3 (`SDL_Renderer` + `SDL_Texture`) を用いた標準的な描画機能を提供します。SDL3 ビルド (KRKRZ_VARIANT=SDL) 専用で、WINVER ビルドには含まれません。

SDL3 ビルドの起動時の既定 DrawDevice は、OpenGL 有効ビルドでは OpenGL ES ベースの [SDLOGLDrawDevice](SDLOGLDrawDevice.md)、OpenGL 無効ビルドではこのクラスです。起動オプション `-drawdevice=sdl` を指定すると OpenGL 有効ビルドでもこのクラスで起動できます ( [コマンドラインオプション](../guide/CommandLine.md) )。`SDL_Renderer` のバックエンドは自動選択で、`-renderer` オプションで明示できます。

なお、このクラスで起動した場合、実行中に OpenGL 系 ( [SDLOGLDrawDevice](SDLOGLDrawDevice.md) / [OGLDrawDevice](OGLDrawDevice.md) ) へ切り替えることはできません ( OpenGL の初期化が通りません )。OpenGL 機能 ( [Canvas](Canvas.md) 等 ) を使う場合は最初から OpenGL 系の DrawDevice で起動してください。

## メンバー一覧

### コンストラクタ

- [SDLDrawDevice](#sdldrawdevice)

### プロパティ

- [interface](#interface)
- [window](#window)
- [sdlVideoPresenterHost](#sdlvideopresenterhost)
- [dialogRendererHost](#dialogrendererhost)
- [viewportBackgroundHost](#viewportbackgroundhost)

---

### SDLDrawDevice

コンストラクタ

**解説**

SDLDrawDevice オブジェクトの構築

SDLDrawDevice クラスのオブジェクトを構築します。

このクラスが起動時の既定 ( OpenGL 無効ビルド、または `-drawdevice=sdl` 指定時 ) の場合、Window.drawDevice には最初からこのクラスのインスタンスが登録されているので、新たに登録する必要はありません。

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

### sdlVideoPresenterHost

プロパティ \ アクセス: `r`

**解説**

オーバーレイ動画 presenter 登録口 (ポインタ値)

オーバーレイ動画側がこの DrawDevice へ pull 型で合成するために読み取る presenter host
へのポインタ値です (WINVER の [videoPresenterHost](Window.BasicDrawDevice.md#videopresenterhost) と同じ規約)。
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
