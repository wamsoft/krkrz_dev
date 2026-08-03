# Live2DPlayer

描画用プレイヤー

Live2DModel と同じインターフェースに加えて描画用メソッドを持つ
生成には Live2DDevice が必要

## メンバー一覧

### コンストラクタ

- [Live2DPlayer](#live2dplayer)

### メソッド

- [clear](#clear)
- [load](#load)
- [loadModel](#loadmodel)
- [clone](#clone)
- [setScale](#setscale)
- [getScale](#getscale)
- [setMatrix](#setmatrix)
- [render](#render)
- [setVoiceValue](#setvoicevalue)
- [setVoiceWeight](#setvoiceweight)
- [setVoiceMode](#setvoicemode)
- [setBlinkingInterval](#setblinkinginterval)
- [setBlinkingSettings](#setblinkingsettings)
- [setBlinkingMode](#setblinkingmode)
- [setMosaicParam](#setmosaicparam)

---

### Live2DPlayer

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `device` | `&nbsp;` | Live2DDevice インスタンス |

**解説**

コンストラクタ

---

### clear

メソッド

**解説**

内容消去

---

### load

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `filename` | `&nbsp;` |  |

---

### loadModel

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `model` | `&nbsp;` | Live2DModel インスタンス |

**解説**

Live2DModel インスタンスからプレイヤーを生成

読み込み済みのモデルの状態を引き継ぐ

---

### clone

メソッド

**解説**

複製

---

### setScale

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `scale` | `&nbsp;` |  |

**解説**

表示スケール設定

---

### getScale

メソッド

---

### setMatrix

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `m11` | `&nbsp;` |  |
| `m12` | `&nbsp;` |  |
| `m13` | `&nbsp;` |  |
| `m21` | `&nbsp;` |  |
| `m22` | `&nbsp;` |  |
| `m23` | `&nbsp;` |  |

**解説**

表示マトリクス指定

---

### render

メソッド

**解説**

表示処理。OpenGLコンテキストで実行すると描画される

---

### setVoiceValue

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `voice` | `&nbsp;` |  |

---

### setVoiceWeight

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `weight` | `&nbsp;` |  |

---

### setVoiceMode

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `mode` | `&nbsp;` |  |

---

### setBlinkingInterval

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `interal` | `&nbsp;` |  |

---

### setBlinkingSettings

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `closing` | `&nbsp;` |  |
| `closed` | `&nbsp;` |  |
| `opening` | `&nbsp;` |  |

---

### setBlinkingMode

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `mode` | `&nbsp;` |  |

---

### setMosaicParam

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

---
