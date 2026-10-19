---
source_hash: 425db22db08e
---

# tTJS

## What is tTJS

The class of the TJS2 script engine. TJS2 is operated through an object of this class.

## Constructor

The tTJS constructor takes no arguments.

tTJS objects cannot be created as automatic variables. They must always be created with the new operator.

The reference count is 1 right after creation. This means that calling the Release method as is frees the tTJS object.

## Destructor

The tTJS destructor is protected and cannot be accessed.

Use the Release method to free a tTJS object.

It is also recommended to call the Shutdown method before freeing a tTJS object.

## AddRef

void tTJS::AddRef()



Increments the reference count of the TJS2 script engine.

## Release

void tTJS::Release()



Decrements the reference count of the TJS2 script engine.

When the reference count reaches 0, the tTJS object is freed.

## Shutdown

void tTJS::Shutdown()



Shuts down the script engine.



When freeing the TJS2 script engine, it is recommended to call this method before the Release method.

## GetGlobal

iTJSDispatch2 * tTJS::GetGlobal()



Gets the **global object**.

An object of the type

is returned.

This method increments the reference count of the global object when returning it.

## GetGlobalNoAddRef

iTJSDispatch2 * tTJS::GetGlobalNoAddRef()



Gets the global object. Unlike GetGlobal, it does not increment the reference count of the global object.

## SetConsoleOutput

void tTJS::SetConsoleOutput(iTJSConsoleOutput *console);



Sets the output destination of the **console**.

The console is where TJS2 writes error messages and other output.



It takes the following argument.

- **console**  
  An **iTJSConsoleOutput** object that defines the console output destination.
  
  iTJSConsoleOutput is an abstract base class defined in tjs.h with the following methods.
  
  - **void iTJSConsoleOutput::**ExceptionPrint**(const tjs_char *msg)**  
    Outputs information about an exception. msg is the message.
  - **void iTJSConsoleOutput::**Print**(const tjs_char *msg)**  
    Outputs other information. msg is the message.

## GetConsoleOutput

tTJSConsoleOutput * tTJS::GetConsoleOutput() const



Gets the console output destination.

## OutputToConsole

void tTJS::OutputToConsole(const tjs_char *msg) const



Outputs a string to the console. msg is the message to output.

## OutpuExceptionToConsole

void tTJS::OutpuExceptionToConsole(const tjs_char *msg) const



Outputs an exception string to the console. msg is the message to output.

## OutputToConsoleWithCentering

void tTJS::OutputToConsoleWithCentering(const tjs_char *msg, tjs_uint width) const



Outputs a string to the console, centered. msg is the message to output, and width is the line width.

If the message has fewer characters than the width, it is centered within the specified width
(all characters are assumed to have the same width, so the layout breaks when full-width characters are mixed in).

## OutputToConsoleSeparator

void tTJS::OutputToConsoleSeparator(const tjs_char *text, tjs_uint count) const



Outputs the separator given by text to the console, count times.

## Dump

void tTJS::Dump(tjs_uint width = 80) const



Outputs the state of TJS2 to the console.

This shows, among other things, the disassembled virtual machine code in each script block.

width specifies the output line width.

## ExecScript

void tTJS::ExecScript(

const tjs_char *script,

tTJSVariant *result = NULL,

iTJSDispatch2 *context = NULL,

const tjs_char *name = NULL,

tjs_int lineofs = 0

)



void tTJS::ExecScript(

const ttstr &script,

tTJSVariant *result = NULL,

iTJSDispatch2 *context = NULL,

const tjs_char *name = NULL,

tjs_int lineofs = 0

)



Executes a script.



It takes the following arguments.

- **const tjs_char *script**
- **const ttstr &script**  
  The script to execute.
- **tTJSVariant *result**  
  A pointer to a tTJSVariant variable that receives the result.
  
  NULL can be specified, in which case the result cannot be received.
- **iTJSDispatch2 *context**  
  The context in which this script runs.
  
  If NULL is specified, the script runs in the global context.
  
  Usually NULL is specified; to run the script in a specific context, specify the object that serves as that context.
- **const tjs_char *name**  
  The name of the script. Usually the script's file name.
  
  It is used, for example, to report which script an exception occurred in.
- **tjs_int lineofs**  
  The line (from 0) at which the script starts.
  
  When a TJS script is embedded in external text, such as a TJS script embedded in another document, specify the line at which the TJS script starts.
  
  It is used, for example, to report where an exception occurred.

## EvalExpression

void tTJS::EvalExpression(

const tjs_char *expression,

tTJSVariant *result = NULL,

iTJSDispatch2 *context = NULL,

const tjs_char *name = NULL

tjs_int lineofs = 0

)



void tTJS::EvalExpression(

const ttstr &expression,

tTJSVariant *result = NULL,

iTJSDispatch2 *context = NULL,

const tjs_char *name = NULL

tjs_int lineofs = 0

)



Evaluates an expression.

See [ExecScript](#execscript) for the arguments.



For operators whose result cannot be obtained, such as the **if operator**, an exception is thrown if result is non-NULL in an attempt to get the result. In that case, result must be NULL.

## SetPPValue

void tTJS::SetPPValue(const tjs_char *name, const tjs_int32 value)



Sets a variable for **conditional compilation**. name is the variable name, and value is the value to set.

## GetPPValue

tjs_int32 tTJS::GetPPValue(const tjs_char *name)



Gets a variable for conditional compilation. name is the variable name. Returns 0 if the variable is not found.

## DoGarbageCollection

tjs_int32 tTJS::DoGarbageCollection()



Performs **garbage collection**. Clears the caches held by TJS2 and completes pending cleanup.
