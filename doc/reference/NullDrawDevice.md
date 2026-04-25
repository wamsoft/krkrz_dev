# NullDrawDevice

NullDrawDevice クラスは、このインスタンスを [Window.drawDevice](Window.md#drawdevice) に登録して使用するための DrawDevice で、何も描画しないダミー実装を提供します。

ヘッドレス実行や、自前の描画パスを完全に外側で制御したいときに使用します。

## メンバー一覧

### コンストラクタ

- [NullDrawDevice](#nulldrawdevice)

### プロパティ

- [interface](#interface)

### メソッド

- [recreate](#recreate)

---

### NullDrawDevice

コンストラクタ

**解説**

NullDrawDevice オブジェクトの構築

NullDrawDevice クラスのオブジェクトを構築します。

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
