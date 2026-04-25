# BitmapLayerTreeOwner

BitmapLayerTreeOwner クラスは、レイヤーツリーを保持し、描画結果を Bitmap クラスで取得できるクラスです。(1.1.0以降)

Layer クラスのコンストラクタの第一引数に window の代わりに渡すことで、それら Layer の描画結果を Bitmap クラスとして画像で取得できます。

## メンバー一覧

### コンストラクタ

- [BitmapLayerTreeOwner](#bitmaplayertreeowner)

### プロパティ

- [bitmap](#bitmap)
- [dirtyRect](#dirtyrect)
- [focusedLayer](#focusedlayer)
- [height](#height)
- [isUpdated](#isupdated)
- [layerEventTargetInterface](#layereventtargetinterface)
- [layerTreeOwnerInterface](#layertreeownerinterface)
- [primaryLayer](#primarylayer)
- [width](#width)

### メソッド

- [clearDirtyRect](#cleardirtyrect)
- [fireClick](#fireclick)
- [fireDisplayRotate](#firedisplayrotate)
- [fireDoubleClick](#firedoubleclick)
- [fireKeyDown](#firekeydown)
- [fireKeyPress](#firekeypress)
- [fireKeyUp](#firekeyup)
- [fireMouseDown](#firemousedown)
- [fireMouseMove](#firemousemove)
- [fireMouseOutOfWindow](#firemouseoutofwindow)
- [fireMouseUp](#firemouseup)
- [fireMouseWheel](#firemousewheel)
- [fireMultiTouch](#firemultitouch)
- [fireRecheckInputState](#firerecheckinputstate)
- [fireReleaseCapture](#firereleasecapture)
- [fireTouchDown](#firetouchdown)
- [fireTouchMove](#firetouchmove)
- [fireTouchRotate](#firetouchrotate)
- [fireTouchScaling](#firetouchscaling)
- [fireTouchUp](#firetouchup)
- [update](#update)

### イベント

- [onChangeLayerImage](#onchangelayerimage)
- [onDisableAttentionPoint](#ondisableattentionpoint)
- [onGetCursorPos](#ongetcursorpos)
- [onReleaseMouseCapture](#onreleasemousecapture)
- [onResetImeMode](#onresetimemode)
- [onResizeLayer](#onresizelayer)
- [onSetAttentionPoint](#onsetattentionpoint)
- [onSetCursorPos](#onsetcursorpos)
- [onSetHintText](#onsethinttext)
- [onSetImeMode](#onsetimemode)
- [onSetMouseCursor](#onsetmousecursor)

---

### BitmapLayerTreeOwner

コンストラクタ

**解説**

BitmapLayerTreeOwner オブジェクトの構築

BitmapLayerTreeOwner クラスのオブジェクトを構築します。

---

### bitmap

プロパティ \ アクセス: `r/w`

**解説**

TODO: bitmap の説明

---

### dirtyRect

プロパティ \ アクセス: `r/w`

**解説**

TODO: dirtyRect の説明

---

### focusedLayer

プロパティ \ アクセス: `r/w`

**解説**

TODO: focusedLayer の説明

---

### height

プロパティ \ アクセス: `r/w`

**解説**

高さ(readonly)

---

### isUpdated

プロパティ \ アクセス: `r/w`

**解説**

TODO: isUpdated の説明

---

### layerEventTargetInterface

プロパティ \ アクセス: `r/w`

**解説**

TODO: layerEventTargetInterface の説明

---

### layerTreeOwnerInterface

プロパティ \ アクセス: `r/w`

**解説**

LTOインターフェイス、内部使用(readonly)

---

### primaryLayer

プロパティ \ アクセス: `r/w`

**解説**

プライマリレイヤ(readonly)

---

### width

プロパティ \ アクセス: `r/w`

**解説**

幅(readonly)

---

### clearDirtyRect

メソッド

**解説**

更新矩形情報をクリアする

---

### fireClick

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | クリックされた位置の x 座標 ( クライアント座標 ) |
| `y` | `&nbsp;` | クリックされた位置の y 座標 ( クライアント座標 ) |

**解説**

クリックをレイヤに通知します(使用非推奨)

---

### fireDisplayRotate

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `orientation` | `&nbsp;` | 画面の向き |
| `rotate` | `&nbsp;` | 角度 |
| `bpp` | `&nbsp;` | bits per pixel |
| `hresolution` | `&nbsp;` | 画面の幅 |
| `vresolution` | `&nbsp;` | 画面の高さ |

**解説**

画面が回転されたことをレイヤに通知します

---

### fireDoubleClick

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | ダブルクリックされた位置の x 座標 ( クライアント座標 ) |
| `y` | `&nbsp;` | ダブルクリックされた位置の y 座標 ( クライアント座標 ) |

**解説**

ダブルクリックをレイヤに通知します(使用非推奨)

---

### fireKeyDown

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `key` | `&nbsp;` | 押されたキーの仮想キーコード |
| `shift` | `&nbsp;` | キーが押された時に同時に押されていたシフト系のキーやマウスのボタンの状態 |

**解説**

キーが押されたことをレイヤに通知します

---

### fireKeyPress

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `key` | `&nbsp;` | 文字 |

**解説**

文字が入力されたことをレイヤに通知します

---

### fireKeyUp

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `key` | `&nbsp;` | 離されたキーの仮想キーコード |
| `shift` | `&nbsp;` | キーが離された時に同時に押されていたシフト系のキーやマウスのボタンの状態 |

**解説**

キーが離されたことをレイヤに通知します

---

### fireMouseDown

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | マウスのボタンが押された位置の x 座標 ( クライアント座標 ) |
| `y` | `&nbsp;` | マウスのボタンが押された位置の y 座標 ( クライアント座標 ) |
| `mb` | `&nbsp;` | 押されたマウスボタン |
| `flags` | `&nbsp;` |  |

**解説**

マウス押下をレイヤに通知します

---

### fireMouseMove

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | マウスが移動した位置の x 座標 ( クライアント座標 ) |
| `y` | `&nbsp;` | マウスが移動した位置の y 座標 ( クライアント座標 ) |
| `flags` | `&nbsp;` | マウスが移動していた時に同時に押されていたシフト系のキーやマウスのボタンの状態 |

**解説**

マウス移動をレイヤに通知します

---

### fireMouseOutOfWindow

メソッド

**解説**

マウスがWindow外に出たことをレイヤに通知します

---

### fireMouseUp

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | マウスのボタンが離された位置の x 座標 ( クライアント座標 ) |
| `y` | `&nbsp;` | マウスのボタンが離された位置の y 座標 ( クライアント座標 ) |
| `mb` | `&nbsp;` | 離されたマウスボタン |
| `flags` | `&nbsp;` | マウスボタンが離された時に同時に押されていたシフト系のキーの状態 |

**解説**

マウス押下をレイヤに通知します

---

### fireMouseWheel

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `shift` | `&nbsp;` | マウスが移動していた時に同時に押されていたシフト系のキーやマウスのボタンの状態 |
| `delta` | `&nbsp;` | ホイールの回転角 |
| `x` | `&nbsp;` | ホイールが回転した位置の x 座標 ( クライアント座標 ) |
| `y` | `&nbsp;` | ホイールが回転した位置の y 座標 ( クライアント座標 ) |

**解説**

マウスのホイール回転をレイヤに通知します

---

### fireMultiTouch

メソッド

**解説**

マルチタッチ状態変化をレイヤに通知します

---

### fireRecheckInputState

メソッド

**解説**

必要なら1秒間隔で呼び出します。

現在のレイヤのマウス位置確認とヒントの更新、カーソルタイプ、レイヤEnter/Leaveが再チェックされます。
内部的にはマウスカーソル移動0呼び出しが行われています。

---

### fireReleaseCapture

メソッド

**解説**

マウスキャプチャ解除をレイヤに通知します

---

### fireTouchDown

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | タッチされた位置の x 座標 ( クライアント座標 ) |
| `y` | `&nbsp;` | タッチされた位置の y 座標 ( クライアント座標 ) |
| `cx` | `&nbsp;` | 指が接触している横方向ピクセル数 |
| `cy` | `&nbsp;` | 指が接触している縦方向ピクセル数 |
| `id` | `&nbsp;` | タッチID |

**解説**

タッチされたことをレイヤに通知します

---

### fireTouchMove

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | タッチ位置の x 座標 ( クライアント座標 ) |
| `y` | `&nbsp;` | タッチ位置の y 座標 ( クライアント座標 ) |
| `cx` | `&nbsp;` | 指が接触している横方向ピクセル数 |
| `cy` | `&nbsp;` | 指が接触している縦方向ピクセル数 |
| `id` | `&nbsp;` | タッチID |

**解説**

タッチが移動されたことをレイヤに通知します

---

### fireTouchRotate

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `startangle` | `&nbsp;` | マルチタッチが開始された時のラジアン角度 |
| `curangle` | `&nbsp;` | イベント発生時のタッチのラジアン角度 |
| `dist` | `&nbsp;` | イベント発生時のタッチのピクセル距離 |
| `cx` | `&nbsp;` | 中心位置の x 座標 ( クライアント座標 ) |
| `cy` | `&nbsp;` | 中心位置の y 座標 ( クライアント座標 ) |
| `flag` | `&nbsp;` | マルチタッチ状態フラグ |

**解説**

回転操作されたことをレイヤに通知します

---

### fireTouchScaling

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `startdist` | `&nbsp;` | マルチタッチが開始された時のピクセル距離 |
| `curdist` | `&nbsp;` | イベント発生時のタッチのピクセル距離 |
| `cx` | `&nbsp;` | 中心位置の x 座標 ( クライアント座標 ) |
| `cy` | `&nbsp;` | 中心位置の y 座標 ( クライアント座標 ) |
| `flag` | `&nbsp;` | マルチタッチ状態フラグです。 |

**解説**

拡大操作されたことをレイヤに通知します

---

### fireTouchUp

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 離された位置の x 座標 ( クライアント座標 ) |
| `y` | `&nbsp;` | 離された位置の y 座標 ( クライアント座標 ) |
| `cx` | `&nbsp;` | 指が接触している横方向ピクセル数 |
| `cy` | `&nbsp;` | 指が接触している縦方向ピクセル数 |
| `id` | `&nbsp;` | タッチID |

**解説**

タッチが離されたことをレイヤに通知します

---

### update

メソッド

**解説**

TODO: update の説明

---

### onChangeLayerImage

イベント

**解説**

Layer 画像が更新された

---

### onDisableAttentionPoint

イベント

**解説**

Layer から注視位置の指定解除された

---

### onGetCursorPos

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**解説**

Layer からカーソル位置取得が呼び出された

必要であればカーソル位置を返す

---

### onReleaseMouseCapture

イベント

**解説**

Layer からマウスキャプチャ解除が呼び出された

必要であればマウスキャプチャ解除を行う

---

### onResetImeMode

イベント

**解説**

IMEモードがリセットされた

---

### onResizeLayer

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |

**解説**

プライマリレイヤーのサイズが変更された

---

### onSetAttentionPoint

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `layer` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**解説**

Layer から注視位置の指定が呼び出された

---

### onSetCursorPos

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**解説**

Layer からカーソル位置設定が呼び出された

必要であればカーソル位置を設定する

---

### onSetHintText

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `sender` | `&nbsp;` |  |
| `hint` | `&nbsp;` |  |

**解説**

Layer からヒントテキスト設定が呼び出された

必要であればヒントテキスト設定を行う

---

### onSetImeMode

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `mode` | `&nbsp;` |  |

**解説**

IMEモードが設定された

---

### onSetMouseCursor

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `cursor` | `&nbsp;` |  |

**解説**

Layer からカーソル設定が呼び出された

必要であればカーソルの変更を行う。

---
