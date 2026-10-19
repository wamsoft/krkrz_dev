---
source_hash: 4674a32a7098
---

# Operations on Strings

## Operations on strings

In TJS2, a string is nominally treated as an object of the **String** class, but no String class actually exists, and a string is not really a String object (although the typeof operator returns "String" for a string).

Still, strings can be treated as objects, and several methods and properties are available on them.

## length

The length property returns the length of the string. Note that it is a property, not a method. You cannot assign a value to it.



TJS handles all characters internally as **UNICODE**, so full-width and half-width characters each count as one character.

```
	var str = "abc漢字";
	var n = str.length;  // n には 5 が代入される
	var n = "abc漢字".length; // これも同じく 5 が代入される
```

## Numeric properties

Indirectly specifying a number as a property accesses the character at that position.

For example, if str is a string or an expression that represents a string, str[0] is a string consisting of its first character.

An exception is thrown if the number is beyond the length of the string or is negative (however, the position just past the last character returns an empty string).



You cannot use it as the target of an assignment.

```
	var str = "abcdef";
	var c = str[0];  // 'a' が c に代入される
	var c = str[2];  // 'c' が c に代入される
	str[3] = 'A'; // 代入式は生成できないのでエラーになる
	var c = str[100]; // c 値が範囲外なのでエラーになる
	var c = str[6]; // 空文字 '' が代入される
```

## charAt

The charAt method returns the character at the specified position in the string. It behaves like the numeric property, but always returns an empty string when the position is out of range (it does not throw an exception).

```
構文 : charAt(<文字位置>)
```

```
	var str = "abcdef";
	var c = str.charAt(3); // 'd' が c に代入される
```

## indexOf

The indexOf method returns the position of a substring.

```
構文 : indexOf(<部分文字列>[,<検索開始位置>])
```

Searches the string for the substring (first argument), starting at the start position (second argument), and returns the position where it is first found. 0 means the beginning of the string; -1 means it was not found. If the start position is omitted, the search begins at the start of the string.

```
	var str = "abcdefghijkl";
	var n = str.indexOf("fgh"); // n には 5 が代入される
	var n = str.indexOf("xyz"); // n には -1 が代入される
```

## toLowerCase

This method takes no arguments.

toLowerCase returns the string with its letters converted to lowercase.

Full-width characters are not converted.



These methods do not modify the original string.

```
	var lwr="ABCDEF".toLowerCase(); // lwr には "abcdef" が代入される
```

> **Note:**
> The current version of TJS2 converts only characters with codes below 0x80.

## toUpperCase

The opposite of toLowerCase: returns the string with lowercase letters converted to uppercase.

## substring

The substring method returns a substring of the string.

```
構文 : substring(<開始文字位置>[,<文字数>])
```

Returns the substring of the given number of characters (second argument) starting at the start position (first argument). The original string is not modified. If the number of characters is omitted, everything from the start position onward is returned.

Note that the meaning of the arguments differs from JavaScript's method of the same name.

```
	var ss="abcdefghijkl".substring(3,3); // ss には "def" が代入される
```

## substr

Same as substring.

## sprintf

The sprintf method formats a string.

```
構文 : sprintf(引数, 引数, ....)
```

Treats the string as a format string and returns the result of formatting the arguments as C's sprintf does. The original string is not modified.

```
	var formatted = "%04X %c %5d".sprintf(v1, v2, dic[v1]);
```

## replace

The replace method performs string replacement.

```
構文 : replace(<パターン>, <置き換え後文字列>)
```

Replaces parts of the string according to the regular expression pattern and returns the resulting string. The original string is not modified.

For details on its behavior, see the replace method of the [RegExp class](regexp.md#replace).

## split

The split method splits the string.

```
構文 : split(<パターン/デリミタ集合>, <(予約)>, <空の要素を無視するか=false>)
```

The first argument is a pattern or a set of delimiter characters; the second is reserved; the third specifies whether to ignore empty elements (default false). Returns an array object containing the result of splitting the string.

See also the split method of the [RegExp class](regexp.md#split) (note the different argument order).

## escape

The escape method converts the string into a form that can be written inside a TJS string literal. Symbols such as \ and " are escaped with \ so they are not interpreted specially.

```
構文 : escape()
```

Returns the escaped string. The original string is not modified.

```
	var escaped = str.escape(); // str 中の " は \" に、\ は \\ に変換されるなど
```

## trim

The trim method returns the string with whitespace removed from its beginning and end. The original string is not modified.

Whitespace here means characters with codes U+0001 through U+0020. This includes ASCII control characters, but not the so-called full-width (ideographic) space.

Consecutive whitespace at the beginning or end is removed entirely.

```
構文 : trim()
```

Returns the string with leading and trailing whitespace removed. The original string is not modified.

```
	var str = "  Hoge ".trim(); // str は "Hoge" です。
```

## reverse

The reverse method returns the string with its characters in reverse order. The original string is not modified.

In the current version of TJS2, behavior is not guaranteed for strings that contain UTF-16 surrogate pairs.

```
構文 : reverse()
```

Returns the string with its characters in reverse order. The original string is not modified.

```
	var str = "Hoge".reverse(); // str は "egoH" です。
```

## repeat

The repeat method returns the string repeated the specified number of times. The original string is not modified.

```
構文 : repeat(count)
```

Returns this string repeated count times. The original string is not modified.

```
	var str = "Hoge".repeat(3); // str は "HogeHogeHoge" です。
```
