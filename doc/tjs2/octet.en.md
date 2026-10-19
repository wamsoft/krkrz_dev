---
source_hash: 245a513d8031
---

# Operations on Octet Strings

## Operations on octet strings

In TJS2, an octet string is nominally treated as an object of the **Octet** class, but no Octet class actually exists, and an octet string is not really an Octet object (although the typeof operator returns "Octet" for an octet string).

Still, octet strings can be treated as objects, and several methods and properties are available on them.



The octet string implementation is incomplete.

## length

The length property returns the length of the octet string. Note that it is a property, not a method. You cannot assign a value to it.

```
	var oct = <% 11 22 33 %>;
	var n = oct.length;  // n には 3 が代入される
	var n = <% 11 22 33 %>.length; // これも同じく 3 が代入される
```

## Numeric properties

Indirectly specifying a number as a property accesses the octet at that position.

The result is the numeric value of the octet.

For example, if oct is an expression that represents an octet string, oct[0] is a number representing the value of the first octet.

An exception is thrown if the number is beyond the length of the octet string or is negative.



You cannot use it as the target of an assignment.

```
	var oct = <% 11 22 33 44 55 %>;
	var c = oct[0];  // 0x11 が c に代入される
	var c = oct[2];  // 0x33 が c に代入される
	oct[3] = 'A'; // 代入式は生成できないのでエラーになる
	var c = oct[100]; // 値が範囲外なのでエラーになる
```
