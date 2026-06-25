# 基本的な使い方

## コンパイル

Borland C++ 5.5 以降 ( C++ Builder 5 以降 ) でコンパイルをすることができます。



コンパイルには boost.org の regex++ が必要になります。



regex++ をインストールした後、各 cpp ファイルをコンパイルしてください。



C++ Builder の場合は、tjs2 の各 cpp ファイルをすべてプロジェクトに追加するだけで OK です。



gcc 3 以降でもコンパイルできます ( 2.95 でもコンパイルできますが wstring 関連の修正が必要 )。

## 簡単な例

```
#include <stdio.h>
#include "tjs.h"
#include "tjsError.h"

int main(int argc, char* argv[])
{
	setlocale(LC_ALL, ""); // ロケールを設定

	tTJS *tjsengine = new tTJS(); // TJS2 スクリプトエンジンを作成

	try
	{
		tTJSVariant result; // 結果を受け取るための変数

		tjsengine->ExecScript(
			TJS_W(
				"function test(x, y) { return x*y; } \n"
				"return test(4, 5);\n"),
				&result, NULL,
				TJS_W("test code"));	// テストスクリプトを実行

		printf("結果 : %d\n", (int)result); // 結果を表示
	}
	catch(eTJSError &e)
	{
		printf("エラーが発生しました : %ls\n", e.GetMessage().c_str());
	}
	catch(...)
	{
		printf("エラーが発生しました\n");
	}

	tjsengine->Shutdown(); // TJS2 スクリプトエンジンをシャットダウン
	tjsengine->Release(); // TJS2 スクリプトエンジンを解放

	return 0;
}
```

- **2～3行目**  
  TJS2 を使用するのに必要なヘッダファイルを読み込んでいます。tjsError.h は TJS の C++ 例外に関する宣言が含まれています。
- **7行目**  
  setlocale でロケールを指定しています。ロケールを指定しないと "C" ロケールになるため、日本語文字のナロー文字とワイド文字間の変換がうまくいきません。
- **9行目**  
  TJS2 スクリプトエンジンを new 演算子で作成しています。
- **11行目**  
  try ブロックに入っています。TJS2 のエラーは例外により通知されるため、例外処理には慎重になる必要があります。
- **13行目**  
  スクリプトを実行した結果を受け取るための tTJSVariant 型の変数を宣言しています。
- **15～20行目**  
  tTJS::ExecScript を使ってスクリプトを実行しています。
  
  第１引数には実行するスクリプトを指定します。tjs_char * 型で渡すために、文字列リテラルを TJS_W マクロを使ってワイド文字列に変換しています。スクリプトでは、関数 test を定義し、その関数を呼んだ結果を返しています。
  
  この例では return 文により実行の結果を返し、それを result 変数で受け取っていますが、結果を受け取る必要がない場合は return 文も tTJS::ExecScript の２番目の引数も必要ありません ( その場合は２番目の引数は NULL を指定します )。
  
  tTJS::ExecScript の３番目の引数は実行コンテキストですが、ここでは NULL を指定します。NULL を指定すると スクリプトは global コンテキスト上で実行されます。
  
  tTJS::ExecScript の４番目の引数は、このスクリプトの名前を指定します。NULLの場合は匿名として扱われます。人間が可読な名前である必要があります。
- **22行目**  
  結果を表示しています。ここでは tTJSVariant を int 型にキャストしています。
- **24行目**  
  eTJSError 型の例外を受け取っています。
- **26行目**  
  eTJSError::GetMessage を使って、例外の理由を表示しています。メッセージを const tjs_char * に変換するために tTJSString::c_str を使っています。tjs_char は ワイド文字のため、printf の変換指定子には %ls を指定しています。
- **28行目**  
  その他の例外を受け取っています。
- **33～34行目**  
  TJS2 スクリプトエンジンを解放しています。解放に先立ち、tTJS::Shutdown を使って TJS2 スクリプトエンジンをシャットダウンしています。

## TJS2側の関数の呼び出し

TJS2側で宣言した関数をC++から呼び出す方法です。

前述の try ブロックの中を以下のように書いてみます。

```
		tTJSVariant result; // 結果を受け取るための変数

		tjsengine->ExecScript(
			TJS_W("function test(x, y) { return x*y; }"), NULL, NULL, TJS_W("test"));

		tjsengine->EvalExpression(TJS_W("test(4, 5)"), &result, NULL, NULL);
			// tTJS::EvalExpression を使って式を実行

		printf("結果 : %d\n", (int)result); // 結果を表示

		iTJSDispatch2 * global = tjsengine->GetGlobalNoAddRef();
			// グローバルオブジェクトを取得

		tTJSVariant param[] = { 4, 5 }; // パラメータとして渡す変数
		tTJSVariant *p_param[] = { param + 0, param + 1 }; // 変数へのポインタの配列

		TJS_THROW_IF_ERROR(global->FuncCall(0, TJS_W("test"), NULL, &result, 2, p_param, NULL));
			// test を関数として呼び出す

		printf("結果 : %d\n", (int)result); // 結果を表示
```

- **3～4行目**  
  関数 test を宣言しています。test は global に登録されます。
- **6行目**  
  tTJS::EvalExpression を使って式を実行しています。それほど速度的にシビアでなくてもよいならば、このように 式を文字列として渡してその結果を受け取ると楽です。
  
  ちなみに、単純な式 ( 関数宣言など、他の実行単位を含まないようなもの ) ならば、ある程度、コンパイル結果がキャッシュされ、２回目以降の式評価を高速に行うことができます。
- **11行目**  
  グローバルオブジェクトを取得しています。tTJS::GetGlobal と tTJS::GetGlobalNoAddRef の違いは、前者が global オブジェクトの参照カウンタをインクリメントするのに対し、後者はインクリメントしないと言うことです。
  
  参照カウンタをインクリメントし、使い終わったらデクリメントすると言うことは、その間中、そのオブジェクトが消滅しないようにロックをかけると言うことです。この例のように、global オブジェクトが消滅する心配のない場合は参照カウンタを操作する必要はありませんので tTJS::GetGlobalNoAddRef を使うことができます。また、この場合は使い終わったときの Release は必要ありません。
- **14～15行目**  
  関数に渡すパラメータを準備しています。iTJSDispatch::FuncCall は、関数に渡すパラメータとして tTJSVariant 型のポインタの配列を必要とするため、このような準備が必要になります。
- **17行目**  
  iTJSDispatch2::FuncCall を使って、関数 "test" を呼び出しています。
  
  FuncCall の最後の引数は、関数 test に渡される this (実行コンテキスト) ですが、この例で宣言した test 内では this を使っていないので NULL を指定してかまいません。実行すべきコンテキストがある場合は、そのオブジェクトを指定する必要があります。
  
  TJS_THROW_IF_ERROR は、tjs_error 型の結果がエラーだった場合、それに対応するエラーメッセージとともに例外を送出するマクロです。

## ネイティブ関数

ネイティブ実装 (C++などで実装された関数) を作成し、TJS2 側からそれにアクセスすることができます。

C++ でなくても、iTJSDispatch2 を実装できる言語ならば、どのような言語で書かれた関数でも呼び出すことができますが、C++ が一番楽でしょう。



C++ で 関数を書く場合は、tTJSNativeFunction (tjsNative.h に記述) からクラスを導出するのが楽です (しかし、iTJSDispatch2 の FuncCall を実装するだけでも関数として動作はできます)。



与えられた２つの引数を乗算して返す、簡単な関数を実装してみます。

```
class TestFunc : public tTJSNativeFunction
{
public:
	tjs_error Process(tTJSVariant *result, tjs_int numparams,
		tTJSVariant **param, iTJSDispatch2 *objthis)
	{
		if(numparams < 2) return TJS_E_BADPARAMCOUNT; // 引数が足りない

		if(!result) return TJS_S_OK; // 結果を格納しなくて良い場合はそのままもどる

		*result = *param[0] * *param[1]; // 計算

		return TJS_S_OK; // 正常に終わったことを示すため TJS_S_OK を返す
	}
};
```

tTJSNativeFunction を継承したクラスで実装すべきなのは、上記の通り Process メソッドだけです。

Process メソッドの引数は以下の通りです。

- **tTJSVariant *result**  
  関数の結果を格納するための tTJSVariant 型の変数へのポインタが渡されます。**呼び出し側が結果を必要としない場合は NULL が渡されます**ので注意してください。
- **tjs_int numparams**  
  関数に渡された引数の数です。
- **tTJSVariant **param**  
  関数に渡された引数が格納された tTJSVariant 型の変数へのポインタの配列です。
- **iTJSDispatch2 *objthis**  
  関数が実行されるべきコンテキストです。コンテキストに依存しない実装をする場合は無視してかまいません。

ネイティブ関数は TJS2 からアクセス可能にするため、TJS2 内からアクセスできるオブジェクトに登録する必要があります。以下の例では、global に "test" という名前で登録しています。また、実際にその関数を呼び出しています。

```
		iTJSDispatch2 * global = tjsengine->GetGlobalNoAddRef();
			// グローバルオブジェクトを取得

		iTJSDispatch2 *func = new TestFunc(); // TestFunc のオブジェクトを作成
		tTJSVariant func_var(func); // tTJSVariant 型 func_var にオブジェクトを設定
		func->Release(); // func を Release

		TJS_THROW_IF_ERROR(
			global->PropSet(TJS_MEMBERENSURE, TJS_W("test"), NULL, &func_var, NULL));
				// 登録

		tTJSVariant result; // 結果を受け取るための変数
		tjsengine->EvalExpression(TJS_W("test(4, 5)"), &result, NULL, NULL);
			// tTJS::EvalExpression を使って式を実行

		printf("結果 : %d\n", (int)result); // 結果を表示
```

- **4～6行目**  
  ネイティブ関数を実装してあるクラス TestFunc のオブジェクトを作成し、それを tTJSVariant 型に変換しています。
  
  5行目で tTJSVariant 型に変換していますが、この時点で tTJSVariant 型が 関数オブジェクトの参照カウンタを自動的に管理するので、6行目で関数オブジェクトを Release しています。
- **8～9行目**  
  global オブジェクトに関数を "test" という名前で登録しています。global オブジェクトの iTJSDispatch2::PropSet を呼んでいますが、メンバを新規作成させるために TJS_MEMBERENSURE フラグを伴って呼び出しています。
- **12～16行目**  
  実際に関数を呼び出し、結果を表示しています。

## ネイティブクラス

TJS2 は C++ 等の言語で書かれたネイティブクラスを扱うための機構を持っています。

各オブジェクト (iTJSDispatch2 インターフェース) にはネイティブインスタンスと呼ばれる、iTJSNativeInstance 型のオブジェクトを登録することができ、これを オブジェクトから取り出すことができます。

ネイティブインスタンスは一意なクラス ID で識別され、ネイティブクラスの作成時にはクラス ID を取得する必要があります。



しかし、これらの操作を行う為のマクロ群が tjsNative.h に定義されているので、これらを利用するのが楽です。

以下の例は、これらのマクロを使って簡単なクラスを実装するものです。



まず、ネイティブインスタンスの実装です。ネイティブインスタンスを実装するには tTJSNativeInstance からクラスを導出します。tTJSNativeInstance は tjsNative.cpp / tjsNative.h に実装されているクラスで、iTJSNativeInstance の基本的な動作を実装しています。

```
class NI_Test : public tTJSNativeInstance // ネイティブインスタンス
{
public:
	NI_Test()
	{
		// コンストラクタ
		Value = 0;
	}

	tjs_error TJS_INTF_METHOD
		Construct(tjs_int numparams, tTJSVariant **param, iTJSDispatch2 *tjs_obj)
	{
		// TJS2 オブジェクトが作成されるときに呼ばれる

		// 引数があればそれを初期値として Value に入れる
		if(numparams >= 1 && param[0]->Type() != tvtVoid)
			Value = (tjs_int)*param[0];

		return S_OK;
	}

	void TJS_INTF_METHOD Invalidate()
	{
		// オブジェクトが無効化されるときに呼ばれる
	}

	void SetValue(tjs_int n) { Value = n; }
	tjs_int GetValue() const { return Value; }

	tjs_int GetSquare() const { return Value*Value; }
	void Add(tjs_int n) { Value += n; }
	void Print() const { printf("%d\n", Value); }

private:
	tjs_int Value; // 値
};
```

- **35行目**  
  話が前後しますが、データメンバです。ネイティブインスタンスには、必要なデータメンバを自由に書くことができます。
- **4～8行目**  
  NI_Test のコンストラクタです。C++ クラスとしての初期化は 後述の Construct よりもここで済ませておき、Construct での初期化は最小限の物にすることをおすすめします。
  
  この例では、データメンバの Value に初期値として 0 を設定しています。
- **10～20行目**  
  new 演算子で TJS2 オブジェクトが作成されるときに呼ばれます。numparams と param 引数は new 演算子に渡された引数を表しています。
  
  tjs_obj 引数は、作成される TJS オブジェクトです。
  
  この例では、引数があれば (さらにそれが void で無ければ )、それを Value の初期値として設定しています。
- **22～25行目**  
  オブジェクトが無効化されるときに呼ばれるメソッドです。ここに終了処理を書くと良いでしょう。
  
  この例では何もしません。
- **27～32行目**  
  データメンバを操作するための公開メソッド群です。後述するネイティブクラス内で、これらを利用するコードを書きます。

オブジェクトを作成するためにはクラスが必要ですので、クラスを記述します。クラスは tTJSNativeClass を導出する形で実装します。tTJSNativeClass は iTJSDispatch2 インターフェースを持っていて、ネイティブクラスとして振る舞うための基本的な動作が実装されています。

TJS からアクセス可能なメソッドやプロパティは、ネイティブクラスのコンストラクタ内に記述します。

```
class NC_Test : public tTJSNativeClass // ネイティブクラス
{
public:
	NC_Test(); // コンストラクタ; 下に記述

	static tjs_uint32 ClassID; // クラスID

private:
	tTJSNativeInstance *CreateNativeInstance()
	{
		return new NI_Test(); // ネイティブインスタンスを作成して返す
	}
};
tjs_uint32 NC_Test::ClassID = (tjs_uint32)-1; // クラスID
```

- **4行目**  
  このクラスのコンストラクタです。実装は後述します。
- **6行目**  
  このクラスのクラス ID を保持するための変数です。14行目に実体があります。
- **9～12行目**  
  CreateNativeInstance メソッドは、ネイティブインスタンスを作成すべきタイミングで呼ばれるメソッドです。ここでは NI_Test クラスのオブジェクトを作成して返しています。

```
NC_Test::NC_Test() : tTJSNativeClass(TJS_W("Test"))
{
	TJS_BEGIN_NATIVE_MEMBERS(/*TJS class name*/Test)

		TJS_DECL_EMPTY_FINALIZE_METHOD

		TJS_BEGIN_NATIVE_CONSTRUCTOR_DECL(
			/*var.name*/_this,
			/*var.type*/NI_Test,
			/*TJS class name*/Test)
		{
			// NI_Test::Construct にも内容を記述できるので
			// ここでは何もしない
			return TJS_S_OK;
		}
		TJS_END_NATIVE_CONSTRUCTOR_DECL(/*TJS class name*/Test)

		TJS_BEGIN_NATIVE_METHOD_DECL(/*func. name*/print) // print メソッド
		{
			TJS_GET_NATIVE_INSTANCE(/*var. name*/_this,
				/*var. type*/NI_Test);

			_this->Print();

			return TJS_S_OK;
		}
		TJS_END_NATIVE_METHOD_DECL(/*func. name*/print)

		TJS_BEGIN_NATIVE_METHOD_DECL(/*func. name*/add) // add メソッド
		{
			TJS_GET_NATIVE_INSTANCE(/*var. name*/_this,
				/*var. type*/NI_Test);

			if(numparams < 1) return TJS_E_BADPARAMCOUNT;

			_this->Add((tjs_int)*param[0]);

			return TJS_S_OK;
		}
		TJS_END_NATIVE_METHOD_DECL(/*func. name*/add)

		TJS_BEGIN_NATIVE_PROP_DECL(value) // value プロパティ
		{
			TJS_BEGIN_NATIVE_PROP_GETTER
			{
				TJS_GET_NATIVE_INSTANCE(/*var. name*/_this,
					/*var. type*/NI_Test);
				*result = _this->GetValue();
				return TJS_S_OK;
			}
			TJS_END_NATIVE_PROP_GETTER

			TJS_BEGIN_NATIVE_PROP_SETTER
			{
				TJS_GET_NATIVE_INSTANCE(/*var. name*/_this,
					/*var. type*/NI_Test);
				_this->SetValue((tjs_int)*param);
				return TJS_S_OK;
			}
			TJS_END_NATIVE_PROP_SETTER
		}
		TJS_END_NATIVE_PROP_DECL(value)

		TJS_BEGIN_NATIVE_PROP_DECL(square) // square 読み出し専用プロパティ
		{
			TJS_BEGIN_NATIVE_PROP_GETTER
			{
				TJS_GET_NATIVE_INSTANCE(/*var. name*/_this,
					/*var. type*/NI_Test);

				*result = _this->GetSquare();

				return TJS_S_OK;
			}
			TJS_END_NATIVE_PROP_GETTER

			TJS_DENY_NATIVE_PROP_SETTER
		}
		TJS_END_NATIVE_PROP_DECL(square)

	TJS_END_NATIVE_MEMBERS
}
```

- **1行目**  
  NC_Test のコンストラクタです。親クラスである tTJSNativeClass のコンストラクタには TJS2 内で使用するクラス名を指定します。
- **3行目**  
  TJS_BEGIN_NATIVE_MEMBERS マクロです。引数には TJS2 内で使用するクラス名を指定します。
  
  このマクロと TJS_END_NATIVE_MEMBERS マクロで挟まれた場所に、クラスのメンバとなるべきメソッドやプロパティの記述をします。
- **4行目**  
  空の finalize メソッドを宣言しています。finalize に相当する処理は tTJSNativeInstance::Invalidate をオーバーライドすることでも実装できますので、通常は空のメソッドで十分です。
- **7～16行目**  
  (TJSの) コンストラクタを宣言しています。TJS でクラスを書くとき、クラス内でクラスと同名のメソッドを宣言している部分に相当します。
  
  
  
  TJS_BEGIN_NATIVE_CONSTRUCTOR_DECL マクロの１番目の引数はネイティブインスタンスに割り当てる変数名で、２場面目の引数はその変数の型名です。この例でのこのブロック内では NI_Test * _this という変数が利用可能で、ネイティブインスタンスにアクセスすることができます。
  
  マクロの３番目の引数は、TJS 内で使用するクラス名を指定します。TJS_END_NATIVE_CONSTRUCTOR_DECL マクロの引数も同様です。
  
  ここも、コンストラクタに相当する処理は tTJSNativeInstance::Construct をオーバーライドする事で実装できるので、ここでは何もせずに S_OK を返します。
- **18～27行目**  
  print メソッドを宣言しています。メソッド名は TJS_BEGIN_NATIVE_METHOD_DECL と TJS_END_NATIVE_METHOD_DECL の両マクロに同じものを指定する必要があります。
  
  このマクロ内で使用可能な変数に tjs_int numparams と tTJSVariant **param があって、それぞれ、渡された引数の数と引数を示しています。このメソッドではそれらは使用していません。
  
  20～21行目は、オブジェクトからネイティブインスタンスを取り出すためのマクロです。この例では _this という NI_Test * 型の変数にネイティブインスタンスを取り出す、という意味になります。以降、_this という変数でネイティブインスタンスにアクセスできます。23行目で、そのネイティブインスタンスの Print メソッドを呼び出しています。
- **29～40行目**  
  add メソッドを宣言しています。ここでは numparams と param を使用しています。
- **42～62行目**  
  value プロパティを宣言しています。TJS_BEGIN_NATIVE_PROP_DECL と TJS_END_NATIVE_PROP_DECL の両マクロには、メソッドの宣言と同じく、プロパティ名を指定します。
  
  
  
  TJS_BEGIN_NATIVE_PROP_GETTER と TJS_END_NATIVE_PROP_GETTER マクロで囲まれた場所には、ゲッターを記述することができます。ゲッター内では tTJSVariant 型である *result に値を設定するように記述します。
  
  同様に、TJS_BEGIN_NATIVE_PROP_SETTER と TJS_END_NATIVE_PROP_SETTER マクロで囲まれた場所にはセッターを記述することができます。セッター内では tTJSVariant 型である *param に設定されるべき値が格納されているので、それを使って処理をします。
- **64～79行目**  
  ここでは読み出し専用プロパティを宣言しています。セッターの代わりに TJS_DENY_NATIVE_PROP_SETTER を書くことにより、読み出し専用プロパティを作ることができます。

ネイティブクラスの登録は、ネイティブ関数の登録と同じです。以下にテストコードを例示します。

```
		iTJSDispatch2 * global = tjsengine->GetGlobalNoAddRef();
			// グローバルオブジェクトを取得

		iTJSDispatch2 *cls = new NC_Test(); // NC_Test のオブジェクトを作成
		tTJSVariant cls_var(cls); // tTJSVariant 型 cls_var にオブジェクトを設定
		cls->Release(); // cls を Release

		TJS_THROW_IF_ERROR(
			global->PropSet(TJS_MEMBERENSURE, TJS_W("Test"), NULL, &cls_var, NULL));
				// 登録

		tjsengine->ExecScript(TJS_W(
			"var test = new Test();\n"
			"test.value = 5;\n"
			"var test2 = new Test(test.square);\n"
			"test2.add(3);\n"
			"test2.print();\n\0"),
				NULL, NULL, NULL); // スクリプトを実行
```
