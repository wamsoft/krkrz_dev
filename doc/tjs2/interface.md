# iTJSDispatch2 インターフェース

## iTJSDispatch2 とは

iTJSDispatch2 は、TJS2 における「オブジェクト」に対するインターフェースを提供する抽象基本クラスです。

TJS2 の「オブジェクト」には関数オブジェクト、クラス、プロパティオブジェクト、配列(辞書配列) などが含まれます。

TJS2 に対するほとんどの操作はこのインターフェースを通じて行うことができます。



以下、このインターフェースを利用する側として説明をします。

## 序数による呼び出し

iTJSDispatch2 のメソッドには、メソッド名の末尾が ByNum で終わる物があります。これは、序数による呼び出しを行うものであり、たとえば メンバ名に "23" を指定して FuncCall を呼ぶのと、序数に 23 を指定して FuncCallByNum を呼ぶのは等価です。

配列オブジェクトにアクセスする時に便利でしょう。



ByNum が末尾につくメソッドは、末尾に ByNum のつかない同名のメソッドの membername 引数と hint 引数がなく、代わりに tjs_int num があります。引数 num には序数を指定します。



以下、序数による呼び出しを行うメソッドについては詳細な説明を省略します (末尾に ByNum のつかない同名のメソッドの説明を参照してください)。

## AddRef

tjs_uint iTJSDispatch2::AddRef(void)



オブジェクトの参照カウンタをインクリメントします。

TJS2 の各オブジェクトは参照カウンタで管理されています。

戻り値はインクリメント後の参照カウンタの値ですが、この値を信用することは推奨されません。

## Release

tjs_uint iTJSDispatch2::Release(void)



オブジェクトの参照カウンタをデクリメントします。

戻り値はデクリメント後の参照カウンタの値で、0 が戻ったときはオブジェクトが解放されたことを表します。しかし、この値を信用することは推奨されません。

## FuncCall

tjs_error iTJSDispatch2::FuncCall(

tjs_uint32 flag,

const tjs_char * membername,

tjs_uint32 *hint,

tTJSVariant *result,

tjs_int numparams,

tTJSVariant **param,

iTJSDispatch2 *objthis

)



関数呼び出しを行います。



引数は以下の通りです。

- **tjs_uint32 flag**  
  呼び出しフラグです(下記参照)。
- **const tjs_char * membername**  
  操作対象とするメンバ名です。
  
  NULL の場合は、このオブジェクト自身に対する操作になります。この場合は、このオブジェクトは関数の機能を持っている必要があります。
- **tjs_uint32 *hint**  
  「**ヒント**」を格納するための変数の領域を指定します。NULLでもかまいません。
  
  ヒントは、２回目以降の同じメンバ名に対する検索を高速に行えるようにするためのものです。hint に tjs_uint32 型の変数へのポインタを指定すると、そこにヒントとなる数値が書き込まれます。２回目以降はその数値を参考にしてメンバを検索します。参考にする程度ですので、ヒントの初期値はどのような値であってもかまいません ( 0 が推奨されます )。また、このような仕組みのため、ヒントとそれに対するメンバ名は１対１で対応しているとより効率的です (tTJSString 型はこのヒントのための機構を持っています)。
  
  オブジェクトによっては、ヒントを利用する機構を持っていないかも知れません。
- **tTJSVariant *result**  
  関数を呼び出した結果を格納するための tTJSVariant 型へのポインタを指定します。
  
  結果が必要ない場合は NULL を指定してかまいません。
- **tjs_int numparams**  
  関数に渡す引数の数を指定します。
- **tTJSVariant **param**  
  関数に渡す引数のポインタの配列を渡します。引数がない場合は NULL でかまいません。
- **iTJSDispatch2 *objthis**  
  関数が実行されるコンテキスト (this オブジェクト) を指定します。

## FuncCallByNum

tjs_error iTJSDispatch2::FuncCall(

tjs_uint32 flag,

tjs_int num,

tTJSVariant *result,

tjs_int numparams,

tTJSVariant **param,

iTJSDispatch2 *objthis

)



序数による関数呼び出しを行います。

## PropGet

tjs_error iTJSDispatch2::PropGet(

tjs_uint32 flag,

const tjs_char * membername,

tjs_uint32 *hint,

tTJSVariant *result,

iTJSDispatch2 *objthis

)



プロパティやメンバ変数の値の取得を行います。



引数は以下の通りです。

- **tjs_uint32 flag**  
  呼び出しフラグです(下記参照)。
- **const tjs_char * membername**  
  操作対象とするメンバ名です。
  
  
  
  NULL の場合は、このオブジェクト自身に対する操作になります。この場合は、このオブジェクトはプロパティ取得の機能を持っている必要があります。
  
  この引数が NULL でも成功するオブジェクトは、プロパティオブジェクトと見なされます。通常、このようなプロパティオブジェクトが他のオブジェクトのメンバになった場合は、このプロパティオブジェクト自体ではなく、そのプロパティオブジェクトに対して PropGet を行った結果が用いられます。この動作は呼び出しフラグに TJS_IGNOREPROP を指定することでバイパスすることができます。
- **tjs_uint32 *hint**  
  ヒントを格納するための変数の領域を指定します。NULLでもかまいません。
  
  ヒントの説明については FuncCall の説明を参照してください。
- **tTJSVariant *result**  
  結果を格納するための tTJSVariant 型へのポインタを指定します。NULL は許されません。
- **iTJSDispatch2 *objthis**  
  このメソッドが実行されるコンテキスト (this オブジェクト) を指定します。

## PropGetByNum

tjs_error iTJSDispatch2::PropGetByNum(

tjs_uint32 flag,

tjs_int num,

tTJSVariant *result,

iTJSDispatch2 *objthis

)



序数による、プロパティやメンバ変数の値の取得を行います。

## PropSet

tjs_error iTJSDispatch2::PropSet(

tjs_uint32 flag,

const tjs_char *membername,

tjs_uint32 *hint,

const tTJSVariant *param,

iTJSDispatch2 *objthis

)



プロパティやメンバ変数の値の設定を行います。



引数は以下の通りです。

- **tjs_uint32 flag**  
  呼び出しフラグです(下記参照)。
- **const tjs_char * membername**  
  操作対象とするメンバ名です。
  
  
  
  NULL の場合は、このオブジェクト自身に対する操作になります。この場合は、このオブジェクトはプロパティ設定の機能を持っている必要があります。
  
  この引数が NULL でも成功するオブジェクトは、プロパティオブジェクトと見なされます。通常、このようなプロパティオブジェクトが他のオブジェクトのメンバになった場合は、このプロパティオブジェクト自体ではなく、そのプロパティオブジェクトに対して PropSet が呼ばれます。この動作は呼び出しフラグに TJS_IGNOREPROP を指定することでバイパスすることができます。
- **tjs_uint32 *hint**  
  ヒントを格納するための変数の領域を指定します。NULLでもかまいません。
  
  ヒントの説明については FuncCall の説明を参照してください。
- **const tTJSVariant *param**  
  設定する値を表す tTJSVariant 型の変数へのポインタを指定します。NULL は許されません。
- **iTJSDispatch2 *objthis**  
  このメソッドが実行されるコンテキスト (this オブジェクト) を指定します。

## PropSetByVS

tjs_error iTJSDispatch2::PropSetByVS(

tjs_uint32 flag,

tTJSVariantString *membername,

const tTJSVariant *param,

iTJSDispatch2 *objthis

)



プロパティやメンバ変数の値の設定を行います。PropSet と異なるのは、メンバ名が tTJSVariantString により参照される点です。内部的に用いられます。tTJSVariantString は同じ文字列用メモリ領域を、複数の文字列オブジェクトが共有して使う機構を持っているため、このメソッドを介してプロパティの設定 (オブジェクト内へのメンバの作成) を行うと、メンバ名に使用される文字列メモリ領域用メモリの増加を防ぐことができます。

このメソッドを実装しない場合は TJS_E_NOTIMPL を返してください。代わりに PropSet が使用されます。また、このメソッドを呼び出して TJS_E_NOTIMPL が返された場合は、PropSet を代わりに使うように実装してください。

## PropSetByNum

tjs_error iTJSDispatch2::PropSetByNum(

tjs_uint32 flag,

tjs_int num,

const tTJSVariant *param,

iTJSDispatch2 *objthis

)



序数による、プロパティやメンバ変数の値の設定を行います。

## GetCount

tjs_error iTJSDispatch2::GetCount(

tjs_int *result,

const tjs_char *membername,

tjs_uint32 *hint,

iTJSDispatch2 *objthis

)



オブジェクトが保持しているメンバの数を返します。



引数は以下の通りです。

- **tjs_int *result**  
  結果を格納するための変数へのポインタを指定します。NULL は許されません。
- **const tjs_char * membername**  
  対象とするメンバの名前を指定します。
  
  NULL の場合、このオブジェクト自身の保持しているメンバの数が帰ります。
  
  メンバ名が指定された場合、もし、そのメンバがオブジェクトならば、そのオブジェクトの保持しているメンバの数を返します。指定されたメンバがオブジェクト型でなかった場合は失敗します。
- **tjs_uint32 *hint**  
  ヒントを格納するための変数の領域を指定します。NULLでもかまいません。
  
  ヒントの説明については FuncCall の説明を参照してください。
- **iTJSDispatch2 *objthis**  
  このメソッドが実行されるコンテキスト (this オブジェクト) を指定します。
  
  この引数は、通常、意味を持ちません(無視されます)。

## GetCountByNum

tjs_error iTJSDispatch2::GetCount(

tjs_int *result,

tjs_int num,

iTJSDispatch2 *objthis

)



GetCount の序数バージョンです。

## DeleteMember

tjs_error iTJSDispatch2::DeleteMember(

tjs_uint32 flag,

const tjs_char *membername,

tjs_uint32 *hint,

iTJSDispatch2 *objthis

)



メンバの削除を行います。



引数は以下の通りです。

- **tjs_uint32 flag**  
  呼び出しフラグです(下記参照)。
- **const tjs_char * membername**  
  対象とするメンバの名前を指定します。NULL は許されません。
- **tjs_uint32 *hint**  
  ヒントを格納するための変数の領域を指定します。NULLでもかまいません。
  
  ヒントの説明については FuncCall の説明を参照してください。
- **iTJSDispatch2 *objthis**  
  このメソッドが実行されるコンテキスト (this オブジェクト) を指定します。
  
  この引数は、通常、意味を持ちません(無視されます)。

## DeleteMemberByNum

tjs_error iTJSDispatch2::DeleteMemberByNum(

tjs_uint32 flag,

tjs_int num,

iTJSDispatch2 *objthis

)



序数によりメンバの削除を行います。

## EnumMembers

tjs_error iTJSDispatch2::EnumMembers(

tjs_uint32 flag,

tTJSVariantClosure *callback,

iTJSDispatch2 *objthis

)



オブジェクト内のメンバを列挙します。

callback にはコールバック関数を指定できますが、現バージョンではコールバック関数内でこのオブジェクトのメンバの作成や削除を行った場合の動作は保証されません。



引数は以下の通りです。

- **tjs_uint32 flag**  
  呼び出しフラグです。呼び出しフラグは、下記のフラグのビット論理和あるいは 0(ゼロ) を指定してください。
  
  - **TJS_IGNOREPROP**  
    プロパティアクセスを無効化します。メンバを列挙し、かつ値を取得する場合、このフラグが指定されていると、メンバがプロパティの場合はプロパティオブジェクトそのものが得られます。このフラグを指定しなかった場合は、プロパティオブジェクトを通して得られた値が得られます。
  - **TJS_ENUM_NO_VALUE**  
    値を取得しません。このフラグが指定されていると、コールバック関数に渡される引数は 2 つになります。指定されていると 3 つになります。
- **tTJSVariantClosure *callback**  
  コールバック関数を指定します。
  
  このコールバック関数は、メンバ一つにつき一回ずつ、callback->FuncCall が呼び出されます。
  
  関数には２つ(TJS_ENUM_NO_VALUEを指定した場合)あるいは３つ(TJS_ENUM_NO_VALUEを指定しなかった場合)の引数が渡されます。
  
  - 第１引数は文字列型になり、メンバ名です
  - 第２引数は整数型になり、そのメンバのフラグです。TJS_HIDDENMEMBER あるいは TJS_STATICMEMBER のビット論理和の組み合わせ、あるいは 0 が指定されます
  - 第３引数はTJS_ENUM_NO_VALUEを指定しなかった場合にのみ存在し、そのメンバの値を表します
- **iTJSDispatch2 *objthis**  
  このメソッドが実行されるコンテキスト (this オブジェクト) を指定します。
  
  この引数は、TJS_IGNOREPROP フラグが指定されない場合、プロパティオブジェクトが実行されるデフォルトのコンテキストとなります。

## Invalidate

tjs_error iTJSDispatch2::Invalidate(

tjs_uint32 flag,

const tjs_char *membername,

tjs_uint32 *hint,

iTJSDispatch2 *objthis

)



無効化を行います。



引数は以下の通りです。

- **tjs_uint32 flag**  
  呼び出しフラグです(下記参照)。
- **const tjs_char * membername**  
  対象とするメンバの名前を指定します。
  
  NULL の場合、このオブジェクト自身が無効化されます。
  
  メンバ名が指定された場合、もし、そのメンバがオブジェクトならば、そのオブジェクトが無効化されます。指定されたメンバがオブジェクト型でなかった場合は失敗します。
- **tjs_uint32 *hint**  
  ヒントを格納するための変数の領域を指定します。NULLでもかまいません。
  
  ヒントの説明については FuncCall の説明を参照してください。
- **iTJSDispatch2 *objthis**  
  このメソッドが実行されるコンテキスト (this オブジェクト) を指定します。
  
  この引数は、通常、意味を持ちません(無視されます)。

## InvalidateByNum

tjs_error iTJSDispatch2::InvalidateByNum(

tjs_uint32 flag,

tjs_int num,

iTJSDispatch2 *objthis

)



序数により無効化を行います。

## IsValid

tjs_error iTJSDispatch2::IsValid(

tjs_uint32 flag,

const tjs_char *membername,

tjs_uint32 *hint,

iTJSDispatch2 *objthis

)



オブジェクトが有効かどうかを調べます。

有効の場合は TJS_S_TRUE が、向こうの場合は TJS_S_FALSE が戻ります。



引数は以下の通りです。

- **tjs_uint32 flag**  
  呼び出しフラグです(下記参照)。
- **const tjs_char * membername**  
  対象とするメンバの名前を指定します。
  
  NULL の場合、このオブジェクト自身の有効性を調べることができます。
  
  メンバ名が指定された場合、もし、そのメンバがオブジェクトならば、そのオブジェクトの有効性を調べることができます。指定されたメンバがオブジェクト型でなかった場合は失敗します。
- **tjs_uint32 *hint**  
  ヒントを格納するための変数の領域を指定します。NULLでもかまいません。
  
  ヒントの説明については FuncCall の説明を参照してください。
- **iTJSDispatch2 *objthis**  
  このメソッドが実行されるコンテキスト (this オブジェクト) を指定します。
  
  この引数は、通常、意味を持ちません(無視されます)。

## IsValidByNum

tjs_error iTJSDispatch2::IsValidByNum(

tjs_uint32 flag,

tjs_int num,

iTJSDispatch2 *objthis

)



序数により、オブジェクトが有効かどうかを調べます。

## CreateNew

tjs_error iTJSDispatch2::CreateNew(

tjs_uint32 flag,

const tjs_char * membername,

tjs_uint32 *hint,

iTJSDispatch2 **result,

tjs_int numparams,

tTJSVariant **param,

iTJSDispatch2 *objthis

)



新規オブジェクトを作成します。

このメソッドは FuncCall メソッドに似て、オブジェクトを新規作成するために引数を渡すことができます。

オブジェクトの雛形となる、いわゆる「クラスオブジェクト」はこのメソッドを実装している必要があります。



引数は以下の通りです。

- **tjs_uint32 flag**  
  呼び出しフラグです(下記参照)。
- **const tjs_char * membername**  
  操作対象とするメンバ名です。
  
  NULL の場合は、このオブジェクト自身に対する操作になります。この場合は、このオブジェクトは、新にオブジェクトを新規作成する機能を持っている必要があります。
- **tjs_uint32 *hint**  
  ヒントを格納するための変数の領域を指定します。NULLでもかまいません。
  
  ヒントの説明については FuncCall の説明を参照してください。
- **iTJSDispatch2 **result**  
  新しく作成したオブジェクトを格納するための iTJSDispatch * 型へのポインタを指定します。NULL は許されません。
- **tjs_int numparams**  
  オブジェクトを新規作成する際に渡す引数の数を指定します。
- **tTJSVariant **param**  
  オブジェクトを新規作成する際に渡す引数のポインタの配列を渡します。引数がない場合は NULL でかまいません。
- **iTJSDispatch2 *objthis**  
  オブジェクトを新規作成する際に実行されるコンテキスト (this オブジェクト) を指定します。

## CreateNewByNum

tjs_error iTJSDispatch2::CreateNew(

tjs_uint32 flag,

tjs_int num,

iTJSDispatch2 **result,

tjs_int numparams,

tTJSVariant **param,

iTJSDispatch2 *objthis

)



序数により新規オブジェクトを作成します。

## IsInstanceOf

tjs_error iTJSDispatch2::IsInstanceOf(

tjs_uint32 flag,

const tjs_char * membername,

tjs_uint32 *hint,

const tjs_char * classname,

iTJSDispatch2 *objthis

)



オブジェクトが、特定のクラスのインスタンスであるかどうかを調べます。

クラス名は classname 引数に文字列で渡されます。

TJS2 の instanceof 演算子により参照されます。

成功した場合、指定されたクラスのインスタンスである場合は TJS_S_TRUE が、そうでない場合は TJS_S_FALSE が帰ります。



引数は以下の通りです。

- **tjs_uint32 flag**  
  呼び出しフラグです(下記参照)。
- **const tjs_char * membername**  
  操作対象とするメンバ名です。
  
  NULL の場合は、このオブジェクト自身に対する操作になります。この場合は、このオブジェクトは、新にオブジェクトを新規作成する機能を持っている必要があります。
- **tjs_uint32 *hint**  
  ヒントを格納するための変数の領域を指定します。NULLでもかまいません。
  
  ヒントの説明については FuncCall の説明を参照してください。
- **const tjs_char *classname**  
  クラス名を文字列で指定します。
- **iTJSDispatch2 *objthis**  
  オブジェクトを新規作成する際に実行されるコンテキスト (this オブジェクト) を指定します。

## IsInstanceOfByNum

tjs_error iTJSDispatch2::IsInstanceOfByNum(

tjs_uint32 flag,

tjs_int num,

const tjs_char * classname,

iTJSDispatch2 *objthis

)



序数により、オブジェクトが、特定のクラスのインスタンスであるかどうかを調べます。

## Operation

tjs_error iTJSDispatch2::Operation(

tjs_uint32 flag,

const tjs_char *membername,

tjs_uint32 *hint,

tTJSVariant *result,

const tTJSVariant *param,

iTJSDispatch2 *objthis

)



メンバに対して演算を行います。演算の種類は flag で指定します。



引数は以下の通りです。

- **tjs_uint32 flag**  
  呼び出しフラグです。下記の通常の呼び出しフラグの他、演算の種類を指定するために以下のフラグのいずれかをビットORで付加する必要があります。
  
  
  
  なお、この説明中で v はメンバの値、p は param 引数で渡すパラメータを表します。
  
  - **TJS_OP_BAND**  
    ビット AND 演算
    
    v &= p
  - **TJS_OP_BOR**  
    ビット OR 演算
    
    v |= p
  - **TJS_OP_BXOR**  
    ビット XOR 演算
    
    v ^= p
  - **TJS_OP_SUB**  
    減算
    
    v -= p
  - **TJS_OP_ADD**  
    加算
    
    v += p
  - **TJS_OP_MOD**  
    モジュラ
    
    v %= p
  - **TJS_OP_DIV**  
    実数除算
    
    v /= p
  - **TJS_OP_IDIV**  
    整数除算
    
    v \= p
  - **TJS_OP_MUL**  
    乗算
    
    v *= p
  - **TJS_OP_LOR**  
    論理 OR
    
    v = v || p
  - **TJS_OP_LAND**  
    論理 AND
    
    v = v && p
  - **TJS_OP_SAR**  
    算術右シフト
    
    v >>= p
  - **TJS_OP_SAL**  
    算術左シフト
    
    v <<= p
  - **TJS_OP_SR**  
    ビット左シフト
    
    v >>>= p
  - **TJS_OP_INC**  
    インクリメント
    
    v++
    
    param 引数は無視されます
  - **TJS_OP_DEC**  
    デクリメント
    
    v--
    
    param 引数は無視されます
- **const tjs_char * membername**  
  操作対象とするメンバ名です。NULL は許されません。
- **tjs_uint32 *hint**  
  ヒントを格納するための変数の領域を指定します。NULLでもかまいません。
  
  ヒントの説明については FuncCall の説明を参照してください。
- **tTJSVariant *result**  
  演算の結果を格納するための tTJSVariant 型の変数へのポインタを指定します。NULL でかまいません。
- **tTJSVariant *param**  
  演算のパラメータを指定します。演算の種類に TJS_OP_INC または TJS_OP_DEC を指定した場合は NULL でかまいません。
- **iTJSDispatch2 *objthis**  
  演算が実行されるコンテキストを指定しますが、通常無視されます。

## OperationByNum

tjs_error iTJSDispatch2::OperationByNum(

tjs_uint32 flag,

tjs_int num,

tTJSVariant *result,

const tTJSVariant *param,

iTJSDispatch2 *objthis

)



序数を用いて、メンバに対して演算を行います。

## NativeInstanceSupport

tjs_error iTJSDispatch2::NativeInstanceSupport(

tjs_uint32 flag,

tjs_int32 classid,

iTJSNativeInstance **pointer

)



オブジェクトにネイティブコードのインスタンスを関連づけたり、オブジェクトからネイティブコードのインスタンスを取得したりします。



引数は以下の通りです。

- **tjs_uint32 flag**  
  呼び出しフラグを指定します。
  
  以下のいずれかの値を指定する必要があります。
  
  - ****TJS_NIS_REGISTER****  
    *pointer で示したネイティブコードのインスタンスを登録します。ネイティブコードのクラスの識別には classid を用います。
  - ****TJS_NIS_GETINSTANCE****  
    classid で指定した クラスID を持つネイティブコードのインスタンスを *pointer に書き込みます。
- **tjs_int32 classid**  
  ネイティブコードのクラス ID を指定します。
  
  ネイティブコードのクラス ID の管理には TJSRegisterNativeClass
  TJSFindNativeClassID
  TJSFindNativeClassName を使用することができますが、通常は これらの処理はネイティブコードを記述するための
  支援コード群 ( tjsNative.cpp/tjsNative.h に記述 ) で自動的に処理されます。
- **iTJSNativeInstance **pointer**  
  ネイティブコードのインスタンスを渡したり、受け取ったりするために、iTJSNativeInstance *型の変数へのポインタを指定します。

## ClassInstanceInfo

tjs_error iTJSDispatch2::ClassInstanceInfo(

tjs_uint32 flag,

tjs_uint num,

tTJSVariant *value

)



IsInstanceOf メソッドで使用する、クラスのインスタンス情報を操作するメソッドです。

オブジェクトがどのクラスのインスタンスかを識別するためにクラス名を追加したり、オブジェクトがどのクラスのインスタンスかを調べるためにクラスを列挙することができます。



引数は以下の通りです。

- **tjs_uint32 flag**  
  呼び出しフラグです。以下のフラグのいずれかを指定します。
  
  - ****TJS_CII_ADD****  
    インスタンス情報を追加します。
    
    value にはクラス名 (文字列) の格納された tTJSVariant 型の変数へのポインタを渡します。
    
    num 引数は無視されます。
  - ****TJS_CII_GET****  
    インスタンス情報を取得します。
    
    num 引数には 0 から始まる 整数を指定します。設定されているインスタンス情報の数を超えて num を指定すると TJS_E_FAIL が戻ります。
    
    value にはクラス名を受け取るための、tTJSVariant 型の変数へのポインタを渡します。
- **tjs_uint num**  
  flag に TJS_CII_GET を指定した場合の序数を指定します。
- **tTJSVariant *value**  
  flag に TJS_CII_ADD を指定した場合は、クラス名が格納された tTJSVariant 型の変数へのポインタを渡します。
  
  flag に TJS_CII_GET を指定した場合は、クラス名を受け取るための tTJSVariant 型の変数へのポインタを渡します。

## 呼び出しフラグ

呼び出しフラグです。

以下の値のビットORによる組み合わせを指定することができます。

- **TJS_MEMBERENSURE**  
  指定されたメンバ名が見つからなかった場合、強制的にメンバを作成します。PropSet に対する呼び出しフラグとして有効です。
  )
- **TJS_MEMBERMUSTEXIST**  
  指定されたメンバ名が見つからなかった場合、エラーにします。これは、Dictionary や Array のような、メンバが見つからない場合にデフォルトで void を返すようなオブジェクトに対して有効です (そのようなオブジェクトでない場合は、メンバが見つからない場合はデフォルトでエラーになります)。
- **TJS_IGNOREPROP**  
  プロパティ操作をバイパスします。
  
  TJS2 のオブジェクトは通常、指定されたメンバがオブジェクトで、かつ、そのオブジェクトに対して PropSet や PropGet が成功する場合 (プロパティオブジェクトの場合)、そのメンバに対する PropSet や PropGet の結果を、そのメンバの代わりと見なして使います。
  
  このフラグを指定すると、このような処理をバイパスするため、指定されたメンバがプロパティオブジェクトであっても、プロパティオブジェクトそのものに対する操作になります。
- **TJS_HIDDENMEMBER**  
  このフラグを指定してメンバを作成すると、メンバは不可視になります。オブジェクトによってはサポートされていないこともあり得ます。
- **TJS_STATICMEMBER**  
  このフラグを指定してメンバを作成すると、メンバはスタティック (実行コンテキストに依存しない) となります。オブジェクトによってはサポートされていないこともあり得ます。

## tjs_error

tjs_error は、iTJSDispatch2 の各メソッド ( AddRef と Release を除く ) が返すエラー型です。

以下の値を採ります。また、ここに載ってない値でも、値が負の場合はエラーと見なす必要があります。これらを判断するために TJS_SUCCEEDED および TJS_FAILED マクロを使用することができます。

- ****TJS_E_MEMBERNOTFOUND****  
  指定されたメンバが見つかりません。
- ****TJS_E_NOTIMPL****  
  呼び出そうとした機能は未実装です。
- ****TJS_E_INVALIDPARAM****  
  不正な引数です。
- ****TJS_E_BADPARAMCOUNT****  
  引数の数が不正です。
- ****TJS_E_INVALIDTYPE****  
  関数ではないかプロパティの種類が違います。
  
  関数でない物を呼び出そうとした場合や、プロパティでない物をプロパティとして扱おうとしたときにこの値が帰ります。
- ****TJS_E_INVALIDOBJECT****  
  オブジェクトはすでに無効化されています。
- ****TJS_E_ACCESSDENYED****  
  読み込みあるいは書き込み専用プロパティに対して行えない操作をしようとしました。
- ****TJS_E_NATIVECLASSCRASH****  
  実行コンテキストが違います。
  
  ネイティブコードで実装されたメソッドを、そのネイティブコードで扱えないコンテキスト (違うクラスのオブジェクト上など) で実行しようとしたときにこの値が帰ります。
- ****TJS_S_TRUE****  
  エラーではありませんが、結果が「真」であることを示します。
- ****TJS_S_FALSE****  
  エラーではありませんが、結果が「偽」であることを示します。
- ****TJS_S_OK****  
  エラーが発生しなかった場合に、通常、この値が帰ります。
- ****TJS_E_FAIL****  
  未定義のエラーが発生した場合、この値が帰ります。
- ****TJS_FAILED**(x)**  
  x がエラーの値の場合に真になるマクロです。
- ****TJS_SUCCEEDED**(x)**  
  x がエラーでない値の場合に真になるマクロです。

エラー定義、および関連するマクロは tjsErrorDef.h に記述されています。

また、エラーではなく (C++における) 実行時例外が投げられる場合があります。プログラミングに関しては、実行時例外を十分に考慮する必要があります。
