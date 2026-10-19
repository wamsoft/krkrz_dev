---
source_hash: c876a2985f76
---

# Factors

## Factors

Factors have the highest precedence in expression evaluation. In addition to ordinary immediate values and identifiers (→ [token](token.md)), they include the following.

## true and false

`true` and `false` (**true and false**) are treated as integers with the values `1` and `0`, respectively.



Avoid comparing `true` or `false` with other expressions. For example, instead of writing `if(true != getBoolean())`, write `if(!getBoolean())`. In logical expressions, "0 is false" and "anything other than 0 is true", not "`1` is true". Also, TJS2 has no logical (Boolean) type, so no automatic conversion between numbers and Booleans takes place.

## void

`void` means "nothing". It is used in various situations to indicate the absence of anything. It is different from `null`.

A freshly declared variable (one that has not been assigned anything) has this value.

When treated as a string, it becomes the empty string (''). When treated as a number, it becomes 0.



To compare `void` values, the `===` or `!==` (identity) operators are recommended.

## null

`null` indicates something that is an object but "does not refer to any object". It is different from `void`.

Attempting to access a null object causes an error.

If you change a function's context to null using the incontextof operator, the function is then executed in the context of the place where it is called.

```
	var objmethod = obj.method;
	objmethod(); // executed in the context of obj
	objmethod = objmethod incontextof null; // change the context to null
	objmethod(); // executed on this (that is, the context at the calling site)
```

## Infinity

`Infinity` represents infinity. Negative infinity is `-Infinity`.

## NaN

`NaN` represents Not a Number. NaN is the numeric value obtained, for example, when the result of a calculation is invalid.

## super

`super` represents the superclass of a class, within that class's methods/properties. Referring to it outside a class method/property, or inside a class that uses multiple inheritance, causes an error.

## global

`global` represents the global object. Through it you can access variables declared outside all blocks, classes, functions that are not class methods, and so on.

```
	var v;
	function test(v)
	{
		global.v=v;  // set the global v to the argument v
	}
```

## this

Within a class's methods and properties, `this` normally represents the object of that class itself.

The "context" specified explicitly or implicitly at call time is what `this` refers to.

## Function Expressions

You can write a function inside an expression using `function`.

For details, see [Functions](function.md).

## Array Literals

You can write an `Array` class object on the spot inside an expression using `**[ ]**`.

For details, see [Array class](array.md).

## Dictionary Literals

You can write a `Dictionary` class object on the spot inside an expression using `**%[ ]**`.

For details, see [Dictionary class](dictionary.md).
