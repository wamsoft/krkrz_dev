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
