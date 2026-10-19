---
source_hash: e9b4d1c27a4f
---

# Statements and Blocks

## Statements and Blocks

Statements and blocks are the major syntactic building blocks of TJS2.

## Statements

A statement is something that ends with **;** (a semicolon). Some statements are an expression followed directly by a semicolon; others are control constructs such as if followed by a semicolon.

```
	a++;
	func1();
	return a+b;
	and so on
```

## Blocks

A block groups multiple statements written between **{ }**. The statements are executed from top to bottom.

```
	{
		a++;
		b++;
	}

	{
		var t=func1();
		func2(t);
		break;
	}
```

A block does not need to be followed by ; (a semicolon).



Every block also creates a variable **scope**.

## Execution Order

In TJS, statements written outside functions, classes and properties are executed as soon as the script runs. Statements inside functions, classes and properties are not executed until they are called.

```
	var a; // executed immediately

	function test()
	{
		a+=10; // not executed until called
	}

	a+=30; // executed immediately
```

More precisely, when a script runs, class definitions, function definitions and property definitions are registered first, and then the remaining elements of the script are executed from the top. As a result, functions, classes and properties can be referenced before their definition within the same script block.

```
	test(); // a function declared after this point can still be referenced within the same script block

	function test()
	{
		inform("yah!");
	}
```

Calling a function (or similar) across different script blocks works if the target function has already been loaded at the time of the call.

Variable declarations, on the other hand, are processed in the order they are read, so variables cannot be referenced before their declaration.

## The Global Object

The global object is a special object whose members are the variables, functions, properties and so on declared at global scope. It can be accessed with the global keyword.
