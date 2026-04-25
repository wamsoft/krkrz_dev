# TJS2 の基本型

## プリミティブ型

tjsTypes.h で定義されているプリミティブ型がいくつかあります。

- ****tjs_int****  
  符号あり整数(最低32bit)
- ****tjs_uint****  
  符号なし整数(最低32bit)
- ****tjs_int8****  
  8bitの符号あり整数
- ****tjs_uint8****  
  8bitの符号なし整数
- ****tjs_int16****  
  16bitの符号あり整数
- ****tjs_uint16****  
  16bitの符号なし整数
- ****tjs_int32****  
  32bitの符号あり整数
- ****tjs_uint32****  
  32bitの符号なし整数
- ****tjs_int64****  
  64bitの符号あり整数
- ****tjs_uint64****  
  64bitの符号なし整数
- ****tjs_char****  
  ワイド文字(TJS2の文字列型のプリミティブ型として使用されます)
- ****tjs_nchar****  
  ナロー文字
- ****tjs_real****  
  実数型(double)
- ****tTVInteger****  
  tjs_int64と同じ
- ****tTVReal****  
  tjs_realと同じ

## tTJSString

tTJSString 型は TJS2 で用いる文字列型で、tjs_char 型のゼロ終結文字列を扱います。tjsString.cpp / tjsString.h に定義されています。また、短く `ttstr` という型名でも利用可能です。

この型は文字列用のメモリの管理を自動的に行うほか、

との親和性が高い型です。

## eTJS

eTJS 型は C++ 例外オブジェクトの基本型です。tjsError.h に定義されています。**GetMessage** というメソッドがあり、例外とともに投げられたメッセージ文字列を取得することができます。

## TJS_W

文字列リテラルを tjs_char * 型に変換するためのマクロです。



例 : TJS_W("文字列リテラル")
