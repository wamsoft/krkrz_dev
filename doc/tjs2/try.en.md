---
source_hash: e98567875b52
---

# Exception Handling

## Exception Handling

An **exception** is, as the word suggests, an "exceptional" situation that would not occur in normal processing. In most cases, you can think of it as the same thing as an "error".

## Where Exceptions Occur

An exception can occur anywhere in a program.

Raising an exception is also called "throwing" an exception.

For example, suppose the following script causes an error.

```
	"3%0"!; // a "division by zero" exception occurs
```

In some cases, like this one, an exception will obviously occur; in other cases, you cannot tell whether one will occur or not.

## Catching Exceptions

You can catch exceptions using the `**try**` keyword and the `**catch**` keyword.

For example, to catch an exception that might occur, you can write a script like the following.

```
	try // an exception might occur, so
	{
		func1(); // an exception might occur here
	}
	catch // catch the exception
	{
		// executed when an exception occurs
		inform("Could not load the image."); // show a message
	}
```

By writing code that might raise an exception inside the try block like this, you can have the catch block executed when an exception occurs. This lets you write error handling cleanly.



If no exception occurs in the try block, the catch block is not executed.



You can write anything in the try block. Sometimes, as in this example, it is clear that a particular line might raise an exception; but even if an exception occurs deep inside a function called by a function called from here, writing try ... catch lets execution return here as soon as the exception occurs.



When an exception occurs, the rest of the block is abandoned and execution returns to where the try is.



If another exception occurs in the catch block, it is not caught here. The exception propagates back up through the function calls, and if a try somewhere else catches exceptions, it is caught there.



Another exception may occur after an exception is thrown and before it reaches the catch block; the behavior in that case is undefined.



If an exception is not caught anywhere in the script, it leaves the script and is passed to the application, which handles it.

> **Note:**
> Such exceptions usually stop execution as an error, so it is recommended to write try ... catch wherever errors are likely to occur.

## Exception Objects

Various information about an exception is thrown along with an object of the **Exception** class. This object is called the exception object, and it can be received with catch. For details, see [Exception class](exception.md).

For example, you can write a script like the following.

```
	try
	{
		loadImages("nothing.jpeg"); // code that might raise an exception
	}
	catch (e) // receive the exception in the variable e
	{
		// e.message is the message string thrown along with the exception.
		// It may explain why the exception occurred.
		inform("Could not load the image.\n"+e.message);
	}
```

As shown, you write a variable in parentheses after catch, and the exception object is received in that variable.

The scope of this variable begins inside the block following catch and ends with that block. The variable does not need to be declared beforehand.

## throw Statement

You can also throw exceptions yourself. Use the `**throw**` keyword to throw an exception.

For example, you can write a script like the following.

```
	function pow2(n)
	{
		// compute 2 to the power of n; n must be a positive integer
		if(n<0) throw new Exception("Negative numbers are not allowed.");
			// ↑ raise an exception
		return 1<<n;
	}
```

If a negative number such as -1 is passed as the argument of this function, an exception is raised. The statement that throws the exception is the following.

```
throw new Exception("Negative numbers are not allowed.");
```

`new Exception("Negative numbers are not allowed.")` creates an object of the Exception class with a string as its argument. For details, see [Exception class](exception.md). This newly created object is then thrown with the throw keyword.

What you throw with the throw keyword does not have to be an Exception class object. You can throw a number, a string, or even a reference to a function. However, throwing an object of the Exception class or a class derived from it is recommended, because then the catch block only needs to be written to expect an Exception class object.

## Rethrowing Exceptions

Sometimes you catch an exception with catch, but there may be another try somewhere that should also receive the exception. In such cases, you can throw the exception again.

You can write a script like the following.

```
	function tryloadimage()
	{
		try
		{
			primaryLayer.loadImages("test1.bmp"); // try loading test1.bmp
		}
		catch(e)
		{
			inform("Failed to load the image.");
			throw e; // show a message, but rethrow the exception
		}
	}

	function test()
	{
		// calls tryloadimage and returns true if the image was loaded,
		// false otherwise
		try
		{
			tryloadimage();
		}
		catch
		{
			return false;
		}
		return true;
	}
```

If you call test() here and the image fails to load, the inform method displays a message, but because the exception is thrown again, it can be caught by the catch in the test function.
