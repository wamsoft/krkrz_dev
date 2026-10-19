---
source_hash: eb23afb0c7f9
---

# Exception Class

## Exception class

The Exception class creates **exception objects**.

The constructor syntax is as follows.

```
new Exception(<メッセージ>)
```

The message is stored in the message property of the created object.

The trace property records the functions and other locations passed through before the exception occurred (as a human-readable string).

All exception objects raised by causes other than scripts (for example, division-by-zero exceptions) are Exception objects.



More properties may be added in the future.

## message

The message property is a string that describes the reason for the exception.
