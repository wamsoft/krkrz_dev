# Threepp.GLRenderer

OpenGL レンダラー

シーンをレンダリングするためのレンダラーです。
============================================================ Renderer クラス ============================================================

## メンバー一覧

### コンストラクタ

- [GLRenderer](#glrenderer)
- [GLRenderer](#glrenderer)

### プロパティ

- [autoClear](#autoclear)
- [autoClearColor](#autoclearcolor)
- [autoClearDepth](#autocleardepth)
- [autoClearStencil](#autoclearstencil)
- [sortObjects](#sortobjects)
- [useLegacyLights](#uselegacylights)
- [toneMappingExposure](#tonemappingexposure)

### メソッド

- [onBeginScene](#onbeginscene)
- [onEndScene](#onendscene)
- [render](#render)
- [setClearColor](#setclearcolor)
- [setPixelRatio](#setpixelratio)
- [setSize](#setsize)
- [setSampleCount](#setsamplecount)
- [setScissorTest](#setscissortest)
- [setShadowMapEnabled](#setshadowmapenabled)
- [setShadowMapType](#setshadowmaptype)
- [setShadowMapAutoUpdate](#setshadowmapautoupdate)
- [setShadowMapNeedsUpdate](#setshadowmapneedsupdate)
- [clear](#clear)
- [clearColor](#clearcolor)
- [clearDepth](#cleardepth)
- [clearStencil](#clearstencil)
- [dispose](#dispose)
- [resetState](#resetstate)

---

### GLRenderer

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `adaptor` | `&nbsp;` | GL コンテキスト提供オブジェクト (GLGetProcAddress を持つ) |
| `width` | `800` | レンダリング幅 |
| `height` | `600` | レンダリング高さ |

**解説**

コンストラクタ

ホストが用意した GL コンテキスト上に描画するレンダラー(デバイス)。
第1引数にホストの GL コンテキスト提供オブジェクト(gles プラグインの
GLESAdaptor 等、GLGetProcAddress プロパティを持つもの)を渡すと、そこから
関数ポインタ(getProcAddress)を取得して glad を初期化する。
これは effekseer / motion プラグインの Device と同じ結線方式。

---

### GLRenderer

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `width` | `800` |  |
| `height` | `600` |  |

**解説**

コンストラクタ (従来形式)

GL コンテキストの current 化と glad の初期化を呼び出し側で
済ませてある場合はこちら。ヘッドレス生成。

---

### autoClear

プロパティ \ アクセス: `r/w`

**解説**

自動クリアするか

---

### autoClearColor

プロパティ \ アクセス: `r/w`

**解説**

カラーバッファを自動クリアするか

---

### autoClearDepth

プロパティ \ アクセス: `r/w`

**解説**

深度バッファを自動クリアするか

---

### autoClearStencil

プロパティ \ アクセス: `r/w`

**解説**

ステンシルバッファを自動クリアするか

---

### sortObjects

プロパティ \ アクセス: `r/w`

**解説**

オブジェクトをソートするか

---

### useLegacyLights

プロパティ \ アクセス: `r/w`

**解説**

旧来ライティング(true)か物理的に正確(false, 既定)か

---

### toneMappingExposure

プロパティ \ アクセス: `r/w`

**解説**

トーンマッピングの露出

---

### onBeginScene

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `width` | `&nbsp;` | サーフェス幅 |
| `height` | `&nbsp;` | サーフェス高さ |

**解説**

フレーム描画開始 (ホスト GL コンテキストが current な状態で呼ぶ)

内部ステートキャッシュを無効化し、描画サイズを設定する。
adaptor.capture() のコールバック内で render() の前に呼ぶ。

---

### onEndScene

メソッド

**解説**

フレーム描画終了

render() 後に呼ぶ。現状は特別な処理を行わないが、ホストとの
GL ステート整合のために呼び出し位置を確保しておく。

---

### render

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `scene` | `&nbsp;` | シーン |
| `camera` | `&nbsp;` | カメラ |

**解説**

シーンをレンダリング

---

### setClearColor

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `color` | `&nbsp;` | 色 (0xRRGGBB) |
| `alpha` | `1` | アルファ値 |

**解説**

クリアカラーを設定

---

### setPixelRatio

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `ratio` | `&nbsp;` |  |

**解説**

ピクセル比を設定

---

### setSize

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `width` | `&nbsp;` |  |
| `height` | `&nbsp;` |  |

**解説**

サイズを設定

---

### setSampleCount

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `count` | `&nbsp;` | 0/1=無効, 2/4/8 など。既定 4。onBeginScene が内部マルチサンプル FBO へ<br>描き onEndScene で解決(resolve)してホスト FBO へ転送する。輪郭のジャギーが軽減される。<br>縁の premultiplied alpha が気になる場合はホスト側(GLESAdaptor.unpremultiply)で補正する。 |

**解説**

MSAA (マルチサンプルアンチエイリアス) のサンプル数を設定

---

### setScissorTest

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `enabled` | `&nbsp;` |  |

**解説**

シザーテストの有効/無効

---

### setShadowMapEnabled

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `enabled` | `&nbsp;` |  |

**解説**

影(ShadowMap)の有効/無効

true でシャドウマップ描画を有効化する。別途、影を落とすライトの
castShadow=true・影を受けるメッシュの receiveShadow=true・影を落とすメッシュの
castShadow=true が必要。GLES/捕捉FBO 経路でも動作する(影用 FBO へ深度を焼き、
本描画時に元の描画先へ復帰する)。
使用例:
renderer.setShadowMapEnabled(true);
var dir = new Threepp.DirectionalLight(0xffffff, 2.0);
dir.setPosition(3, 5, 2); dir.castShadow = true;
dir.setShadowOrthoBounds(-6, 6, 6, -6); dir.setShadowNearFar(0.5, 30);
scene.add(dir);
floor.receiveShadow = true; box.castShadow = true;

---

### setShadowMapType

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `type` | `&nbsp;` |  |

**解説**

0=Basic,1=PCF(既定),2=PCFSoft,3=VSM 相当

---

### setShadowMapAutoUpdate

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `enabled` | `&nbsp;` |  |

**解説**

毎フレーム影を更新(既定 true)

---

### setShadowMapNeedsUpdate

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `enabled` | `&nbsp;` |  |

**解説**

autoUpdate=false 時に1回だけ更新

---

### clear

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `color` | `true` |  |
| `depth` | `true` |  |
| `stencil` | `true` |  |

**解説**

バッファをクリア

---

### clearColor

メソッド

**解説**

カラーバッファをクリア

---

### clearDepth

メソッド

**解説**

深度バッファをクリア

---

### clearStencil

メソッド

**解説**

ステンシルバッファをクリア

---

### dispose

メソッド

**解説**

リソースを解放

---

### resetState

メソッド

**解説**

状態をリセット

---
