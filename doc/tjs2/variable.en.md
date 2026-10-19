---
source_hash: fd094e945617
---

# Variables

## Variables

Variables in TJS2 are declared with the **var** keyword. In TJS2, a variable cannot be used unless it has been declared.

The form of the var keyword is as follows.

```
　var variable_name;
```

You can specify several variable names separated by **,** (commas). If a variable needs an initial value, use the form

```
　var variable_name = initial_value;
```

to assign an initial value to the variable.

```
	var variable=0;
	var var2=variable+2;
	var var3="this is var3.";
	var var1,var2,var3;
	var a=0,b=1,c=3;
```

You do not need to specify a type when declaring a variable. It takes on the type of whatever is assigned to it. Types are also converted automatically during calculations and depending on context.

## Variable Names

Any identifier is valid as a variable name.

```
	var ampan;
	var 123a;  // NG: starts with a digit
	var function; // NG: function is a reserved word
	var function1; // OK: contains a reserved word but is not the reserved word itself
	var 変数その一; // so-called full-width (Japanese) characters can also be used
```

## Declaring a Variable Twice

Declaring a variable with the same name more than once does not cause an error. However, if an initial value is given in a second or later declaration, that initial value is assigned to the variable. If no initial value is given in a second or later declaration, the variable becomes void.

```
	var a=0;
	var a; // second declaration (no error; a becomes void)
	var a=-1; // third declaration (no error; -1 is assigned to a)
```

## Variable Scope

A variable declared inside a part enclosed in {  } (a block) is valid only within that block; that is, it is a **local variable**.

Also, unlike C, there is no restriction on where variables can be declared.

```
	while(t--)
	{
		var ratio=t/all; // declare variable 'ratio'
		setRatio(ratio);
	}

	// by the time control reaches here, 'ratio' has been removed

	var test; // variables can be declared here too
```

When a variable with the same name as a variable outside the block is declared inside the block, only the newly declared variable can be accessed within that block.

```
	var ratio=0;
	if(flag)
	{
		var ratio; // same name as a variable declared outside the block

		ratio=buf.position / buf.totalTime; // only the ratio inside the block can be accessed
		setRatio(ratio);
	}

	// leaving the block removes the inner ratio, but the outer ratio is unchanged
	ratio=-1;
```

> **Note:**
> A variable declared with var outside every scope (this is called the global scope) becomes a member of the global object.
