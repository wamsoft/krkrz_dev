# Pad

Pad拡張

## メンバー一覧

### メソッド

- [registerExEvent](#registerexevent)

---

### registerExEvent

メソッド

**解説**

拡張イベントを有効にする（登録失敗で例外が発生）

拡張イベントとして以下が発生：
onClose  閉じるボタンが押された

※borderStyleなどの変更によりウィンドウが作り直されるとイベントが発生しなくなるので注意
⇒その場合は再度registerExEvent()を呼ぶ

---
