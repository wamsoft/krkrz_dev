---
source_hash: ae1b57a3541d
---

# Style

## Style

In terms of style, TJS2 is a descendant of the C language. Unlike BASIC and similar languages, where a statement ends at a line break, TJS2 is basically "free-form".



However, unlike JavaScript, a statement cannot be terminated by a line break.

## Free-Form

Characters commonly called "**whitespace**", such as line breaks, spaces and tabs, can be inserted anywhere as long as they do not change the meaning. Conversely, they must be inserted where needed to keep the meaning clear.

```
(1)
	function func(a,b) { a++; return a+b; }

(2)
	function func(a,b) {
		a++;
		return a+b;
	}

(3)
	function func(a,b)
	{
		a++;
		return a+b;
	}

(4)
	function
	func
	(
	a
	,
	b
	)
	{
	a
	++
	;
	return
	a
	+
	b
	;
	}

(5)
	functionfunc(a,b){a++;returna+b;}

(6)
	f unction fu nc(a,b)
	{
		a+ +;

	ret urn a+b;
	}
```

(1) through (4) all mean the same thing. For readability, however, (2) or (3) is recommended.

(5) is written without spaces; the words run together and the code is not parsed correctly.

(6) has spaces where they must not be, so it causes an error.

## Comments

Text enclosed between `/*` and `*/` is treated as a comment and is ignored. Comments can be nested.

Likewise, everything after `//` on a line is treated as a comment.

```
	function example(a,b,c)
	{
		return a*b/c; // returns a*b/c
	}

	/*
		Comments can also be written like this
		/* Comments can be nested */
	*/
```
