# ゲーム画面の表示画角制御 (ビューポート)

外側ウインドウ ( surface ) の中に内側ゲーム画面を任意のサイズ・位置・倍率で
配置し、周囲の余白を背景色や壁紙画像で埋めることができます。ゲーム本来の解像度を保ったままウインドウサイズに合わせてレターボックス
表示・整数倍拡大・センタリングなどを行いたいときに使います。

内部構造の詳細は src/core 側のガイドを参照:

- [doc/Viewport.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/Viewport.md)

!!! note "対応ビルド / 対応 DrawDevice"
    配置の指定 ( fit / zoom / align / offset ) は **Windows ネイティブ ( WINVER )
    ビルドと SDL3 / 汎用ビルドの双方**で利用できます ( WINVER 対応は 2026-08-17 )。

    余白の**塗り分け** ( [Window.viewportBgColor](../../reference/Window.md#viewportbgcolor) /
    [Window.setViewportWallpaper](../../reference/Window.md#setviewportwallpaper) ) は、
    描画デバイスが対応している場合のみ効きます。同梱の
    [BasicDrawDevice](../../reference/Window.BasicDrawDevice.md) ( WINVER 既定 ) /
    [SDLDrawDevice](../../reference/SDLDrawDevice.md) / SDLOGL /
    [OGLDrawDevice](../../reference/OGLDrawDevice.md) はすべて対応しています。
    対応していない描画デバイス ( NullDrawDevice やプラグイン製のもの ) では
    余白はそのデバイス既定の塗りつぶしのままになります
    ( 判定は `drawDevice.viewportBackgroundHost` が非 0 かどうか )。

---

## 旧来と同じ表示にしたいとき

既定は `fit = "contain"` / `align = 中央` です。ウインドウが内側ゲーム画面と違う
サイズになったとき、アスペクト維持で拡大縮小して中央に置きます。

吉里吉里2 / 吉里吉里Z 従来の「ウインドウを広げてもゲームは原寸のまま左上」に
したい場合は、次を明示してください。

```tjs
window.setViewport("none", 1.0, 0, 0);   // fit=none, zoom=1.0, alignX=0, alignY=0
```

!!! tip "通常は違いが出ません"
    [Window.setInnerSize](../../reference/Window.md#setinnersize) で内側サイズを
    常に「primaryLayer のサイズ × [setZoom](../../reference/Window.md#setzoom) の倍率」に
    保っている限り、どのフィット方式でも等倍 1:1 で表示されます。差が出るのは
    **ユーザがウインドウをリサイズ / 最大化した場合**、**拡大率の異なるモニタへ
    移動した場合**、および**ウインドウサイズを変更できない環境 ( モバイル /
    コンソール )** です。

---

## 概念モデル

```
[外側 surface] = Window.innerWidth / innerHeight = OS ウインドウ client
        │  ビューポート設定 (fit / zoom / align / offset)
        ▼
[内側ゲーム]  = primaryLayer のサイズ (TJS から setSize で指定)
```

- **外側 surface** … [Window.innerWidth](../../reference/Window.md#innerwidth) /
  [Window.innerHeight](../../reference/Window.md#innerheight)。Elements UI
  オーバレイもこの座標系です。
- **内側ゲーム** … primaryLayer のサイズ。`primaryLayer.setSize(w, h)` で決まり、
  [Window.setInnerSize](../../reference/Window.md#setinnersize) とは独立です。
- 両者を一致させれば従来どおり全面等倍。異なるサイズにすると、設定に従って
  ゲームが surface 内へ配置され、余白が生じます。

マウス座標は配置に応じて自動的にゲーム論理座標へ補正されるため、どの fit/zoom でも
入力は正しくゲーム内部へ届きます。

---

## fit 方式

| 値 | 動作 |
|---|---|
| `"contain"` | アスペクト維持で収まる最大 ( レターボックス )。**既定** |
| `"cover"` | アスペクト維持で埋める最小 ( はみ出しは clip ) |
| `"fill"` | アスペクト無視で surface 全面へ引き伸ばし |
| `"none"` | 原寸 ( 倍率 1.0 ) |
| `"integer"` | 収まる範囲で最大の整数倍 ( 最低 1 倍、ドット等倍維持 ) |
| `"custom"` | [Window.viewportZoom](../../reference/Window.md#viewportzoom) の倍率を使用 |

---

## ウインドウの縦横比を固定する ( aspectLock )

ビューポートが決めるのは「**外側 surface の中でゲーム画面をどう置くか**」で、
外側 surface の**形そのもの**は、ユーザのリサイズやプラットフォームまかせです。
これを固定したいときに [Window.aspectLock](../../reference/Window.md#aspectlock)
を使います。

```tjs
window.aspectLock = "16:9";        // ウインドウの内側を 16:9 に固定
window.viewportFit = "integer";    // その中にゲーム画面をドットバイドットで配置
window.aspectLock = "";            // 固定を解除
```

ゲーム画面 ( primaryLayer ) の比率と、ウインドウ全体の比率を**分けたい**ときに
効きます。たとえばゲーム画面が 640x400 ( 8:5 ) でも、ウインドウ全体は 16:9 に
保ったままその中へ整数倍で置く、という構成です。UI ( Elements のオーバレイ等 ) を
16:9 の基本サイズで作っている場合、ウインドウが 16:9 に保たれていないと
UI とゲーム画面の枠がずれてしまうため、この固定が要ります。

有効にすると次の 2 つが変わります。

- ユーザによるウインドウのリサイズがこの比率へ拘束されます ( ドラッグ操作中も
  比率が保たれます )。
- [Window.setZoom](../../reference/Window.md#setzoom) が高さをこの比率から
  決めるようになります ( 従来は「primaryLayer のサイズ × 倍率」だったため、
  倍率を設定するたびにレイヤの比率へ戻っていました )。

設定した時点の内側サイズも、**幅を基準に**この比率へ合わせられます。

!!! warning "SDL3 / 汎用ビルド専用"
    Windows ネイティブ ( WINVER ) ビルドでは何も行いません。設定しても無視され、
    読み出すと常に空文字列が返ります。

---

## TJS API

[Window](../../reference/Window.md) クラスに以下のメンバーが追加されています。

### プロパティ

| メンバー | 説明 |
|---|---|
| [viewportFit](../../reference/Window.md#viewportfit) | フィット方式 ( 文字列 )。既定 `"contain"` |
| [viewportZoom](../../reference/Window.md#viewportzoom) | `"custom"` 時の倍率。既定 1.0 |
| [viewportAlignX](../../reference/Window.md#viewportalignx) | 水平配置 0=左 / 0.5=中央 / 1=右 |
| [viewportAlignY](../../reference/Window.md#viewportaligny) | 垂直配置 0=上 / 0.5=中央 / 1=下 |
| [viewportOffsetX](../../reference/Window.md#viewportoffsetx) | 水平オフセット ( px ) |
| [viewportOffsetY](../../reference/Window.md#viewportoffsety) | 垂直オフセット ( px ) |
| [viewportBgColor](../../reference/Window.md#viewportbgcolor) | 余白の背景色 `0xRRGGBB` |
| [aspectLock](../../reference/Window.md#aspectlock) | ウインドウ自体の縦横比を固定 ( `"16:9"` 等 )。既定 `""` = 固定なし。**SDL3 / 汎用ビルド専用** |

### メソッド

| メンバー | 説明 |
|---|---|
| [setViewport](../../reference/Window.md#setviewport)(fit [,zoom [,alignX [,alignY [,offsetX [,offsetY]]]]]) | 配置をまとめて設定 |
| [setViewportWallpaper](../../reference/Window.md#setviewportwallpaper)(image [,fit [,alignX [,alignY]]]) | 余白の壁紙画像を設定 |
| [clearViewportWallpaper](../../reference/Window.md#clearviewportwallpaper)() | 壁紙を解除 |

壁紙の `image` にはストレージ名 ( 文字列 ) のほか、[Layer](../../reference/Layer.md) /
[Bitmap](../../reference/Bitmap.md) オブジェクトを直接渡すこともできます ( 参照保持されます )。

---

## 使用例

```tjs
var win = new Window();
win.setInnerSize(1280, 720);       // 外側ウインドウ

var lay = new Layer(win, null);    // primaryLayer
lay.setSize(640, 400);             // 内側ゲーム解像度
win.add(lay);

win.viewportBgColor = 0xff203060;  // 余白の色
win.viewportFit = "integer";       // 整数倍 (640x400 → 1280x800 は不可なので 1 倍)

// または 180% センタリング:
win.setViewport("custom", 1.8);

// 余白に壁紙 (ストレージ名でもオブジェクトでも可):
win.setViewportWallpaper("bg_pattern.png", "cover");
// win.setViewportWallpaper(myBitmap, "cover");   // Layer / Bitmap を直接渡す
```
