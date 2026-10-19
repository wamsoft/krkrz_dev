---
source_hash: 953f1c1cd83f
---

# with Statement

## with Statement

The **with** statement specifies the object to refer to when the left-hand side (the object) of the `.` (dot) operator is omitted.



The syntax is as follows.

```
with(expression)
	statement or block
```

When a `.` (dot) operator with its left-hand side omitted is used inside the "statement or block", the object that `.` (dot) operator refers to is the object specified by expression in the with statement.

```
	with(obj) .member = 1; // same as obj.member = 1;

	with(obj)
	{
		.member1 = 1; // assign 1 to obj.member1
		.member2 = 2; // assign 2 to obj.member2
		.member3++; // increment obj.member3
		.method(); // call obj.method
	}
```

This statement is especially useful for reducing typing when setting many properties on an object or calling methods on it in succession.



For example, a script like

```
	var object = new Foo();
	object.setPos(0, 0);
	object.setSize(100, 100);
	object.name = "Untitled";
	object.color = 0xffffffff;
```

can be written as follows.

```
	var object = new Foo();
	with(object)
	{
		.setPos(0, 0);
		.setSize(100, 100);
		.name = "Untitled";
		.color = 0xffffffff;
	}
```

## The with Statement and Objects

The expression given to a with statement is evaluated only once, when the with statement starts executing; after that, the result is simply referred to.



For example, even if you write

```
this.dic = %[];
with(this.dic)
{
	.member = 1; // assign 1 to this.dic.member
	this.dic = 0; // assign something else to dic
	.member = 2; // assign 2 to this.dic.member
}
```

the second assignment to .member will succeed. This is because this.dic is evaluated when the with statement starts executing, and that result is used from then on. this.dic is not evaluated each time.



Because the expression is evaluated only once, in cases where an object is referred to many times, code to look up the object is not generated each time, which can make things faster.



You can think of the example above as generating code equivalent to the following.

```
this.dic = %[];
{
	var anonymous_special_local_variable = this.dic;
	anonymous_special_local_variable.member = 1;
	this.dic = 0;
	anonymous_special_local_variable.member = 2;
}
```

In a with statement, the result of evaluating expression is assigned to an anonymous special local variable that can be accessed only through a . (dot) operator with its left-hand side omitted. From then on, a . (dot) operator with its left-hand side omitted refers to that "anonymous special local variable".

The scope in which the result of evaluating expression is held can be regarded as the same as the local variable scope of that "anonymous special local variable" (and the range affected by the with statement is the same).

## The . Operator Outside a with Statement

When the left-hand side of the `.` (dot) operator is omitted outside a with statement, it refers to the global object.

For example, writing



`.foo = 1;`



outside a with statement means the same as



`global.foo = 1;`
