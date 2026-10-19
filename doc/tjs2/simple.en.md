---
source_hash: dc8e3c7ddb62
---

# Basic Usage

## Compiling

TJS2 can be compiled with Borland C++ 5.5 or later (C++ Builder 5 or later).



Compiling requires regex++ from boost.org.



After installing regex++, compile each cpp file.



With C++ Builder, just add all the tjs2 cpp files to the project.



It can also be compiled with gcc 3 or later (2.95 also works, but requires fixes related to wstring).

## A simple example

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

- **Lines 2-3**
  Include the header files needed to use TJS2. tjsError.h contains the declarations for TJS C++ exceptions.
- **Line 7**
  Set the locale with setlocale. Without it, the "C" locale is used, and conversion of Japanese characters between narrow and wide strings does not work correctly.
- **Line 9**
  Create the TJS2 script engine with the new operator.
- **Line 11**
  Enter a try block. TJS2 reports errors through exceptions, so exception handling needs care.
- **Line 13**
  Declare a tTJSVariant variable that receives the result of running the script.
- **Lines 15-20**
  Run the script with tTJS::ExecScript.

  The first argument is the script to run. To pass it as tjs_char *, the string literal is converted to a wide string with the TJS_W macro. The script defines a function test and returns the result of calling it.

  In this example, the result is returned by a return statement and received in the result variable. If you do not need the result, neither the return statement nor the second argument of tTJS::ExecScript is required (in that case, pass NULL as the second argument).

  The third argument of tTJS::ExecScript is the execution context; NULL is passed here. With NULL, the script runs in the global context.

  The fourth argument of tTJS::ExecScript is the name of this script. NULL means anonymous. It should be a human-readable name.
- **Line 22**
  Display the result. Here the tTJSVariant is cast to int.
- **Line 24**
  Catch exceptions of type eTJSError.
- **Line 26**
  Display the reason for the exception using eTJSError::GetMessage. tTJSString::c_str converts the message to const tjs_char *. Since tjs_char is a wide character, %ls is used as the printf conversion specifier.
- **Line 28**
  Catch all other exceptions.
- **Lines 33-34**
  Free the TJS2 script engine. Before freeing it, shut it down with tTJS::Shutdown.

## Calling TJS2 functions

This shows how to call a function declared in TJS2 from C++.

Rewrite the inside of the try block above as follows.

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

- **Lines 3-4**
  Declare the function test. test is registered in global.
- **Line 6**
  Run an expression with tTJS::EvalExpression. If speed is not critical, passing an expression as a string and receiving its result like this is convenient.

  Incidentally, for simple expressions (ones that do not contain other execution units such as function declarations), the compiled result is cached to some extent, so evaluating the expression a second time and later is faster.
- **Line 11**
  Get the global object. The difference between tTJS::GetGlobal and tTJS::GetGlobalNoAddRef is that the former increments the reference count of the global object and the latter does not.

  Incrementing the reference count and decrementing it when you are done locks the object so that it is not destroyed in the meantime. When there is no risk of the global object being destroyed, as in this example, you do not need to touch the reference count, so you can use tTJS::GetGlobalNoAddRef. In that case, you also do not need to call Release when you are done.
- **Lines 14-15**
  Prepare the parameters to pass to the function. iTJSDispatch::FuncCall requires an array of pointers to tTJSVariant as the function parameters, so this preparation is necessary.
- **Line 17**
  Call the function "test" with iTJSDispatch2::FuncCall.

  The last argument of FuncCall is the this (execution context) passed to test. The test declared in this example does not use this, so NULL is fine. If there is a context to run in, you need to pass that object.

  TJS_THROW_IF_ERROR is a macro that throws an exception with the corresponding error message when a tjs_error result indicates an error.

## Native functions

You can create native implementations (functions implemented in C++ or other languages) and access them from TJS2.

Functions written in any language that can implement iTJSDispatch2 can be called, not just C++, but C++ is probably the easiest.



When writing a function in C++, deriving a class from tTJSNativeFunction (declared in tjsNative.h) is the easiest way (although implementing just FuncCall of iTJSDispatch2 is enough for it to work as a function).



Let's implement a simple function that multiplies its two arguments and returns the result.

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

As shown above, the only method a class derived from tTJSNativeFunction needs to implement is Process.

The arguments of the Process method are as follows.

- **tTJSVariant *result**
  A pointer to a tTJSVariant variable that stores the function's result. Note that **NULL is passed when the caller does not need the result**.
- **tjs_int numparams**
  The number of arguments passed to the function.
- **tTJSVariant **param**
  An array of pointers to tTJSVariant variables holding the arguments passed to the function.
- **iTJSDispatch2 *objthis**
  The context in which the function should run. You can ignore it if your implementation does not depend on the context.

To make a native function accessible from TJS2, register it in an object that TJS2 can access. The following example registers it in global under the name "test" and then calls it.

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

- **Lines 4-6**
  Create an object of TestFunc, the class that implements the native function, and convert it to tTJSVariant.

  Line 5 converts it to tTJSVariant. From this point, the tTJSVariant manages the function object's reference count automatically, so line 6 releases the function object.
- **Lines 8-9**
  Register the function in the global object under the name "test". It calls iTJSDispatch2::PropSet on the global object with the TJS_MEMBERENSURE flag so that the member is newly created.
- **Lines 12-16**
  Actually call the function and display the result.

## Native classes

TJS2 has a mechanism for handling native classes written in languages such as C++.

Each object (iTJSDispatch2 interface) can have an object of type iTJSNativeInstance, called a native instance, registered on it, and the native instance can be retrieved from the object.

A native instance is identified by a unique class ID, and a class ID must be obtained when creating a native class.



However, tjsNative.h defines a set of macros for these operations, and using them is the easiest way.

The following example uses these macros to implement a simple class.



First, the native instance. To implement a native instance, derive a class from tTJSNativeInstance. tTJSNativeInstance is a class implemented in tjsNative.cpp / tjsNative.h that implements the basic behavior of iTJSNativeInstance.

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

- **Line 35**
  Out of order, but this is the data member. A native instance can have any data members it needs.
- **Lines 4-8**
  The constructor of NI_Test. It is recommended to do the C++-level initialization here rather than in Construct (described below), and keep the initialization in Construct to a minimum.

  In this example, the data member Value is initialized to 0.
- **Lines 10-20**
  Called when a TJS2 object is created with the new operator. The numparams and param arguments represent the arguments passed to the new operator.

  The tjs_obj argument is the TJS object being created.

  In this example, if an argument is given (and it is not void), it is set as the initial value of Value.
- **Lines 22-25**
  The method called when the object is invalidated. This is a good place for cleanup.

  This example does nothing.
- **Lines 27-32**
  Public methods that operate on the data member. The native class described below contains code that uses them.

Creating objects requires a class, so we write one next. The class is implemented by deriving from tTJSNativeClass. tTJSNativeClass has the iTJSDispatch2 interface and implements the basic behavior needed to act as a native class.

Methods and properties accessible from TJS are written in the native class's constructor.

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

- **Line 4**
  The constructor of this class. Its implementation is shown below.
- **Line 6**
  A variable holding this class's class ID. It is defined on line 14.
- **Lines 9-12**
  CreateNativeInstance is called when a native instance should be created. Here it creates and returns an NI_Test object.

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

- **Line 1**
  The constructor of NC_Test. The class name used in TJS2 is passed to the constructor of the parent class, tTJSNativeClass.
- **Line 3**
  The TJS_BEGIN_NATIVE_MEMBERS macro. Its argument is the class name used in TJS2.

  The methods and properties that become members of the class are written between this macro and the TJS_END_NATIVE_MEMBERS macro.
- **Line 4**
  Declares an empty finalize method. The equivalent of finalize can also be implemented by overriding tTJSNativeInstance::Invalidate, so an empty method is usually enough.
- **Lines 7-16**
  Declares the (TJS) constructor. This corresponds to the method with the same name as the class when writing a class in TJS.



  The first argument of the TJS_BEGIN_NATIVE_CONSTRUCTOR_DECL macro is the variable name assigned to the native instance, and the second argument is that variable's type name. In this example, a variable NI_Test * _this is available inside this block, through which you can access the native instance.

  The third argument of the macro is the class name used in TJS. The same goes for the argument of the TJS_END_NATIVE_CONSTRUCTOR_DECL macro.

  Here too, the constructor's work can be implemented by overriding tTJSNativeInstance::Construct, so this block does nothing and returns S_OK.
- **Lines 18-27**
  Declares the print method. The same method name must be given to both the TJS_BEGIN_NATIVE_METHOD_DECL and TJS_END_NATIVE_METHOD_DECL macros.

  Inside these macros, the variables tjs_int numparams and tTJSVariant **param are available; they hold the number of arguments passed and the arguments themselves. This method does not use them.

  Lines 20-21 use a macro that retrieves the native instance from the object. In this example, it means "retrieve the native instance into a variable _this of type NI_Test *". From there on, the native instance can be accessed through _this. Line 23 calls the Print method of that native instance.
- **Lines 29-40**
  Declares the add method. This one uses numparams and param.
- **Lines 42-62**
  Declares the value property. As with method declarations, the property name is given to both the TJS_BEGIN_NATIVE_PROP_DECL and TJS_END_NATIVE_PROP_DECL macros.



  The getter is written between the TJS_BEGIN_NATIVE_PROP_GETTER and TJS_END_NATIVE_PROP_GETTER macros. In the getter, set the value into *result, which is a tTJSVariant.

  Likewise, the setter is written between the TJS_BEGIN_NATIVE_PROP_SETTER and TJS_END_NATIVE_PROP_SETTER macros. In the setter, the value to set is stored in *param, a tTJSVariant, so use it for processing.
- **Lines 64-79**
  Declares a read-only property. Writing TJS_DENY_NATIVE_PROP_SETTER instead of a setter makes the property read-only.

Registering a native class is the same as registering a native function. Here is some test code.

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
