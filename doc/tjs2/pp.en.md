---
source_hash: 53661e42f7e3
---

# Preprocessor

## Preprocessor

TJS2 can process **conditional compilation expressions** (the equivalent of C's #if and #endif). These are processed before the script is actually parsed, and can be used to exclude or include parts of the script depending on conditions.

Unlike C preprocessor directives, conditional compilation expressions are free-form and can be written anywhere. There is no requirement, as with C directives, to write only one directive per line.

## @set Directive

The @set directive evaluates a conditional compilation expression and discards the result. The syntax is as follows.

```
	@set(expression)
```

"expression" is a conditional compilation expression. The following operators can be used in it.

```
	,  =  !=  ==  ||  &&  |  ^  &  <  >  <=  >=  +  -  %  *  /  !  +  -  ( )
```

For the meaning of these operators, see [Expressions and Operators](expr_and_op.md). However, the only data type that can be handled is integer.

You can also use arbitrary variables and immediate values. Variable names follow the same naming rules as TJS2 [variables](variable.md), and immediate values the same rules as the immediate values in [Tokens](token.md).

However, variables used in the preprocessor and variables used in TJS2 scripts do not interfere with each other (they do not share the same namespace).

## @if and @endif Directives

The @if directive evaluates a conditional compilation expression; if the result is 0, everything up to the next @endif is not parsed. If the result is nonzero, it is parsed.

The syntax is as follows.

```
	@if(expression)              ...         @endif
```

"expression" is a conditional compilation expression. @if ... @endif can be nested.

```
	@if(flag==0)  // a variable that has not been assigned anything is treated as 0
		@set(flag=1)
		****
	@endif
	// ↑ makes the script written in the **** part compile only once

	@if(version>=0x02040009)
		@if(flag)
			****
		@endif
	@endif
	// ↑ compiles the **** part only when version is 0x02040009 (2.4.9) or later and flag is nonzero
```

## Predefined Variables

The **version** variable represents the current TJS2 version.



It is a number in the hexadecimal form 0x0XYYZZZZ, where X is the major version, YY is the minor version, and ZZZZ is the release number. For example, 0x02040009 means version 2.4.9.
