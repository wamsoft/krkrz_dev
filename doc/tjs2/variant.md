# tTJSVariant 型

## tTJSVariant とは

tTJSVariant 型は、TJS2 における「変数」のデータを扱う型です。

tTJSVariant 型は内部型をもっていて、一つの型で void(未定義)、オブジェクト、整数、実数、文字列、オクテット列を表すことができます。

また、演算に関してはこれらの内部型の変換を自動的に扱います。

## tTJSVariantType

tTJSVariant の内部型を表す列挙型です。tTJSVariant::**Type** メソッドで取得することができます。

- ****tvtVoid****  
  void型です。tTJSVariant 型を引数無しのコンストラクタで構築した場合はこの型になります。nullではありません。
- ****tvtObject****  
  オブジェクト型です。null の場合はこの内部型になります。
- ****tvtString****  
  文字列型です。
- ****tvtOctet****  
  オクテット列型です。
- ****tvtInteger****  
  整数型です。tTVInteger 型の数値を保持します。
- ****tvtReal****  
  実数型です。tTVReal 型の数値を保持します。

## オブジェクト参照

内部型のうち、オブジェクトは参照カウンタ方式による管理を行います。

tTJSVariant 自体は参照カウンタの管理を自動的に行いますが、tTJSVariant から

を取得する各メソッドや、tTJSVariantClosure 型を取得するメソッドからオブジェクトへのポインタを取り出したあとの、参照カウンタの管理には関知しないので注意してください。

## オブジェクト型

**tTJSVariantClosure** 型は、tTJSVariant 内部でオブジェクトを保持している型です。この型には iTJSDispatch2 インターフェースを２つ保持する機構があり、一つはオブジェクトそのもの、もう一つはそのオブジェクトが実行されるコンテキストの情報を持っています。

tTJSVariantClosure 型は iTJSDispatch2 インターフェースが持っている各メソッドを持っています。tTJSVariantClosure 経由でこれらのメソッドにアクセスすれば、実行コンテキストを正しく処理することができます。



tTJSVariantClosure 型を tTJSVariant 型から取り出すために tTJSVariant::**AsObjectClosure** と tTJSVariant::**AsObjectClosureNoAddRef** の２つがあります。前者はオブジェクトの参照カウンタをインクリメントしますが、後者はインクリメントしません。

tTJSVariantClosure 型は参照カウンタを自動的に管理する機構を持たないため、tTJSVariantClosure 型を tTJSVariant 型から取り出した後は参照カウンタの管理に注意する必要があります。

## 文字列型

TJS2 の文字列は参照カウンタ方式で管理されていて、単純なコピーなどでは文字列の参照カウンタが増えるだけで文字列の実体は複製されません。

tTJSVariantString 型は、tTJSVariant 型と **tTJSString** 型で使われる、文字列を管理するための型です。tTJSVariantString 型を tTJSVariant 型から取り出すには tTJSVariant::**AsString** を用いることができます (このメソッドは参照カウンタをインクリメントします)。ただし、tTJSVariantString 型自体は参照カウンタを自動的に管理する機構を持っていないため、tTJSVariantString を使うときは注意が必要です。

tTJSString 型ならば参照カウンタを管理できるので、tTJSString 型に変換するのが楽でしょう ( tTJSVariant は tTJSString との変換演算子が定義されています )。

## オクテット列型

TJS2 のオクテット列も文字列型同様、参照カウンタ方式で管理されています。

**tTJSVariantOctet** 型は、オクテット列を管理するための型です。この型も tTJSVariantString や tTJSVariantClosure 同様、参照カウンタを管理するための機構を持ってないので注意してください。tTJSVariantOctet 型を tTJSVariant 型から取り出すには tTJSVariant::**AsOctet** (参照カウンタをインクリメントする)、tTJSVariant::**AsOctetNoAddRef** (参照カウンタをインクリメントしない) を用いることができます。

## 変換

tTJSVariant には様々な変換演算子やコンストラクタが定義されているので、プリミティブ型のように扱うことができます。

上記のように、参照カウンタで管理される型との変換を行う場合は十分に注意する必要があります。

## 演算

様々な演算子がオーバーロードされているので、演算に関してもプリミティブ型同様に行うことができます。演算の過程で必要になるような型変換などは自動的に処理されます。
