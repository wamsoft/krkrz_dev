# プラグインについて

## プラグインとは

吉里吉里に接続して、吉里吉里の機能を拡張するために使われます。

現段階で、吉里吉里で使用可能なプラグインの種類には３つあり、

- Susie Plug-in (画像読み込みとアーカイブアクセス)
- WaveSoundBufferで再生可能な形式を拡張するためのプラグイン
- そのほかの吉里吉里専用のプラグイン

となっています。



プラグインを使用する場合は [Plugins.link](../reference/Plugins.md#link) メソッドを使用して吉里吉里本体に接続する必要があります。

## プラグインの検索

[Plugins.link](../reference/Plugins.md#link) メソッドでは、指定されたプラグインを以下の順序で探します。

1. 吉里吉里本体と同じフォルダ
2. 吉里吉里本体以下と同じフォルダにある plugin (64bit版ではplugin64) フォルダ内
3. 自動検索パス

自動検索パスが、アーカイブ内などローカルファイルとしてアクセスできない場所にあると、吉里吉里はプラグインを**吉里吉里本体と同じフォルダ**に展開しようとします。これが問題を起こすことがあるため、プラグインは「吉里吉里本体と同じフォルダ」か「吉里吉里本体以下と同じフォルダにある plugin フォルダ内」に置くことを**強く推奨します**。


32bit版/64bit版でのプラグインの読み分けを行うためにも plugin/plugin64 フォルダ内に置くことは重要です。

また、吉里吉里の設定ツール ( Releaser や -userconf オプション ) は、プラグインごとの埋め込みオプションの情報を収集するためにプラグインを探しますが、以下の順序で探します。

1. 吉里吉里本体と同じフォルダ
2. 吉里吉里本体以下と同じフォルダにある plugin フォルダ内

吉里吉里の設定ツールは自動検索パスまでは検索しないため、設定項目を含むプラグインは「吉里吉里本体と同じフォルダ」か「吉里吉里本体以下と同じフォルダにある plugin フォルダ内」に置かなければなりません。

## プラグインの自動読み込み

吉里吉里はプラグインを自動的に検索して起動時に読み込む機能があります。自動的にプラグインを読み込ませたい場合は、プラグインの拡張子を dll から tpm に変更する必要があります。

吉里吉里は起動時 (startup.tjsを実行する直前) に、以下のフォルダから拡張子 tpm のファイルを探し、プラグインとして自動的に読み込みます。

- 吉里吉里本体と同じフォルダ
- 吉里吉里本体以下と同じフォルダにある plugin (64bit版ではplugin64) フォルダ内

吉里吉里は探したプラグインを名前で昇順に並び替え、その順序でプラグインを読み込みます。たとえば、aaa.tpm は aab.tpm よりも先に読み込まれます。これはプラグインのおいてあるフォルダには影響せず、プラグインの名前にのみ影響されます (吉里吉里本体と同じフォルダに z.tpm があっても、plugin フォルダ内に a.tpm があれば a.tpm が先に読み込まれます )。プラグインの読み込み順序を規定したい場合は、プラグインのファイル名を変える必要があります。

## プラグインの作成について

吉里吉里のソース中に、吉里吉里付属のプラグインのソースがありますので参考にしてみてください。

現段階では、「その他の吉里吉里専用のプラグイン」の仕様は**固まっていません**。将来仕様が変更されても、ソースレベルでの互換性は保たれるとおもうので、バイナリレベルでの互換性が失われた場合でも、吉里吉里本体に合わせて再構築すれば使えるようになるとは思います。

## Susie Plug-in について

Takechin 氏作の画像ビューア「Susie32」用のプラグインを利用することができます。

00IN 形式 (画像用プラグイン) と 00AM 形式 (アーカイブ用プラグイン) を使うことができますが、以下の制限、あるいは吉里吉里独自の仕様があります。

- 吉里吉里は拡張子で画像の形式を判断するため、本来の拡張子 ( GetPluginInfo 関数が返すもの ) と違う拡張子がついたような画像に対応できない ( アーカイブは対応形式をすべてチェックするので拡張子が異なっていても OK )
- 32bpp のビットマップはアルファチャンネル付きのビットマップとして見なされる
- 一部、受け付けられないビットマップ形式がある (RLE 圧縮された物や BITFIELDS が指定されているものなど )
- Susie プラグイン経由での画像読み込みやアーカイブアクセスは、吉里吉里がネイティブに扱う画像形式や xp3 アーカイブに比べてパフォーマンスがかなり低くなる
- アーカイブ中のファイルはメモリ上に展開されるため、大きなファイルを扱うには不向き
- アーカイブ内アーカイブには未対応
- Mac binary には未対応

また、Susie plug-in の規格に完全に対応していないプラグインの中には、吉里吉里と相性の悪いプラグインも存在します。

## 吉里吉里付属のプラグインについて

吉里吉里Z に標準で同梱されているプラグインの一覧です。各プラグインのソースコードは [wamsoft](https://github.com/wamsoft) 配下の各リポジトリで管理されています。

クラスを追加するものはリファレンスの各クラスのページを、既存クラスを拡張するものは拡張先クラスのページの「プラグイン拡張」節を参照してください。

### 全プラットフォーム共通

| プラグイン | 説明 |
|---|---|
| **AlphaMovie** | アルファチャンネル付き動画 ( .amv ) を再生する [AlphaMovie](../reference/AlphaMovie.md) クラスを追加します。 |
| **csvParser** | CSV ファイルを解析する [CSVParser](../reference/CSVParser.md) クラスを追加します。 |
| **expat** | XML を解析する [XMLParser](../reference/XMLParser.md) クラスを追加します。 |
| **extrans** | wave / mosaic / turn / rotatezoom / rotatevanish / rotateswap / ripple の追加トランジション 7 種を登録します。詳細は [トランジション](Transition.md) を参照してください。 |
| **extNagano** | 3duniversal / blurfade / scanline / zoomfade / rgbfade / spin / flutter / book / imagewipe / honeyturn / morphing / multiripple の追加トランジション 12 種を登録します。詳細は [トランジション](Transition.md) を参照してください。 |
| **getSample** | 再生中サウンドのサンプル値を取得するメソッドを [WaveSoundBuffer](../reference/WaveSoundBuffer.md) に追加します。 |
| **json** | JSON の読み書き ( evalJSON / saveJSON 等 ) を [Scripts](../reference/Scripts.md) に追加します。 |
| **KAGParserEx** | KAG シナリオを解析する [KAGParser](../reference/KAGParser.md) クラスを追加します ( 本体組み込み版を拡張版で置き換えます )。 |
| **krkr_richtext** | 多言語・装飾対応のリッチテキスト描画を行う [RichText](../reference/RichText.md) クラス群と [Layer](../reference/Layer.md) 拡張を追加します。 |
| **layerExAreaAverage** | 面積平均法による高品質な縮小コピーを [Layer](../reference/Layer.md) に追加します。 |
| **layerExBTOA** | 青成分をアルファ値へ変換するメソッドを [Layer](../reference/Layer.md) に追加します。 |
| **layerExImage** | 明度/コントラスト/色相/彩度の調整やノイズ追加などの画像処理を [Layer](../reference/Layer.md) に追加します。 |
| **layerExLongExposure** | 長時間露光 ( フレーム累積合成 ) 風の効果を [Layer](../reference/Layer.md) に追加します。 |
| **layerExRaster** | ラスタスクロール効果を [Layer](../reference/Layer.md) に追加します。 |
| **layerExSave** | レイヤ画像の非同期セーブ ( PNG / TLG5 ) を [Layer](../reference/Layer.md) / [Window](../reference/Window.md) に追加します。 |
| **layerExVector** | thorvg による SVG などのベクター描画を [Layer](../reference/Layer.md) に追加します ( [GdiPlus](../reference/GdiPlus.md) 互換 API )。 |
| **lineParser** | 行単位のテキスト解析を行う [LineParser](../reference/LineParser.md) クラスを追加します。 |
| **minizip** | ZIP アーカイブの読み込み ( zip:// 自動検索パス ) と作成を行う [Zip](../reference/Zip.md) / [Unzip](../reference/Unzip.md) クラスを追加します。 |
| **psdfile** | Photoshop PSD ファイルを読み込む [PSD](../reference/PSD.md) クラスを追加します。 |
| **saveStruct** | Array / Dictionary の saveStruct を拡張し、UTF-8 など出力エンコーディングを指定可能にします ( [Scripts](../reference/Scripts.md) 参照 )。 |
| **scriptsEx** | スクリプト実行系のユーティリティを [Scripts](../reference/Scripts.md) に追加します。 |
| **shrinkCopy** | 高速な縮小コピーを [Layer](../reference/Layer.md) に追加します。 |
| **sigcheck** | ファイル署名のバックグラウンド検証を [Window](../reference/Window.md) に追加します。 |

### Windows ( WINVER ビルド ) 専用

Win32 API に依存しているため、現時点では WINVER ビルドでのみ利用できます。

| プラグイン | 説明 |
|---|---|
| **addFont** | プライベートフォント ( .ttf / .otf ) の動的追加を行います。 |
| **binaryStream** | ファイルをバイナリレベルで読み書きする [BinaryStream](../reference/BinaryStream.md) クラスを追加します。 |
| **fpslimit** | メインループの実行頻度に制限をかけます ( 現在は本体の -contfreq オプションで代替できます )。 |
| **fstat** | ファイルサイズや更新日時の取得などを [Storages](../reference/Storages.md) に追加します。 |
| **gamepad** | ゲームパッドを直接扱う [Pad](../reference/Pad.md) クラスを追加します。 |
| **httprequest** | HTTP 通信を行う [HttpRequest](../reference/HttpRequest.md) クラスを追加します。 |
| **layerExDraw** | GDI+ による図形/テキスト描画を行う [GdiPlus](../reference/GdiPlus.md) クラス群を追加します。 |
| **memfile** | メモリ上の仮想ファイル ( mem:// ) を [Storages](../reference/Storages.md) に追加します。 |
| **menu** | ウィンドウメニューを構築する [MenuItem](../reference/MenuItem.md) クラスを追加します。 |
| **messenger** | 外部プロセスとの WM_COPYDATA ベースのメッセージ交換を [Window](../reference/Window.md) に追加します。 |
| **msgreceiver** | 外部制御の口 ( WM_COPYDATA 受信 ) を追加します ( 非推奨。messenger を利用してください )。 |
| **process** | 外部プロセスの起動と監視を行う [Process](../reference/Process.md) クラスを追加します。 |
| **shellExecute** | 関連付けアプリケーションによるファイル / URL のオープンを [System](../reference/System.md) に追加します。 |
| **stdio** | 標準入出力へのアクセスを [System](../reference/System.md) に追加します。 |
| **systemEx** | OS 情報の取得などのユーティリティを [System](../reference/System.md) に追加します。 |
| **tftSave** | レンダリング済みフォントデータの保存機能を [System](../reference/System.md) / [Layer](../reference/Layer.md) に追加します。 |
| **varfile** | TJS の変数空間 ( 辞書中の octet ) をファイルとして参照する var:// アクセスを追加します。 |
| **win32dialog** | Win32 ネイティブダイアログを構築する [WIN32Dialog](../reference/WIN32Dialog.md) クラスを追加します。 |
| **win32ole** | OLE オートメーション / ActiveX を扱う [WIN32OLE](../reference/WIN32OLE.md) / [ActiveX](../reference/ActiveX.md) / [JScriptHost](../reference/JScriptHost.md) クラスを追加します。 |
| **windowEx** | ウィンドウ操作の各種拡張を [Window](../reference/Window.md) / [System](../reference/System.md) / [Console](../reference/Console.md) などに追加します。 |
| **windowExProgress** | 実行ブロック中でも表示され続けるプログレスバー付きウィンドウ表示を [Window](../reference/Window.md) に追加します。 |

#### OpenGL ES 描画系

GLES ( ANGLE/glad ) で描画するプラグイン群です。描画先の GL コンテキストは吉里吉里本体の `OGLDrawDevice` か、`krkrgles` の `GLESAdaptor` が供給します。現状ソースが `tjs_char == wchar_t` / Win32 W-API 前提のため、WINVER ビルドでのみ利用できます。

| プラグイン | 説明 |
|---|---|
| **krkrgles** | OpenGL ES ( ANGLE/EGL 経由 ) で描画した結果を [Layer](../reference/Layer.md) へ吸い上げる `GLESAdaptor` / `GLESTexture` クラスを追加します。GPU 上で完結するポストエフェクト機構を持ちます。 |
| **krkreffekseer** | [Effekseer](https://effekseer.github.io/) のエフェクト ( .efk / .efkefc / .efkzip ) をホスト供給の GL コンテキストへ描画する `EffekseerDevice` / `EffekseerEffect` / `EffekseerPlayer` クラスを追加します。 |
| **krkrlive2d** | Live2D Cubism モデルを再生・描画する `Live2DDevice` / `Live2DModel` / `Live2DPlayer` / `Live2DMatrix` クラスを追加します。**Live2D Cubism Core が必要なため、環境変数 `CUBISM_SDK` が設定されているときのみビルドされます** ( ドライバ側 CMake が `$CUBISM_SDK/Core` を参照 )。 |
