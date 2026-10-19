---
source_hash: 6f6716df76ab
---

# Functions

## Functions

A function in TJS2 is nearly synonymous with a **subroutine**. Something that does not return a value is still treated as a function.

A function that is a member of a class or object is sometimes specifically called a "**method**".

## Writing Functions

A function is written in the following form.

```
	function function_name ( argument_list )
	{
		function body
	}
```

To define a function, first write **function**, followed by the function's name. The function becomes available under the name written here.

In the function body, you can write the statements and blocks you want to execute within the function.

```
	function test(a) { System.inform(a); }
	function func(a, b, c, d)
	{
		test(a);
		test(b);
		test(c);
		test(d);
		return a+b-c*d;
	}
```

Using the instanceof operator with "Function" on a function yields true (in the example above, func instanceof "Function" is true).

## Calling Functions

A function is called using the **( )** operator, as follows.

`
function_name( arguments )

`
If there are no arguments, write `function_name( )`. Each argument is an expression; separate multiple arguments with commas.

```
	func();
	func(1+2, 1-2);
	func(func2());
```

If you leave an argument empty without an expression, void is assumed for it.

```
	func(,1); // treated as void, 1
	func(,); // treated as void, void
```

## Argument List

In the argument list, write the names of variables that receive the passed arguments. The arguments passed in the call are assigned to these variables in order, starting from the first.

```
	function test(a, b, c)
	{
		// at this point, variables a, b and c are available,
		// holding the three arguments that were passed.
		// if called as test(1, 2, 3), a holds 1,
		// b holds 2, and c holds 3.
	}
```

These arguments are local variables and cannot be accessed once execution leaves the function.



In TJS2, passing fewer or more arguments than declared does not cause an error (as an exception, functions not written in TJS2, i.e. functions implemented in C++ or similar, may raise an error). If more arguments are passed than declared, the extra ones are ignored; if fewer are passed, the missing variables receive void.

```
	function test(a, b)
	{
		// if called as test(1), a holds 1 and b holds void.
		// if called as test(1,2,3), a holds 1, b holds 2, and 3 is ignored
	}
```

Each argument in the argument list can be given a default value (a **default argument**) with = followed by the value. The specified value is used automatically when void is passed or when fewer arguments than declared are given.

```
	function test(a = -1, b = 1)
	{
		// if...
		// called as test(), a=-1, b=1
		// called as test(5), a=5, b=1
		// called as test(void,void), a=-1, b=1
		// called as test(,4), a=-1, b=4
	}
```

A function that does not need to receive arguments can omit the argument list.

```
	function test
	{
		// a function that takes no arguments
	}
```

## Function Expressions

Using the function keyword inside an expression creates a nameless function, a function expression (an **anonymous function**).

In this case, the function name is omitted.

```
	var func = function(i) { return i*5; };
	var func2 = function { System.inform("hoge"); };
	var v = func(); // call func
	func2(); // call func2
```

## Forwarding Arguments

If you write only **...** as the argument when calling a function, the arguments passed to the function containing the call are passed as-is to the called function. Even if the argument variables have been modified, or too few arguments were received, the correct original contents and number of arguments are passed.

```
	function test()
	{
		test2(...);
		// test2 receives the arguments passed to test,
		// with the same contents and count as when they were passed
	}
```

## Receiving Arguments as an Array

Arguments can be received as an array. To do so, declare the function with '*****' appended to the argument name.

```
	function func(args*)
	{
		// args is an array whose elements are the arguments passed to this function
		// for example, if called as func(1, 2, 3, 4),
		// args contains four elements, holding the numbers
		// 1 2 3 4 in order from the first.
	}
```

You can also receive all the arguments from a certain position to the end as an array. If there are not enough arguments, the array is empty.

```
	function func(x, args*)
	{
		// for example, if called as func(1, 2, 3, 4),
		// x holds 1, and args contains three elements,
		// holding the numbers 2 3 4 in order from the first.
		// if called as func(1), there are not enough arguments,
		// so args is an array with no elements.
	}
```

This is useful for handling a variable number of arguments.



You can also omit the argument name. In that case, it can be used as a nameless * when expanding an array into arguments, as described below.

## Expanding an Array into Arguments

An array can be expanded and passed to a function as arguments. As when receiving arguments as an array, append '*****' to the expression you want to expand when calling the function. The expression to be expanded with '*' must evaluate to an array.

```
	var args = [1, 2, 3, 4];
	func(args*);
	// args contains the four elements 1 2 3 4,
	// so this means the same as func(1, 2, 3, 4);.
	func(0, args*, 5);
	// it can also be placed in the middle of the arguments.
	// in this case, it means the same as func(0, 1, 2, 3, 4, 5);
	// .
```

If you specify just * as an argument without an expression, the arguments represented by the nameless '*' in the declaration of the function containing the call are passed as-is to the called function.

```
	function func(func_array, *)
	{
		// calls each function in func_array, passing
		// its position in func_array followed by
		// the second and subsequent arguments passed to func
		// as-is
		for(var i = 0; i < func_array.count; i++)
			func_array[i](i, *);
	}
```

A function call using a nameless * is processed more efficiently than one using a named array.

```
	function func(ar*) { func2(ar*); }
	function func(*) { func2(*); }
	// the two above mean exactly the same thing, but the lower one is more efficient
```

A nameless * has the same effect as "Forwarding Arguments". The following two function declarations mean the same thing.

```
	function func() { func2(...); }
	function func(*) { func2(*); }
```
