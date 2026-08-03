# Live2DDevice

## メンバー一覧

### コンストラクタ

- [Live2DDevice](#live2ddevice)

### メソッド

- [onBeginScene](#onbeginscene)
- [onEndScene](#onendscene)
- [prepareShaders](#prepareshaders)

---

### Live2DDevice

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `oglbase` | `&nbsp;` | GetProcAddress を保持してるオブジェクト<br>以下のいずれかを指定できる:<br>- krkrgles プラグインが提供する OpenGL コンテキストオブジェクト<br>- 新しい吉里吉里Z の OGLDrawDevice (本体組み込みの OpenGL 描画デバイス)<br>現在の OGLコンテキストに対して初期化されます |

---

### onBeginScene

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `width` | `&nbsp;` |  |
| `height` | `&nbsp;` |  |

**解説**

全体の描画開始時に1度だけ呼び出す

※生成時のコンテキストで呼び出すこと

---

### onEndScene

メソッド

**解説**

全体の描画完了時に1度だけ呼び出す

---

### prepareShaders

メソッド

**解説**

シェーダの事前コンパイルを実行する

未呼び出しの場合は初回描画時にまとめてコンパイルされ
数秒程度の待ち時間が発生するため、起動時などに呼んでおくことを推奨
※生成時のコンテキストで呼び出すこと

---
