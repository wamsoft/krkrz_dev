---
source_hash: 0d64eeb16ed5
---

# switch Statement

## switch Statement

The switch statement lets you write an if ... else if chain more concisely. It has the following syntax.

```
switch(base_expression)
{
**case** condition_expression1 :

case condition_expression2 :

:
:

**default**:

:
:
}
```

base_expression is an expression, and it is evaluated first. Each condition_expression? following a case inside the block after switch is also an expression.

The condition_expression? entries are evaluated one after another within the block. When a result equals base_expression, execution starts from there. Statements written before a matching condition_expression? are skipped. Once a match is found, subsequent case and default labels are ignored.

default: can be omitted. If default is present, the statements following default are executed when none of the condition_expression? entries match.

To leave the block, write **break**;. Forgetting break and running on into the next case is a common mistake, so be careful.

```
	switch(a)
	{
	case 0:
		inform("a is 0");
		break;
	case 1:
		inform("a is 1");
		break;
	case 2:
		inform("a is 2");
		break;
	default:
		inform("a is neither 0, 1 nor 2");
	}


	switch(a)
	{
	case 0:
	case 1: // no break, so case 0 falls through to here
		inform("a is 0 or 1");
		break;
	case 2:
		inform("a is 2");
	} // no default, so nothing is executed for values other than 0, 1 and 2


	switch(a)
	{
	case b+1: // an expression can follow case
		inform("a==b+1");
		break;
	case c+b:
		inform("a==c+b");
	}

	switch(str)
	{
	case "aiueo": // strings can be used too
		type=1;
		break;
	case "kakikukeko":
		type=2;
		break;
	}
```
