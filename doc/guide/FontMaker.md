# レンダリング済みフォントデータの作成

## レンダリング済みフォントについて

**レンダリング済みフォント** ( `.tft` ) は、フォントをあらかじめビットマップに変換しておいたデータです。[Font.mapPrerenderedFont](../reference/Font.md#mapprerenderedfont) で実際のフォントに割り当てて使います。使わない場合、吉里吉里は必要に応じて実行時にフォントを描画します。

制作者側の環境で作成するので、プレーヤ側の環境に左右されずに同じ字形を出せます。ビットマップなので、1 つのファイルで扱えるのは 1 つの大きさだけです。

> **Note:**
> 元のフォントの著作者が、このような用途 ( フォントから作った多数の文字のビットマップをゲームとともに配布し、文字表示に使うこと ) を許可しているかどうか分からない場合は、著作者に確認してください。使う文字だけに絞って作成すると、ライセンス上の問題が緩和される場合があります ( 下の「作成ツールの使い方」 )。

## 作成手段

吉里吉里2 に付属していた作成ツール ( `krkrfont.exe` ) は吉里吉里Z では提供していません。代わりに **tftSave プラグイン** で作成します。

- `tftSave.dll` — `.tft` を書き出すプラグイン ( **Windows ビルド ( WINVER ) 専用** )。フォントの描画には GDI ( `Layer.drawGlyph` ) か DirectWrite ( `Layer.renderGlyph`、試験的 ) を使います。読み込むと `Layer.drawGlyph` がこのプラグインのもの ( グリフを描いて寸法を設定する ) に置き換わります
- 作成ツール — tftSave のソースに同梱されているスクリプト ( `src/plugins/tftSave/data/` の `startup.tjs` / `krkrfontex.tjs` )。吉里吉里Z 本体で動く GUI ツールです

`.tft` の描画 ( `Font.mapPrerenderedFont` ) は全ビルドで使えます。作成だけが Windows 専用です。

## 作成ツールの使い方

tftSave のソースの `data/` フォルダを起動フォルダにして吉里吉里Z ( Windows ビルド ) を起動すると、作成ツールの画面が開きます。実行には次のプラグインが必要です。

- `tftSave.dll`
- `win32dialog.dll` ( 画面。追加スクリプト `win32dialog.tjs` も必要 )
- `csvParser.dll` ( 使用文字の走査で CSV を読む場合のみ )

各項目は次のとおりです ( 画面の「ヘルプ」ボタンでも表示できます )。

- **字体** — 出力するフォントのフェイス・サイズ・修飾 ( 太字 / 斜体 ) を指定します
- **出力** — 出力する `.tft` ファイルを指定します
- **作成対象文字** — 出力する文字の一覧が表示されます。ファイル走査を使う場合は「更新」を押すと一覧に反映されます
- **組み込みリスト** — 作成対象に含める文字のセットを選びます ( 半角 ASCII / 基本文字 / 記号類 / 常用漢字 )
- **ファイル走査** — テキストファイルの中で使われている文字を作成対象に加えます
    - 走査方法: `Array` ( コメントも含めすべての文字 ) / `KAGParser` ( KAG のテキスト部分だけ。コメントやタグの文字は除く ) / `CSVParser` / `CSV_UTF8` ( CSV を UTF-8 として読む )
    - 「再帰検索追加」で指定フォルダ以下の `*.txt` と `*.ks` を、「ファイル追加」で 1 ファイルずつ追加します
- **作成** — `.tft` を作成します

フォントが持つすべての文字ではなく、**ゲームで実際に使う文字だけ**を出力できます。

## スクリプトから作成する

作成ツールを使わずに、スクリプトから直接書き出すこともできます。文字ごとに、グリフの画像と寸法を持ったレイヤを返すコールバックを渡します。

```tjs
Plugins.link("tftSave.dll");
var layer = new Layer(win, win.primaryLayer);
layer.font.face = "ＭＳ ゴシック";
layer.font.height = 24;
var chars = [];
for (var c = 0x20; c < 0x7f; c++) chars.add(c);
System.savePreRenderedFont("ascii24.tft", chars, function(ch) {
    layer.drawGlyph(ch);   // グリフを描き、寸法 ( blackbox_x 等 ) を layer に設定する
    return layer;
});
```

API の詳細は [System.savePreRenderedFont](../reference/System.md#saveprerenderedfont) と、Layer のプラグイン拡張 ( [Layer.md](../reference/Layer.md) の「プラグイン拡張: tftSave」 ) を参照してください。作成済みの `.tft` の文字一覧の読み出し ( [loadPreRenderedFont](../reference/System.md#loadprerenderedfont) ) と、グリフの寸法の修正 ( [modifyPreRenderedFont](../reference/System.md#modifyprerenderedfont) ) もできます。
