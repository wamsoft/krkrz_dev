---
source_hash: d1c4b56a59f9
---

# The tTJSVariant Type

## What is tTJSVariant

tTJSVariant is the type that holds the data of a "variable" in TJS2.

tTJSVariant has an internal type, so a single type can represent void (undefined), objects, integers, real numbers, strings, and octet strings.

It also handles conversions between these internal types automatically during operations.

## tTJSVariantType

An enumeration that represents the internal type of a tTJSVariant. It can be obtained with the tTJSVariant::**Type** method.

- ****tvtVoid****  
  The void type. A tTJSVariant constructed with the no-argument constructor has this type. It is not null.
- ****tvtObject****  
  The object type. null also has this internal type.
- ****tvtString****  
  The string type.
- ****tvtOctet****  
  The octet string type.
- ****tvtInteger****  
  The integer type. Holds a tTVInteger value.
- ****tvtReal****  
  The real number type. Holds a tTVReal value.

## Object references

Among the internal types, objects are managed with reference counting.

tTJSVariant manages reference counts automatically by itself, but note that it does not manage the reference count after you extract a pointer to an object through the methods that obtain an [iTJSDispatch2](interface.md) from a tTJSVariant, or through the methods that obtain a tTJSVariantClosure.

## Object type

**tTJSVariantClosure** is the type that holds an object inside a tTJSVariant. It holds two iTJSDispatch2 interfaces: one is the object itself, and the other carries the context in which the object runs.

tTJSVariantClosure has every method that the iTJSDispatch2 interface has. Accessing these methods through tTJSVariantClosure handles the execution context correctly.



There are two ways to extract a tTJSVariantClosure from a tTJSVariant: tTJSVariant::**AsObjectClosure** and tTJSVariant::**AsObjectClosureNoAddRef**. The former increments the object's reference count; the latter does not.

tTJSVariantClosure has no mechanism to manage reference counts automatically, so you need to take care of reference counting after extracting it from a tTJSVariant.

## String type

TJS2 strings are managed with reference counting; a simple copy only increments the string's reference count and does not duplicate the string itself.

tTJSVariantString is the type used by tTJSVariant and **tTJSString** to manage strings. You can extract a tTJSVariantString from a tTJSVariant with tTJSVariant::**AsString** (this method increments the reference count). However, tTJSVariantString itself has no mechanism to manage reference counts automatically, so use it with care.

tTJSString does manage reference counts, so converting to tTJSString is the easier route (tTJSVariant defines conversion operators to and from tTJSString).

## Octet string type

Like strings, TJS2 octet strings are managed with reference counting.

**tTJSVariantOctet** is the type that manages octet strings. Like tTJSVariantString and tTJSVariantClosure, it has no mechanism to manage reference counts, so be careful. You can extract a tTJSVariantOctet from a tTJSVariant with tTJSVariant::**AsOctet** (increments the reference count) or tTJSVariant::**AsOctetNoAddRef** (does not increment the reference count).

## Conversion

tTJSVariant defines a variety of conversion operators and constructors, so it can be used like a primitive type.

As noted above, take great care when converting to and from types managed by reference counting.

## Operations

Many operators are overloaded, so operations can be performed just as with primitive types. Any type conversions needed during an operation are handled automatically.
