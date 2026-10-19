# KAGParser

Manual written as pseudo-code

Kirikiri Z KAGParserEx plugin.

Provides the KAGParser class, which parses KAG scenario files.
Linking it with Plugins.link("KAGParserEx.dll") replaces the KAGParser class with
this plugin's extended version (unlinking restores the original).

KAGParser is a lexer that interprets a KAG scenario from the beginning (or from a given label)
and returns the "next tag" as a dictionary on each call to getNextTag().
It does not display text or execute tags itself (the caller, such as KAG3's MainWindow,
interprets and executes the tags returned by getNextTag()).

Example:
var parser = new KAGParser();
parser.loadScenario("first.ks");
parser.goToLabel("*start");
var tag;
while((tag = parser.getNextTag()) !== void) {
// tag.tagname holds the tag name; the other members hold the attributes
}

The dictionary returned by getNextTag() holds the tag name in the tagname member and the tag's
attributes as "attribute name => value (string)". Body text is returned one character at a time
as a pseudo-tag whose tagname is "ch" (the character is in the text member), and line breaks as a
pseudo-tag whose tagname is "r" (with eol=true at the end of a line).

When processSpecialTags is true (the default), the following system tags are handled inside
the parser and do not appear in the values returned by getNextTag():
if / ignore / elsif / else / endif / endignore (conditionals),
macro / endmacro / erasemacro (recording and deleting macros),
pmacro / erasepmacro (registering and deleting parameter macros),
jump / call / return (jumps and calls within the scenario),
emb (embedding the result of an expression).

Extensions over the original KAGParser (the version built into Kirikiri Z):
- Tags can span multiple lines via the multiLineTagEnabled property
(put " \" at the end of a line and start the next line with ";")
- The value returned by getNextTag() has a taglist member (an array of the tag names
in the order they were written)
- Parameter macro expansion (the paramMacros property / the pmacro and
erasepmacro system tags). When a registered parameter name appears in a tag,
it is processed as if the registered parameter list had been inserted there
- The emb tag accepts an escape parameter. With escape=false, a result in
"[...]" form is not escaped and is evaluated as a normal tag
- Parameters written before "*" (all remaining parameters) in a macro expansion
remain in effect (in the original they are overwritten and lost)

## Members

### Constructors

- [KAGParser](#kagparser)

### Properties

- [curStorage](#curstorage)
- [curLabel](#curlabel)
- [curLine](#curline)
- [curPos](#curpos)
- [curLineStr](#curlinestr)
- [processSpecialTags](#processspecialtags)
- [ignoreCR](#ignorecr)
- [debugLevel](#debuglevel)
- [macros](#macros)
- [paramMacros](#parammacros)
- [macroParams](#macroparams)
- [mp](#mp)
- [callStackDepth](#callstackdepth)
- [multiLineTagEnabled](#multilinetagenabled)

### Methods

- [loadScenario](#loadscenario)
- [goToLabel](#gotolabel)
- [callLabel](#calllabel)
- [getNextTag](#getnexttag)
- [assign](#assign)
- [clear](#clear)
- [store](#store)
- [restore](#restore)
- [clearCallStack](#clearcallstack)
- [interrupt](#interrupt)
- [resetInterrupt](#resetinterrupt)

---

### KAGParser

Constructor

**Description**

Constructor (no arguments)

---

### curStorage

Property \ Access: `r/w`

**Description**

Storage name of the scenario being parsed. Setting it behaves like loadScenario()

---

### curLabel

Property \ Access: `r`

**Description**

Name of the last label passed (read-only)

---

### curLine

Property \ Access: `r`

**Description**

Line number being parsed, starting at 0 (read-only)

---

### curPos

Property \ Access: `r`

**Description**

Character position within the line being parsed, starting at 0 (read-only)

---

### curLineStr

Property \ Access: `r`

**Description**

Contents of the line being parsed (read-only)

---

### processSpecialTags

Property \ Access: `r/w`

**Description**

Whether system tags (if / macro / jump / emb, etc.) are handled inside the parser

If false, these are also returned from getNextTag() as normal tags. Defaults to true.

---

### ignoreCR

Property \ Access: `r/w`

**Description**

If true, line breaks in the scenario are ignored (no "r" pseudo-tags are returned). Defaults to false

---

### debugLevel

Property \ Access: `r/w`

**Description**

Debug output level: 0 (none), 1 (brief) or 2 (detailed)

---

### macros

Property \ Access: `r`

**Description**

Dictionary of recorded macros (macro name => macro body string) (read-only)

---

### paramMacros

Property \ Access: `r`

**Description**

Dictionary of parameter macros (read-only; KAGParserEx extension)

When registered as "parameter name => [ parameter name, value, parameter name, value, ... ]",
an occurrence of a registered parameter name in a tag is processed as if the registered contents
had been inserted there. A leading % or & in a value is expanded at run time.
Entries can also be registered and deleted with the pmacro / erasepmacro system tags.

---

### macroParams

Property \ Access: `r`

**Description**

Dictionary of the arguments passed to the macro currently running (read-only)

---

### mp

Property \ Access: `r`

**Description**

Alias for macroParams (read-only)

---

### callStackDepth

Property \ Access: `r`

**Description**

Depth of the call stack built by callLabel() (read-only)

---

### multiLineTagEnabled

Property \ Access: `r/w`

**Description**

Whether tags may span multiple lines (KAGParserEx extension). Defaults to false

If true, a tag can be split across lines by putting " \" at the end of a line
(at least one space is required before it) and starting the next line with ";".
The tag name must be on the first line.

---

### loadScenario

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `storage` | `&nbsp;` | Storage name of the scenario file (.ks) to load. |

**Description**

Loads a scenario file

The parse position moves to the beginning of the file. If the same storage is
already loaded, it is not reloaded.

---

### goToLabel

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `label` | `&nbsp;` | Name of the destination label, with a leading *, as in "*labelname". |

**Description**

Moves to the given label

Moves the parse position to the given label in the current scenario file.

---

### callLabel

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `label` | `&nbsp;` | Name of the destination label, with a leading *, as in "*labelname". |

**Description**

Pushes the current position onto the call stack and moves to the given label

The return system tag returns to the calling position.
The current call depth is available from the callStackDepth property.

---

### getNextTag

Method

**Return value**

A dictionary object holding the tag information, or void when the end of the
scenario is reached.

**Description**

Gets the next tag

The tag name is stored in the tagname member and the tag's attributes as
"attribute name => value". Body text is returned as a pseudo-tag with tagname="ch" (one character
in the text member), and line breaks as a pseudo-tag with tagname="r" (with eol=true at the end of a line).
If an interruption was requested with interrupt(), a pseudo-tag with tagname="interrupt"
is returned.

As a KAGParserEx extension, a taglist member is added (an array of the tag names stored
in that dictionary, in the order they were written).

KAGParser reuses the returned dictionary object internally, so copy it if you need to
keep its contents.

---

### assign

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `src` | `&nbsp;` | KAGParser object to copy from. |

**Description**

Copies the state of another KAGParser object

---

### clear

Method

**Description**

Clears the state

Resets the loaded scenario, call stack, macros and other state
to the initial state.

---

### store

Method

**Return value**

A dictionary object representing the current state (parse position, call stack, macros, etc.).

**Description**

Returns the state as a dictionary

Keep the returned dictionary and pass it to restore() to restore
the state. Useful for storing it in save data (bookmarks).

---

### restore

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `dic` | `&nbsp;` | Dictionary object returned by store(). |

**Description**

Restores a state obtained with store()

---

### clearCallStack

Method

**Description**

Clears the call stack

Discards everything pushed onto the call stack by callLabel().

---

### interrupt

Method

**Description**

Requests that parsing be interrupted

The next time getNextTag() returns a tag, a pseudo-tag with tagname="interrupt"
is returned instead of the normal tag. Use it to break out of the parse loop from
asynchronous event handling and the like.

---

### resetInterrupt

Method

**Description**

Cancels an interruption requested with interrupt()

---
