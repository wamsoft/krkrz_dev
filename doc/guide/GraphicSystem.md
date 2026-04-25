# グラフィックシステム

## グラフィックシステムについて

吉里吉里は、レイヤによるグラフィックの表示機構を持っています。

各レイヤはアルファブレンドによる透過重ね合わせや階層構造管理機能を持っています。また、レイヤを GUI 部品 (ウィジット) として動作させることができるように、ユーザからの入力を受け取るための機構 ( フォーカス ) を持っています。



重ね合わされたレイヤは、描画デバイスと呼ばれる機構にて、ウィンドウに描画されます。デフォルトでは BasicDrawDevice と呼ばれる、単純にレイヤの出力をウィンドウに描画するだけのデバイスが使用されます。描画デバイスは[Window.drawDevice](../reference/Window.md#drawdevice)プロパティを操作することで自由に差し替えられるようになっており、用途に応じた演出効果などをユーザが独自に(プラグインの形式で)定義することとができますが、吉里吉里Zが内蔵しているのは前述の BasicDrawDevice のみです。

## 読み書き可能な画像形式

標準状態の吉里吉里で、[Layer.loadImages](../reference/Layer.md#loadimages) でレイヤに読み込む、レイヤに書きこむことのできる形式は以下の通りです。

- **BMP**  
  Windows 標準のビットマップ形式です。32 bpp の BMP はアルファチャネル付きビットマップと見なされます。
  
  RLE圧縮されたビットマップは読み込むことができません。
- **PNG**  
  Portable Network Graphic 形式を読み込むことができます。アルファチャネル付きビットマップ PNG も読み込むことができます。
- **JPEG**  
  JPEG 形式を読み込むことができます。算術圧縮されたものや可逆圧縮のものは読み込むことができませんが、そもそも滅多に見かけないのでかまわないかと思います。
- **TLG5**  
  吉里吉里独自の可逆圧縮フォーマットです。拡張子は .tlg です。アルファチャネル付きのものも読み込むことができます。圧縮率はさほど高くありませんが、高速に展開できるのが特徴です。この形式は**マスク画像(_m) あるいは領域画像 (_p) に使用することはできません**。アルファチャンネル無しのフルカラー画像、あるいはアルファチャンネル付きのフルカラー画像のみを扱うことができます。
- **TLG6**  
  吉里吉里独自の可逆圧縮フォーマットです。拡張子はTLG5と同じく .tlg です。TLG6は高い圧縮率が特徴です。展開速度はTLG5の２倍弱かかりますが、それでもPNGの２倍以上高速に展開でき、サイズもPNGより2縲鰀4割小さくなります。
- **JPEG XR**  
  JPEG XR形式を読み込むことができます。不可逆ですが JPEG よりも高画質でアルファチャンネルもサポートされています。
  
  画質を優先して圧縮すると可逆圧縮画像と見分けがつきづらく、ファイルサイズも小さいためサイズが重要な時は有用です。
  
  Ver 1.1.0 からサポートされ、現在読み込みのみ対応しています。
  
  Ver 1.3.0 から保存にも対応しました。
- **メイン/マスク分離形式**  
  メイン/マスク分離形式は、色情報の画像(メイン) とアルファチャネル(マスク) の画像が分離している形式で、マスク画像は、メイン画像のファイル名に _m が付加されたものとなります ( たとえば、abc.jpeg に対して abc_m.jpeg )。
  
  メイン/マスク画像の形式が異なっていてもかまいません。

その他、Susie Plug-in を使って読み込み可能な画像形式を増やすことができます。Susie plug-in は [Plugins.link](../reference/Plugins.md#link) メソッドで読み込むことができます。

Susie Plug-in から 32bpp のビットマップが渡された場合は、アルファチャネル付きビットマップと見なされます。

## レイヤタイプ

吉里吉里のレイヤは様々な合成モード(レイヤタイプ)で表示することができます。

以下の合成モードがあり、lt で始まるレイヤタイプ定数を [Layer.type](../reference/Layer.md#type) プロパティに指定することができます。

なお、式中の *result* は結果、*dest* は重ね合わせ先の画像の輝度、*src* は重ね合わせる画像の輝度、*α*は重ね合わせる画像のピクセルごとのアルファ値で、すべて値の範囲は 0.0 縲鰀 1.0 とします。

また、ここでは説明のために以下の関数を定義します。

- abs(*a*) : *a* の絶対値
- max(*a*, *b*) : *a* と *b* のどちらか大きい方
- min(*a*, *b*) : *a* と *b* のどちらか小さい方
- blend(*a*, *b*, *r*) = *a* × (1.0 - *r*) + *b* × *r*

- ****ltOpaque** (**ltCoverRect**)**  
  ltOpaque は透過を伴わない表示です。常にレイヤの矩形全体が完全不透明な表示になります ( このレイヤタイプに限りませんが、[Layer.opacity](../reference/Layer.md#opacity) で不透明度を下げている場合はそれに従います )。
  
  
  
  式 : *result* = *src*
  
  > **Note:**
  > ltCoverRect でも同じ意味になりますが、2.23 beta 2 未満における古い名称です。
- ****ltAlpha** (**ltTransparent**)**  
  ltAlpha はアルファ合成を行います。透過を行う際のもっとも基本的なタイプです。BMP や Susie plug-in からのアルファチャネルの入力においても下記の式が使われます。
  
  
  
  式 : *result* = blend(*dest*, *src*, *α*)
  
  > **Note:**
  > ltTransparent でも同じ意味になりますが、2.23 beta 2 未満における古い名称です。
- ****ltAddAlpha****  
  ltAddAlpha は加算アルファ合成を行います。
  
  でこの形式に適した画像を出力できます。また、[Layer.convertType](../reference/Layer.md#converttype) メソッドで ltAlpha からこの形式に変換することができます。
  
  ltAddAlphaのレイヤは、ltAlpha のレイヤの直接の子になると正常に表示できません。
  
  
  
  式 : *result* = min(1.0, *dest* × ( 1.0 - *α* ) + *src*)
- ****ltAdditive****  
  ltAdditive は加算合成を行います。光彩の表現に適しています。Photoshopにおける「覆い焼き(リニア)」ですが、Photoshopと同じ効果を得たい場合は後述の ltPsAdditive を使用してください。ltPsAdditive と違い、ltAdditive では *α*は無視されます。
  
  中性色 (重ね合わせても変化のない色) は黒です。
  
  
  
  式 : *result* = min(1.0, *dest* + *src*)
- ****ltSubtractive****  
  ltSubtractive は減算合成を行います。*α*は無視されます。
  
  中性色は白です。
  
  
  
  式 : *result* = max(0.0, *dest* + *src* - 1.0)
  
  > **Note:**
  > *result* = *dest* - *src* と違うのは src が反転しないかするかの違いだけです。
- ****ltMultiplicative****  
  ltMultiplicative は乗算合成を行います。*α*は無視されます。
  
  中性色は白です。
  
  
  
  式 : *result* = *dest* × *src*
- ****ltDodge****  
  ltDodge は「覆い焼き」合成を行います。光に照らされたものの表現に適しています。*α*は無視されます。
  
  中性色は黒です。
  
  
  
  式 : *result* = min(1.0, *dest* ÷ ( 1.0 -  *src* ) )
- ****ltLighten****  
  ltLighten は「比較(明)」合成を行います。*α*は無視されます。
  
  中性色は黒です。
  
  
  
  式 : *result* = max(*dest*, *src*)
- ****ltDarken****  
  ltDarken は「比較(暗)」合成を行います。*α*は無視されます。
  
  中性色は白です。
  
  
  
  式 : *result* = min(*dest*, *src*)
- ****ltScreen****  
  ltLighten は「スクリーン乗算」合成を行います。*α*は無視されます。
  
  中性色は黒です。
  
  
  
  式 : *result* = 1.0 - ( 1.0 - *dest* ) × ( 1.0 - *src* )
- ****ltPsNormal****  
  ltPsNormal は ltAlpha と同じ効果を持ちます。歴史的な理由で ltAlpha とは別のルーチンや名称となっています。
- ****ltPsAdditive****  
  ltPsAdditive はPhotoshop互換の「覆い焼き(リニア)」合成(加算合成)を行います。ltAdditive と違い、*α*は無視されません。
  
  中性色は黒です。
  
  
  
  式 : *result* = blend(*dest*, min(1.0, *dest* + *src*), *α*)
- ****ltPsSubtractive****  
  ltPsSubtractive はPhotoshop互換の「焼き込み(リニア)」合成(減算合成)を行います。ltSubtractive と違い、*α*は無視されません。
  
  中性色は白です。
  
  
  
  式 : *result* = blend(*dest*, max(0.0, *dest* + *src* - 1.0), *α*)
- ****ltPsMultiplicative****  
  ltPsMultiplicative はPhotoshop互換の「乗算」合成を行います。ltMultiplicative と違い、*α*は無視されません。
  
  中性色は白です。
  
  
  
  式 : *result* = blend(*dest*, *dest* × *src*, *α*)
- ****ltPsScreen****  
  ltPsScreen はPhotoshop互換の「スクリーン」合成を行います。ltScreen と違い、*α*は無視されません。
  
  中性色は黒です。
  
  
  
  式 : *result* = blend(*dest*, 1.0 - (1.0 - *dest*) × (1.0 - *src*), *α*)
- ****ltPsOverlay****  
  ltPsOverlay はPhotoshop互換の「オーバーレイ」合成を行います。
  
  中性色は50%灰色です。
  
  
  
  式 : *result* = blend(*dest*, overlay(*dest*, *src*), *α*)
  
  ここで overlay(*a*, *b*) =
  
  *a* × *b* × 2.0  ( *a* < 0.5 のとき)
  
  1.0 - (1.0 - *a*) × (1.0 - *b*) × 2.0 (それ以外のとき)
- ****ltPsHardLight****  
  ltPsHardLight はPhotoshop互換の「ハードライト」合成を行います。
  
  中性色は50%灰色です。
  
  
  
  式 : *result* = blend(*dest*, hardlight(*dest*, *src*), *α*)
  
  ここで hardlight(*a*, *b*) =
  
  *a* × *b* × 2.0  (*b* < 0.5 のとき)
  
  1.0 - (1.0 - *a*) × (1.0 - *b*) × 2.0 (それ以外のとき)
- ****ltPsSoftLight****  
  ltPsSoftLight はPhotoshop互換の「ソフトライト」合成を行います。
  
  中性色は50%灰色です。
  
  
  
  式 : *result* = blend(*dest*, softlight(*dest*, *src*), *α*)
  
  ここで softlight(*a*, *b*) =
  
  *a*(0.5 ÷ *b*)  (*b* > 0.5 のとき)
  
  *a*((1.0 - *b*) × 2)  (それ以外のとき)
- ****ltPsColorDodge****  
  ltPsColorDodge はPhotoshop互換の「覆い焼きカラー」合成を行います。ltDodge と違い、*α*は無視されません。
  
  中性色は黒です。
  
  
  
  式 : *result* = blend(*dest*, min(1.0, *dest* ÷ ( 1.0 -  *src* ) ), *α*)
- ****ltPsColorDodge5****  
  ltPsColorDodge はPhotoshopのバージョン 5.x 以下と互換の「覆い焼きカラー」合成を行います。ltPsColorDodge とは式が若干異なります。
  
  中性色は黒です。
  
  
  
  式 : *result* = min(1.0, *dest* ÷ ( 1.0 - *src* × *α*) )
- ****ltPsColorBurn****  
  ltPsColorBurn はPhotoshop互換の「焼き込みカラー」合成を行います。
  
  中性色は白です。
  
  
  
  式 : *result* = blend(*dest*, max(0.0, 1.0 - (1.0 - *dest*) ÷ *src*), *α*)
- ****ltPsLighten****  
  ltPsLighten はPhotoshop互換の「比較(明)」合成を行います。ltLighten と違い、*α*は無視されません。
  
  中性色は黒です。
  
  
  
  式 : *result* = blend(*dest*, max(*dest*, *src*), *α*)
- ****ltPsDarken****  
  ltPsDarken はPhotoshop互換の「比較(暗)」合成を行います。ltDarken と違い、*α*は無視されません。
  
  中性色は白です。
  
  
  
  式 : *result* = blend(*dest*, min(*dest*, *src*), *α*)
- ****ltPsDifference****  
  ltPsDifference はPhotoshop互換の「差の絶対値」合成を行います。
  
  中性色は黒です。
  
  
  
  式 : *result* = blend(*dest*, abs(*dest* - *src*), *α*)
- ****ltPsDifference5****  
  ltPsDifference5 はPhotoshopのバージョン 5.x 以下と互換の「差の絶対値」合成を行います。ltPsDifference とは式が若干異なります。
  
  中性色は黒です。
  
  
  
  式 : *result* = abs(*dest* - *src* × *α*)
- ****ltPsExclusion****  
  ltPsExclusion はPhotoshop互換の「除外」合成を行います。
  
  中性色は黒です。
  
  
  
  式 : *result* = blend(*dest*,  *dest* + *src* - 2.0 × *src* × *dest*, *α*)

## アルファ合成と加算アルファ合成

吉里吉里は、二つのアルファ合成モードを持っています。

- **アルファ合成**  
  [Layer.type](../reference/Layer.md#type) プロパティで **ltAlpha** を指定するとこの表示タイプになります。
  
  ltAlphaは多くのグラフィックソフトが採用しているアルファ合成モードです。他のグラフィックソフトで出力したデータをそのまま読み込む場合はこのモードが適しています。
- **加算アルファ合成**  
  [Layer.type](../reference/Layer.md#type) プロパティで **ltAddAlpha** を指定するとこの表示タイプになります。
  
  この形式はアルファ合成に比べて以下のメリット・デメリットがあります。
  
  - 式がアルファ合成よりも単純なため、表示が高速に行え、多くの描画メソッドでも高速な描画が可能です
  - アルファ合成と一緒に加算合成も表現できます
  - この形式に対応しているグラフィックソフトがほとんどありません
  
  ltAddAlphaと同じ合成モードに対応しているグラフィックソフトはそうはないと思いますので、他ソフトの出力を吉里吉里でこの形式で扱うには、
  
  でこのタイプの画像を出力するか、[Layer.convertType](../reference/Layer.md#converttype) メソッドで ltAlpha からこの形式に変換する必要があります。
  
  画像フォーマットコンバータでは、Photoshop形式で、「通常」レイヤーと「覆い焼き(リニア)」レイヤーの組み合わさった入力を、加算アルファ合成用画像の入力として受け付けることができます。

## レイヤタイプと描画方式と演算モード

吉里吉里にはレイヤタイプ (ltで始まる定数で指定)と、描画方式 (dfで始まる定数で指定) と、演算モード (omで始まる定数で指定)があります。

それぞれ似たような名称を持っていますが、用途は以下のように分かれています。

- **レイヤタイプ**  
  レイヤタイプは [Layer.type](../reference/Layer.md#type) プロパティで指定する値で、レイヤがどのように表示されるかを指定します。
- **描画方式**  
  描画方式は [Layer.face](../reference/Layer.md#face) プロパティで指定する値で、レイヤにどのように描画するかを指定します。dfAutoを指定すると、レイヤタイプに従って適切な描画方式が決定されます。レイヤタイプに最適な描画方法とは異なる描画方式で描画することもできます。
  
  [Layer.copyRect](../reference/Layer.md#copyrect) メソッドのようなレイヤ間のコピーを行うメソッドでは、どの情報をコピーするかの選択にも用いられます。dfBoth (あるいは dfAlpha あるいは dfAddAlpha の場合) は、メインとマスクの両方がコピーされます。dfMain (あるいは dfOpaque) の場合はメインのみがコピーされます。dfMask の場合はマスクのみ、dfProvince の場合は領域画像のみがコピーされます。
  
  同様に、[Layer.fillRect](../reference/Layer.md#fillrect) メソッドでは、どの情報を塗りつぶすかの選択に用いられます。dfBoth (あるいは dfAlpha あるいは dfAddAlpha の場合) は、メインとマスクの両方が塗りつぶされます。dfMain (あるいは dfOpaque) の場合はメインのみがコピー塗りつぶされます。dfMask の場合はマスクのみ、dfProvince の場合は領域画像のみが塗りつぶされます。
- **演算モード**  
  演算モードは [Layer.operateRect](../reference/Layer.md#operaterect) メソッドなどの引数で指定する値で、演算元(重ね合わせるレイヤ) をどのように扱うかを指定する値です。omAuto を指定すると、演算元のレイヤタイプに従って適切なモードが決定されます。

## アルファチャンネルの保護

[Layer.face](../reference/Layer.md#face) プロパティで指定する描画方式が **dfOpaque** の場合、[Layer.holdAlpha](../reference/Layer.md#holdalpha) プロパティで、描画先 (メソッドを実行しようとするレイヤ)のアルファチャンネルを保護するかどうかを指定できます。

アルファチャンネルを保護すると、アルファチャンネル (不透明度) は保護され、透明な部分は透明なままになります。

アルファチャンネルを保護しないと、アルファチャンネル (不透明度) は破壊されます。破壊されるとは、どのような状態になるか分からなくなると言うことです。

しかし、[Layer.type](../reference/Layer.md#type) プロパティが **ltAlpha** でも **ltAddAlpha** でも無い場合は、レイヤのアルファチャンネルは使われませんから、Layer.holdAlpha プロパティを偽にしても、通常は問題はありません。また、偽にすれば、多くのメソッドにおいて真の時よりも高速に描画できます。
