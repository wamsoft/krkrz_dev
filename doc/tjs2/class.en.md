---
source_hash: c3ccacae9ea9
---

# Classes

## Classes

A class is a template for creating objects. Variables belonging to a class are called member variables, functions belonging to a class are called member functions or methods, and properties belonging to a class are called member properties.



A class is basically declared as follows.

```
**class** classname
{
	// write members, member methods and member properties here

	function classname() // constructor
	{
	}

	function **finalize**()
	{
	}
}
```

The class name is an identifier.



Inside the class, write the variables, methods and properties that become members when an object of the class is created.



A class always has exactly one method with the same name as the class, called the **constructor**. When an object is created with the **new** operator, this function is called with the arguments given to the new operator.



A class also has a special method called finalize. It is called when the object is destroyed, and it is optional; you do not have to write it.

```
	class test
	{
		function test()
		{
			// constructor
			// write what to do when the object is created here
			variable = 0;
		}

		function finalize()
		{
			// finalize method
			// write what to do when the object is destroyed here
		}

		function method1()
		{
			// method
			System.inform(variable);
		}

		var variable; // member variable

		property prop // member property
		{
			getter() { return variable; }
		}
	}
```

Using the instanceof operator with "Class" on a class yields true (in the example above, test instanceof "Class" is true).

## Creating Objects

To create an object of a declared class, use the new operator.

After the new operator, write the class name and the arguments to pass to the constructor, just like a function call.

```
	class Test
	{
		var variable1 = getValue(); // member variable initialization

		function Test(arg1, arg2) // constructor
		{
			// here, the arguments given to the new operator are passed to arg1 and arg2
		}
	}

	var newobject = new Test(1, 2); // create an object of the test class, passing 1, 2 as arguments
```

When an object of a class is created, processing happens in the following order.

1. First, an empty object is created
2. Methods and properties are registered
3. Member variables are created (variables that need initialization are initialized at this point)
4. The constructor is executed

> **Note:**
> Even if the constructor takes no arguments, you cannot omit the ( ) of the new operator. You cannot write new Test as in JavaScript; you must write new Test( ).

In particular, when creating an object of a class inside that class's methods or properties, or creating an object of that class's superclass, the following causes an error.

```
	class Test
	{
		function Test() // constructor
		{
		}

		function func()
		{
			return new Test(); // error
		}
	}
```

This is because when you simply write Test inside the class's methods or properties, the constructor Test is closer in scope than the class Test, so the constructor Test is referenced. To avoid this, you need to use global. explicitly, as below (because classes are registered in global).

```
	class Test
	{
		function Test() // constructor
		{
		}

		function func()
		{
			return new global.Test(); // this is OK
		}
	}
```

## Invalidating Objects

In TJS2, deleting an object involves two stages: **invalidating** the object and deleting the object.

When an object is invalidated, its finalize method is called and the object is marked as invalid. After that, every access to the object fails and raises an exception. You can check whether an object has been invalidated with the **isvalid** operator.



An object can be invalidated with the **invalidate** operator.

```
	class Test
	{
		var variable;

		function Test()
		{
			// constructor
			variable = new AnotherClass();
		}

		function finalize()
		{
			// the finalize method is called when the object is invalidated
			invalidate variable;
		}
	}

	var object = new Test(); // create the object

	(omitted)

	invalidate object; // invalidate the object
```

Even without the invalidate operator, an object is deleted once it is no longer needed. At that point, if it has not been invalidated, it is invalidated then.

TJS2 has no clear rule about when an object is deleted, so deletion and invalidation "can happen at any time". Therefore, since an object that has not been invalidated is invalidated when it is deleted, its finalize method may be called at an unexpected time. To avoid this, it is recommended to invalidate objects with the invalidate operator when you are done with them.

> **Note:**
> The invalidate operator works much like the C++ delete operator.
>
> Unlike the C++ delete operator, the TJS2 delete operator deletes members and local variables. It does not invalidate or delete the object itself, although deleting a member or local variable can end up causing an object to be invalidated or deleted.

## Accessing Objects

The member variables, methods and member properties of a created object are accessed with the **.** (member selection) operator or **[ ]** (indirect member selection operator).

```
	var obj=new MyLayer(window,window.prmaryLayer)
	obj.method1(); // call a method; same as obj['method1']()
	obj.num = 3; // assign to a member variable; same as obj['num']=3
	obj.prop1++; // access a member property; same as obj['prop1']++
```

## Closures

The methods and member properties of a created object are registered in the object together with information about which object they are members of.

Therefore, even if you take a method or member property out of the object and use it, it still accesses the original object. This feature is called a closure. The object being accessed is called the **context**.

```
	var obj = new FooBarClass(); // create an object
	obj.method(); // call the object's method normally
	var objmethod = obj.method; // assign a reference to the object's method to objmethod
	objmethod(); // calls objmethod, which accesses obj just like obj.method()
```

The **incontextof** operator changes the information about which object a member belongs to, providing a way to execute a method in an arbitrary context.

```
	(objmethod incontextof obj2)(); // operates on obj2
	(objmethod incontextof this)(); // operates on this
```

## Inheritance

The keyword **extends** lets a class inherit from another class. Inheritance means taking over the members of the class being inherited from.

The class being inherited from is called the **superclass**, and the inheriting class is called the **subclass**.

Declare the class as follows.

```
	class Class1 // superclass
	{
		function Class1() // Class1 constructor
		{
		}

		function finalize() // Class1 finalize
		{
		}

		function method1() // method1
		{
		}
	}


	class Class2 extends Class1
	{
		function Class2() // Class2 constructor
		{
			super.Class1(); // call the Class1 constructor
		}

		function finalize() // Class2 finalize
		{
			super.finalize();
		}
	}

	var obj = new Class2(); // create a Class2 object
	obj.method1(); // Class2 inherits method1 from Class1, so it can be used
```

In the example above, Class2 inherits from Class1. We also say that Class2 is **derived** from Class1.

The Class2 constructor calls the Class1 constructor, and Class2's finalize calls Class1's finalize. **If a subclass does not call the corresponding superclass method within these methods, the behavior is undefined** (more precisely, the current version does not check whether it was called), so always write these calls.



To refer to the superclass from a subclass, you can use the keyword **super**, as in the example above. This keyword can be used only inside a subclass and represents the superclass.



With inheritance, an object created with the new operator is initialized in the following order.

1. First, an empty object is created
2. Methods and properties are registered (from the superclass first, toward the subclass)
3. Member variables are created (from the superclass first, toward the subclass)
4. The subclass constructor is called
5. The superclass constructor is called (from within the subclass constructor)

## Multiple Inheritance

Writing multiple superclass names after extends enables multiple inheritance.

```
	class SubClass extends ClassA, ClassB
	{
		function SubClass() // SubClass constructor
		{
			ClassA(); // call the ClassA constructor
			ClassB(); // call the ClassB constructor
		}

		function finalize() // Class2 finalize
		{
			global.ClassA.finalize();
			global.ClassB.finalize();
		}
	}
```

Because the super keyword cannot be used, you must specify the classes explicitly. The reason for going out of the way to access the class through global. when calling a superclass method, as in the example, is that simply writing ClassA inside the subclass refers to the ClassA constructor. The classes themselves are registered in global, so you access them through global..



With multiple inheritance, an object created with the new operator is initialized in the same order as without multiple inheritance, but the superclass methods and properties are registered in the order the classes are written after the extends keyword. If the base classes have methods or properties with the same name, the one written later takes precedence. Hidden methods and properties can be accessed by writing the class name explicitly, as in global.ClassA.hiddenMethod().

## Overriding

Declaring something in a subclass with the same name as a superclass method or member property hides the superclass method. This is called overriding.

The finalize method that appeared in the explanation above overrides the superclass's finalize method.

```
	class Class1 // superclass
	{
		function Class1() // Class1 constructor
		{
		}

		function finalize() // Class1 finalize
		{
		}

		function method1() // method1
		{
			(omitted)
		}
	}


	class Class2 extends Class1
	{
		function Class2() // Class2 constructor
		{
			super.Class1(); // call the Class1 constructor
		}

		function finalize() // Class2 finalize
		{
			super.finalize();
		}

		function method1() // override Class1.method1
		{
			(omitted)
			if(omitted) return super.method1();
			(omitted)
		}
	}

	var obj = new Class2(); // create a Class2 object
	obj.method1(); // Class2's method1 is called
```

In subclass methods and properties, you can access superclass methods and properties using the super keyword.



Member variables cannot be overridden. Member variables are registered on a single object, so if the subclass and superclass have a member variable with the same name,
the subclass variable overwrites the superclass variable.
