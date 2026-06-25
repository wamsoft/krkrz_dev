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

吉里吉里に標準で添付されているプラグインの説明です。

- ****wuvorbis.dll****  
  **OggVorbis** を吉里吉里で再生可能にするためのプラグインです。
- ****wumsadp.dll****  
  **Microsoft ADPCM** 形式の .wav ファイルを吉里吉里で再生可能にするためのプラグインです。
- ****wutcwf.dll****  
  **TCWF** 形式のファイルを吉里吉里で再生可能にするためのプラグインです。
- ****extrans.dll****  
  吉里吉里本体のトランジションの種類を拡張するためのプラグインで、吉里吉里本体に接続するといくつかのトランジションが使用可能になります。
  
  このプラグインの使い方については
  
  を参照してください。
- ****dirlist.dll****  
  指定されたディレクトリ内にあるファイルのリストを得るためのプラグインです。
  
  このプラグインを接続すると **getDirList** という関数が使用可能になります。
  
  `getDirList(ディレクトリ)`
  
  の形式で指定すると、そのディレクトリ内にあるすべてのファイルのリストを
  配列で返してきます。このリストにはディレクトリも含まれ、ディレクトリの場合は
  要素の文字列の最後に '/' がついています。
  
  また、このリストには通常、 './' と '../' の２つの要素が含まれます。
  
  この関数は指定されたディレクトリ直下のファイルのリストを得るだけで、再帰的に
  それよりも下層のディレクトリのファイルを得ることはありません。
- ****fftgraph.dll****  
  WaveSoundBuffer と同期して、簡易的なスペクトラムアナライザー（スペアナ）を表示させるための
  プラグインです。
  
  このプラグインを接続すると **drawFFTGraph** という関数が使用可能になります。
  
  使い方は吉里吉里ソースに含まれる fftgraph のソースおよび KAG 用のスペアナプラグインを
  参照してください。
- ****win32ole.dll****  
  ActiveX コントロール吉里吉里のウィンドウに貼り付けたり、OLE オートメーション可能なオブジェクトを吉里吉里から操作するためのプラグインです。
  
  これを使用すると、たとえば吉里吉里のウィンドウに Web ブラウザ (Internet Explorer) や メディアプレーヤを貼り付けたり、Excel を吉里吉里から操作したりすることができます。
  
  使用方法については 吉里吉里ソースの [kirikiri2/trunk/kirikiri2/src/plugins/win32/win32ole/manual.tjs](https://sv.kikyou.info/trac/kirikiri/browser/kirikiri2/trunk/kirikiri2/src/plugins/win32/win32ole/manual.tjs) および [kirikiri2/trunk/kirikiri2/tests/win32ole](https://sv.kikyou.info/trac/kirikiri/browser/kirikiri2/trunk/kirikiri2/tests/win32ole) ディレクトリを参照してください。
- ****wsh.dll** (experimental)**  
  吉里吉里で JScript、VBScript、PerlScript を使用可能にするプラグインです (RubyScript の動作については調整中です)。
  
  このプラグインを接続すると、[Scripts.exec](../reference/Scripts.md#exec) と [Scripts.execStorage](../reference/Scripts.md#execstorage) が拡張されます。
  
  Scripts.exec は第２引数に 拡張子、あるいは ProgId 、あるいは CLSID を受け付けるようになります。Scripts.execStorage も Scripts.exec 同様に第２引数に拡張子、あるいは ProgId 、あるいは CLSID を受け付けるようになりますが、第２引数が省略された場合は第１引数の拡張子から言語が決定されます。
  
  拡張子は js, vbs, pl, rb のいずれかで、ProgId は、それぞれ JScript, VBScript, PerlScript, RubyScript となります。CLSID を指定する場合は、スクリプトエンジンのクラスIDを指定します。これら以外の拡張子が渡された場合は TJS スクリプトとして実行します。
  
  使用方法については 吉里吉里ソースの [kirikiri2/trunk/kirikiri2/tests/wsh](https://sv.kikyou.info/trac/kirikiri/browser/kirikiri2/trunk/kirikiri2/tests/wsh) ディレクトリを参照してください。
- ****agg.dll** (experimental)**  
  吉里吉里で [AGG (Anti-Grain Geometry)](http://www.antigrain.com/) を利用して図形描画を行うプラグインです。
  
  簡易的な SVG 読み込み/描画機能を利用することができます。
  
  SVG を描画するには、たとえば
  
  ```
  var svg  = new AGGPrimitive(layer, "SVG", "tiger.svg");
  var svg1 = new AGGPrimitive(layer, "SVG", "tiger.svg");
  ```
  
  とします (もとの AGG の SVG 読み込みサポートの制限により、読み込めない SVG が多いです)。
  
  詳しくは 吉里吉里ソースの [kirikiri2/trunk/kirikiri2/src/plugins/win32/layerExAgg](https://sv.kikyou.info/trac/kirikiri/browser/kirikiri2/trunk/kirikiri2/src/plugins/win32/layerExAgg/) ディレクトリを参照してください。
- ****csvParser.dll** (experimental)**  
  吉里吉里で CSV (Comma Separated Values) ファイルを読み込むためのプラグインです。
  
  詳しくは 吉里吉里ソースの [kirikiri2/trunk/kirikiri2/src/plugins/win32/csvParser](https://sv.kikyou.info/trac/kirikiri/browser/kirikiri2/trunk/kirikiri2/src/plugins/win32/csvParser/) ディレクトリを参照してください。
- ****expat.dll** (experimental)**  
  吉里吉里で [Expat](http://expat.sourceforge.net/) を通じて XML ァイルを読み込むためのプラグインです。
  
  詳しくは 吉里吉里ソースの [kirikiri2/trunk/kirikiri2/src/plugins/win32/expat](https://sv.kikyou.info/trac/kirikiri/browser/kirikiri2/trunk/kirikiri2/src/plugins/win32/expat/) ディレクトリを参照してください。
- ****json.dll** (experimental)**  
  吉里吉里で [JSON](http://www.json.org/) を読み込むためのプラグインです。
  
  詳しくは 吉里吉里ソースの [kirikiri2/trunk/kirikiri2/src/plugins/win32/json](https://sv.kikyou.info/trac/kirikiri/browser/kirikiri2/trunk/kirikiri2/src/plugins/win32/json/) ディレクトリを参照してください。
- ****layerExImage.dll** (experimental)**  
  レイヤに対し、明度とコントラストの調整、色相と彩度の調整、ノイズ追加を読み込むためのプラグインです。
  
  詳しくは 吉里吉里ソースの [kirikiri2/trunk/kirikiri2/src/plugins/win32/layerExImage](https://sv.kikyou.info/trac/kirikiri/browser/kirikiri2/trunk/kirikiri2/src/plugins/win32/layerExImage/) ディレクトリを参照してください。
- ****perspective.dll** (experimental)**  
  レイヤのパースペクティブ変形を行うプラグインです。
  
  詳しくは 吉里吉里ソースの [kirikiri2/trunk/kirikiri2/src/plugins/win32/layerPerspective](https://sv.kikyou.info/trac/kirikiri/browser/kirikiri2/trunk/kirikiri2/src/plugins/win32/layerExPerspective/) ディレクトリを参照してください。
- ****saveStruct.dll****  
  Array/Dictionary の saveStruct の処理を、Unicode (UTF-16)ではなく、現在のコードページまたは UTF-8 で出力可能にする物です。
  
  詳しくは 吉里吉里ソースの [kirikiri2/trunk/kirikiri2/src/plugins/win32/saveStruct](https://sv.kikyou.info/trac/kirikiri/browser/kirikiri2/trunk/kirikiri2/src/plugins/win32/saveStruct/) ディレクトリを参照してください。
- ****fstat.dll****  
  Storages クラスに、ファイルのサイズや更新日時などの情報を取得したり、ファイルをストレージシステム内から取り出すメソッドを追加します。
  詳しくは 吉里吉里ソースの [kirikiri2/trunk/kirikiri2/src/plugins/win32/fstat](https://sv.kikyou.info/trac/kirikiri/browser/kirikiri2/trunk/kirikiri2/src/plugins/win32/fstat/) ディレクトリを参照してください。
- ****clipboardEx.dll**(experimental)**  
  Clipboard クラスに、画像やTJS式をクリップボードを介してやりとりする機能や、クリップボードの更新を自動検知するハンドラを登録する機能を追加します。
  詳しくは 吉里吉里ソースの [kirikiri2/trunk/kirikiri2/src/plugins/win32/clipboardEx](https://sv.kikyou.info/trac/kirikiri/browser/kirikiri2/trunk/kirikiri2/src/plugins/win32/clipboardEx/) ディレクトリを参照してください。
