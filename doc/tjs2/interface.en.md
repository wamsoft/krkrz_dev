---
source_hash: afc2e564d15a
---

# The iTJSDispatch2 Interface

## What is iTJSDispatch2

iTJSDispatch2 is an abstract base class that provides the interface to "objects" in TJS2.

"Objects" in TJS2 include function objects, classes, property objects, arrays (and dictionary arrays), and so on.

Almost every operation on TJS2 can be performed through this interface.



The following describes the interface from the caller's point of view.

## Calling by ordinal

Some iTJSDispatch2 methods have names ending in ByNum. These call by ordinal; for example, calling FuncCall with the member name "23" is equivalent to calling FuncCallByNum with the ordinal 23.

This is handy when accessing array objects.



A method ending in ByNum lacks the membername and hint arguments of the method with the same name without ByNum, and instead has tjs_int num. The num argument specifies the ordinal.



Detailed descriptions of the methods that call by ordinal are omitted below (see the method with the same name without ByNum).

## AddRef

tjs_uint iTJSDispatch2::AddRef(void)



Increments the object's reference count.

Every TJS2 object is managed by reference counting.

The return value is the reference count after incrementing, but relying on this value is not recommended.

## Release

tjs_uint iTJSDispatch2::Release(void)



Decrements the object's reference count.

The return value is the reference count after decrementing; 0 means the object has been freed. However, relying on this value is not recommended.

## FuncCall

tjs_error iTJSDispatch2::FuncCall(

tjs_uint32 flag,

const tjs_char * membername,

tjs_uint32 *hint,

tTJSVariant *result,

tjs_int numparams,

tTJSVariant **param,

iTJSDispatch2 *objthis

)



Calls a function.



The arguments are as follows.

- **tjs_uint32 flag**  
  Call flags (see below).
- **const tjs_char * membername**  
  The name of the member to operate on.
  
  If NULL, the operation applies to this object itself. In that case, this object must be able to act as a function.
- **tjs_uint32 *hint**  
  The storage for a variable that holds a "**hint**". May be NULL.
  
  A hint speeds up the second and later lookups of the same member name. If you pass a pointer to a tjs_uint32 variable as hint, a number serving as the hint is written there, and later lookups use that number as a reference when searching for the member. Since it is only a reference, the initial value of the hint can be anything (0 is recommended). Because of how this works, it is more efficient when hints and member names correspond one-to-one (tTJSString has a built-in mechanism for this hint).
  
  Some objects may not have a mechanism that uses hints.
- **tTJSVariant *result**  
  A pointer to a tTJSVariant that receives the result of the function call.
  
  May be NULL if the result is not needed.
- **tjs_int numparams**  
  The number of arguments to pass to the function.
- **tTJSVariant **param**  
  An array of pointers to the arguments to pass to the function. May be NULL if there are no arguments.
- **iTJSDispatch2 *objthis**  
  The context (this object) in which the function runs.

## FuncCallByNum

tjs_error iTJSDispatch2::FuncCall(

tjs_uint32 flag,

tjs_int num,

tTJSVariant *result,

tjs_int numparams,

tTJSVariant **param,

iTJSDispatch2 *objthis

)



Calls a function by ordinal.

## PropGet

tjs_error iTJSDispatch2::PropGet(

tjs_uint32 flag,

const tjs_char * membername,

tjs_uint32 *hint,

tTJSVariant *result,

iTJSDispatch2 *objthis

)



Gets the value of a property or member variable.



The arguments are as follows.

- **tjs_uint32 flag**  
  Call flags (see below).
- **const tjs_char * membername**  
  The name of the member to operate on.
  
  
  
  If NULL, the operation applies to this object itself. In that case, this object must support property get.
  
  An object for which this succeeds even when the argument is NULL is regarded as a property object. Normally, when such a property object is a member of another object, the result of calling PropGet on the property object is used instead of the property object itself. This behavior can be bypassed by specifying TJS_IGNOREPROP in the call flags.
- **tjs_uint32 *hint**  
  The storage for a variable that holds the hint. May be NULL.
  
  See FuncCall for a description of hints.
- **tTJSVariant *result**  
  A pointer to a tTJSVariant that receives the result. NULL is not allowed.
- **iTJSDispatch2 *objthis**  
  The context (this object) in which this method runs.

## PropGetByNum

tjs_error iTJSDispatch2::PropGetByNum(

tjs_uint32 flag,

tjs_int num,

tTJSVariant *result,

iTJSDispatch2 *objthis

)



Gets the value of a property or member variable by ordinal.

## PropSet

tjs_error iTJSDispatch2::PropSet(

tjs_uint32 flag,

const tjs_char *membername,

tjs_uint32 *hint,

const tTJSVariant *param,

iTJSDispatch2 *objthis

)



Sets the value of a property or member variable.



The arguments are as follows.

- **tjs_uint32 flag**  
  Call flags (see below).
- **const tjs_char * membername**  
  The name of the member to operate on.
  
  
  
  If NULL, the operation applies to this object itself. In that case, this object must support property set.
  
  An object for which this succeeds even when the argument is NULL is regarded as a property object. Normally, when such a property object is a member of another object, PropSet is called on the property object rather than replacing the property object itself. This behavior can be bypassed by specifying TJS_IGNOREPROP in the call flags.
- **tjs_uint32 *hint**  
  The storage for a variable that holds the hint. May be NULL.
  
  See FuncCall for a description of hints.
- **const tTJSVariant *param**  
  A pointer to a tTJSVariant holding the value to set. NULL is not allowed.
- **iTJSDispatch2 *objthis**  
  The context (this object) in which this method runs.

## PropSetByVS

tjs_error iTJSDispatch2::PropSetByVS(

tjs_uint32 flag,

tTJSVariantString *membername,

const tTJSVariant *param,

iTJSDispatch2 *objthis

)



Sets the value of a property or member variable. Unlike PropSet, the member name is referenced through a tTJSVariantString. This is used internally. Because tTJSVariantString lets multiple string objects share the same string memory, setting properties (creating members in an object) through this method avoids increasing the memory used for member-name strings.

If you do not implement this method, return TJS_E_NOTIMPL; PropSet is used instead. Conversely, when calling this method returns TJS_E_NOTIMPL, your code should fall back to PropSet.

## PropSetByNum

tjs_error iTJSDispatch2::PropSetByNum(

tjs_uint32 flag,

tjs_int num,

const tTJSVariant *param,

iTJSDispatch2 *objthis

)



Sets the value of a property or member variable by ordinal.

## GetCount

tjs_error iTJSDispatch2::GetCount(

tjs_int *result,

const tjs_char *membername,

tjs_uint32 *hint,

iTJSDispatch2 *objthis

)



Returns the number of members the object holds.



The arguments are as follows.

- **tjs_int *result**  
  A pointer to a variable that receives the result. NULL is not allowed.
- **const tjs_char * membername**  
  The name of the target member.
  
  If NULL, the number of members held by this object itself is returned.
  
  If a member name is given and that member is an object, the number of members held by that object is returned. Fails if the specified member is not of object type.
- **tjs_uint32 *hint**  
  The storage for a variable that holds the hint. May be NULL.
  
  See FuncCall for a description of hints.
- **iTJSDispatch2 *objthis**  
  The context (this object) in which this method runs.
  
  This argument normally has no meaning (it is ignored).

## GetCountByNum

tjs_error iTJSDispatch2::GetCount(

tjs_int *result,

tjs_int num,

iTJSDispatch2 *objthis

)



The ordinal version of GetCount.

## DeleteMember

tjs_error iTJSDispatch2::DeleteMember(

tjs_uint32 flag,

const tjs_char *membername,

tjs_uint32 *hint,

iTJSDispatch2 *objthis

)



Deletes a member.



The arguments are as follows.

- **tjs_uint32 flag**  
  Call flags (see below).
- **const tjs_char * membername**  
  The name of the target member. NULL is not allowed.
- **tjs_uint32 *hint**  
  The storage for a variable that holds the hint. May be NULL.
  
  See FuncCall for a description of hints.
- **iTJSDispatch2 *objthis**  
  The context (this object) in which this method runs.
  
  This argument normally has no meaning (it is ignored).

## DeleteMemberByNum

tjs_error iTJSDispatch2::DeleteMemberByNum(

tjs_uint32 flag,

tjs_int num,

iTJSDispatch2 *objthis

)



Deletes a member by ordinal.

## EnumMembers

tjs_error iTJSDispatch2::EnumMembers(

tjs_uint32 flag,

tTJSVariantClosure *callback,

iTJSDispatch2 *objthis

)



Enumerates the members in the object.

callback specifies a callback function. In the current version, behavior is not guaranteed if members of this object are created or deleted inside the callback.



The arguments are as follows.

- **tjs_uint32 flag**  
  Call flags. Specify a bitwise OR of the flags below, or 0 (zero).
  
  - **TJS_IGNOREPROP**  
    Disables property access. When enumerating members together with their values, with this flag a member that is a property yields the property object itself. Without this flag, the value obtained through the property object is returned.
  - **TJS_ENUM_NO_VALUE**  
    Does not get values. With this flag, two arguments are passed to the callback function; otherwise, three.
- **tTJSVariantClosure *callback**  
  The callback function.
  
  callback->FuncCall is called once for each member.
  
  The function receives two arguments (if TJS_ENUM_NO_VALUE is specified) or three (if it is not).
  
  - The first argument is a string: the member name
  - The second argument is an integer: the member's flags, which are a bitwise OR of TJS_HIDDENMEMBER and TJS_STATICMEMBER, or 0
  - The third argument exists only if TJS_ENUM_NO_VALUE is not specified, and holds the member's value
- **iTJSDispatch2 *objthis**  
  The context (this object) in which this method runs.
  
  When the TJS_IGNOREPROP flag is not specified, this argument is the default context in which property objects run.

## Invalidate

tjs_error iTJSDispatch2::Invalidate(

tjs_uint32 flag,

const tjs_char *membername,

tjs_uint32 *hint,

iTJSDispatch2 *objthis

)



Invalidates an object.



The arguments are as follows.

- **tjs_uint32 flag**  
  Call flags (see below).
- **const tjs_char * membername**  
  The name of the target member.
  
  If NULL, this object itself is invalidated.
  
  If a member name is given and that member is an object, that object is invalidated. Fails if the specified member is not of object type.
- **tjs_uint32 *hint**  
  The storage for a variable that holds the hint. May be NULL.
  
  See FuncCall for a description of hints.
- **iTJSDispatch2 *objthis**  
  The context (this object) in which this method runs.
  
  This argument normally has no meaning (it is ignored).

## InvalidateByNum

tjs_error iTJSDispatch2::InvalidateByNum(

tjs_uint32 flag,

tjs_int num,

iTJSDispatch2 *objthis

)



Invalidates by ordinal.

## IsValid

tjs_error iTJSDispatch2::IsValid(

tjs_uint32 flag,

const tjs_char *membername,

tjs_uint32 *hint,

iTJSDispatch2 *objthis

)



Checks whether an object is valid.

Returns TJS_S_TRUE if valid and TJS_S_FALSE if invalid.



The arguments are as follows.

- **tjs_uint32 flag**  
  Call flags (see below).
- **const tjs_char * membername**  
  The name of the target member.
  
  If NULL, the validity of this object itself is checked.
  
  If a member name is given and that member is an object, the validity of that object is checked. Fails if the specified member is not of object type.
- **tjs_uint32 *hint**  
  The storage for a variable that holds the hint. May be NULL.
  
  See FuncCall for a description of hints.
- **iTJSDispatch2 *objthis**  
  The context (this object) in which this method runs.
  
  This argument normally has no meaning (it is ignored).

## IsValidByNum

tjs_error iTJSDispatch2::IsValidByNum(

tjs_uint32 flag,

tjs_int num,

iTJSDispatch2 *objthis

)



Checks whether an object is valid, by ordinal.

## CreateNew

tjs_error iTJSDispatch2::CreateNew(

tjs_uint32 flag,

const tjs_char * membername,

tjs_uint32 *hint,

iTJSDispatch2 **result,

tjs_int numparams,

tTJSVariant **param,

iTJSDispatch2 *objthis

)



Creates a new object.

Like the FuncCall method, this method can pass arguments for creating the new object.

So-called "class objects", which serve as templates for objects, must implement this method.



The arguments are as follows.

- **tjs_uint32 flag**  
  Call flags (see below).
- **const tjs_char * membername**  
  The name of the member to operate on.
  
  If NULL, the operation applies to this object itself. In that case, this object must be able to create new objects.
- **tjs_uint32 *hint**  
  The storage for a variable that holds the hint. May be NULL.
  
  See FuncCall for a description of hints.
- **iTJSDispatch2 **result**  
  A pointer to an iTJSDispatch * that receives the newly created object. NULL is not allowed.
- **tjs_int numparams**  
  The number of arguments to pass when creating the object.
- **tTJSVariant **param**  
  An array of pointers to the arguments to pass when creating the object. May be NULL if there are no arguments.
- **iTJSDispatch2 *objthis**  
  The context (this object) used when creating the object.

## CreateNewByNum

tjs_error iTJSDispatch2::CreateNew(

tjs_uint32 flag,

tjs_int num,

iTJSDispatch2 **result,

tjs_int numparams,

tTJSVariant **param,

iTJSDispatch2 *objthis

)



Creates a new object by ordinal.

## IsInstanceOf

tjs_error iTJSDispatch2::IsInstanceOf(

tjs_uint32 flag,

const tjs_char * membername,

tjs_uint32 *hint,

const tjs_char * classname,

iTJSDispatch2 *objthis

)



Checks whether an object is an instance of a particular class.

The class name is passed as a string in the classname argument.

Used by the TJS2 instanceof operator.

On success, returns TJS_S_TRUE if the object is an instance of the specified class, and TJS_S_FALSE otherwise.



The arguments are as follows.

- **tjs_uint32 flag**  
  Call flags (see below).
- **const tjs_char * membername**  
  The name of the member to check.
  
  If NULL, checks whether this object itself is an instance of the specified class.
- **tjs_uint32 *hint**  
  The storage for a variable that holds the hint. May be NULL.
  
  See FuncCall for a description of hints.
- **const tjs_char *classname**  
  The class name as a string.
- **iTJSDispatch2 *objthis**  
  The context (this object) in which this method runs.

## IsInstanceOfByNum

tjs_error iTJSDispatch2::IsInstanceOfByNum(

tjs_uint32 flag,

tjs_int num,

const tjs_char * classname,

iTJSDispatch2 *objthis

)



Checks whether an object is an instance of a particular class, by ordinal.

## Operation

tjs_error iTJSDispatch2::Operation(

tjs_uint32 flag,

const tjs_char *membername,

tjs_uint32 *hint,

tTJSVariant *result,

const tTJSVariant *param,

iTJSDispatch2 *objthis

)



Performs an operation on a member. The kind of operation is specified in flag.



The arguments are as follows.

- **tjs_uint32 flag**  
  Call flags. In addition to the ordinary call flags below, one of the following flags must be ORed in to specify the kind of operation.
  
  
  
  In this description, v is the member's value and p is the parameter passed in the param argument.
  
  - **TJS_OP_BAND**  
    Bitwise AND
    
    v &= p
  - **TJS_OP_BOR**  
    Bitwise OR
    
    v |= p
  - **TJS_OP_BXOR**  
    Bitwise XOR
    
    v ^= p
  - **TJS_OP_SUB**  
    Subtraction
    
    v -= p
  - **TJS_OP_ADD**  
    Addition
    
    v += p
  - **TJS_OP_MOD**  
    Modulo
    
    v %= p
  - **TJS_OP_DIV**  
    Real division
    
    v /= p
  - **TJS_OP_IDIV**  
    Integer division
    
    v \= p
  - **TJS_OP_MUL**  
    Multiplication
    
    v *= p
  - **TJS_OP_LOR**  
    Logical OR
    
    v = v || p
  - **TJS_OP_LAND**  
    Logical AND
    
    v = v && p
  - **TJS_OP_SAR**  
    Arithmetic right shift
    
    v >>= p
  - **TJS_OP_SAL**  
    Arithmetic left shift
    
    v <<= p
  - **TJS_OP_SR**  
    Logical right shift (unsigned right shift)
    
    v >>>= p
  - **TJS_OP_INC**  
    Increment
    
    v++
    
    The param argument is ignored
  - **TJS_OP_DEC**  
    Decrement
    
    v--
    
    The param argument is ignored
- **const tjs_char * membername**  
  The name of the member to operate on. NULL is not allowed.
- **tjs_uint32 *hint**  
  The storage for a variable that holds the hint. May be NULL.
  
  See FuncCall for a description of hints.
- **tTJSVariant *result**  
  A pointer to a tTJSVariant variable that receives the result of the operation. May be NULL.
- **tTJSVariant *param**  
  The parameter of the operation. May be NULL when the operation is TJS_OP_INC or TJS_OP_DEC.
- **iTJSDispatch2 *objthis**  
  The context in which the operation runs; usually ignored.

## OperationByNum

tjs_error iTJSDispatch2::OperationByNum(

tjs_uint32 flag,

tjs_int num,

tTJSVariant *result,

const tTJSVariant *param,

iTJSDispatch2 *objthis

)



Performs an operation on a member, by ordinal.

## NativeInstanceSupport

tjs_error iTJSDispatch2::NativeInstanceSupport(

tjs_uint32 flag,

tjs_int32 classid,

iTJSNativeInstance **pointer

)



Associates a native-code instance with an object, or retrieves a native-code instance from an object.



The arguments are as follows.

- **tjs_uint32 flag**  
  Call flags.
  
  Must be one of the following values.
  
  - ****TJS_NIS_REGISTER****  
    Registers the native-code instance given by *pointer. classid identifies the native-code class.
  - ****TJS_NIS_GETINSTANCE****  
    Writes the native-code instance with the class ID given by classid to *pointer.
- **tjs_int32 classid**  
  The class ID of the native code.
  
  Native-code class IDs can be managed with TJSRegisterNativeClass,
  TJSFindNativeClassID
  and TJSFindNativeClassName, but normally this is handled automatically by the helper code for writing native code
  (in tjsNative.cpp/tjsNative.h).
- **iTJSNativeInstance **pointer**  
  A pointer to an iTJSNativeInstance * variable used to pass or receive the native-code instance.

## ClassInstanceInfo

tjs_error iTJSDispatch2::ClassInstanceInfo(

tjs_uint32 flag,

tjs_uint num,

tTJSVariant *value

)



Manipulates the class instance information used by the IsInstanceOf method.

You can add class names to identify which classes an object is an instance of, or enumerate the classes to find out which classes it is an instance of.



The arguments are as follows.

- **tjs_uint32 flag**  
  Call flags. Specify one of the following.
  
  - ****TJS_CII_ADD****  
    Adds instance information.
    
    Pass in value a pointer to a tTJSVariant variable holding the class name (a string).
    
    The num argument is ignored.
  - ****TJS_CII_GET****  
    Gets instance information.
    
    Specify a 0-based integer in num. If num exceeds the number of registered entries, TJS_E_FAIL is returned.
    
    Pass in value a pointer to a tTJSVariant variable that receives the class name.
- **tjs_uint num**  
  The ordinal used when flag is TJS_CII_GET.
- **tTJSVariant *value**  
  When flag is TJS_CII_ADD, pass a pointer to a tTJSVariant variable holding the class name.
  
  When flag is TJS_CII_GET, pass a pointer to a tTJSVariant variable that receives the class name.

## Call flags

The call flags.

You can specify a bitwise OR of the following values.

- **TJS_MEMBERENSURE**  
  If the specified member name is not found, the member is created. Effective as a call flag for PropSet.
  )
- **TJS_MEMBERMUSTEXIST**  
  If the specified member name is not found, an error is returned. This is useful for objects such as Dictionary and Array that return void by default when a member is not found (for other objects, a missing member is an error by default).
- **TJS_IGNOREPROP**  
  Bypasses property handling.
  
  Normally, when the specified member is an object on which PropSet or PropGet succeeds (a property object), TJS2 objects use the result of PropSet or PropGet on that member in place of the member itself.
  
  This flag bypasses that handling, so even if the specified member is a property object, the operation applies to the property object itself.
- **TJS_HIDDENMEMBER**  
  A member created with this flag is hidden. Some objects may not support it.
- **TJS_STATICMEMBER**  
  A member created with this flag is static (independent of the execution context). Some objects may not support it.

## tjs_error

tjs_error is the error type returned by the iTJSDispatch2 methods (except AddRef and Release).

It takes the following values. Any negative value, even one not listed here, must be treated as an error. The TJS_SUCCEEDED and TJS_FAILED macros can be used to check this.

- ****TJS_E_MEMBERNOTFOUND****  
  The specified member was not found.
- ****TJS_E_NOTIMPL****  
  The requested feature is not implemented.
- ****TJS_E_INVALIDPARAM****  
  Invalid argument.
- ****TJS_E_BADPARAMCOUNT****  
  Invalid number of arguments.
- ****TJS_E_INVALIDTYPE****  
  Not a function, or the wrong kind of property.
  
  Returned when trying to call something that is not a function, or to treat something that is not a property as a property.
- ****TJS_E_INVALIDOBJECT****  
  The object has already been invalidated.
- ****TJS_E_ACCESSDENYED****  
  An operation not permitted on a read-only or write-only property was attempted.
- ****TJS_E_NATIVECLASSCRASH****  
  Wrong execution context.
  
  Returned when a method implemented in native code is run in a context that the native code cannot handle (such as on an object of a different class).
- ****TJS_S_TRUE****  
  Not an error; indicates that the result is "true".
- ****TJS_S_FALSE****  
  Not an error; indicates that the result is "false".
- ****TJS_S_OK****  
  Normally returned when no error occurred.
- ****TJS_E_FAIL****  
  Returned when an unspecified error occurred.
- ****TJS_FAILED**(x)**  
  A macro that is true when x is an error value.
- ****TJS_SUCCEEDED**(x)**  
  A macro that is true when x is not an error value.

The error definitions and related macros are in tjsErrorDef.h.

Also, instead of an error code, a runtime exception (in the C++ sense) may be thrown. Your code must take runtime exceptions fully into account.
