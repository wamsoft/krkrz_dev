---
source_hash: 574ead5a8817
---

# RegExp Class

## RegExp class

The RegExp class handles **regular expression patterns**.

Perl-compatible patterns can be used.

It resembles JavaScript's RegExp class, but compatibility is limited.



The constructor syntax is as follows.

```
new RegExp(<パターン文字列>, <フラグ文字列=''>);
```

The first argument (pattern string) is the regular expression pattern. Note that a \ in the pattern must be written as \\ inside a string literal.

The second argument (flag string, default '') is a combination of the characters g, i, and l.

g is the global search flag. With this flag, the match, exec, and replace methods process every part of the string that matches the pattern.

The i flag makes matching case-insensitive for letters.

The l flag enables locale-aware collation.

```
	var re = new RegExp("[a-z]+[0-9]*", "gi");
	var re = new RegExp("\\.\\.\\."); // /\.\.\./ ( ... にマッチさせたい )
```

## Regular expression patterns

A regular expression pattern can also be written between / and /. See "Regular Expression Patterns" in [Tokens](token.md).

## compile

The compile method sets a new regular expression pattern on the regular expression object.

Its arguments are the same as the RegExp constructor's.

## test

The test method returns whether the given string matches the pattern.

```
構文 : test(<文字列>)
```

Returns true if the string matches the pattern, and false otherwise.

This method updates the values of this object's properties.

## exec

The exec method performs regular expression matching on the given string and returns an array containing the match results.

```
構文 : exec(<文字列>)
```

If the pattern does not match, the array has 0 elements.

If it matches, element 0 (the first element) holds the entire matched part, and the following elements hold each captured part (the parts enclosed in ( ) in the pattern).

This method updates the values of this object's properties.

## match

The match method is the same as exec, except that it does not update this object's properties.

```
構文 : match(<文字列>)
```

## replace

The replace method performs string replacement and returns the resulting string.

```
構文 : replace(<対象文字列>, <置き換え文字列>)
```

It matches against the target string (first argument), replaces the matched parts with the replacement string (second argument), and returns the resulting string.

If you pass a function instead of a string as the replacement, that function is called to perform each replacement. The function takes one argument: an array object representing the matched part of the target string (see the [exec](#exec) method for this array). The matched part of the target string is replaced with the string the function returns.

This method ignores the start property.

## split

The split method splits the target string at the places that match the regular expression pattern.

```
構文 : split(<対象文字列>, <(予約)>, <空の要素を無視するか=false>)
```

Returns an array object containing the result of splitting the string. The second argument is reserved.

If the pattern contains capture groups ( `(...)` ), the substrings captured by each match are stored in the array in order, right after the segment preceding that match (the same behavior as JavaScript's String.split and Kirikiri 2). Groups that did not participate in the match are stored as empty strings.

If the third argument is true, empty elements (both segments and capture groups) are removed from the result (default false).

See also the [split](string.md#split) method of the String class.

## matches

The matches property is a read-only property holding an array of the matched parts.

If the pattern does not match, the array has 0 elements.

If it matches, element 0 (the first element) holds the entire matched part, and the following elements hold each captured part (the parts enclosed in ( ) in the pattern).

## start

A property that holds the position at which the search starts. It can also be set.

## index

A read-only property that holds the position of the first character of the matched part. Positions start at 0, so it is 0 if the match begins at the first character of the target string.

## lastIndex

A read-only property that holds the position of the character following the last character of the matched part. Positions start at 0.

## input

A read-only property that holds the target string of the match.

## leftContext

A read-only property that holds the part of the target string to the left of the matched part.

## rightContext

A read-only property that holds the part of the target string to the right of the matched part.

## lastMatch

Represents the matched string. Same as matches[0].

## lastParen

Returns the last of the matched parts. Same as matches[matches.count-1].

## RegExp.last

The RegExp instance on which test or exec was most recently executed.

```
例 : if(/pat(\d+)/.test(target)) { return RegExp.last.matches[1]; }
```

## Copyright notice

The regular expression feature is implemented with John Maddock's [Regex++](http://ourworld.compuserve.com/homepages/John_Maddock/regexpp.htm). Many thanks to him for publishing such a useful library.



Copyright (c) 1998-2001



Dr John Maddock



Permission to use, copy, modify, distribute and sell this software and its documentation for any purpose is hereby granted without fee, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation. Dr John Maddock makes no representations about the suitability of this software for any purpose. It is provided "as is" without express or implied warranty.
