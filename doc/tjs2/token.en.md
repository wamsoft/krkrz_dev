---
source_hash: 51d940a6276d
---

# Tokens

## Tokens

While a script is being parsed, it is broken down entirely into units called tokens, which are then processed.

Where one token ends and the next begins depends on the kind of token.

## Bare Words

A "bare word" is a sequence of certain characters written directly in a script, not quoted with `""` or `''`.

Bare words follow these rules.

- They consist of lowercase and uppercase letters, '`_`' (underscore), digits, and so-called full-width characters. However, a digit cannot come first.
- Everything up to the end of such a run is treated as one bare word.

```
	ampan  // OK
	123a // NG: starts with a digit
	_asdf // OK: an underscore can come first
	continue // this is a reserved word; OK
	全角文字 // so-called full-width characters are OK in a bare word
```

Bare words are further classified into reserved words and identifiers.

## Reserved Words

The following are reserved words, not identifiers. Every bare word that is not a reserved word is an identifier.



`
break  continue  const  catch  class  case

debugger  default  delete  do  extends  export

enum  else  function  finally  false  for

global  getter  goto  incontextof  Infinity

invalidate  instanceof  isvalid  import  int  in

if  NaN  null  new  octet  protected  property

private  public  return  real  synchronized  switch

static  setter  string  super  typeof  throw

this  true  try  void  var  while  with`




Each of these reserved words has a special meaning that plays an important role in the script syntax. Some of them are used as operators.

However, not all of these reserved words are used in the current version.

## Identifiers

"Identifiers" are all bare words that are not reserved words. They are used for names you can choose freely, such as variables, functions and class names.

An identifier that contains a reserved word is recognized as an identifier, not a reserved word, as long as it is not the reserved word itself.

## Symbols

Symbols are also broken out as tokens. The symbols are as follows.



`>>>=  >>>  >>=  >>  >=  >  <<=  <=

<->  <<  <  ===  ==  =>  =  !==  !=  !

&&=  &&  &=  &  ||=

||  |=  |  ...   .   ++  +=  +  -=  --  -  *=

*  /=  /  \=  \  %=  %  ^=  ^  [  ]  (  )  ~

?  :  ,  ;  {  }  #  $`



These are extracted as tokens by longest match. For example, `++` is broken out as the single symbol `++`, not as `+` and `+`. If you want to write them as separate `+` and `+`, you need to put a space or similar between them.



Each symbol has an important meaning as an element of the syntax. Some symbols are used as operators.

## Numeric Literals

A numeric literal starts with a digit or a `.` (decimal point). `TJS2` recognizes the following forms.

A number written normally is a decimal numeric literal.

```
	0
	3.1
	342.3
	1
```

For decimal numbers, you can also use `e` or `E` for an **exponent** in base 10. `e` and `E` mean the same thing.

```
	1e-3   // 1×10^-3 ( 0.001 )
	3.4e10   // 3.4×10^10
	9.3E-2  // 9.3×10^-2 ( 0.093 )
```

Prefixing a number with `0x` or `0X` makes it **hexadecimal**. `0x` and `0X` mean the same thing.

```
	0x1234
	0Xff
	0x3f33
```

Prefixing a number with `0b` or `0B` makes it **binary**.

```
	0b0100
	0B0010100010100001
```

A number starting with `0` is treated as **octal**.

```
	01234
	033
```

Hexadecimal, octal and binary numbers also support a fractional part and an exponent with p. p specifies an exponent in base 2.

```
	0b1.1    // 1 + 1/2, i.e. 1.5
	0x2.f    // 2 + 15/16, i.e. 2.9375
	0x1p8    // 1 × 2^8, i.e. 256.0
```

A numeric literal continues as one literal as long as the characters are valid numeric literal characters.

## String Literals

A string literal is enclosed in `""` (double quotes) or `''` (single quotes). You can use either double quotes or single quotes.

Inside `""` (double quotes), ' (a single quote) does not need to be escaped with `\`, and inside `''` (single quotes), `"` (a double quote) does not need to be escaped.

```
	"this is a string."
	'this is also a string.'
	"Can't use without a quotation."
```

Inside a string, `**\**` (backslash; shown as a yen sign in some Japanese fonts) has a special meaning. Its meaning depends on the character that follows. Writing a special sequence after \ is called **escaping**.

```
\\    : the \ mark itself
\'    : ' (single quote)
\"    : " (double quote)
\a    : BEL (audible bell)
\b    : BS (backspace)
\f    : FF (form feed)
\n    : LF (line feed)
\r    : CR (carriage return)

\t    : HT (horizontal tab)
\v    : VT (vertical tab)
\xH   : H = hexadecimal number (H is the character code)
\XH   : same as above
```

In the `\xH` form, H is a hexadecimal number. That number is treated as a character code and replaced with that single character.

```
	'Can\'t help'  ( uses \' )
	"\x1234"     ( the character with code 0x1234 as a wide character )
```

In the `\xH` form, as long as the characters following \x are valid hexadecimal digits (0-9, A-F, a-f), they are considered part of H. However, at most 4 digits are recognized in environments where a wide character is 16 bits, and at most 8 digits on 32-bit machines (16 bits on Windows, 32 bits on Linux and Solaris).

If you write `"\x22An Apple"`, the beginning is taken as \x22A. To avoid this, split the string and write the parts consecutively, as in `"\x22" "An Apple"`. In TJS, consecutive string literals like this are treated as a single string.



For strings, see also [Strings](string.md).

## @-Prefixed String Literals

If you put @ before a string literal, the parts of that literal between & and ;, or between ${ and }, are treated as expressions, and the results of evaluating them are expanded in place (if you write an expression between & and ; or between ${ and }, its result is embedded there).

If you do not want & or $ to be expanded, put \ before the & or $.

```
	@"1+2=&1+2;"  ( becomes the string "1+2=3" )
	@"The value of variable f is &f;"  ( expands the value of variable f at &f; )
	@"The result of calling function func is &func();"  ( anything valid as an expression can go between & and ; )
	@"The result of calling function func is ${func()}"  ( same as above )
	@"true \&\& false is &true && false;"  ( writing \ before & prevents & from being expanded )
```

Expressions written here can access variables and so on (including local variables) that are accessible from the place where the string is written.

## Octet Literals

An octet literal is enclosed in `<%` and `%>`, and octet data (binary data) can be written inside it.

The data consists of two-digit hexadecimal numbers separated by spaces or similar.

```
	<% 00 01 02 03 %>
	<% ff ff ff 00 04 0f ff 30 %>
```

For octet sequences, see also [Octet Sequences](octet.md).

## Regular Expression Patterns

A regular expression pattern is enclosed between `/` and `/`, and a regular expression can be written inside it.

Flag characters can follow the pattern: g is the global search flag (match everything found; without this flag only the first match is used), i is the case-insensitive flag, and l is the flag for using localized collation.

A regular expression pattern written this way is treated as an object of the RegExp class.

```
	/[0-9]-[0-9]-[0-9]/
	/^;\s*(.*?)\s*=(.*)$/
	/start(.*?)end/gi
```

For regular expression patterns, see also [RegExp class](regexp.md).
