---
source_hash: 73a367d441bf
---

# TJS2 Basic Types

## Primitive types

tjsTypes.h defines several primitive types.

- ****tjs_int****  
  Signed integer (at least 32 bits)
- ****tjs_uint****  
  Unsigned integer (at least 32 bits)
- ****tjs_int8****  
  8-bit signed integer
- ****tjs_uint8****  
  8-bit unsigned integer
- ****tjs_int16****  
  16-bit signed integer
- ****tjs_uint16****  
  16-bit unsigned integer
- ****tjs_int32****  
  32-bit signed integer
- ****tjs_uint32****  
  32-bit unsigned integer
- ****tjs_int64****  
  64-bit signed integer
- ****tjs_uint64****  
  64-bit unsigned integer
- ****tjs_char****  
  Wide character (used as the primitive type of TJS2 strings)
- ****tjs_nchar****  
  Narrow character
- ****tjs_real****  
  Real number type (double)
- ****tTVInteger****  
  Same as tjs_int64
- ****tTVReal****  
  Same as tjs_real

## tTJSString

tTJSString is the string type used by TJS2. It holds a zero-terminated string of tjs_char. It is defined in tjsString.cpp / tjsString.h, and is also available under the shorter name `ttstr`.

In addition to managing string memory automatically, this type works well with the [tTJSVariant type](variant.md).

## eTJS

eTJS is the base type of C++ exception objects. It is defined in tjsError.h. Its **GetMessage** method returns the message string thrown with the exception.

## TJS_W

A macro that converts a string literal to the tjs_char * type.



Example: TJS_W("string literal")
