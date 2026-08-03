# EffekseerDevice

描画デバイス

OpenGL(ES) コンテキストごとに 1 つ生成する。

## メンバー一覧

### コンストラクタ

- [EffekseerDevice](#effekseerdevice)

### プロパティ

- [instanceMax](#instancemax)
- [squareMaxCount](#squaremaxcount)
- [premultipliedAlpha](#premultipliedalpha)
- [projectionMode](#projectionmode)
- [frameRate](#framerate)
- [restorationOfStates](#restorationofstates)
- [clearDepth](#cleardepth)
- [verbose](#verbose)
- [surfaceWidth](#surfacewidth)
- [surfaceHeight](#surfaceheight)
- [totalInstanceCount](#totalinstancecount)
- [drawCallCount](#drawcallcount)
- [drawVertexCount](#drawvertexcount)
- [deviceInfo](#deviceinfo)

### メソッド

- [onBeginScene](#onbeginscene)
- [onEndScene](#onendscene)
- [update](#update)
- [beginUpdate](#beginupdate)
- [endUpdate](#endupdate)
- [onLostDevice](#onlostdevice)
- [onResetDevice](#onresetdevice)
- [stopAll](#stopall)
- [setCapacity](#setcapacity)
- [setPerspective](#setperspective)
- [setOrthographic](#setorthographic)
- [setCamera](#setcamera)
- [resetCamera](#resetcamera)
- [getGLError](#getglerror)

---

### EffekseerDevice

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `oglbase` | `&nbsp;` | GLGetProcAddress を保持するオブジェクト (GetProcAddress提供元)<br>以下のいずれかを指定できる:<br>- krkrgles プラグインの GLESAdaptor<br>- 新しい吉里吉里Z の OGLDrawDevice (本体組み込みの OpenGL 描画デバイス)<br>現在の OpenGL ES コンテキストに対して初期化される。<br>※コンテキストが current な状態で生成すること |

**解説**

コンストラクタ

---

### instanceMax

プロパティ \ アクセス: `r/w`

**解説**

読み出し専用

---

### squareMaxCount

プロパティ \ アクセス: `r/w`

**解説**

読み出し専用

---

### premultipliedAlpha

プロパティ \ アクセス: `r/w`

**解説**

乗算済みアルファで描画するか (既定 false)。

変更するとマネージャ/レンダラが作り直される (setCapacity と同じ注意)。

---

### projectionMode

プロパティ \ アクセス: `r/w`

**解説**

投影モード

EffekseerDevice.EffekseerProjectionOrthographic … 平行投影 (既定)
EffekseerDevice.EffekseerProjectionPerspective  … 透視投影

---

### frameRate

プロパティ \ アクセス: `r/w`

**解説**

進行の基準フレームレート (既定 60)。

progress(tick) / update(tick) のミリ秒をフレーム数へ換算するのに使う。

---

### restorationOfStates

プロパティ \ アクセス: `r/w`

**解説**

描画前後で GL ステートを保存/復元するか (既定 true)。

吉里吉里や他プラグインの GL 描画と混在させる場合は true のままにする。

---

### clearDepth

プロパティ \ アクセス: `r/w`

**解説**

onBeginScene で深度バッファをクリアするか (既定 true)

エフェクト側のノードで深度テスト(ZTest)が有効な場合、描画先の深度値と
比較される。吉里吉里が用意するオフスクリーンバッファは深度が未初期化の
ことがあり (krkrgles の capture はカラーとステンシルしかクリアしない)、
そのままだとエフェクトが一切表示されない。
既定では毎フレーム 1.0 で初期化する。呼び出し側で深度を管理している
場合のみ false にする。

---

### verbose

プロパティ \ アクセス: `r/w`

**解説**

資材のオープン結果や Effekseer の詳細ログを吉里吉里のログへ出す (既定 false)

テクスチャが見つからない等の切り分けに使う。

---

### surfaceWidth

プロパティ \ アクセス: `r/w`

**解説**

読み出し専用: 最後の onBeginScene の幅

---

### surfaceHeight

プロパティ \ アクセス: `r/w`

**解説**

読み出し専用: 同 高さ

---

### totalInstanceCount

プロパティ \ アクセス: `r/w`

**解説**

読み出し専用: 全パーティクル数

---

### drawCallCount

プロパティ \ アクセス: `r/w`

**解説**

読み出し専用: 直近のドローコール数

---

### drawVertexCount

プロパティ \ アクセス: `r/w`

**解説**

読み出し専用: 直近の頂点数

---

### deviceInfo

プロパティ \ アクセス: `r/w`

**解説**

読み出し専用: 設定値一式(辞書)

---

### onBeginScene

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `width` | `&nbsp;` | 描画対象の幅(ピクセル) |
| `height` | `&nbsp;` | 描画対象の高さ(ピクセル)<br>※生成時のコンテキストで呼び出すこと |

**解説**

描画開始。投影行列を更新して Effekseer の描画を開始する。

---

### onEndScene

メソッド

**解説**

描画終了。

---

### update

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `tick` | `&nbsp;` | 経過時間(ミリ秒)<br>プレイヤー個別に progress() する場合は呼ばなくてよい。 |

**解説**

全エフェクトをまとめて進行させる。

---

### beginUpdate

メソッド

**解説**

プレイヤー個別進行のまとめ処理

多数の EffekseerPlayer.progress() を呼ぶ場合、beginUpdate()〜endUpdate()
で囲むと内部のバッファ入れ替えが 1 回で済む。
device.beginUpdate();
for (...) players[i].progress(tick);
device.endUpdate();

---

### endUpdate

メソッド

---

### onLostDevice

メソッド

**解説**

GLリソースの破棄/再構築 (コンテキスト喪失への対応)

---

### onResetDevice

メソッド

---

### stopAll

メソッド

**解説**

再生中の全エフェクトを停止する

---

### setCapacity

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `instanceMax` | `&nbsp;` | 同時に存在できるパーティクル数の上限 (既定 4000) |
| `squareMaxCount` | `&nbsp;` | 1描画あたりのスプライト数の上限 (既定 8192) |

**解説**

内部バッファ容量を設定する。内部のマネージャ/レンダラが作り直されるため、

※エフェクト読み込み前・プレイヤー生成前に呼ぶこと。
既存の EffekseerEffect / EffekseerPlayer は無効化される。

---

### setPerspective

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `fovDegree` | `&nbsp;` | 垂直画角(度)  既定 45 |
| `znear` | `&nbsp;` | 近クリップ面  既定 1 |
| `zfar` | `&nbsp;` | 遠クリップ面  既定 10000<br>カメラは「Z=0 の平面で 1 ワールド単位 = 1 ピクセル」になる距離へ自動配置される。 |

**解説**

透視投影に切り替えてパラメータを設定する

---

### setOrthographic

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `znear` | `&nbsp;` | 近クリップ面 |
| `zfar` | `&nbsp;` | 遠クリップ面 |

**解説**

平行投影に切り替えて奥行き範囲を設定する

---

### setCamera

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `px` | `&nbsp;` |  |
| `py` | `&nbsp;` |  |
| `pz` | `&nbsp;` |  |
| `tx` | `&nbsp;` |  |
| `ty` | `&nbsp;` |  |
| `tz` | `&nbsp;` |  |

**解説**

カメラを手動配置する (配置と同じ画面中央原点のピクセル座標)

既定では原点 (画面中央) を正面から見る位置に自動配置される。

---

### resetCamera

メソッド

**解説**

カメラを自動配置へ戻す

---

### getGLError

メソッド

**解説**

直近の GL エラーコードを取得する (読み出すとクリアされる。0 ならエラーなし)

---
