# Layer と Bitmap と ImageFunction

吉里吉里Z で画像を扱うクラスは [Layer](../reference/Layer.md) と [Bitmap](../reference/Bitmap.md) の
2 つがあり、そこに [ImageFunction](../reference/ImageFunction.md) というメソッドだけのクラスが加わります。
この 3 者がどういう関係にあるのか、どれをいつ使えばよいのかをまとめます。

## 3 行でいうと

- **Layer** は「表示される画像」。画像バッファに加えて、親子ツリー・表示位置・不透明度・入力イベント・再描画通知を持つ。
- **Bitmap** は「表示されない画像バッファ 1 枚」。読み込み・保存・ピクセルアクセスはできるが、**描画メソッドを一切持たない**。
- **ImageFunction** は、Layer が持っている描画メソッドから *Layer 固有の事情* (表示属性・クリップ矩形・更新通知) を取り除いて、
  **Bitmap に対して直接呼べるようにした静的メソッド置き場**。Bitmap に描画メソッドが無い穴を埋めるためのクラス。

## 構造

TJS2 から見えるクラスは 3 つですが、ピクセルを実際に保持し・加工するエンジン内部の実体 (`tTVPBaseBitmap`) は 1 種類しかありません。
Layer も Bitmap もそれを抱えているだけで、描画アルゴリズム (Blt / StretchBlt / AffineBlt / 塗りつぶし / 文字描画 …) は完全に共通です。

```text
 TJS2 レベル
 ┌────────────────────────────────┐   ┌──────────────────────────────┐   ┌───────────────────────┐
 │ Layer                          │   │ Bitmap                       │   │ ImageFunction         │
 │  ・親子ツリー / 表示位置       │   │  ・画像 1 枚だけ             │   │  ・全メソッド static  │
 │  ・visible / opacity / type    │   │  ・width / height / buffer   │   │  ・インスタンスを     │
 │  ・face / holdAlpha / clip*    │   │  ・load / loadAsync / save   │   │    作る意味は無い     │
 │  ・入力イベント / フォーカス   │   │  ・getPixel / setPixel       │   │                       │
 │  ・描画メソッド多数            │   │  ・独自の描画メソッドは無い  │   │                       │
 │  ・描画すると update() が走る  │   │                              │   │                       │
 └───────────────┬────────────────┘   └───────────────┬──────────────┘   └───────────┬───────────┘
                 │ MainImage                          │                              │
                 │ ProvinceImage (領域画像)           │ (1 枚だけ)                   │ 第 1 引数に
                 ▼                                    ▼                              │ Bitmap を取る
 C++ レベル  ┌───────────────────────────────────────────────────────────┐           │
             │ tTVPBaseBitmap                                            │◀──────────┘
             │  ピクセルバッファ本体 (32bpp / 8bpp、コピーオンライト共有)│
             │  Blt / StretchBlt / AffineBlt / Fill / DrawText / Blur …  │
             └───────────────────────────────────────────────────────────┘
```

つまり **ImageFunction は「Layer の描画メソッドの Bitmap 版」** です。
内部で呼ばれる処理は Layer 版とまったく同じもので、違うのは「誰が引数を決めるか」だけです。

## なぜ Bitmap と ImageFunction が要るのか

Layer は単体では作れません。コンストラクタに [Window](../reference/Window.md) (または
[BitmapLayerTreeOwner](../reference/BitmapLayerTreeOwner.md)) と親レイヤが必要で、
描画するたびに再描画領域の通知 (`update`) が走り、ツリー全体の合成対象になります。
「画面には出さないが加工したい画像」— 素材の前処理、キャッシュ、スクリーンショットの加工、非同期読み込み — には重すぎます。

Bitmap はその軽い受け皿で、`new Bitmap(w, h)` だけで作れて、表示にもツリーにも一切関わりません。
ただし Bitmap 自身は描画メソッドを持たないため、Bitmap の上で合成・文字描画・フィルタをかける手段として ImageFunction が用意されています。

Bitmap 側にしか無い機能もあります。代表は **非同期画像読み込み** ([Bitmap.loadAsync](../reference/Bitmap.md#loadasync)) で、
Layer には対応するメソッドがありません。読み込んだあと
[Layer.copyFromBitmapToMainImage](../reference/Layer.md#copyfrombitmaptomainimage) で Layer に渡すのが定石です。

## メソッド対応表

| 処理 | Layer | ImageFunction (対象は Bitmap) | Bitmap 自身 |
| --- | --- | --- | --- |
| 矩形塗りつぶし | `fillRect` | `fillRect` | — |
| 半透明・マスク塗りつぶし | `colorRect` | `colorRect` | — |
| 文字描画 | `drawText` | `drawText` (Font を明示指定) | — |
| グリフ描画 | `drawGlyph` | `drawGlyph` | — |
| シェイピング文字描画 | `drawShapedText` / `drawShapedTextArea` | **なし** | — |
| 矩形コピー | `copyRect` | `operateRect` + `omOpaque` / `dfOpaque` | — |
| 矩形演算合成 | `operateRect` | `operateRect` | — |
| 拡大縮小コピー | `stretchCopy` | `operateStretch` + `omOpaque` / `dfOpaque` | — |
| 拡大縮小演算合成 | `operateStretch` | `operateStretch` | — |
| アフィンコピー | `affineCopy` | `operateAffine` + `omOpaque` / `dfOpaque` | — |
| アフィン演算合成 | `operateAffine` | `operateAffine` | — |
| 9patch コピー | `copy9Patch` | `copy9Patch` | — |
| 矩形ブラー | `doBoxBlur` | `doBoxBlur` | — |
| ガンマ補正 | `adjustGamma` | `adjustGamma` | — |
| グレースケール化 | `doGrayScale` | `doGrayScale` | — |
| 左右 / 上下反転 | `flipLR` / `flipUD` | `flipLR` / `flipUD` | — |
| ツリー合成コピー | `piledCopy` | **なし** (子レイヤの概念が無い) | — |
| ピクセル読み書き | `getMainPixel` / `setMainPixel` / `getMaskPixel` / `setMaskPixel` | — | `getPixel` / `setPixel` / `getMaskPixel` / `setMaskPixel` |
| 画像読み込み | `loadImages` | — | `load` / `loadAsync` / `loadHeader` |
| 画像保存 | `saveLayerImage` | — | `save` |
| 共有の解除 | `independMainImage` | — | `independ` |
| 画像サイズ変更 | `setImageSize` | — | `setSize` |

!!! note "コピー系が ImageFunction に無い理由"
    `copyRect` / `stretchCopy` / `affineCopy` に相当する専用メソッドは ImageFunction にはありません。
    `mode = omOpaque`, `face = dfOpaque`, `hda = false` を指定した `operate*` がそのまま単純コピー (`bmCopy`) になるためです。
    ただし `affineCopy` の `clear` 引数 (変換後の範囲外をクリアする機能) に相当するものはありません。

## Layer が暗黙に使う値は、ImageFunction では全部明示引数

同じ描画処理でも、Layer 版は自分自身のプロパティから引数を組み立てます。Bitmap にはそれらのプロパティが無いので、
ImageFunction では呼び出し側がすべて明示的に渡します。**移植時に食い違いが出やすいのはここです。**

| Layer が暗黙に使うもの | ImageFunction での対応 |
| --- | --- |
| [Layer.face](../reference/Layer.md#face) | `face` 引数 (既定 `dfAlpha`) |
| [Layer.holdAlpha](../reference/Layer.md#holdalpha) | `hda` 引数 (既定 `false`) |
| [Layer.clipLeft](../reference/Layer.md#clipleft) ほかクリップ矩形 | `cliprect` 引数 (既定は**画像全体**、`null` でクリップ無し) |
| [Layer.font](../reference/Layer.md#font) | `drawText` の `font` 引数。[Font](../reference/Font.md) オブジェクトの指定が必須 (`new Font()` で単体生成可) |
| 演算元 [Layer.type](../reference/Layer.md#type) による `omAuto` の解決 | 解決先が無いため **`omAuto` は常に `omAlpha` に落ちる** |
| 描画後の `update()` による再描画通知 | **なし** (Bitmap は表示されないので不要) |
| [Layer.imageModified](../reference/Layer.md#imagemodified) | なし |

!!! warning "`omAuto` の扱い"
    `omAuto` は「演算元 **Layer** の `type` プロパティから合成方法を決める」という意味です。
    Bitmap には `type` が無いので、ImageFunction では `omAuto` は無条件に `omAlpha` になります。
    同じことは `Layer.operateRect` などに **Bitmap を演算元として渡した場合**にも起こります
    (この場合も `omAuto` は `omAlpha` 扱い)。加算合成やスクリーン合成をしたいなら `mode` を明示してください。

## Layer ⇄ Bitmap の行き来

### Layer の描画メソッドに Bitmap を渡す (1.1.0 以降)

以下の Layer メソッドは、コピー元 / 演算元 (`src`) に **Layer でも Bitmap でも**指定できます。

`copyRect` / `copy9Patch` / `operateRect` / `stretchCopy` / `operateStretch` / `affineCopy` / `operateAffine`

素材を Bitmap で持っておき、そこから Layer へ描き込む用途にはこれが一番手数が少ない方法です。
なお `piledCopy` (子レイヤを含めた合成コピー) と `assignImages` は Layer 専用で、Bitmap は渡せません。

### Layer → Bitmap

```tjs
var bmp = new Bitmap();
layer.copyToBitmapFromMainImage(bmp);   // メイン画像を bmp へ
```

内部では**コピーオンライトの共有**が行われるだけなので、ピクセルの実コピーは発生せず高速です
(どちらかに書き込んだ時点で自動的に分離されます)。マスク (アルファ) を含む 32bpp がそのまま渡りますが、
**領域画像 (province) は渡りません**。

### Bitmap → Layer

```tjs
layer.copyFromBitmapToMainImage(bmp);   // bmp をレイヤのメイン画像に
```

こちらもコピーオンライト共有ですが、Layer 側では

- レイヤの画像サイズが Bitmap のサイズに変更される
- クリップ矩形がリセットされる
- `update` が走り再描画される

という副作用があります。レイヤの画像サイズを保ったまま一部だけ差し替えたい場合は
`copyRect` / `operateRect` に Bitmap を渡すほうを使ってください。

### ImageFunction に Layer は渡せない

ImageFunction の各メソッドは **Bitmap オブジェクトしか受け付けません**。Layer を渡すと引数不正の例外になります。
Layer の画像を ImageFunction で加工したい場合は、いったん `copyToBitmapFromMainImage` で Bitmap に受け、
加工後に `copyFromBitmapToMainImage` で書き戻します。

### レイヤツリーの合成結果を Bitmap で得る

Window を用意せずにレイヤツリーを組み、その合成結果を Bitmap として取り出したい場合は
[BitmapLayerTreeOwner](../reference/BitmapLayerTreeOwner.md) を使います。
Layer のコンストラクタ第 1 引数に Window の代わりに渡すと、そのツリーの描画結果が
`BitmapLayerTreeOwner.bitmap` から Bitmap として得られます。

## 落とし穴

**再描画されない**
: Bitmap は表示要素ではないので、ImageFunction で描き込んでも画面は何も変わりません。
  Layer へ反映して初めて見えるようになります。

**コピーオンライトの共有**
: `Bitmap.copyFrom` / `assignImages` / `copyToBitmapFromMainImage` などは実バッファを共有するだけです。
  通常は書き込み直前に自動で分離されるので意識不要ですが、全面を書き潰すことが分かっているなら
  [Bitmap.independ](../reference/Bitmap.md#independ) に `false` を渡して先に分離しておくと無駄なコピーを省けます。

**バッファ直接アクセス**
: [Bitmap.buffer](../reference/Bitmap.md#buffer) は読み取り専用ポインタで、書き込むなら
  [Bitmap.bufferForWrite](../reference/Bitmap.md#bufferforwrite) を使います (参照した時点で共有が解除されます)。
  [Bitmap.bufferPitch](../reference/Bitmap.md#bufferpitch) は**負の値になり得ます** (ボトムアップ格納)。
  なお Bitmap には Layer と同名の別名プロパティ (`imageWidth` / `imageHeight` / `mainImageBuffer` /
  `mainImageBufferForWrite` / `mainImageBufferPitch`) もあり、プラグインや DrawDevice が
  Layer と Bitmap を区別せずに画像を取得できるようになっています。

**8bpp の Bitmap**
: `new Bitmap(w, h, 8)` で 8bpp の画像も作れますが、色とアルファを前提とした処理
  (`operate*` 系、`fillRect` の一部など) は 8bpp に対して例外を投げます。8bpp は領域画像 (province) 相当の用途向けです。

**アルファチャンネルの破壊**
: 乗算・加算・スクリーンなどの演算系合成は、`hda`(= Layer の `holdAlpha`) が偽だと合成先のアルファを保護しません。
  `ltAlpha` 相当のアルファ付き画像に対して演算合成する場合は `hda = true` を指定してください。
  指定を忘れると結果が真っ黒になる (アルファが 0 になる) といった症状になります。

**シェイピング文字描画は Layer のみ**
: `drawShapedText` / `drawShapedTextArea` / `measureShapedText` 系は Layer にしかありません。
  Bitmap に対する複雑なテキストレイアウトが必要な場合は、いったん Layer に描いてから Bitmap へ受けることになります。

## 典型パターン

### 画面に出さずに素材を合成してから Layer へ渡す

```tjs
// 640x480 の作業用 Bitmap を作り、不透明な黒でクリア
var work = new Bitmap(640, 480);
ImageFunction.fillRect(work, 0xff000000);          // isalpha=true なので 0xAARRGGBB

// 背景素材を単純コピー (copyRect 相当)
var bg = new Bitmap("bg.png");
ImageFunction.operateRect(work, 0, 0, bg, null, null, omOpaque, dfOpaque);

// 文字を載せる (Font は明示的に用意する)
var font = new Font();
font.face   = "IPAGothic";
font.height = 24;
ImageFunction.drawText(work, font, 16, 16, "スコア: 1200", 0xffffff);

// できあがった画像をレイヤへ (ここで初めて画面に反映される)
layer.copyFromBitmapToMainImage(work);
```

### 非同期に画像を読み込んでレイヤへ流し込む

```tjs
class AsyncImage extends Bitmap {
    var target;
    function AsyncImage(target) {
        super.Bitmap();
        this.target = target;
    }
    function onLoaded(meta, async, error, message) {
        if (error) { Debug.message("読み込み失敗: " + message); return; }
        if (target !== null && target isvalid) target.copyFromBitmapToMainImage(this);
    }
}

var img = new AsyncImage(layer);
img.loadAsync("bg.png");    // 完了は onLoaded に通知される
```

!!! warning
    非同期読み込み中は [Bitmap.loading](../reference/Bitmap.md#loading) 以外のメンバにアクセスすると例外になります。
    また `onLoaded` が呼ばれる時点で対象の Layer が既に無効化されている可能性があるため、上の例のように有効性を確認してください。

### Layer の画像を加工して書き戻す

```tjs
var tmp = new Bitmap();
layer.copyToBitmapFromMainImage(tmp);    // 共有されるだけなので速い
ImageFunction.doGrayScale(tmp);          // ここで初めて実体が分離される
ImageFunction.doBoxBlur(tmp, 4, 4);
layer.copyFromBitmapToMainImage(tmp);    // 書き戻し (update が走る)
```

## 参照

- [Layer クラスリファレンス](../reference/Layer.md)
- [Bitmap クラスリファレンス](../reference/Bitmap.md)
- [ImageFunction クラスリファレンス](../reference/ImageFunction.md)
- [BitmapLayerTreeOwner クラスリファレンス](../reference/BitmapLayerTreeOwner.md)
- [グラフィックシステム](GraphicSystem.md) — レイヤタイプ・描画方式 (`df*`)・演算モード (`om*`) の意味
