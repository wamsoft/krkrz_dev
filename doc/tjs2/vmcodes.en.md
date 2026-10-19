---
source_hash: d149c5cad1a1
---

# Virtual Machine

## TJS2 VM

TJS2 first compiles scripts into binary code for a virtual machine (the TJS2 **VM**) and then executes it.

Disassembled TJS2 VM code is shown when an exception occurs or when a dump is performed, so this page briefly describes the virtual machine.

## Instruction code

The TJS2 VM is independent for each execution unit, such as a function or property; a function never shares its instruction code space, register space, flag, or constant area with another function.

The instruction pointer (ip) always starts at 0 at the beginning of a function or other unit.

A short, human-readable name for an instruction code is called a mnemonic.

## Registers

TJS2 VM registers are written as %(number) in mnemonics. The number can be negative. There is no limit on the number of registers. Local variables, temporary values during computation, and so on are all stored in registers. There is no main memory or stack.

A register holds the same kinds of values as a TJS2 variable: integers, real numbers, objects, strings, octet strings, and void.

In the current version, register %0 is always void. Register %-1 is this. Register %-2 is a special object called the **this proxy**: a member lookup on it first checks this, and if the member is not there, checks global. The this proxy does not exist in global-level execution units. Function arguments and the like are stored in registers %-3, %-4, and so on before execution starts.

Apart from such registers, whose purpose is predetermined or which hold values before execution, register values are undefined when execution starts.

## Flag

The TJS2 VM has a single flag, which stores the result of comparisons. The flag is either true or false.

## Constant area

The TJS2 VM constant area stores constants and is written as *(number) in mnemonics. The constant area is read-only; the const instruction moves a value from it into a register. The "names" used to access object members by name, such as function and property names, are also stored in the constant area.

## VM mnemonics

Some instructions have operands of the form `%obj.*name` or `%obj.%name`; these involve object member access.

An operand of the form `%obj.*name` is a direct reference: it refers to the member named by `*name` in the object given by register `%obj`.

An operand of the form `%obj.%name` is an indirect reference: it refers to the member named by `%name` in the object given by register `%obj`.

The mnemonics of such instructions have the suffix d or pd (direct / property direct), or i or pi (indirect / property indirect).

Those with p in the suffix invoke the property handler of the target register (the behavior of the unary '*' operator).

- ****nop**  
(no operation)**  
  Does nothing.
- ****const**  
(copy constant value)**  
  Syntax: `const %dest, *src`
  
  
  Copies the value at *src in the constant area to register %dest.
- ****cp**  
(copy register)**  
  Syntax: `cp %dest, %src`
  
  
  Copies the value of register %src to register %dest.
- ****cl**  
(clear register)**  
  Syntax: `cl %dest`
  
  
  Sets register %dest to void.
- ****ccl**  
(clear register)**  
  Syntax: `ccl %low-%high`
  
  
  Sets all registers from %low through %high to void.
- ****tt**  
(test true)**  
  Syntax: `tt %reg`
  
  
  Sets the flag to true if register %reg represents true, and to false if it represents false.
- ****tf**  
(test false)**  
  Syntax: `tf %reg`
  
  
  The opposite of tt: sets the flag to false if register %reg represents true, and to true if it represents false.
- ****ceq**  
(compare equal)**  
  Syntax: `ceq %reg1, %reg2`
  
  
  Sets the flag to true if %reg1 and %reg2 are equal by ordinary comparison (the behavior of the == operator), and to false otherwise.
- ****cdeq**  
(compare distinct equal)**  
  Syntax: `cdeq %reg1, %reg2`
  
  
  Sets the flag to true if %reg1 and %reg2 are equal by identity comparison (the behavior of the === operator), and to false otherwise.
- ****clt**  
(compare littler than)**  
  Syntax: `clt %reg1, %reg2`
  
  
  Sets the flag to true if %reg1 < %reg2, and to false otherwise.
- ****cgt**  
(compare greater than)**  
  Syntax: `cgt %reg1, %reg2`
  
  
  Sets the flag to true if %reg1 > %reg2, and to false otherwise.
- ****setf**  
(set flag)**  
  Syntax: `setf %dest`
  
  
  Sets %dest to true (a nonzero integer) if the flag is true, and to false (integer 0) if it is false.
- ****setnf**  
(set not flag)**  
  Syntax: `setnf %dest`
  
  
  The opposite of setf: sets %dest to true (a nonzero integer) if the flag is false, and to false (integer 0) if it is true.
- ****lnot**  
(logical not)**  
  Syntax: `lnot %reg`
  
  
  Inverts the truth value of %reg.
- ****nf**  
(not flag)**  
  Syntax: `nf`
  
  
  Inverts the flag.
- ****jf**  
(jump if flag)**  
  Syntax: `jf ip`
  
  
  Jumps to ip if the flag is true.
- ****jnf**  
(jump if not flag)**  
  Syntax: `jnf ip`
  
  
  Jumps to ip if the flag is false.
- ****inc**, **incpd**, **incpi**, **incp**  
(increment)**  
  Syntax: `inc %reg`
  
  Syntax: `incpd %res, %obj.*name`
  
  Syntax: `incpi %res, %obj.%name`
  
  Syntax: `incp %res, %propobj`
  
  
  
  Increments %reg, %obj.*name, %obj.%name, or %propobj.
  
  Of the instructions above, those that take %res also store the result in %res if res is not 0.
- ****dec**, **decpd**, **decpi**, **decp**  
(decrement)**  
  Syntax: `dec %reg`
  
  Syntax: `decpd %res, %obj.*name`
  
  Syntax: `decpi %res, %obj.%name`
  
  Syntax: `decp %res, %propobj`
  
  
  
  Decrements %reg, %obj.*name, %obj.%name, or %propobj.
  
  Of the instructions above, those that take %res also store the result in %res if res is not 0.
- ****lor**, **lorpd**, **lorpi**, **lorp**  
(logical or)**  
  Syntax: `lor %dest, %src`
  
  
  Computes the logical OR of %dest and %src and stores the result in %dest.
  
  
  Syntax: `lorpd %res, %obj.*name, %src`
  
  
  Computes the logical OR of %obj.*name and %src and stores the result in %obj.*name.
  
  
  Syntax: `lorpi %res, %obj.%name, %src`
  
  
  Computes the logical OR of %obj.%name and %src and stores the result in %obj.%name.
  
  
  Syntax: `lorp %res, %propobj, %src`
  
  
  Computes the logical OR of %propobj and %src and stores the result in %propobj.
  
  
  Of the instructions above, those that take %res also store the result in %res if res is not 0.
- ****land**, **landpd**, **landpi**, **landp**  
(logical and)**  
  Syntax: `land %dest, %src`
  
  
  Computes the logical AND of %dest and %src and stores the result in %dest.
  
  
  Syntax: `landpd %res, %obj.*name, %src`
  
  
  Computes the logical AND of %obj.*name and %src and stores the result in %obj.*name.
  
  
  Syntax: `landpi %res, %obj.%name, %src`
  
  
  Computes the logical AND of %obj.%name and %src and stores the result in %obj.%name.
  
  
  Syntax: `landp %res, %propobj, %src`
  
  
  Computes the logical AND of %propobj and %src and stores the result in %propobj.
  
  
  Of the instructions above, those that take %res also store the result in %res if res is not 0.
- ****bor**, **borpd**, **borpi**, **borp**  
(bitwise or)**  
  Syntax: `bor %dest, %src`
  
  
  Computes the bitwise OR of %dest and %src and stores the result in %dest.
  
  
  Syntax: `borpd %res, %obj.*name, %src`
  
  
  Computes the bitwise OR of %obj.*name and %src and stores the result in %obj.*name.
  
  
  Syntax: `borpi %res, %obj.%name, %src`
  
  
  Computes the bitwise OR of %obj.%name and %src and stores the result in %obj.%name.
  
  
  Syntax: `borp %res, %propobj, %src`
  
  
  Computes the bitwise OR of %propobj and %src and stores the result in %propobj.
  
  
  Of the instructions above, those that take %res also store the result in %res if res is not 0.
- ****bxor**, **bxorpd**, **bxorpi**, **bxorp**  
(bitwise xor)**  
  Syntax: `bxor %dest, %src`
  
  
  Computes the bitwise XOR of %dest and %src and stores the result in %dest.
  
  
  Syntax: `bxorpd %res, %obj.*name, %src`
  
  
  Computes the bitwise XOR of %obj.*name and %src and stores the result in %obj.*name.
  
  
  Syntax: `bxorpi %res, %obj.%name, %src`
  
  
  Computes the bitwise XOR of %obj.%name and %src and stores the result in %obj.%name.
  
  
  Syntax: `bxorp %res, %propobj, %src`
  
  
  Computes the bitwise XOR of %propobj and %src and stores the result in %propobj.
  
  
  Of the instructions above, those that take %res also store the result in %res if res is not 0.
- ****band**, **bandpd**, **bandpi**, **bandp**  
(bitwise and)**  
  Syntax: `band %dest, %src`
  
  
  Computes the bitwise AND of %dest and %src and stores the result in %dest.
  
  
  Syntax: `bandpd %res, %obj.*name, %src`
  
  
  Computes the bitwise AND of %obj.*name and %src and stores the result in %obj.*name.
  
  
  Syntax: `bandpi %res, %obj.%name, %src`
  
  
  Computes the bitwise AND of %obj.%name and %src and stores the result in %obj.%name.
  
  
  Syntax: `bandp %res, %propobj, %src`
  
  
  Computes the bitwise AND of %propobj and %src and stores the result in %propobj.
  
  
  Of the instructions above, those that take %res also store the result in %res if res is not 0.
- ****sar**, **sarpd**, **sarpi**, **sarp**  
(shift arithmetic right)**  
  Syntax: `sar %dest, %src`
  
  
  Shifts %dest arithmetically right by the number of bits given by %src and stores the result in %dest.
  
  
  Syntax: `sarpd %res, %obj.*name, %src`
  
  
  Shifts %obj.*name arithmetically right by the number of bits given by %src and stores the result in %obj.*name.
  
  
  Syntax: `sarpi %res, %obj.%name, %src`
  
  
  Shifts %obj.%name arithmetically right by the number of bits given by %src and stores the result in %obj.%name.
  
  
  Syntax: `sarp %res, %propobj, %src`
  
  
  Shifts %propobj arithmetically right by the number of bits given by %src and stores the result in %propobj.
  
  
  Of the instructions above, those that take %res also store the result in %res if res is not 0.
- ****sal**, **salpd**, **salpi**, **salp**  
(shift arithmetic left)**  
  Syntax: `sal %dest, %src`
  
  
  Shifts %dest arithmetically left by the number of bits given by %src and stores the result in %dest.
  
  
  Syntax: `salpd %res, %obj.*name, %src`
  
  
  Shifts %obj.*name arithmetically left by the number of bits given by %src and stores the result in %obj.*name.
  
  
  Syntax: `salpi %res, %obj.%name, %src`
  
  
  Shifts %obj.%name arithmetically left by the number of bits given by %src and stores the result in %obj.%name.
  
  
  Syntax: `salp %res, %propobj, %src`
  
  
  Shifts %propobj arithmetically left by the number of bits given by %src and stores the result in %propobj.
  
  
  Of the instructions above, those that take %res also store the result in %res if res is not 0.
- ****sr**, **srpd**, **srpi**, **srp**  
(shift bitwise right)**  
  Syntax: `sr %dest, %src`
  
  
  Shifts %dest logically (bitwise) right by the number of bits given by %src and stores the result in %dest.
  
  
  Syntax: `srpd %res, %obj.*name, %src`
  
  
  Shifts %obj.*name logically (bitwise) right by the number of bits given by %src and stores the result in %obj.*name.
  
  
  Syntax: `srpi %res, %obj.%name, %src`
  
  
  Shifts %obj.%name logically (bitwise) right by the number of bits given by %src and stores the result in %obj.%name.
  
  
  Syntax: `srp %res, %propobj, %src`
  
  
  Shifts %propobj logically (bitwise) right by the number of bits given by %src and stores the result in %propobj.
  
  
  Of the instructions above, those that take %res also store the result in %res if res is not 0.
- ****add**, **addpd**, **addpi**, **addp**  
(add)**  
  Syntax: `add %dest, %src`
  
  
  Adds %src to %dest and stores the result in %dest.
  
  
  Syntax: `addpd %res, %obj.*name, %src`
  
  
  Adds %src to %obj.*name and stores the result in %obj.*name.
  
  
  Syntax: `addpi %res, %obj.%name, %src`
  
  
  Adds %src to %obj.%name and stores the result in %obj.%name.
  
  
  Syntax: `addp %res, %propobj, %src`
  
  
  Adds %src to %propobj and stores the result in %propobj.
  
  
  Of the instructions above, those that take %res also store the result in %res if res is not 0.
- ****sub**, **subpd**, **subpi**, **subp**  
(subtract)**  
  Syntax: `sub %dest, %src`
  
  
  Subtracts %src from %dest and stores the result in %dest.
  
  
  Syntax: `subpd %res, %obj.*name, %src`
  
  
  Subtracts %src from %obj.*name and stores the result in %obj.*name.
  
  
  Syntax: `subpi %res, %obj.%name, %src`
  
  
  Subtracts %src from %obj.%name and stores the result in %obj.%name.
  
  
  Syntax: `subp %res, %propobj, %src`
  
  
  Subtracts %src from %propobj and stores the result in %propobj.
  
  
  Of the instructions above, those that take %res also store the result in %res if res is not 0.
- ****mod**, **modpd**, **modpi**, **modp**  
(modulo)**  
  Syntax: `mod %dest, %src`
  
  
  Stores in %dest the remainder of dividing %dest by %src.
  
  
  Syntax: `modpd %res, %obj.*name, %src`
  
  
  Stores in %obj.*name the remainder of dividing %obj.*name by %src.
  
  
  Syntax: `modpi %res, %obj.%name, %src`
  
  
  Stores in %obj.%name the remainder of dividing %obj.%name by %src.
  
  
  Syntax: `modp %res, %propobj, %src`
  
  
  Stores in %propobj the remainder of dividing %propobj by %src.
  
  
  Of the instructions above, those that take %res also store the result in %res if res is not 0.
- ****div**, **divpd**, **divpi**, **divp**  
(real divide)**  
  Syntax: `div %dest, %src`
  
  
  Divides %dest by %src (real division) and stores the result in %dest.
  
  
  Syntax: `divpd %res, %obj.*name, %src`
  
  
  Divides %obj.*name by %src (real division) and stores the result in %obj.*name.
  
  
  Syntax: `divpi %res, %obj.%name, %src`
  
  
  Divides %obj.%name by %src (real division) and stores the result in %obj.%name.
  
  
  Syntax: `divp %res, %propobj, %src`
  
  
  Divides %propobj by %src (real division) and stores the result in %propobj.
  
  
  Of the instructions above, those that take %res also store the result in %res if res is not 0.
- ****idiv**, **idivpd**, **idivpi**, **idivp**  
(integer divide)**  
  Syntax: `idiv %dest, %src`
  
  
  Divides %dest by %src (integer division) and stores the result in %dest.
  
  
  Syntax: `idivpd %res, %obj.*name, %src`
  
  
  Divides %obj.*name by %src (integer division) and stores the result in %obj.*name.
  
  
  Syntax: `idivpi %res, %obj.%name, %src`
  
  
  Divides %obj.%name by %src (integer division) and stores the result in %obj.%name.
  
  
  Syntax: `divp %res, %propobj, %src`
  
  
  Divides %propobj by %src (integer division) and stores the result in %propobj.
  
  
  Of the instructions above, those that take %res also store the result in %res if res is not 0.
- ****mul**, **mulpd**, **mulpi**, **mulp**  
(multiply)**  
  Syntax: `mul %dest, %src`
  
  
  Multiplies %dest by %src and stores the result in %dest.
  
  
  Syntax: `mulpd %res, %obj.*name, %src`
  
  
  Multiplies %obj.*name by %src and stores the result in %obj.*name.
  
  
  Syntax: `mulpi %res, %obj.%name, %src`
  
  
  Multiplies %obj.%name by %src and stores the result in %obj.%name.
  
  
  Syntax: `mulp %res, %propobj, %src`
  
  
  Multiplies %propobj by %src and stores the result in %propobj.
  
  
  Of the instructions above, those that take %res also store the result in %res if res is not 0.
- ****bnot**  
(bitwise not)**  
  Syntax: `bnot %reg`
  
  
  Inverts each bit of %reg and stores the result back in %reg.
- ****asc**  
(ascii code)**  
  Syntax: `asc %reg`
  
  
  Stores in %reg the character code of the first character of the string in %reg (the `#` operator).
- ****chr**  
(make character)**  
  Syntax: `chr %reg`
  
  
  Creates the single character corresponding to the number in %reg and stores it back in %reg (the `$` operator).
- ****num**  
(number)**  
  Syntax: `num %reg`
  
  
  Converts register %reg to a number.
- ****chs**  
(change sign)**  
  Syntax: `chs %reg`
  
  
  Negates the number in register %reg.
- ****inv**  
(invalidate)**  
  Syntax: `inv %reg`
  
  
  Invalidates the object in %reg.
- ****chkinv**  
(invalidate)**  
  Syntax: `chkinv %reg`
  
  
  Sets %reg to true if the object in %reg has not been invalidated, and to false otherwise.
- ****int**  
(convert to integer)**  
  Syntax: `int %reg`
  
  
  Converts register %reg to an integer.
- ****real**  
(convert to real)**  
  Syntax: `real %reg`
  
  
  Converts register %reg to a real number.
- ****string**  
(convert to string)**  
  Syntax: `string %reg`
  
  
  Converts register %reg to a string.
- ****octet**  
(convert to octet)**  
  Syntax: `octet %reg`
  
  
  Converts register %reg to an octet string.
- ****typeof**, **typeofd**, **typeofi**  
(check type)**  
  Syntax: `typeof %reg`
  
  Syntax: `typeofd %obj.*name`
  
  Syntax: `typeofi %obj.%name`
  
  
  
  Determines the type of %reg, %obj.*name, or %obj.%name, and stores a string representing that type back in %reg, %obj.*name, or %obj.%name.
- ****eval**  
(evaluate expression)**  
  Syntax: `eval %reg`
  
  
  Evaluates the string in %reg as an expression and stores the result back in %reg.
- ****eexp**  
(execute expression)**  
  Syntax: `eexp %reg`
  
  
  Evaluates the string in %reg as an expression and discards the result.
- ****chkins**  
(check instance)**  
  Syntax: `chkins %reg, %classname`
  
  
  Stores true in %reg if the object in %reg is an instance of the class whose name is given by %classname, and false otherwise.
- ****call**, **calld**, **calli**  
(function call)**  
  Syntax: `call %dest, %func(%arg1, %arg2, %arg3, ...)`
  
  Syntax: `calld %dest, %obj.*name(%arg1, %arg2, %arg3, ...)`
  
  Syntax: `calli %dest, %obj.%name(%arg1, %arg2, %arg3, ...)`
  
  
  
  Calls the function object given by %func, %obj.*name, or %obj.%name with the arguments %arg1, %arg2, %arg3, ..., and stores the result in %dest. If %dest is %0, the result is discarded (not stored in %0).
- ****new**  
(create new)**  
  Syntax: `new %dest, %func(%arg1, %arg2, %arg3, ...)`
  
  
  Constructs an instance of the class object given by %func with the arguments %arg1, %arg2, %arg3, ..., and stores the result in %dest.
- ****gpd**, **gpds**  
(get property direct)**  
  Syntax: `gpd %dest, %obj.*name`
  
  Syntax: `gpds %dest, %obj.*name`
  
  
  
  Looks up the member named by *name in the object given by %obj and copies its value to %dest.
  
  gpd invokes the property handler; gpds does not, and gets the property object itself.
- ****gpi**, **gpis**  
(get property indirect)**  
  Syntax: `gpi %dest, %obj.%name`
  
  Syntax: `gpis %dest, %obj.%name`
  
  
  
  Looks up the member named by %name in the object given by %obj and copies its value to %dest.
  
  gpi invokes the property handler; gpis does not, and gets the property object itself.
- ****spd**, **spde**, **spdeh**, **spds**  
(set property direct)**  
  Syntax: `spd %obj.*name`
  
  Syntax: `spde %obj.*name`
  
  Syntax: `spdeh %obj.*name`
  
  Syntax: `spds %obj.*name`
  
  
  
  Assigns the value of %src to the member named by *name in the object given by %obj.
  
  spd performs an ordinary access; an exception is thrown if the member does not exist.
  
  spde creates the member if it does not exist.
  
  spdeh sets the member as a hidden member. This has no effect in the current version.
  
  spds does not invoke the property handler and replaces the property object itself.
- ****spi**, **spie**, **spis**  
(set property indirect)**  
  Syntax: `spi %obj.%name`
  
  Syntax: `spie %obj.%name`
  
  Syntax: `spis %obj.%name`
  
  
  
  Assigns the value of %src to the member named by %name in the object given by %obj.
  
  spi performs an ordinary access; an exception is thrown if the member does not exist.
  
  spie creates the member if it does not exist.
  
  spis does not invoke the property handler and replaces the property object itself.
- ****getp****  
  Syntax: `getp %reg, %propobj`
  
  
  
  Invokes the getter of the property object given by %propobj and assigns the property's value to %reg. This is the behavior of the unary '*' operator.
- ****setp****  
  Syntax: `setp %propobj, %reg`
  
  
  
  Invokes the setter of the property object given by %propobj to set the value of %reg. This is the behavior of the unary '*' operator.
- ****deld**, **deli**  
(delete member)**  
  Syntax: `deld %reg, %obj.*name`
  
  Syntax: `deli %reg, %obj.%name`
  
  
  
  Deletes the member named by *name or %name from the object given by %obj.
  
  Stores in %reg whether the deletion succeeded; if %reg is %0, the result is discarded.
- ****srv**  
(set result value)**  
  Syntax: `srv %reg`
  
  
  Sets the value of %reg as the function's return value (the function returns the value in %reg).
- ****ret**  
(return)**  
  Syntax: `ret`
  
  
  Returns to the caller.
- ****entry**  
(enter try block)**  
  Syntax: `entry ip, %reg`
  
  
  Enters an exception-protected block. If an exception occurs, jumps to ip and sets the exception object in %reg.
- ****extry**  
(exit from try block)**  
  Syntax: `extry`
  
  
  Leaves an exception-protected block.
- ****throw**  
(throw exception object)**  
  Syntax: `throw %reg`
  
  
  Throws the object in %reg as an exception object.
- ****chgthis**  
(change this)**  
  Syntax: `chgthis %dest, %src`
  
  
  Changes the closure part (context) of the object in %dest to the object given by %src.
- ****global**  
(get global object)**  
  Syntax: `global %dest`
  
  
  Stores the global object in %dest.
- ****addci**  
(add class instance information)**  
  Syntax: `addci %dest, %info`
  
  
  Adds %info to the class instance information of the object in %dest.
- ****regmember**  
(register members)**  
  Syntax: `regmember`
  
  
  Registers the class members in the "this" object. Used internally.
- ****debugger**  
(call debugger)**  
  Syntax: `debugger`
  
  
  Breaks execution and invokes the debugger. In the current implementation, this invokes the native debugger rather than a TJS2 debugger.
