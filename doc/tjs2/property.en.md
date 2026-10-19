---
source_hash: 136af0fa06ff
---

# Properties

## Properties

A property can be used just like a variable, but in reality, like a method call, accessing it involves calling a **setter** and a **getter**. Setters and getters are sometimes called property handlers.



The syntax is as follows.

```
**property** identifier
{
	setter(argument)
	{
		// setter body goes here
	}

	getter()
	{
		// getter body goes here
		return expression; // value returned by the getter
	}
}
```

The setter and getter may be written in the opposite order.

The property is registered as a member of the class in which it is written, or of the global object. Reading a value from this identifier goes through the getter, and setting a value goes through the setter. Like methods, setters and getters can contain any code. For the setter, write the variable that receives the value as the argument in the ( ) after setter. The getter returns a value with a **return** statement.



The () after getter can be omitted.



If you write both a setter and a getter for an identifier, the property can be both read and written. If you write only one of them, for example only a getter, the property is read-only and writing to it causes an error.

```
	var value;

	property property1 // declare property 'property1'
	{
		setter(v)
		{
			// a setter takes exactly one argument
			value=v; // process argument v

			inform("value set.");
		}

		getter
		{
			// declare the getter for the same identifier 'property1' as propset
			// a getter has no arguments
			inform("value get.");
			return value; // return as the return value
		}
	}

	property1=5; // assigning to property1 calls the setter
	property1++; // in an expression like this, the getter is called,
	             // then the setter is called to set the value
}
```

Like variables, functions and classes, properties can be **overridden**.

## Property Objects

A property is itself an object. However, when it is registered in some object, normal access just calls the property handlers, and you cannot access the property object itself.

To get the property object itself, use the `**&**` operator. The retrieved property object can be stored in a local variable.

You can also use the `&` operator to register a property object.

```
	property prop // declare property prop
	{
		(omitted)
	}

{
	var p = &prop; // get the property object and store it in a local variable

	&object.property1 = p; // register p as property1 of object
}
```

With the `&` operator, you can access the property object itself without calling the getter or setter. Without the `&` operator, it is a normal property access.



A property object retrieved into a local variable can have its property handlers called with the `*****` operator, even without registering it in an object.

```
	property prop // declare property prop
	{
		(omitted)
	}

{
	var p = &prop; // get the property object and store it in a local variable

	*p = 30; // call the setter to set 30
	func(*p); // call the getter to get the value and pass it to func
}
```

> **Note:**
> When storing a property object in a var variable as shown above, make the variable a local variable. This is because once a property object is registered in an object, it behaves not as a property object but as a property, going through its getter and setter. In other words, if you register a property object in a global variable (= a member of global) or a member of an object instead of a local variable, it behaves just like an ordinary property. Of course, it is fine to use the & operator to retrieve a property object registered in a global variable or object member this way.

Using the instanceof operator with "Property" on a property object yields true (in the example above, &prop instanceof "Property" is true).
