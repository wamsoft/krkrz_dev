---
source_hash: 6a3045745fb9
---

# Debugging

## About Debugging Applications

Debugging is the work of finding and fixing bugs ( the causes of malfunctions or unintended behavior ) in an application.

Kirikiri has several features that help with debugging. This page explains how to use them to debug your application.

## Debug Message Output

Kirikiri provides several destinations for messages that help with debugging.

- **[Console](Console.md)**
  When launched from the command line, the various debug messages output by the Kirikiri system and by user scripts can be shown in the terminal.

In particular, the console shows the messages a user program outputs with [Debug.message](../reference/Debug.md#message). By calling the method anywhere in the program to display the contents of variables, you can see their values while the program runs.

For how to display messages and how to write logs to a file, see "Debugging options" in [Command-Line Options](CommandLine.md) and the [Debug class](../reference/Debug.md).

## Debug Mode

If you specify `-debug` in the [command-line options](CommandLine.md) (setting "debug mode" to ' enabled '), Kirikiri runs in debug mode.

In debug mode, TJS2 runs more slowly, but several features useful for debugging are enabled.

- **Type information tracking**  
  Information about TJS2 objects is enhanced.
  
  Outside debug mode, if you try to get information about, for example, the method obj.doAction of some object, you only get
  
  ```
  コンソール : obj.doAction = (object)(object 0x0279E130:0x01EB0BD4)
  ```
  
  but with debug mode enabled, you get type information like
  
  ```
  コンソール : obj.doAction = (object)(object 0x0279E130[(function) MyClass.doAction]:0x01EB0BD4[instance of class MyClass])
  ```
  
  (Of the two parts separated by ':', the first is the type of the object and the second is the context in which the object runs ).
  
  This option is practically essential when tracing with a debugger.
  
  (In the current version) this feature is active wherever an object is converted to a string.
- **Object leak detection**  
  Enables warnings at exit about objects that have not been deleted (released).
  
  In TJS2, objects you create are normally deleted automatically by garbage collection, and no explicit deletion is needed. However, bugs in plugins or the Kirikiri engine, or circular references, can leave objects undeleted (leaked).
  
  In debug mode, objects that are still not released at exit are written to the console log file.
  
  Note that even if only a single object is not released, all objects related to it are detected, so the log file can become huge.
  
  
  
  The [System.exit](../reference/System.md#exit) method terminates the application in a way close to a forced exit. Note that exiting the application with this method leaks many objects and records a large amount of log.
  
  > **Note:**
  > A circular reference is a situation where A references B and B references A.
  >
  > For example, the following script creates a circular reference.
  >
  > ```
  > var a = %[], b = %[];
  > a.b = b; b.a = a;
  > ```
  >
  > In this situation, object a needs b, and object b needs a. The garbage collection method TJS2 uses (reference counting) has difficulty detecting such situations and releasing the objects, so TJS2 does not detect them. As a result, these objects are never deleted (you can break the circular reference by explicitly invalidating one of the objects with the invalidate operator).
  >
  >
  >
  > In plugins, mishandling reference counts can leak objects. If you write a plugin that handles TJS2 objects, be very careful with reference counts.
- **Warnings about script execution on objects being deleted**  
  When an object is deleted or invalidated, its finalize method is called.
  
  In TJS2, "you cannot know when" an object will be deleted, so the finalize method may be called at an odd time and cause unexpected behavior. In debug mode, a warning is shown in the console at such "unstable timings", that is, when an object that was not invalidated is deleted by garbage collection and its finalize method is called.
  
  The warning looks like this.
  
  ```
  警告: anonymous@0x016DFA7C(9)[(function) finalize]: 削除中のオブジェクト 0x0167DD44[instance of class A] 上でコードが実行されています。このオブジェクトの作成時の呼び出し履歴は以下の通りです:
                       anonymous@0x016DFA7C(13)[(top level script) global]
  ```
  
  To prevent this, it is recommended to explicitly invalidate objects created with new using the invalidate operator once you are done with them.
  
  However, for objects of classes that have no finalize method, or whose finalize method does nothing problematic, such as Array, Dictionary, and Date, explicit invalidation may not be needed.
  
  The warning above is shown when an object is about to be deleted without explicit invalidation and TJS2 script is about to run in its context.
- **Getting the call stack**  
  Lets scripts get the TJS2 function/method call stack.
  
  Use the [Scripts.getTraceString](../reference/Scripts.md#gettracestring) method for this.
  
  When something goes wrong in the middle of the program and you do not know where a method was called from, you can use this method to output the call stack to the console, for example.

## Debugging TJS2 with VSCode

Kirikiri Z has a built-in **Debug Adapter Protocol (DAP)** server. Combined
with the dedicated VSCode extension [krkrz-vscode](https://github.com/wamsoft/krkrz-vscode),
you can debug TJS2 scripts the same way as in ordinary programming languages.

### Requirements

- Kirikiri Z engine: a binary built with the build option `KRKRZ_ENABLE_DAP=ON`
  ( ON by default )
- VSCode 1.75 or later
- The [krkrz-vscode](https://github.com/wamsoft/krkrz-vscode) extension

The old `ENABLE_DEBUGGER` ( a Win32-only custom protocol based on `WM_COPYDATA` )
was removed on 2026-04-25 and replaced by DAP.

### Installing the Extension

It is not yet published on the Marketplace, so for now, build it directly from
the repository and install it.

```bash
git clone https://github.com/wamsoft/krkrz-vscode.git
cd krkrz-vscode
npm install
npm run package         # → krkrz-vscode-X.Y.Z.vsix を生成
code --install-extension krkrz-vscode-0.0.1.vsix
```

To run it in the Extension Development Host for development, run
`npm run compile`, open this folder in VSCode, and press **F5**.

### Launching

Launch Kirikiri Z with `-dap=<port>`. `-dap=yes` uses the default port ( 6635 ).

```
krkrz64.exe -dap=6635 path\to\data
```

In VSCode, choose "Run and Debug" → "create a launch.json file" → "Kirikiri Z"
to get snippets. There are two forms: `Attach` ( connect to a running krkrz )
and `Launch` ( spawn krkrz and connect ).

Main settings in `launch.json`:

| Setting | Type | Default | Description |
|---|---|---|---|
| `request` | string | — | `attach` or `launch` |
| `host` | string | `127.0.0.1` | DAP server host |
| `port` | number | `6635` | TCP port |
| `stopOnEntry` | bool | `false` | Stop at the first VM line right after connecting |
| `program` | string | — | Absolute path of the krkrz executable to launch with `launch` |
| `data` | string | — | Data folder for `launch` |
| `args` | string[] | `[]` | Additional krkrz options ( e.g. `["-debug", "-loglevel=DEBUG"]` ) |
| `cwd` | string | Directory containing program | Working directory |
| `env` | object | `{}` | Additional environment variables |

### Supported Features

- Breakpoints ( conditional / log points supported )
- Stepping ( Over / In / Out )
- Pause / resume
- Multi-frame call stack ( Locals / `this` / Globals for each frame )
- Variable inspection ( Object / Array / Dictionary can be expanded )
- Expression evaluation in Watch / Hover / Debug Console
- Stopping on exceptions ( Uncaught Exceptions filter )
- Stopping at TJS `debugger;` statements
- Forwarding TJS log output to the Debug Console

### Known Limitations

- Breakpoints can be set only on lines of `.tjs` scripts executed by the TJS VM
  ( lines that do not hit the TJS VM hook cannot have breakpoints )
- While stopped on an exception or breakpoint, all of krkrz ( rendering,
  ContinuousHandler, etc. ) stops. Resume with VSCode's Continue / Stop
  buttons, or from Kirikiri Z's built-in [REPL](Console.md#repl) ( REPL input
  is processed even while stopped )
- Mutations to result objects of conditional breakpoints / Watch / Hover
  evaluation are not reflected in the frame ( they go through a snapshot )
- `setBreakpoints` always returns verified as `true`, so breakpoints placed on
  nonexistent lines are not detected as invalid
- TJS class names are not reflected in `exceptionInfo.typeName` ( currently
  fixed to "Exception" )
- Hit count breakpoints are not supported

For detailed usage, how to build the extension, and the latest supported
features, see the [krkrz-vscode README](https://github.com/wamsoft/krkrz-vscode).
The extension also includes TJS2 syntax highlighting.
