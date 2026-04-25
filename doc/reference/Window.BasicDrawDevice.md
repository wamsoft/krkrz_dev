# Window.BasicDrawDevice

Window.BasicDrawDevice クラスは、このインスタンスを [Window.drawDevice](Window.md#drawdevice) に登録して使用するための DrawDevice で、標準的な描画機能を提供します。

## メンバー一覧

### コンストラクタ

- [BasicDrawDevice](#basicdrawdevice)

### プロパティ

- [interface](#interface)

### メソッド

- [recreate](#recreate)

### イベント

- [onDisplayRotate](#ondisplayrotate)

---

### BasicDrawDevice

コンストラクタ

**解説**

BasicDrawDevice オブジェクトの構築

Window.BasicDrawDevice クラスのオブジェクトを構築します。

初期状態で Window.drawDevice にはこのクラスのインスタンスが登録されているので、新たに登録する必要はありません。

---

### interface

プロパティ \ アクセス: `r`

**解説**

インターフェースオブジェクトを取得

プラグインなどで DrawDevice オブジェクトを利用するためにあります。

---

### recreate

メソッド

**解説**

内部デバイス再生成

内部デバイスの再生成を行います。

通常使用することはありません。

---

### onDisplayRotate

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `orientation` | `&nbsp;` | 画面の向き( orientation ) です。<br>以下のいずれかの値になります。<br>oriUnknown (取得失敗/不明), oriPortrait(縦向き), oriLandscape(横向き) |
| `angle` | `&nbsp;` | 角度です。<br>角度 ( angle ) は、0、90、180、270、-1 のいずれかで、取得できなかった時は-1となります。<br>角度は、そのデバイスデフォルトからの回転角なので、縦向きのデバイスでは縦向きで0となります。<br>通常のデバイスだと、横向きで0が多ようです。<br>縦向きが0になるのは最近の8インチタブレットなどで、縦向きが標準の向きとなっているものです。 |
| `bpp` | `&nbsp;` | bits per pixel です。 |
| `width` | `&nbsp;` | 画面の幅です。 |
| `height` | `&nbsp;` | 画面の高さです。 |

**解説**

画面が回転されたとき(1.1.0以降)

画面が回転されたときに呼び出されるイベント関数を表します。

**関連:** [Window.onDisplayRotate](Window.md#ondisplayrotate) / [Window.displayOrientation](Window.md#displayorientation) / [Window.displayRotate](Window.md#displayrotate)

---
