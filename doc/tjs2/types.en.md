---
source_hash: d9162eb05fad
---

# Data Types

## Data Types

In TJS2, variables have no "type", but values have types internally. Rather than having no types, TJS2 handles types automatically and dynamically.

The internal types are `void`, integer, real, string, object, and octet.

## void

void represents nothing (its meaning differs from JavaScript). A freshly declared variable is `void`.

To compare `void` values, use the `===` (identity) operator.

The `**typeof**` operator returns `"void"` for it.

## Integer

TJS2 handles integers with 64-bit precision. Integers are normally treated as **signed integers**; the only exception is the `**>>>**` operator, which treats its left operand as an **unsigned integer**.

The typeof operator returns `"**Integer**"` for it.

## Real

TJS2 handles real numbers with 64-bit precision (**double precision**).

The typeof operator returns `"**Real**"` for it.

## String

TJS2 handles zero-terminated strings of unlimited length. "Zero-terminated" means strings are handled on the assumption that a string ends at `\0`.

The internal character encoding is **UTF-16LE**, stored as a fixed 16 bits per character. Characters outside the BMP are represented as **surrogate pairs**.

The typeof operator returns `"**String**"` for it.

For the list of methods and properties available on strings, see [Strings](string.md).

## Object

The object type holds an object. Besides objects allocated with the `new` operator, functions, classes, property objects and so on are all of the object type.

The `typeof` operator returns `"**Object**"` for it.



Unlike TJS and JavaScript, the TJS2 object type internally holds two pointers: one to the object itself, and one to the object that serves as the context in which it should be used. This enables so-called closures. The `incontextof` operator changes this context part.

The following classes in particular have dedicated literal notations in TJS2 syntax and appear frequently.

- **Arrays** ([Array class](array.md)) — an ordered sequence of elements. Writing `[ ... ]` in an expression creates one on the spot.
- **Dictionaries** ([Dictionary class](dictionary.md)) — a mapping from string keys to values. Writing `%[ ... ]` in an expression creates one on the spot.
- **Regular expression patterns** ([RegExp class](regexp.md)) — patterns for matching and replacing strings. They can be written as literals in the form `/.../`.

## Octet

The octet type handles a sequence of 8-bit data (an octet sequence). It is mainly used for **binary data**.

The `typeof` operator returns `"**Octet**"` for it.

For the list of methods and properties available on octet sequences, see [Octet Sequences](octet.md).
