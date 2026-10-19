---
source_hash: 579df7b67d80
---

# Type Annotation Syntax

Kirikiri Z can run TJS with type annotations.
Annotations only keep the parser from raising an error; the script behaves exactly the same as without them. They are used, for example, to take advantage of editor IntelliSense.

The syntax looks like the examples below.

## Variable declarations
Append a colon to the variable name, followed by the type.
```
var i:int;
var win:Window = new Window();
```

## Function definitions
Append a colon to an argument name, followed by the type.
The return type can be given after the argument list.
```
function add(param1:int, param2:int) : int {
    return param1 + param2;
}
```

## Function expressions
Argument and return types can be given the same way as in function definitions.
```
var f = function(param1:string) : void {};
```

## Property definitions
You can specify the type of the setter argument and of the getter return value separately.
```
property prop {
    setter(value:int) {}
    getter:int { return 0; }
}
```
