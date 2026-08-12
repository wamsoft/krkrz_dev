# フォントシステム

吉里吉里Z のフォントまわり (登録・名前解決・描画・検索) の総合ガイドです。
フォントの用意から登録手順、各 API の使い分けまでをここにまとめています。

## 全体構成

```
  フォントファイル (.ttf/.otf/.ttc)
    │  ①exe 埋め込み (resource/)      ②data 外だし + fonts.json (宣言・遅延)
    │  ③実行時登録 (Font.addFont 等)  ④システムフォント (Windows GDI)
    ▼
  ┌───────────────────────────────────────────────┐
  │ FontSystem (名前→ストレージ対応・遅延ロード)  │←─ fonts.json
  │ FontStream (共有オンメモリバッファ / 1フォント1部) │
  └───────────────┬───────────────────────────────┘
                  ▼
  ┌───────────────────────────────────────────────┐
  │ glyphware (統一フォントエンジン:               │
  │  FreeType + HarfBuzz + BiDi / レジストリ・検索) │
  └───┬───────────────┬───────────────┬───────────┘
      ▼               ▼               ▼
  Layer.drawText   Layer.draw     ThorVG テキスト
  (ラスタライザ     GlyphwareText  (Elements UI /
   3種切替)        (シェイピング)   layerExVector)
```

- フォントのバイトデータは **`FontStream` 共有バッファに 1 フォント 1 部**だけ
  読み込まれ、drawText・Elements UI・layerExVector・プラグインのすべてが同じ
  バッファを共有します (XP3 内フォント対応・オンメモリ)。
- グリフ生成・シェイピング・メタデータ検索は統一フォントエンジン
  **glyphware** に集約されています。従来の GDI / FreeType ラスタライザも
  互換のためそのまま残っています。

## ラスタライザ

`Layer.drawText` の文字画像を作るエンジンは [Font.rasterizer](../reference/Font.md#rasterizer)
(静的プロパティ) で切り替えられます。

| 値 | Windows ネイティブ版 (WINVER) | SDL 版ほか |
|---|---|---|
| 0 | FreeType | FreeType **(既定)** |
| 1 | GDI **(既定)** | glyphware |
| 2 | glyphware | - |

- 既定値は従来互換のまま (WINVER=GDI / その他=FreeType) です。
- **glyphware ラスタライザ**は classic とレイアウト互換 (セル送り・影・縁取り・
  下線/取消線・VS15/16 など) を保ちながら、フォールバック連鎖・カラー絵文字・
  合成 bold/italic に対応します。既知の差分: アンチエイリアス指定 off でも
  常に AA 描画になります (`font.hinting` / `font.antialiased` は無視)。

## フォントの用意と登録手順

### ① exe 埋め込み (resource/)

エンジンの `resource/` フォルダに置いた `.ttf/.otf` はビルド時に実行ファイルへ
埋め込まれ、起動時から使用できます (既定同梱: Noto Sans JP / Roboto /
Noto Emoji / elements_basic)。ゲーム側で増やすものではなく、エンジン既定
フォントの置き場所です。埋め込みフォントはストレージ名
`resource://./ファイル名` でもアクセスできます。

### ② data 外だし + fonts.json (推奨)

大きいフォント (カラー絵文字・CJK バリエーション等) は data フォルダに置き、
**`fonts.json` で宣言**します。起動時には名前だけ登録され、実ファイルは
**初回使用時に遅延ロード**されるため起動時間・メモリに影響しません。

```json
{
  "version": 1,
  "fonts": [
    { "file": "fonts/notocoloremoji.ttf",
      "family": "Noto Color Emoji",
      "subfamily": "Regular",
      "aliases": ["Noto Color Emoji Regular"],
      "weight": 400,
      "scripts": ["Zsye"],
      "flags": ["emoji", "color"],
      "ranges": [[9728, 9983], [126976, 129791]] }
  ]
}
```

- `fonts.json` は **data フォルダ (プロジェクトルート) 直下**に置きます。
- `file` 以外はすべて任意です。`subfamily` / `fullName` / `postScriptName` /
  `weight` (100-900) / `width` (1-9) / `italic` / `faceIndex` / `languages` /
  `aliases` / `flags` (`emoji` `color` `monospace`) / `ranges` (収録コード
  ポイント区間) を宣言できます。
- 宣言した `scripts` / `ranges` / スタイルは [Font.queryFonts](../reference/Font.md#queryfonts)
  が**フォントファイルを開かずに**検索へ使います。
- **生成ツール**で自動生成できます (要 `pip install fonttools`):

```
python tools/fontgen/gen_fonts_json.py \
    --fonts-dir <データ>/fonts --root <データ> --out <データ>/fonts.json
```

生成器は family を純粋な family 名にし、classic ラスタライザの face 名規約
(「family subfamily」連結、例 "Noto Color Emoji Regular") を `aliases` に
出力するため、どちらの名前でも解決できます。

同梱例: コアデモの `src/core/data/fonts` には Noto Color Emoji に加えて
RTL 用の **Noto Sans Arabic / Noto Sans Hebrew** を同梱しています
(SDL 版含む全プラットフォームでアラビア語/ヘブライ語が同一表示)。他の
スクリプトも Noto ファミリ (https://notofonts.github.io/) から取得すると
埋め込みの Noto Sans JP / Roboto と見た目が揃います
(候補: Noto Sans Thai / Devanagari / KR / SC / TC など。詳細は
`src/core/data/fonts/README.md`)。

### ③ 実行時登録 (スクリプト)

- [Font.addFont](../reference/Font.md#addfont)`(storage)` — フォントファイルを
  即時ロードして登録し、収録フェイス名の配列を返します。
- [Font.registerFontFile](../reference/Font.md#registerfontfile)`(storage[, family])`
  — `family` を指定すると **ファイルを開かない遅延登録** (fonts.json 1 エントリ
  相当) になります。省略時は addFont と同じ即時ロードです。

```tjs
Font.addFont("mygame_font.ttf");                       // 即時ロード
Font.registerFontFile("fonts/big_cjk.ttf", "MyCJK");   // 遅延 (初回使用時に読む)
```

### ④ システムフォント (Windows ネイティブ版)

WINVER では OS にインストール済みのフォントを**フォント名だけで**使えます
(GDI 名前解決)。glyphware 系の経路 (rasterizer=2 / drawShapedText /
Elements) でも `"メイリオ"` `"MS PGothic"` 等の名前がそのまま解決され、
TTC のフェイス番号も正しく選択されます。`addFont` プラグインで登録した
埋め込みフォントも同様に名前で使えます。

## フォント名の規約と解決順序

`Font.face` や `fontKey` に書いた名前 (カンマ区切りで**フォールバック連鎖**)
は、次の順で解決されます:

1. **fonts.json / registerFontFile の宣言名** (family / aliases) → ストレージ
2. **ストレージパス** (`fonts/foo.ttf`、`resource://./…` など実在するもの)
3. **(WINVER) インストール済み GDI フォント名** (addFont 登録分を含む)
4. 解決できない名前は既定フェイスへフォールバック

classic (FreeType) の face 名は「family subfamily」連結 (例 "Noto Sans JP
Regular") である点に注意してください。fonts.json 生成器が連結名を alias に
出すので、通常はどちらの表記でも動きます。

## 絵文字

[Font.emojiMode](../reference/Font.md#emojimode) (0=無効 / 1=モノクロ / 2=カラー)
で絵文字グリフの扱いを選びます。

- カラー絵文字フォント (既定 "Noto Color Emoji") は fonts.json の外だし宣言が
  前提です。未配置の場合は同梱モノクロ絵文字 (Noto Emoji) へ自動フォール
  バックします (豆腐にはなりません)。
- 既定フォント名は `Font.emojiFaceName` / `Font.colorEmojiFaceName` で変更可能。
- WINVER の既定ラスタライザ (GDI) は絵文字グリフを持たないため、
  `Font.rasterizer = 0` (FreeType) または `= 2` (glyphware) にして使います。
- VS15 (テキスト表示) / VS16 (絵文字表示) のバリエーションセレクタに対応します。

## フォント検索とメタデータ

登録済みフォントは [Font.queryFonts](../reference/Font.md#queryfonts) で
リッチ検索できます (条件はすべて省略可、結果はランク順の辞書配列):

```tjs
// カラー絵文字フォントを探す
var r = Font.queryFonts(%[ containsText : "😀", color : 1 ]);
// 日本語を収録した太字を探す
var r = Font.queryFonts(%[ containsText : "あ", weight : 700 ]);
```

単一フォントの SFNT メタデータは [Font.getFontInfo](../reference/Font.md#getfontinfo)
で取得できます (family / subfamily / weight / color 等)。fonts.json で
宣言済みの情報はフォントを開かずに応答します。

## 多言語シェイピング描画 (glyphware)

`Layer.drawText` は従来どおり「1 文字ずつのセル送り」ですが、
[Layer.drawShapedText](../reference/Layer.md#drawshapedtext) は
**HarfBuzz シェイピング + BiDi** による本格的な多言語 1 行描画を行います:

- アラビア文字の連結・合字・カーニング、ヘブライ/アラビアの右→左 (BiDi)
- コードポイント単位のフォールバック連鎖 (Font.face カンマ区切り)
- カラー絵文字、合成 bold/italic、下線/取消線、回転 (angle)
- 描画属性は [Font](../reference/Font.md) オブジェクト 1 個で渡します
  (void = レイヤ自身の font / 文字列 = face のみ差し替え)

[Layer.drawShapedTextArea](../reference/Layer.md#drawshapedtextarea) は
矩形内への**簡易折り返し描画**です。`\n` の明示改行、英語等のワード単位
折り返し、日本語の文字単位折り返し (行頭/行末の簡易禁則付き)、行揃え
(左/中央/右)、行間調整に対応します。

`count` 引数 (drawShapedText / drawShapedTextArea 共通) に 0 以上を渡すと
先頭 count 「文字」だけを描画でき、タイプライタ表示に使えます。この
「文字」は描画時に一塊として扱われる**クラスタ単位** (合字・結合文字・
絵文字 ZWJ シーケンスで 1) で、総数は
[Layer.shapedTextCount](../reference/Layer.md#shapedtextcount) で取得します。
全文をシェイピング/折り返し確定してから先頭部分だけを描くため、表示途中で
字形や折り返し位置が変化 (リフロー) しません。

計測は [Layer.measureShapedText](../reference/Layer.md#measureshapedtext)
で行います (インク境界と ascent/descent、クラスタ数を返します)。

動作サンプル: コアデモギャラリー (`src/core/data`) の
「多言語シェイピング (glyphware)」シーンで、アラビア語/ヘブライ語 (RTL)・
BiDi 混在・絵文字混在・計測・矩形内折り返し・タイプライタ表示の実例を
確認できます。

## UI 系 (Elements) と layerExVector のフォント

- **Elements ダイアログ** ([ダイアログ](Dialog.md)) のテキストは glyphware で
  描画されます。テーマフォントには埋め込みフォント (Roboto / Noto Sans JP /
  Noto Emoji) が自動登録され、追加フォントは
  `Dialog.registerFont(family, storage[, weight, slant, stretch])` /
  `Dialog.registerFontDir(dir)` で登録します。ストレージパス (XP3 内・
  `resource://` 含む) をそのまま渡せます。
- **layerExVector プラグイン** (`GdiPlus.loadFont(storage, name)`) も同じ
  エンジンを共有します。`resource://./notosansjp-regular.otf` のように
  本体埋め込みフォントを指定でき、フォントを同梱しなくてもアウトライン
  文字を描画できます。
- どの経路も同一フォントは FontStream の共有バッファ 1 部を使うため、
  複数箇所で同じフォントを使ってもメモリは増えません。

## プラグインからの利用 (C++)

tp_stub にフォントサービス API (`TVPCreateFontStream` / `TVPFontAcquireFace` /
`TVPFontShapeLine` / `TVPFontQueryFaces` ほか) が公開されており、プラグインも
共有バッファ・グリフ供給・シェイピング・検索を利用できます。詳細はエンジン
リポジトリの `src/core/doc/FontEngine.md` (内部実装ノート) を参照してください。

## トラブルシューティング

- **フォント名を指定したのに既定フォントで描かれる** — 名前が未登録です。
  `Font.getFontInfo(名前)` が void を返すか確認し、fonts.json の宣言名 /
  aliases、または `Font.addFont` の戻り値のフェイス名を使ってください。
- **カラー絵文字が白黒になる** — カラー絵文字フォントが未配置 (fonts.json
  未宣言) だとモノクロへフォールバックします。`Font.queryFonts(%[color:1])`
  で配置状況を確認できます。
- **WINVER で絵文字が出ない** — 既定ラスタライザ (GDI) は絵文字非対応です。
  `Font.rasterizer = 2` (または 0) にしてください。
- **"MS Gothic" の幅が経路によって違う** — FreeType の名前解決は英名 TTC で
  別フェイス (PGothic) に化けることがあります。実 family 名
  ("ＭＳ ゴシック" 等) を使うと全経路で一致します。

## 関連資料

- リファレンス: [Font](../reference/Font.md) / [Layer](../reference/Layer.md)
- [ダイアログ (Elements)](Dialog.md)
- レンダリング済みフォント: [FontMaker](FontMaker.md)
- エンジン内部実装 (開発者向け): `src/core/doc/FontEngine.md`
