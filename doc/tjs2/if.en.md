---
source_hash: c79610bd4961
---

# if Statement

## if Statement

The if statement decides whether to execute part of a script based on a condition, as in "if X, then do Y".

The syntax is as follows.

```
if(expression)
	statement or block
else
	statement or block
```

The first "statement or block" is executed when expression evaluates to true, and the second "statement or block" is executed when it evaluates to false. The **else** part can be omitted if it is not needed.

```
	if(a==b)
		inform("a and b are equal");

	if(a<b)
	{
		var t;
		t=a; a=b; b=t; // swap a and b
	}

	if(a==b)
		inform("a and b are equal");
	else
		inform("a and b are different");
```

## Matching if and else

An else follows the rule "it pairs with the nearest preceding if that does not yet have an else".



For example, if you write

```
	if(expr) // ★
		if(expr) // ●
			statement;
		else // ●
			statement;
	else // ★
		statement;
```

the else marked ★ pairs with the if marked ★, and the else marked ● pairs with the if marked ●.

Be careful: in a free-form language like TJS2, even if you get the indentation wrong and write

```
	if(expr) // ★
		if(expr) // ●
			statement;
	else // ●
		statement;
```

the pairing is still as described above.

If you want to make the pairing explicit, enclose the inner part in a block, like this:

```
	if(expr) { // ★
		if(expr) // ●
			statement;
	}
	else // ★
		statement;
```
