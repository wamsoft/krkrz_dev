# 読み上げ ( スクリーンリーダー )

## 読み上げについて

吉里吉里Z のゲーム画面は、OS のスクリーンリーダー ( Windows のナレーター、macOS の VoiceOver、Linux の Orca など ) から読めます。画面の部品の名前・役割・値・状態を OS のアクセシビリティ API ( UI Automation / NSAccessibility / AT-SPI ) へ渡すので、目の見えない人や見えにくい人が、読み上げを聞きながらキーボードで遊べます。

対応しているのはデスクトップ ( Windows / macOS / Linux ) の通常ビルドです。SDL3 版・Windows ネイティブ ( WINVER ) 版のどちらでも動きます。ブラウザ ( Web ) 版にはこの口がありません。

スクリーンリーダーに渡す内容は、次の 3 つから集まります。

| 出どころ | 何もしなくても読まれるか | 使う口 |
|---|---|---|
| Elements のダイアログ / パネル | 読まれる | 画面 JSON の `"a11y"` キーで補う |
| Layer に描いた UI ( 選択肢・メニュー・設定画面など ) | 読まれない | [ElementsDialog.setGameA11y](../reference/ElementsDialog.md#setgamea11y) か [ElementsDialog.a11yLayers](../reference/ElementsDialog.md#a11ylayers) |
| 任意の文 ( 本文・結果の通知など ) | — | [ElementsDialog.announce](../reference/ElementsDialog.md#announce) |

スクリーンリーダーが繋がるまでは何もしません。繋がっていない間の負荷はほぼありません。

動く例はコアデモ `src/core/data/a11y` ( ギャラリーの「読み上げ ( スクリーンリーダー )」 ) にあります。

## Elements のダイアログ

[ダイアログ](ElementsDialog.md) で出した画面は、そのまま読まれます。ボタンの文字・ラベル付きの行・グループの見出しなどから名前を、部品の種類から役割 ( ボタン・チェックボックス・スライダー… ) を、表示中の値から値を、本体が自動で決めます。入力欄は文字・単語・行の単位で読め、キャレットの移動も追えます。

自動で足りないところは、部品に `"a11y"` キーを足して補います。文字列なら名前、辞書なら詳しく指定します。

```jsonc
{ "type": "sprite_button", "id": "btn_save", "a11y": "セーブ" }
{ "type": "slider", "id": "vol_bgm",
  "a11y": { "label_id": "cfg.bgm", "description_id": "cfg.bgm.help", "value_var": "vol_bgm_disp" } }
{ "type": "label", "text_var": "msg_body", "a11y": { "live": "polite" } }
{ "type": "image", "a11y": { "hidden": true } }
```

| キー | 意味 |
|---|---|
| `label` / `label_id` | 名前 ( `_id` は文字列表から引くので、言語の切り替えに追従します ) |
| `description` / `description_id` | 補足の説明 |
| `role` | 役割の上書き ( `"heading"` / `"status"` など ) |
| `value_var` | 表示する値を持つ変数の名前 |
| `live` | `"polite"` / `"assertive"`。`text_var` が変わると読み上げます |
| `hidden` | 部品を子ごと読み上げから外します ( 飾りの画像など ) |

画面の最上位に `"a11y": { "title": "…" }` を置くと、画面に入ったときにその名前で読まれます。

絵だけのボタン ( `sprite_button` / `atlas_*` ) は文字を持たないので、`"a11y"` で名前を付けてください。

## Layer に描いた UI を読ませる

Layer に描いた UI は Elements の外にあるので、何もしなければ読まれません。読ませる方法は 2 つあり、併用もできます。

| 方法 | 向いている場面 | 手間 |
|---|---|---|
| [a11yLayers](../reference/ElementsDialog.md#a11ylayers) | Layer のフォーカス連鎖 ( `focusable` ) で操作する UI。ボタンを 1 枚ずつ Layer で作っている場合 | 小さい。真にするだけで載り、Layer にメンバを足して補う |
| [setGameA11y](../reference/ElementsDialog.md#setgamea11y) | 1 枚の Layer に複数の項目を描いている UI ( 選択肢・一覧・メニュー ) や、フォーカスを自前で管理している UI | ノードの表をスクリプトで作って渡す |

### フォーカス連鎖の Layer を自動で載せる ( a11yLayers )

```tjs
ElementsDialog.a11yLayers = true;
```

これで、フォーカス連鎖に入っている Layer ( `focusable` かつ `joinFocusChain` ) が読み上げツリーに載ります。名前は [hint](../reference/Layer.md#hint)、役割はボタンです。フォーカスは [Window.focusedLayer](../reference/Window.md#focusedlayer) に従います。

スクリーンリーダーで「押す」と、本体はその Layer にフォーカスを移してから Enter キーを送ります。Enter で押せる作りにしておけば、ほかに何も要りません。

読まれ方は、Layer にメンバを生やして変えます。

```tjs
class AutoModeButton extends Layer
{
    var a11yRole = "check_box";   // クラスで持たせるときは var で宣言する
    var checked = false;          // check_box は checked メンバから状態を読む
    // ...
}

heading.a11yName = "セーブとロード";   // フォーカスできない見出しも載る
heading.a11yRole = "heading";
deco.a11yHidden  = true;               // 飾りは子ごと外す
```

| メンバ | 内容 |
|---|---|
| `a11yName` / `a11yRole` | 名前 / 役割。どちらかがあれば、フォーカスできない Layer も載ります |
| `a11yValue` / `a11yDescription` | 値 / 補足の説明 |
| `a11yStates` | 配列か `"checked,selected"` の形の状態 |
| `a11yHidden` | 真なら子ごと外します |
| `onA11yAction(action, arg)` | スクリーンリーダーからの操作を受けます。false を返すと既定の処理も行います |

値を持つ部品 ( スライダーなど ) の増減は、既定の処理がありません。`onA11yAction` で受けてください。

```tjs
class VolumeSlider extends Layer
{
    var a11yRole = "slider";
    var value = 50;
    property a11yValue { getter() { return value + "%"; } }

    function onA11yAction(action, arg)
    {
        switch (action) {
        case "increment": setValue(value + 10); return true;
        case "decrement": setValue(value - 10); return true;
        case "set_value": setValue(+arg); return true;
        }
        return false;   // focus は既定の処理 ( focus() ) に任せる
    }
    // ...
}
```

読み直しは最大 150ms に 1 回です ( フォーカスが変わったときはすぐ )。`a11yValue` などを property にする場合は軽く保ってください。Layer の `name` が読み上げツリーの id ( `layer:<name>` ) になるので、付けておくと確認のときに指しやすくなります。

### ノードの表を渡す ( setGameA11y )

選択肢のように、1 枚の Layer に複数の項目を描いている場合は、項目ごとのノードをスクリプトが作って渡します。

```tjs
function pushChoices()
{
    var nodes = [ %[ id:"choices", role:"list", name:"どうする?" ] ];
    for (var i = 0; i < choices.count; i++) {
        nodes.add(%[
            id:"choice" + i, role:"list_item", name:choices[i], parent:"choices",
            states:(i == current) ? "focusable,selected" : "focusable",
            rect:[ 100, 400 + i * 60, 600, 48 ]   // primary layer の座標
        ]);
    }
    // 第 2 引数はフォーカスを置くノード。選択肢を操作している間だけ渡す
    ElementsDialog.setGameA11y(nodes, choiceLayer.focused ? "choice" + current : void);
}

ElementsDialog.onGameA11yAction = function(id, action, arg) {
    var i = +id.substr(6);                       // "choice<N>"
    if (action == "focus") { current = i; redraw(); pushChoices(); }
    else if (action == "click") { current = i; decide(); }
} incontextof this;
```

- 表は呼ぶたびに丸ごと差し替わります。差分は本体が取るので、選択が変わるたびに全体を渡してかまいません。
- 本体はフォーカスや値を自分では動かしません。スクリーンリーダーから `focus` / `click` が来たら、ゲームの状態を変えてから `setGameA11y` を呼び直します。
- `rect` を付けると、スクリーンリーダーがその位置を枠で示します ( ナレーターの青い枠など )。ウィンドウの拡大縮小とレターボックスは本体が換算します。
- 第 2 引数の `focus` を渡している間は、スクリーンリーダーのフォーカスがそのノードに固定されます。`a11yLayers` と併用するときは、自前の UI を操作している間だけ渡してください。
- 自前で載せる Layer には `a11yHidden = true` を立て、`a11yLayers` の自動と二重に載らないようにします。
- ゲーム本体のノードはダイアログより下に並びます。モーダルなダイアログの表示中は隠れます。

使える役割・状態・キーの一覧は [setGameA11y](../reference/ElementsDialog.md#setgamea11y) を参照してください。

## 任意の文を読ませる ( announce )

```tjs
ElementsDialog.announce("セーブしました");
ElementsDialog.announce("体力が残りわずかです", true);   // 割り込み
```

フォーカスの移動では読まれないこと ( 本文・操作の結果・状態の変化 ) を読ませます。最前面のダイアログか、ダイアログが無ければゲーム本体の読み上げ欄 ( live region ) に入ります。同じ文を続けて渡しても毎回読みます。

本文を読ませるかどうかを、スクリーンリーダーが繋がっているかで切り替える場合は、[a11yActive](../reference/ElementsDialog.md#a11yactive) を読む直前に見るか、[onA11yActiveChanged](../reference/ElementsDialog.md#ona11yactivechanged) で受けてください。Windows では、ウィンドウが前面になるまで接続済みになりません。

KAG3 には読み上げの拡張を入れていません。KAG 系の作品は、作品側のスクリプトでメッセージの本文を `announce` に渡し、選択肢を `setGameA11y` で載せて対応します。

## 確かめ方

- **実際に聞く**: ゲームを起動してからナレーター ( Windows は Win + Ctrl + Enter ) などを起動し、ウィンドウを前面にします。
- **REPL で見る**: `-replfile` などで REPL を動かすと、スクリーンリーダー無しでも確かめられます ( [REPL](../topics/core/repl.md) )。

| コマンド | 内容 |
|---|---|
| `.a11y` | 読み上げツリー ( スクリーンリーダーに見えるもの ) を JSON で表示 ( [Agent.a11yTree](../reference/Agent.md#a11ytree) ) |
| `.a11ylog [N]` | 読み上げログ。おおよそ何と読むかを 1 行ずつ ( [Agent.a11yLog](../reference/Agent.md#a11ylog) ) |
| `.a11ydo <node> <action> [arg]` | スクリーンリーダーと同じ経路で操作する ( [Agent.a11yAction](../reference/Agent.md#a11yaction) ) |
| `.say <text>` | announce |

読み上げログは次のような行になります。

```
[focus] 南へ行く, list item, selected
[polite] 「南へ行く」を選びました
[focus] 音量, slider, 50%
[value] 音量, 60%
```

## 注意点

- `setGameA11y` / `a11yLayers` / `onGameA11yAction` などは**クラス全体に効く**設定です。場面を抜けるときは `clearGameA11y()` / `a11yLayers = false` で戻してください。
- 対象はメインウィンドウだけです。`showModalJson` が開く専用ウィンドウと、2 枚目以降の `Window` にはまだ対応していません。
- 入力欄の変換中 ( IME で確定する前 ) の文字は、アプリ側からは出しません。変換中の文字や候補は OS の IME 自体がスクリーンリーダーへ伝えます。入力欄が持つのは確定した文字だけです。
- ビルドオプション `KRKRZ_USE_A11Y` ( デスクトップの通常ビルドは既定 ON ) を OFF にすると、OS へは出なくなります。REPL での確認の口は残ります。
- 実行時に OS へ出したくない場合は `ElementsDialog.a11yMode = "off"` にします。

仕様の全体と設計時の記録は [アクセシビリティ ( スクリーンリーダー ) 対応](../specification/accessibility.md) にあります。

## 関連 API

- [ElementsDialog](../reference/ElementsDialog.md): `announce` / `a11yActive` / `onA11yActiveChanged` / `a11yMode` / `a11yLabel` / `setGameA11y` / `clearGameA11y` / `onGameA11yAction` / `a11yLayers`
- [Layer](../reference/Layer.md): Layer に生やす読み上げ用のメンバ ( クラス説明 )
- [Agent](../reference/Agent.md): `a11yTree` / `a11yLog` / `a11yAction`
