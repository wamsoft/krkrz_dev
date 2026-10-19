---
source_hash: 1b6341c1104b
---

# Creating Pre-rendered Font Data

## About pre-rendered fonts

A **pre-rendered font** ( `.tft` ) is font data converted to bitmaps in advance. You use it by mapping it to an actual font with [Font.mapPrerenderedFont](../reference/Font.md#mapprerenderedfont). Without it, Kirikiri renders the font at run time as needed.

Because it is created on the author's machine, it produces the same glyphs regardless of the player's environment. Since it is bitmap data, one file can cover only one size.

> **Note:**
> If you are not sure whether the author of the original font permits this kind of use (distributing bitmaps of many characters made from the font with your game and using them for text display), check with the author. Creating the file with only the characters you actually use may ease licensing concerns (see "Using the creation tool" below).

## How to create them

The creation tool bundled with Kirikiri 2 ( `krkrfont.exe` ) is not provided with Kirikiri Z. Use the **tftSave plugin** instead.

- `tftSave.dll` — a plugin that writes `.tft` files ( **Windows build (WINVER) only** ). It renders the font with GDI ( `Layer.drawGlyph` ) or DirectWrite ( `Layer.renderGlyph`, experimental ). Loading it replaces `Layer.drawGlyph` with the plugin's version (which draws a glyph and sets its metrics)
- Creation tool — scripts bundled with the tftSave source ( `startup.tjs` / `krkrfontex.tjs` in `src/plugins/tftSave/data/` ). It is a GUI tool that runs on the Kirikiri Z engine

Drawing with `.tft` ( `Font.mapPrerenderedFont` ) works in every build. Only creation is Windows-only.

## Using the creation tool

Launch Kirikiri Z (Windows build) with the `data/` folder of the tftSave source as the startup folder, and the creation tool's window opens. It requires the following plugins.

- `tftSave.dll`
- `win32dialog.dll` (for the window; the additional script `win32dialog.tjs` is also required)
- `csvParser.dll` (only when reading CSV files while scanning for used characters)

The fields are as follows (they can also be shown with the 「ヘルプ」 (Help) button in the window).

- **字体 (Font)** — Specifies the face, size, and style (bold / italic) of the font to output
- **出力 (Output)** — Specifies the `.tft` file to write
- **作成対象文字 (Target characters)** — Shows the list of characters to output. When using file scanning, press 「更新」 (Update) to reflect the results in the list
- **組み込みリスト (Built-in lists)** — Selects character sets to include (half-width ASCII / basic characters / symbols / jōyō kanji, the standard list of commonly used kanji)
- **ファイル走査 (File scan)** — Adds the characters used in text files to the targets
    - Scan methods: `Array` (every character, including comments) / `KAGParser` (only the text portions of KAG; excludes characters in comments and tags) / `CSVParser` / `CSV_UTF8` (reads CSV as UTF-8)
    - 「再帰検索追加」 (Add recursively) adds `*.txt` and `*.ks` files under the specified folder; 「ファイル追加」 (Add file) adds files one at a time
- **作成 (Create)** — Creates the `.tft`

Instead of every character the font contains, you can output **only the characters your game actually uses**.

## Creating from a script

You can also write the file directly from a script without the creation tool. Pass a callback that, for each character, returns a layer holding the glyph image and its metrics.

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

For API details, see [System.savePreRenderedFont](../reference/System.md#saveprerenderedfont) and the Layer plugin extensions ("プラグイン拡張: tftSave" in [Layer.md](../reference/Layer.md)). You can also read the character list of an existing `.tft` ( [loadPreRenderedFont](../reference/System.md#loadprerenderedfont) ) and modify glyph metrics ( [modifyPreRenderedFont](../reference/System.md#modifyprerenderedfont) ).
