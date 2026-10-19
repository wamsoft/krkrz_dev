---
source_hash: 9c18522bd20b
---

# Expressions and Operators

## Expressions and Operators

An **expression** is a collection of operators and operands, or an immediate value.



Normally, you can write the following in a script.



`
expression;

`


When an expression is followed by a semicolon like this, the expression is evaluated (= executed) on the spot, and its result as an expression is discarded.

```
	a = b;
	// the = operator assigns variable b to variable a

	func();
	// the ( ) operator calls func as a function, but the function's return value
	// is discarded

	1 + 3;
	// the + operator adds 1 and 3, but the result is discarded (in practice this
	// expression has no effect, so it is not even executed)
```

## True and False

Some operators deal with true or false (logical values). A result of 0 is false, and anything other than 0 is true.

When the truth of a string is tested, an empty string is false; otherwise, the string is converted to a number, and if that succeeds, the truth of that number is used; if it fails, the result is false.

## Operators

The operators are described below in order from lowest to highest precedence.

## if Operator

The if operator `if` evaluates what is on its left only if what is on its right evaluates to true.

```
	a=b if b!=0; // assign b to a if b is not 0
```

The operator has no result value.

## Sequence Operator

The sequence operator `**,**` (comma) evaluates what is on its left, then what is on its right. It does nothing else. The value of the whole operator is the result of evaluating what is on its right. When several commas appear in a row, the operands are evaluated from left to right.

```
	c = (a=1, b=2); // a=1, b=2 are evaluated, and 2 is assigned to c
	a=1, b=2, c=3; // evaluated in the order a=1, b=2, c=3
```

## Assignment Operators

The assignment operators are as follows.



`**=**  **<->**  **&=**  **|=**  **^=**  **-=**  **+=**  **%=**  **/=**  **\=**  ***=**  **||=**  **&&=**  **>>=**  **<<=**  **>>>=**`


Of these, the = operator is the simple assignment operator. It assigns the result of evaluating its right side to its left side, and the value of the whole operator is the result of evaluating its right side.

```
	a = 0;  // assign 0 to a
	a = b = c = 0; // assign 0 to c, b, a in that order
```

The `<->` operator swaps values. It first evaluates its left side, then its right side. It then assigns the result of the right side to the left side, and the result of the left side to the right side. The operator has no result value.

Currently, each side is **evaluated twice**: once to get its value and once to assign to it. This may change in the future, so do not write code that depends on the number of evaluations.



All other operators take the form `operator=`; writing `A operator= B` means `A = A operator B`. The value of the whole operator is the result of the operation.

## Conditional Operator

The conditional operator `**? :**` is a ternary operator. Written as `A ? B : C`, it evaluates A; if A is true, it evaluates B and ignores C; if A is false, it evaluates C and ignores B. The value of the whole operator is the value of whichever of B or C was evaluated.



The conditional operator can be used as an lvalue.

```
	a = b==0 ? c : b; // if b is 0, assign c to a; otherwise assign b to a
	b==0 ? (a=c) : (a=b); // same meaning as above
	(a ? b : c ) = d; // assign d to b if a is true, or to c if a is false (used as an lvalue)
```

## Logical OR Operator

The logical OR operator `**||**` first evaluates its left side; if it is true, the right side is ignored and the result of the whole operator is true. If the left side evaluates to false, the right side is evaluated, and its truth value becomes the result of the whole operator.

## Logical AND Operator

The logical AND operator `**&&**` first evaluates its left side; if it is false, the right side is ignored and the result of the whole operator is false. If the left side evaluates to true, the right side is evaluated, and its result becomes the result of the whole operator.

## Bitwise OR Operator

The bitwise OR operator `**|**` performs a bitwise logical OR. It evaluates its left side, then its right side, and the value of the whole operator is the bitwise OR of the results treated as integers.

## Bitwise XOR Operator

The bitwise XOR operator `**^**` performs a bitwise logical XOR. It evaluates its left side, then its right side, and the value of the whole operator is the bitwise XOR of the results treated as integers.

## Bitwise AND Operator

The bitwise AND operator `**&**` performs a bitwise logical AND. It evaluates its left side, then its right side, and the value of the whole operator is the bitwise AND of the results treated as integers.

## Equality Operators

`**==**  **!=**  **===**  **!==**` are the equality operators.

- **`==` operator**  
  The `==` operator evaluates its left side first, then its right side. If the two are equal, the whole operator is true; otherwise it is false. If the two sides have different types, they are converted appropriately before comparison. For example, `-1 == '-1'` is true.
- **`!=` operator**  
  The `!=` operator is the `==` operator with its truth value reversed.
- **`===` operator**  
  The `===` operator is called the identity comparison operator. It is the same as the `==` operator, except that no type conversion is performed; it is true only if the types match as well.
- **`!==` operator**  
  The `!==` operator is the `===` operator with its truth value reversed.

## Comparison Operators

`**<**  **>**  **<=**  **>=**` are the comparison operators.

- **`<` operator**  
  The `<` operator evaluates its left side first, then its right side. It is true if the result of the left side is less than the result of the right side, and false otherwise.
- **`>` operator**  
  The `>` operator evaluates its left side first, then its right side. It is true if the result of the right side is less than the result of the left side, and false otherwise.
- **`<=` operator**  
  The `<=` operator evaluates its left side first, then its right side. It is true if the result of the left side is less than or equal to the result of the right side, and false otherwise.
- **`>=` operator**  
  The `>=` operator evaluates its left side first, then its right side. It is true if the result of the right side is less than or equal to the result of the left side, and false otherwise.

If both operands are strings, they are compared in wide character code order (normally Unicode).

## Bit Shift Operators

`**>>**  **<<**  **>>>**` are the bit shift operators.

- **`>>` operator**  
  The `>>` operator first evaluates its left side, then its right side. The result of the whole operator is the left result, treated as an integer, shifted right (signed) by the number of bits given by the right result.
- **`<<` operator**  
  The `<<` operator first evaluates its left side, then its right side. The result of the whole operator is the left result, treated as an integer, shifted left by the number of bits given by the right result.
- **`>>>` operator**  
  The `>>>` operator is the same as the `>>` operator, except that it treats the result of the left side as an unsigned integer.

## Additive Operators

`**+**  **-**` are the addition and subtraction operators, respectively.

- **`+` operator**  
  The `+` operator evaluates its left side first, then its right side. If both results are numbers, numeric addition is performed and becomes the result of the whole operator. If either or both are strings, string concatenation is performed, and the result of the whole operator is the string formed by appending the right result to the left result. Numbers are converted to strings, and objects are converted to strings if possible.
- **`-` operator**  
  The `-` operator evaluates its left side first, then its right side. It then subtracts the right result from the left result as numbers, and that becomes the value of the whole operator.

## Multiplicative Operators

`**%**  **/**  **\**  *****` are the remainder, division, integer division and multiplication operators, respectively.

- **`%` operator**  
  The `%` operator evaluates its left side first, then its right side. The value of the whole operator is the remainder of dividing the left side by the right side. Both values are treated as integers.
- **`/` operator**  
  The `/` operator evaluates its left side first, then its right side. The value of the whole operator is the left side divided by the right side. The values are treated as real numbers.
- **`\` operator**  
  The `\` operator performs division like the / operator, but the values are treated as integers.
- **`*` operator**  
  The `*` operator evaluates its left side first, then its right side. The value of the whole operator is the left side multiplied by the right side. The values are treated as real numbers.

## General Unary Operators

All of the following are unary operators (`instanceof` is an exception).

- **`**!**` operator**  
  The prefix `!` operator is the logical NOT operator. The value of the whole operator is the truth value of its right side, reversed.
- **`**~**` operator**  
  The `~` operator is the bitwise NOT operator. The value of the whole operator is the result of evaluating its right side, treated as an integer, with each bit inverted (1→0, 0→1).
- **`**--**` operator**  
  The prefix `--` operator is the prefix **decrement** operator. It subtracts 1 from its right side, and the value after subtraction is the value of the whole operator.
- **`**++**` operator**  
  The prefix `++` operator is the prefix **increment** operator. It adds 1 to its right side, and the value after addition is the value of the whole operator.
- **`**new**` operator**  
  The `new` operator makes the function call expression on its right create an object instead of calling a function.
- **`**invalidate** operator`**  
  The `invalidate` operator evaluates its right side and invalidates the resulting object. If the right side is void, a string, a number or an octet sequence, it does nothing. It also does nothing if the object has already been invalidated. If null is given, an exception is raised.
- **`**isvalid** operator`**  
  The `isvalid` operator evaluates its right or left side, and is true if the resulting object is valid and false if it is invalid. Placing the operator before or after its operand means the same thing. If the operand is void, a string, a number or an octet sequence, it always returns true. If null is given, an exception is raised.
- **`**delete** operator`**  
  The `delete` operator deletes the object member or local variable written on its right. It is true if the deletion succeeds and false if it fails.
- **`**typeof** operator`**  
  The `typeof` operator evaluates its right side and yields one of the following strings depending on the type: void: "void", integer: "Integer", real: "Real", object: "Object", string: "String", octet sequence: "Octet". However, if an object member is specified and the member does not exist, it yields "undefined".
- **`**#** operator`**  
  The `#` operator evaluates its right side and yields the character code of its first character, treated as a string.
- **`**$** operator`**  
  The `$` operator evaluates its right side, treats the result as a character code, and yields the single character it represents.
- **`**+** operator`**  
  The unary `**+**` operator evaluates its right side. If the right side is a real number or an integer, it does nothing. Otherwise, it tries to convert it to a real number or a number, and that becomes the result of the whole operator. When converting a string to a number, a failed conversion does not raise an exception but yields 0. A real number representation containing a decimal point is converted to a real number; otherwise it is converted to an integer. If the string starts with 0x, 0b or 0, it is interpreted as hexadecimal, binary or octal, respectively.
- **`**-** operator`**  
  The unary `-` operator evaluates its right side (the operand that follows it), treats the result as a number, and yields it with its sign reversed.
- **`**&** operator`**  
  The unary `&` operator changes access to the object member written on its right into access to the property object itself, bypassing the property handlers. For example, in propobj = &obj.prop;, the property handlers of obj's member property prop are not invoked; instead, a reference to the **property object** of member property prop itself is assigned to propobj. The behavior is undefined if the right side is not a property access.
- **`***** operator`**  
  The unary `*` operator invokes the property handlers of the object written on its right. The right side must be an expression representing a property object. For example, *propobj = 1; calls the setter handler of the property object propobj and assigns 1.
- **`**instanceof** operator`**  
  The `instanceof` operator evaluates its left side, then its right side. The right side should be something that evaluates to a string naming a class; the result is true if the left side is an instance of that class, and false otherwise.

## Function Calls, Parentheses, Postfix Increment/Decrement and More

- **`**(  )** operator`**  
  The `(  )` operator changes the order of evaluation, or performs a function call.
- **`**[  ]** operator`**  
  The `[  ]` operator is the indirect member selection operator. Written as `A [ B ]`, it evaluates A first, then B. It looks up the member named by B (as a string) in A, and the whole operator becomes an access to that member. When used as an lvalue, it also creates member B in the object if it does not exist.
- **`**.** operator`**  
  The `.` operator is the direct member selection operator. Written as `A.B`, it evaluates A, looks up B in A, and the whole operator becomes an access to that member. When used as an lvalue, it also creates member B in the object if it does not exist.
  If the left side of the `.` operator is omitted, it refers to a member of the global object when outside a with statement, or to a member of the object specified by the with statement when inside one.
- **`**++** operator`**  
  The postfix `++` operator is the postfix increment operator. It adds 1 to its left side, and the value of the whole operator is the left side before the addition.
- **`**--** operator`**  
  The postfix `--` operator is the postfix decrement operator. It subtracts 1 from its left side, and the value of the whole operator is the left side before the subtraction.
- **`**!** operator`**  
  The postfix `!` operator is the expression evaluation operator. It treats the result of evaluating its left side as a string and interprets it as an expression string. The result is the result of interpreting and evaluating that expression string. The expression runs in the this context (the this at the place where the operator is used).
- **`**incontextof** operator`**  
  The `incontextof` operator evaluates its left side first, then its right side. The result of the whole operation is the object obtained from the left side with its context part replaced by the result of evaluating the right side.
- **`**int** operator`**  
  The int operator evaluates its right side, and the result of the whole operator is that value converted to an integer. It can also be written as (int), like a C cast.
- **`**real** operator`**  
  The real operator evaluates its right side, and the result of the whole operator is that value converted to a real number. It can also be written as (real), like a C cast.
- **`**string** operator`**  
  The string operator evaluates its right side, and the result of the whole operator is that value converted to a string. It can also be written as (string), like a C cast.
