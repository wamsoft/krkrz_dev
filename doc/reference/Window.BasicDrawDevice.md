# Window.BasicDrawDevice

Window.BasicDrawDevice クラスは、このインスタンスを [Window.drawDevice](Window.md#drawdevice) に登録して使用するための DrawDevice で、標準的な描画機能を提供します。

## メンバー一覧

### コンストラクタ

- [BasicDrawDevice](#basicdrawdevice)

### プロパティ

- [interface](#interface)

### メソッド

- [recreate](#recreate)

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
