# よくある落とし穴 (TJS2 / エンジン API)

コアデモ (`src/core/data/*`) を書きながら実際に踏んだものを集めた実践メモです。
どれも「エラーにならず、黙って違う結果になる」たぐいのものなので、
症状から逆引きできるようにしています。

---

## TJS2 言語

### 文字の取り出しは `str[i]`。`str[i, 1]` は別物

`str[i, 1]` はカンマ式 `(i, 1)` が評価されて **常に `str[1]`** になります。
エラーにならないため、文字列処理の結果が「全部同じ文字」になって初めて気づきます。

```tjs
var s = "abcdef";
var c1 = s[2];        // "c"      … 正しい
var c2 = s.charAt(2); // "c"      … 範囲外でも例外にならない版
var c3 = s[2, 1];     // "b" (!)  … カンマ式なので常に s[1]
```

→ [文字列に対する操作](../../tjs2/string.md)

### `Math.floor()` などは実数を返す

整数に丸めたつもりでも型は実数のままなので、文字列連結すると
`"1.000000000000000"` のように出ます。表示や添字に使うなら `(int)` を付けます。

```tjs
var n = Math.floor(payload + 0.5);
dm("index = " + n);        // "index = 1.000000000000000"
dm("index = " + (int)n);   // "index = 1"
```

### 匿名関数は外側のローカル変数を捕捉しない

TJS2 の関数式はクロージャではありません。 コールバック内から使いたい値は
**メンバ変数か global** に置きます。

```tjs
function start() {
    var scene = this;                       // これはコールバックから見えない
    var t = new Timer(function() {
        scene.close();                      // → 例外: メンバ "scene" が見つかりません
    }, "");
}
```

```tjs
// メンバ変数にするか、global に置く
global.__scene = this;
var t = new Timer(function() { global.__scene.close(); }, "");
```

### 非数値文字列の `if` は常に偽

`if("abc")` は真になりません ( 数値化されて 0 になります )。
存在判定は `typeof` か `!== void` で行います。

```tjs
if (typeof System.appDataPath != "undefined") { ... }   // 正しい
if (obj.name !== void) { ... }                          // 正しい
```

---

## レイヤ / 描画

### `Layer.visible` の既定は false

生成しただけでは表示されません。 デモで「何も出ない」原因のほとんどがこれです。

### `hitType` は `htMask` と `htProvince` の 2 値

「矩形全面で当たる」設定は `htRect` ではなく **`hitThreshold = 0`** です。

### `drawText` の色は 24bit RGB

`0xRRGGBB` の 6 桁で指定します。 8 桁 ( `0xAARRGGBB` ) を渡すとシステムカラー
指定とみなされ、意図せず黒くなります。

### `Layer.invalidate` は子レイヤを無効化しない

子は「親から切り離されるだけ」で生き残り、描画も黙って成功します。
サブツリーごと捨てるなら再帰的に invalidate してください
( demolib の `invalidateLayerTree` が実装例 )。

### `operateRect` の乗算系は `holdAlpha`

`omMultiplicative` 等は転送先のアルファを 0 にしてしまうため、
`ltAlpha` レイヤに対して使うと真っ黒になります。 転送先を保つなら
`holdAlpha = true` を指定します。

### 更新矩形は必要最小限に

`update()` を引数なしで呼ぶ ( = 全面 ) 癖があると、静止画面でも毎フレーム
画面全体を GPU へ転送し続けます。 「消す矩形」「描く矩形」だけを update すれば
転送量は桁で変わります ( 実測はコアデモ `perf_stats` / 解説は
`src/core/doc/ScreenTransfer.md` )。

---

## ビルドによって有無が変わる API

同じスクリプトを Windows ネイティブ ( WINVER ) ビルドと SDL3 ビルドの双方で
動かすなら、次のものは `typeof` で存在を確認してから使います。

| API | 状況 |
|---|---|
| `System.appDataPath` / `personalPath` | WINVER 限定。保存先は `System.dataPath` を使う |
| `System.desktopLeft/Top/Width/Height` | WINVER 限定。解像度だけなら `System.screenWidth/Height` |
| `System.urldecode` / `readRegValue` 等 | Windows 拡張。SDL3 ビルドには無い |
| `System.setMemoryOverlay` / `setPadOverlay` | フラグは全ビルド共通だが、描画するのは OGL 系 / SDL の DrawDevice ( WINVER 既定の D3D11 では出ない ) |
| `Layer.imeMode` / `setAttentionPoint` | 値は全ビルドで保持されるが、実際に効くのは WINVER |
| `Window.setZoom` | 挙動が異なる ( SDL3 はウィンドウがリサイズされる。[Window.setZoom](../../reference/Window.md#setzoom) 参照 ) |
| `Dialog` 系 / `WebServer` | ビルドオプション ( `KRKRZ_USE_ELEMENTS` / `KRKRZ_REPL_WEB` ) 次第 |

---

## 入力

### 文字入力は `onKeyPress`、キーは `onKeyDown`

`onKeyDown` は仮想キーコード、`onKeyPress` は文字そのもの ( IME 確定文字を含む )
を扱います。 文字を集めたい処理を `onKeyDown` で書くと IME 入力が取れません。

### Elements パネル表示中はパッド入力がパネルに吸われる

`VK_PAD*` はパネルのウィジェット操作 ( 十字 = フォーカス移動 / A = 決定 ) に
消費され、ゲーム側の `onKeyDown` には届きません。 必ずゲームで受けたいボタンは
[Dialog.registerHotKey](../../reference/Dialog.md#registerhotkey) で確保すると
パネルをバイパスします ( コアデモ `pad_advanced` に ON/OFF の比較あり )。

### アナログスティックは無操作でも 0 にならない

`System.getPadAxis` は無操作でも ±0.05 程度を返します。 ゲーム側で
デッドゾーン処理を入れてください。

### `Agent.keyPress` では文字入力イベントが出ない

注入されるのはキーイベントだけです ( 文字は OS のテキスト入力経路を通るため )。
自動テストで文字を入れるなら Elements の入力欄 + `Agent.text` を使います。

---

## その他

### `Clipboard.asText` はテキストが無いと void

空文字列ではなく void が返ります。 `if (v === void)` で判定してください。

### JSON の組み立てにプラグインを前提にしない

`Scripts.toJSONString` / `evalJSON` は json プラグインの拡張です。 コア機能だけで
完結させたい場合は手組みするか、`Dialog.dictToJson` ( Elements 有効時 ) を使います。

---

## 関連

- [TJS2 言語仕様](../../tjs2/index.md)
- [クラスリファレンス](../../reference/System.md)
- コアデモ ( `src/core/data/` ) — 各デモの `readme.txt` に、そのデモで踏んだ
  注意点を個別に書いてあります
