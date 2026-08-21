---
name: krkrz
description: 吉里吉里Z (kirikiri Z) 本体クラス API のリファレンス。TJS2 で吉里吉里Z 上のスクリプトを書く、レビューする、デバッグするときに使う。Layer / Window / Bitmap / System / Storages / Font / Plugins / Timer / Debug / AsyncTrigger / Scripts / BinaryStream / Matrix32 / Matrix44 / Rect / ImageFunction のコア API、サウンド系 (WaveSoundBuffer / SoundBuffer / VideoOverlay)、DrawDevice (BasicDrawDevice / SDLDrawDevice / OGLDrawDevice / NullDrawDevice)、OpenGL 描画系 (Canvas / Texture / ShaderProgram / Offscreen / VertexBinder / VertexBuffer)、および主要プラグイン提供クラス (HttpRequest / GdiPlus.* / WIN32Dialog / CSVParser / LineParser / Process / Pad / MenuItem / Unzip / Zip / PSD / SimpleHTTPServer) を網羅。**呼び出されたら必ず「共通パターン」と「クロスカッティング概念」を確認し、必要な詳細クラスは doc/reference/*.md を Read しに行くこと。** TJS2 言語そのものや組み込みクラス (Array / Dictionary / Math 等) は別 skill (`tjs2`) を参照。エンジン内部構造 (C++ 実装、レンダリングパイプライン詳細) は対象外。
---

# 吉里吉里Z 本体クラス API リファレンス

吉里吉里Z (kirikiri Z) が TJS2 から見えるクラス API のスキル。スクリプト
作者の視点で「どのクラスを使うか」「どのメソッドを呼ぶか」を素早く
引き当てるためのもの。深い説明は reference/*.md を Read で取りに行く。

## 重要: 作業に入る前に

1. **下の「クロスカッティング概念」を必ず確認**。Layer ツリー / イベント /
   ストレージ / DrawDevice の思考モデルを取り違えると、API の組合せを
   誤る ( 例: Layer は GUI 部品でもあり描画面でもある、Bitmap は Layer
   とは別の独立した bits 領域 )。
2. **TJS2 言語そのものの疑問は別 skill (`tjs2`) を参照**。`var` / 辞書
   リテラル `%[ ... ]` / `new Foo()` 括弧必須 など、JS と違う文法は
   そちらに集約してある。
3. **クラス固有の詳細は `doc/reference/<Class>.md` を Read**。本ファイルは
   入口で、深掘りは reference にある。

## クロスカッティング概念 (これを取り違えると詰む)

### Layer ツリー

- 1 ウィンドウは 1 つの **プライマリレイヤ** ([Window.primaryLayer](doc/reference/Window.md#primarylayer)) を持つ
- [Layer](doc/reference/Layer.md) は親子のツリー構造。`parent`/`children`/`order` で位置決め
- レイヤは「描画面 (画像を持つ Bitmap)」+「GUI 部品 (フォーカス・カーソル・hint・hitTest)」を **両方兼ねる**
- 描画関連プロパティ: `width`/`height` (描画領域), `imageWidth`/`imageHeight` (Bitmap 部分), `clip*` (クリップ矩形), `face` (描画面の種類), `type` (合成方式)
- [Layer.face](doc/reference/Layer.md#face) の値で `dfBoth`/`dfMain`/`dfProvince`/`dfAlpha` 等を切替
- 入力: `cursor`/`hint`/`hitType`/`focusable`/`enabled` がレイヤ単位、`focused` でフォーカス
- 描画: `loadImages`/`drawText`/`fillRect`/`copyRect`/`affineCopy` 等。`update()` で再描画フラグ
- 動的生成は `new Layer(window, parent)` + `setImageSize(w, h)` + `setSize(w, h)` がほぼ定型

### イベント

- **同期イベント**: メソッド呼び出し中に発生 ( 例: SoundBuffer の `onStatusChanged` を `play` 中に )
- **非同期イベント**: イベントキュー経由、他のハンドラ完了後に配信 ( 例: `onTimer`、ユーザ入力 )
- **画面反映も非同期**: 同じハンドラ内で何度 `update` しても、ハンドラから抜けるまで画面に出ない
- スクリプト側から非同期イベントを起こすには [AsyncTrigger](doc/reference/AsyncTrigger.md)
- イベントハンドラの登録は **プロパティに関数を代入** ( `layer.onMouseDown = function(x, y, ...) { ... }` )
- サブクラスから super のハンドラを上書きする場合は `function onTimer() { super.onTimer(...);  ... }` のような書き方
- 詳細: `doc/guide/EventSystem.md`

### 統一ストレージ名 ( `file://./...` )

- 表記: `メディア://ドメイン/パス` ( 区切りは `/` )
- ローカルファイル: `file://./c/program files/...` ( Windows ドライブ文字含む )
- アーカイブ内: `archive.xp3>file.png` (区切り `>`、2.19 beta 14 以降。旧 `#` は `-arcdelim=#` で互換可)
- 自動検索パス: [Storages.addAutoPath](doc/reference/Storages.md#addautopath) で登録、相対名で findable に
- 全てのパスは `Storages.getFullPath` で正規化される。`TVP_NO_NORMALIZE_PATH` 未定義ビルドではディレクトリ列挙結果も小文字化
- 詳細: `doc/guide/StorageSystem.md`

### ファイル/画像キャッシュ ( 2 層構造 )

- **file 層**: ストレージから読んだバイナリをメモリに保持 ( StorageCache )。`addCacheTargetExtension(ext, minSize)` で対象登録
- **decode 層**: 画像のデコード結果 Bitmap を保持 ( ImageCache )。`addDecodeTargetExtension(ext, minSize)` で対象登録
- バックグラウンド prefetch: [Storages.requestCache](doc/reference/Storages.md#requestcache) (両層に発火), [Storages.requestFastCache](doc/reference/Storages.md#requestfastcache)
- 進行確認: [Storages.isCacheLoading](doc/reference/Storages.md#iscacheloading) (file層), [Storages.isImagePrefetchLoading](doc/reference/Storages.md#isimageprefetchloading) (decode層)
- pin 管理: [Storages.pinCache](doc/reference/Storages.md#pincache) / [Storages.unpinCache](doc/reference/Storages.md#unpincache) ( pin したものは transient clear で消えない )
- 全削除/部分削除: [Storages.clearAllCaches](doc/reference/Storages.md#clearallcaches) / [Storages.clearTransientCaches](doc/reference/Storages.md#cleartransientcaches) / [Storages.clearCache](doc/reference/Storages.md#clearcache)
- エントリ列挙: [Storages.getFileCacheList](doc/reference/Storages.md#getfilecachelist) / [Storages.getImageCacheList](doc/reference/Storages.md#getimagecachelist)
- 詳細: `doc/topics/core/memory_observation.md`

### DrawDevice ( ウィンドウ → 画面への描画器 )

- [Window.drawDevice](doc/reference/Window.md#drawdevice) プロパティで切替可能
- 4 種: [BasicDrawDevice](doc/reference/Window.BasicDrawDevice.md) (WINVER 既定、Direct3D), [SDLDrawDevice](doc/reference/SDLDrawDevice.md) (SDL3 既定、SDL_Renderer), [OGLDrawDevice](doc/reference/OGLDrawDevice.md) (OpenGL ES、Canvas/Shader/Texture/Offscreen が有効), [NullDrawDevice](doc/reference/NullDrawDevice.md) (描画しない)
- **OGLDrawDevice は lazy 初期化**: TJS から差し替えた瞬間に GL コンテキスト生成、それまでは Canvas/Texture/Shader 等は使えない
- 起動時 default は `-drawdevice` オプションで上書き可 ( `sdl` / `sdlogl` / `ogl` )

### OpenGL 系 ( OGLDrawDevice 配下のみ有効 )

- [Canvas](doc/reference/Canvas.md) — OGL 描画コンテキスト、`drawTexture`/`fillRect`/`drawTransition`(表裏2テクスチャのクロスフェード/rule画像ユニバーサルトランジション内蔵、phase 0-1・rule は tcfAlpha・vague 0-255) 等
- [Texture](doc/reference/Texture.md) — GL テクスチャ。Bitmap や Storage から生成
- [Offscreen](doc/reference/Offscreen.md) — オフスクリーンレンダーターゲット
- [ShaderProgram](doc/reference/ShaderProgram.md) — GLSL シェーダ
- [VertexBuffer](doc/reference/VertexBuffer.md) / [VertexBinder](doc/reference/VertexBinder.md) — 頂点バッファ
- OGLDrawDevice をアクティブにしていない状態でこれらを new しても無効

### Bitmap と Layer の関係

- [Bitmap](doc/reference/Bitmap.md) は **独立した bits 領域**。Layer.mainImageBuffer 経由でも触れるが、別オブジェクトとして new できる
- [BitmapLayerTreeOwner](doc/reference/BitmapLayerTreeOwner.md) は「Layer ツリーを Bitmap に書き出す」のためのコンテナ。スクリーンショットや動的レイヤレンダリングに使う
- Layer は描画面 + GUI、Bitmap は純粋なピクセル列。混同しない

### finalize と invalidate

- すべてのクラスは GC または明示的 `invalidate` でオブジェクト破棄。`finalize()` メソッドが定義されていれば呼ばれる
- Window / Layer / Bitmap 等の重量級オブジェクトは明示的 `invalidate` を推奨
- finalize 内で例外を出すと処理系が苦しむので注意

## クラス索引 ( doc/reference/<Name>.md を Read )

ファイルは krkrz_dev リポジトリルート相対で `doc/reference/<Name>.md`。
オンライン版は <https://wamsoft.github.io/krkrz_dev/reference/<name>/> 。

### ウィンドウ / レイヤ / 描画

| クラス | 主な役割 |
|---|---|
| [Window](doc/reference/Window.md) | メインウィンドウ、サイズ、`drawDevice`、入力イベント `onKeyDown`/`onMouseDown` 等、`primaryLayer` |
| [Layer](doc/reference/Layer.md) | レイヤツリー、Bitmap 描画 (`loadImages` / `drawText` / `fillRect` / `copyRect` / `affineCopy`)、GUI 機能 |
| [Bitmap](doc/reference/Bitmap.md) | 独立した bits 領域、`load`/`save`/`loadAsync` |
| [BitmapLayerTreeOwner](doc/reference/BitmapLayerTreeOwner.md) | Layer ツリーを Bitmap に書き出す |
| [Font](doc/reference/Font.md) | フォント設定 (face / height / italic / bold / strikeout) |
| [Rect](doc/reference/Rect.md) | 矩形 |
| [Matrix32](doc/reference/Matrix32.md) / [Matrix44](doc/reference/Matrix44.md) | 2D / 3D 変換行列 |
| [ImageFunction](doc/reference/ImageFunction.md) | 画像変換ユーティリティ |
| [PreRenderedFontImage](doc/reference/PreRenderedFontImage.md) | 事前レンダリングフォント (tftSave plugin 提供) |

### DrawDevice

| クラス | プラットフォーム |
|---|---|
| [BasicDrawDevice](doc/reference/Window.BasicDrawDevice.md) | WINVER 既定 (Direct3D) |
| [SDLDrawDevice](doc/reference/SDLDrawDevice.md) | SDL3 既定 (SDL_Renderer) |
| [OGLDrawDevice](doc/reference/OGLDrawDevice.md) | OpenGL ES、Canvas/Shader が有効化される |
| [NullDrawDevice](doc/reference/NullDrawDevice.md) | 描画なし (ヘッドレス / 検証用) |

### OpenGL ( OGLDrawDevice 配下のみ )

| クラス | 役割 |
|---|---|
| [Canvas](doc/reference/Canvas.md) | OGL 描画コンテキスト |
| [Texture](doc/reference/Texture.md) | GL テクスチャ |
| [Offscreen](doc/reference/Offscreen.md) | オフスクリーンレンダーターゲット |
| [ShaderProgram](doc/reference/ShaderProgram.md) | GLSL シェーダ |
| [VertexBuffer](doc/reference/VertexBuffer.md) | 頂点バッファ |
| [VertexBinder](doc/reference/VertexBinder.md) | 頂点属性バインダ |

### サウンド / 動画

| クラス | 役割 |
|---|---|
| [WaveSoundBuffer](doc/reference/WaveSoundBuffer.md) | 波形音声 (BGM/SE) |
| [WaveSoundBuffer.PhaseVocoder](doc/reference/WaveSoundBuffer.PhaseVocoder.md) | ピッチ/テンポ独立変更 |
| [SoundBuffer](doc/reference/SoundBuffer.md) | サウンドバッファ ( PCM 生成等の低レベル ) |
| [VideoOverlay](doc/reference/VideoOverlay.md) | 動画再生 |

### ストレージ / I/O

| クラス | 役割 |
|---|---|
| [Storages](doc/reference/Storages.md) | ファイル/アーカイブ操作、auto path、cache 管理 |
| [BinaryStream](doc/reference/BinaryStream.md) | バイナリストリーム |

### システム / イベント / プラグイン

| クラス | 役割 |
|---|---|
| [System](doc/reference/System.md) | OS情報、コマンドライン、メモリ統計、ゲームパッド、`addContinuousHandler` |
| [Plugins](doc/reference/Plugins.md) | プラグインの link/unlink、`canLink` で事前判定 |
| [Scripts](doc/reference/Scripts.md) | スクリプトのコンパイル/実行 |
| [Timer](doc/reference/Timer.md) | 周期/単発タイマ |
| [AsyncTrigger](doc/reference/AsyncTrigger.md) | 非同期イベントの自前発火 |
| [Debug](doc/reference/Debug.md) | ログ出力 / コンソール出力 |
| [Console](doc/reference/Console.md) | コンソールウィンドウ |
| [Clipboard](doc/reference/Clipboard.md) | クリップボード I/O |
| [Controller](doc/reference/Controller.md) | コントローラ (デバッグ操作 UI ) |

### プラグイン提供クラス (主要)

| クラス | 提供 plugin | 用途 |
|---|---|---|
| [HttpRequest](doc/reference/HttpRequest.md) | httprequest | HTTP クライアント |
| [GdiPlus.Image](doc/reference/GdiPlus.Image.md) / [.Path](doc/reference/GdiPlus.Path.md) / [.Matrix](doc/reference/GdiPlus.Matrix.md) / [.Font](doc/reference/GdiPlus.Font.md) / [.Appearance](doc/reference/GdiPlus.Appearance.md) / [.PointF](doc/reference/GdiPlus.PointF.md) / [.RectF](doc/reference/GdiPlus.RectF.md) | layerExDraw | GDI+ ベクター描画 |
| [WIN32Dialog](doc/reference/WIN32Dialog.md) / [WIN32DialogEX](doc/reference/WIN32DialogEX.md) / [.Header](doc/reference/WIN32Dialog.Header.md) / [.Items](doc/reference/WIN32Dialog.Items.md) | win32dialog | Win32 ダイアログ |
| [CSVParser](doc/reference/CSVParser.md) | csvParser | CSV パーサ |
| [LineParser](doc/reference/LineParser.md) | lineParser | 行パーサ |
| [Process](doc/reference/Process.md) | process | プロセス起動 |
| [Pad](doc/reference/Pad.md) | windowEx | ゲームパッド (高機能版) |
| [MenuItem](doc/reference/MenuItem.md) | menu | メニュー項目 |
| [Unzip](doc/reference/Unzip.md) / [Zip](doc/reference/Zip.md) | minizip | ZIP I/O |
| [PSD](doc/reference/PSD.md) | psdfile | PSD ファイル読込 |
| [SimpleHTTPServer](doc/reference/SimpleHTTPServer.md) | httpserv | 簡易 HTTP サーバ |

### 主要ユーティリティプラグイン (Scripts / Array / Dictionary 拡張)

これらは吉里吉里本体ではなくプラグインだが、実運用のスクリプトが常時前提にしていることが多い。standalone tool を書くときは自分でリンクが必要:

| プラグイン | 提供機能 | 備考 |
|---|---|---|
| `scriptsEx.dll` | `Scripts.foreach(obj, func, args*)` / `Scripts.getObjectKeys(obj)` / `Scripts.getObjectCount(obj)` / `Scripts.getObjectContext(obj)` / `Scripts.equalStruct(a, b)` / `Scripts.clone(obj)` / `Scripts.propSet` / `Scripts.propGet` | Dictionary の列挙 API は本体に無いので事実上必須 |
| `saveStruct.dll` | `Array.save2(file, utf8=false, newline=0)` / `Array.saveStruct2(file, utf8, newline, opt)` / `Dictionary.saveStruct2(file, utf8, newline, opt)` / `.toStructString(newline, opt)` | 組み込み `Array.save` は UTF-16 LE + BOM 固定なので、UTF-8 テキスト保存が必要ならこちらを使う |
| `fstat.dll` | `Storages.dirlist(dir)` / `Storages.dirlistEx(dir)` / `Storages.createDirectory(dir)` / `Storages.isExistentDirectory(dir)` | ディレクトリ走査 / 作成。**引数のディレクトリパスは末尾 `/` 必須** (無いと "'/' must be specified..." throw) |
| `PackinOne.dll` | 上記 fstat / saveStruct / scriptsEx の一部機能を統合提供 | wamsoft 独自の統合版。ただし link 時に fstat 経由でパス検証が走り、standalone 環境では init throw する場合がある。単機能を欲しいだけなら個別プラグインの方が安全 |

**Scripts.foreach の落とし穴** ( scriptsEx.dll ):
コールバック関数の実行コンテキストは呼び出し元プラグイン側なので、**外側関数の local 変数を参照するとランタイム例外**になる。対策:
- 追加引数機構を使う: `Scripts.foreach(obj, function(k, v, arg) { ... }, arg)`
- `Scripts.getObjectKeys(obj)` で keys 配列を取り、素の `for` ループでイテレート (最も確実)

詳細は tjs2 skill の「クロージャの落とし穴」も参照。

## 共通パターン

### イベントハンドラ登録

```tjs
// プロパティに関数を代入
layer.onMouseDown = function(x, y, button, shift) { ... };

// または class サブクラスで override
class MyLayer extends Layer {
    function MyLayer(win, parent) { super.Layer(win, parent); }
    function onMouseDown(x, y, button, shift) {
        super.onMouseDown(x, y, button, shift);
        // 追加処理
    }
}
```

### Layer の典型初期化

```tjs
var lay = new Layer(window, parent);
lay.setImageSize(640, 480);   // Bitmap 部分のサイズ
lay.setSize(640, 480);         // 表示サイズ
lay.setPos(0, 0);              // 位置
lay.loadImages("bg/title");    // 自動検索パスから
lay.visible = true;
```

### 非同期画像読み込み + cache

```tjs
Storages.addCacheTargetExtension(".png");
Storages.addDecodeTargetExtension(".png");
Storages.requestCache("bg/title.png");  // 非同期 prefetch
// ... 後で loadImages したときに cache hit
```

### Timer 周期処理

```tjs
class MyTimer extends Timer {
    function MyTimer() { super.Timer(); interval = 1000; enabled = true; }
    function onTimer() { /* 1秒毎 */ }
}
```

### DrawDevice 切替で OGL 有効化

```tjs
// OGLDrawDevice に切替えてから Canvas/Shader 系を new する
window.drawDevice = new OGLDrawDevice();
var canvas = new Canvas(window);
var tex = new Texture(window, "image.png");
```

## 関連ドキュメント

- ガイド (概念解説): `doc/guide/EventSystem.md`, `doc/guide/StorageSystem.md`, `doc/guide/GraphicSystem.md`, `doc/guide/SoundSystem.md`, `doc/guide/CommandLine.md`
- 周辺情報: `doc/topics/core/*.md` (gamepad〔刻印/位置 2 系統・padStyle〕, viewport, engine_setting, memory_observation, low_memory, draw_stats, pad_overlay, repl, logging, anti_cracking)
- TJS2 言語本体は別 skill (`tjs2`)

## 関連スキル

- skill `tjs2` — TJS2 言語仕様と組込クラス (Array / Dictionary / Math / Date / RegExp / Exception 等)
- (未作成) 吉里吉里Z 内部構造 / engine internals — C++ 実装、レンダリングパイプライン、SIMD、プラグインローダ等

エンジン内部は別 skill 化予定。本スキルは TJS から見える表層 API のみ。
