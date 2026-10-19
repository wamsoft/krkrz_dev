---
source_hash: ccf30e8e9339
---

# while Statement

## while Statement

The **while** statement repeatedly executes a statement or block while a given condition is true. It is used to create loops.

The syntax is as follows.

```
while(expression)
	statement or block
```

The "statement or block" is executed repeatedly as long as the condition expression is true.



The behavior is as follows:

(1) First, evaluate expression; if it is false, the statement or block is not executed

(2) Execute the statement or block

(3) Evaluate expression; if the result is true, go to (2), otherwise the while statement ends



In other words, if expression is false from the start, the statement or block is never executed. Also, expression is not evaluated continuously; its truth is checked once each time the statement or block has been executed.

At step (3), if the body is a block, execution leaves the block once (meaning its variables and so on are discarded).

```
	while(func()) ;
	/* keep evaluating func() and do nothing while func() is true */

	while(func()) i++;
	/* keep executing i++ while func() is true */

	while(i < 5) // while i is less than 5
	{
		func(i);
		i++;
	}
```

## break

Use the break statement to end a while loop partway through.

```
	while(true) // infinite loop unless break is executed
	{
		if(func()) break; // end the while loop if func() is true
		func2(); // reached if break above was not executed
	}
	// execution comes here once break is executed
```

## continue

Use the continue statement to restart from the evaluation of the condition partway through.

When continue is executed, execution moves to (3).

```
	var i = 0;
	while(i < 5)
	{
		if(func1()) continue;
		// if func1() is true, the condition i < 5 is checked, and if it is true,
		// execution resumes from the top of the block
		func2();
		i++;
	}
```

## do～while

The do～while statement is the same as the while statement, except that the condition is not checked first.

The syntax is as follows.

```
do
	statement or block
while(expression);
```

Because the condition is not checked first, the "statement or block" is executed even if the condition is false at the do.

Once the "statement or block" has been executed, the condition is checked; if it is false, the loop exits, and if it is true, the statement or block is executed again, and so on.
