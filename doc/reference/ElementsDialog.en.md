# ElementsDialog

!!! warning "Experimental (not covered by stability guarantees)"
    The shape of this API is not settled yet. **It may change or be removed
    without notice** (the major version is not bumped even for incompatible changes).
    See [versioning](https://github.com/wamsoft/krkrz_develop/blob/master/doc/Versioning.md)
    for how versions are bumped.

    Elements ベースの UI 機構はまだ形が固まっていません。2026-09-04 にはクラス名自体を `Dialog` から改名しました ( 互換エイリアス無し )。

The ElementsDialog class drives general-purpose Elements-based dialogs from TJS

It supports both SDL3 and WINVER builds.

Pass a layout definition in JSON / JSONC ( comments and trailing commas allowed ) to
show a dialog containing buttons, checkboxes, toggles, text input, and more.
There are three operating modes.

Besides JSON / JSONC strings, layout definitions can also be passed as TJS Dictionary / Array
objects directly through the Dict methods ( [showDict](#showdict) /
[showModalDict](#showmodaldict) ).

- **Non-modal (overlay display)**
Shown with [showJson](#showjson) / [showFile](#showfile). The main
loop keeps running while it is shown, and [onAction](#onaction)
fires each time a button is pressed or a value changes. It stays until you
call [close](#close) explicitly or a close event occurs in the dialog.
- **Blocking modal (separate window)**
Calling [showModalJson](#showmodaljson) / [showModalFile](#showmodalfile) with
a title ( and width / height ) opens a new native window,
stops TJS execution until it is closed, and returns the result as a Dictionary.
- **Blocking modal (overlay on the game screen)**
Calling [showModalJson](#showmodaljson) / [showModalFile](#showmodalfile) with
only the JSON argument shows the dialog over the existing game screen without opening a separate window,
and blocks until it is closed.

Driving "flows" that move between multiple screens is also supported. Use
[showFlow](#showflow) / [showFlowScreens](#showflowscreens) for blocking execution and
[startFlow](#startflow) /
[startFlowScreens](#startflowscreens) for non-modal ( resident ) execution. On screen
transitions, [onScreen](#onscreen) / [onScreenLeave](#onscreenleave)
fire, and widget operations are still notified through [onAction](#onaction).

Multiple non-modal dialogs can be shown at the same time ( they are drawn stacked
in z-order; the mouse uses hit testing, and keyboard focus goes to the frontmost handler first ).
Setting the `grabFocus` argument to false shows the dialog as a resident HUD that does not
take focus. With `showJson(json, true, false)`
( non-modal with focus ), the panel can be operated with keys / pad while
unhandled keys pass through to the host; keys the host must always receive can be
reserved with [registerHotKey](#registerhotkey).

For details on the element types in the JSON spec ( label / button / input_box / checkbox / toggle /
text_box / text_area / vtile / htile / vspacer / hspacer, etc. ), their attributes, and
layout density settings ( `"gap"` / the top-level `"style"` block ), see the
[elements_modal README](https://github.com/wamsoft/elements/blob/develop/external/elements_modal/README.md);
for details on keyboard / gamepad configuration with the `"input"` node, see the
[keyboard navigation spec](https://github.com/wamsoft/elements/blob/develop/docs/keyboard-navigation.md).

To flow body text into a rectangle, use `text_area`. Line wrapping, line-start / line-end
breaking rules (kinsoku), and character-by-character display use the same logic as
[Layer.drawShapedTextArea](Layer.md#drawshapedtextarea), so
**the same text at the same width breaks at the same positions**.
Giving a variable name to `"count_var"` advances the character display via [setVar](#setvar);
since wrapping is fixed for the whole text, advancing does not cause reflow
( intended for subtitles and dialogue windows. The existing `text_box` is kept as is for compatibility ).

The displayed screen can be read by the OS screen reader ( Narrator / VoiceOver / Orca ).
The `"a11y"` key in the screen JSON supplies names and roles. UI drawn on the game's own
Layers can also be exposed with [setGameA11y](#setgamea11y) / [a11yLayers](#a11ylayers),
and [announce](#announce) makes the screen reader read arbitrary text. For the full specification, see
[Accessibility (screen reader) support](../specification/accessibility.md).

The ElementsDialog class is not available in executables built with `KRKRZ_USE_ELEMENTS=OFF`.
ElementsDialog is also available in the WINVER (native Windows / D3D11) build
(non-modal / overlay modal / separate-window modal / flows /
text input are all supported).

## Members

### Constructors

- [ElementsDialog](#elementsdialog)

### Properties

- [defaultFontFamily](#defaultfontfamily)
- [active](#active)
- [modalActive](#modalactive)
- [atlasCacheStats](#atlascachestats)
- [atlasCacheBudget](#atlascachebudget)
- [language](#language)
- [watchVars](#watchvars)
- [fontLanguages](#fontlanguages)
- [virtualKeyboard](#virtualkeyboard)
- [hasPhysicalKeyboard](#hasphysicalkeyboard)
- [focusRing](#focusring)
- [baseSize](#basesize)
- [renderScale](#renderscale)
- [renderCache](#rendercache)
- [partialRedraw](#partialredraw)
- [renderCount](#rendercount)
- [renderStats](#renderstats)
- [a11yActive](#a11yactive)
- [a11yMode](#a11ymode)
- [a11yLabel](#a11ylabel)
- [a11yLayers](#a11ylayers)

### Methods

- [showJson](#showjson)
- [showFile](#showfile)
- [showDict](#showdict)
- [showModalJson](#showmodaljson)
- [showModalFile](#showmodalfile)
- [showModalDict](#showmodaldict)
- [dictToJson](#dicttojson)
- [showFlow](#showflow)
- [showFlowScreens](#showflowscreens)
- [startFlow](#startflow)
- [startFlowScreens](#startflowscreens)
- [close](#close)
- [registerFont](#registerfont)
- [registerFontDir](#registerfontdir)
- [registerHotKey](#registerhotkey)
- [unregisterHotKey](#unregisterhotkey)
- [clearHotKeys](#clearhotkeys)
- [beginKeyCapture](#beginkeycapture)
- [endKeyCapture](#endkeycapture)
- [registerImage](#registerimage)
- [registerLayerImage](#registerlayerimage)
- [unregisterImage](#unregisterimage)
- [clearImages](#clearimages)
- [setSharedVar](#setsharedvar)
- [getSharedVars](#getsharedvars)
- [clearSharedVars](#clearsharedvars)
- [setAtlasImage](#setatlasimage)
- [swappableAtlases](#swappableatlases)
- [setVar](#setvar)
- [getVar](#getvar)
- [listVars](#listvars)
- [focus](#focus)
- [activate](#activate)
- [trimAtlasCache](#trimatlascache)
- [setPadIconBase](#setpadiconbase)
- [setPadTheme](#setpadtheme)
- [setPadIconAlias](#setpadiconalias)
- [renderStatsReset](#renderstatsreset)
- [announce](#announce)
- [setGameA11y](#setgamea11y)
- [clearGameA11y](#cleargamea11y)

### Events

- [onScreen](#onscreen)
- [onScreenLeave](#onscreenleave)
- [onAction](#onaction)
- [onDrag](#ondrag)
- [onVar](#onvar)
- [onClose](#onclose)
- [onKeyCapture](#onkeycapture)
- [onA11yActiveChanged](#ona11yactivechanged)
- [onGameA11yAction](#ongamea11yaction)

---

### ElementsDialog

Constructor

**Description**

Constructs an ElementsDialog object

Constructs an object of the ElementsDialog class.

---

### defaultFontFamily

Property \ Access: `r/w`

**Type**: `string`

**Description**

Default font family

Gets / sets the default font family names ( comma-separated ) for label / button, etc.,
applied to the Elements theme. Both the getter and the setter
are meaningful only after the Elements runtime has been initialized ( after the first dialog is shown ).

---

### active

Property \ Access: `r`

**Type**: `bool`

**Description**

Whether this ElementsDialog instance is active ( read-only )

True while a non-modal dialog / flow opened by this ElementsDialog is
active. Right after calling [close](#close), teardown has not finished yet,
so it stays true; it switches to false once teardown completes.

Use it for timing control, such as starting the next modal dialog only after
closing a non-modal UI.

---

### modalActive

Property \ Access: `r`

**Type**: `bool`

**Description**

Whether a modal dialog is being shown ( read-only )

True if any instance opened with the [showModalJson](#showmodaljson) family or a modal flow
is active ( it returns the process-wide state no matter which instance it is read from ).
Resident overlays that do not take focus ( subtitles, HUDs, etc. )
are not included.

Use it in a top-level hotkey ( [System.registerHotKey](System.md#registerhotkey) )
callback to decide "do nothing and pass through while a modal is shown".

**See also:** [ElementsDialog.active](ElementsDialog.md#active)

---

### atlasCacheStats

Property \ Access: `r/w`

**Type**: `Dictionary`

**Description**

Resident size of the atlas decode cache ( read-only )

Atlas images are decoded and cached keyed by "path + scale" and
reused. **They are not released when switching screens** — this avoids the case where, after long play,
the heap becomes fragmented, a large contiguous block cannot be allocated, decoding fails, and a screen
is built without its pictures. This property lets you check how much is held at scene boundaries
( it acts like a static property for the whole class ).

Returns a dictionary with `bytes` ( total bytes after RGBA expansion ) / `count` ( number of entries ) /
`budget` ( current budget ).

```tjs
var st = global.ElementsDialog.atlasCacheStats;
Debug.message("アトラス常駐 %.1f MB (%d 件)".sprintf(st.bytes / 1048576.0, st.count));
```

**See also:** [ElementsDialog.trimAtlasCache](ElementsDialog.md#trimatlascache)

---

### atlasCacheBudget

Property \ Access: `r/w`

**Type**: `Integer`

**Description**

Budget of the atlas decode cache ( bytes )

Assigning changes it **permanently**; lowering it trims the cache immediately.
Setting 0 disables the cache ( decode every time ).
The default is 192MB, large enough to keep one screen's worth of atlases loaded
( it acts like a static property for the whole class ).

**See also:** [ElementsDialog.trimAtlasCache](ElementsDialog.md#trimatlascache)

---

### language

Property \ Access: `r/w`

**Type**: `String`

**Description**

i18n display language

The key used to look up the screen JSON's top-level `strings` ( textID → per-language strings )
( it acts like a static property for the whole class ). Specify the keys used in `strings` as is,
such as `"ja"` / `"en"` / `"tc"` / `"sc"`.

```tjs
global.ElementsDialog.language = "en";     // 表示中の画面もその場で切り替わる
```

Assigning **applies immediately to all displayed dialogs** ( widgets with `text_id` / `text_list_id` /
`options_id` are re-resolved, and the display changes without reopening the screen ).
It also becomes the default for screens opened afterward. Pickers keep their selected index
and only replace the displayed strings.

Reading returns the configured language. If unset, it is an empty string ( = follows each screen JSON's
`lang` setting ). Nothing happens on screens without `strings`.

---

### watchVars

Property \ Access: `r/w`

**Description**

Targets of variable change notification

A property that narrows down / explicitly specifies the variables received by [onVar](#onvar).

- Array of variable names ... notifies only those variables
- `"*"` ... notifies all variables
- Empty array ... no notifications ( stops them explicitly )
- void ... reverts to the default

The default ( unset ) is "all variables if [onVar](#onvar) is implemented".
Variables from `"vars_on_hover"` and drag positions are rewritten every frame,
so if you only need specific variables, listing their names is lighter. Setting it while a dialog is shown
takes effect immediately.

---

### fontLanguages

Property \ Access: `r/w`

**Type**: `Object`

**Description**

Language-dependent font substitution table

A table for multilingual UIs that have separate fonts per writing system ( Noto Sans JP / TC / SC, etc. ),
used to substitute families during font resolution according to the display language
( it acts like a static property for the whole class ). Kanji at code points shared between Japanese and Chinese
can be drawn with the regional glyph forms that match the display language.

Assign a dictionary ( or a JSON string of the same shape ) keyed by language code, each with `map` ( family name or
[registerFont](#registerfont) alias → substitute family ) and `fallback` ( optional; the order of the theme's default
family chain for that language ).

```tjs
global.ElementsDialog.fontLanguages = %[
"tc" => %[ "map" => %[ "Noto Sans JP" => "Noto Sans TC" ] ],
"sc" => %[ "map" => %[ "Noto Sans JP" => "Noto Sans SC" ] ] ];
global.ElementsDialog.language = "sc";   // 以後 "Noto Sans JP" 指定は SC フォントで描画
```

`map` applies to widgets' `"font"` settings and to each family token in the theme's default chain;
`"#tag=val"` variable axis suffixes are preserved ( if JP/TC/SC are variable fonts with the same
axes, weight settings carry over as is ). The language applied is
the widget's explicit `"locale"` if present, otherwise [language](#language).
Languages with no entry in the table are not substituted.

It is the same table as the top-level `"font_languages"` in the screen JSON / app.jsonc, and entries are
merged per language ( later settings override per language ). Reading returns the last
assigned table as a JSON string ( an empty string if unset; declarations on the screen JSON side
are not included ).

`text_area` fixes its font at build time, so it does not follow language switches while displayed
( reopening the screen applies them ).

---

### virtualKeyboard

Property \ Access: `r/w`

**Type**: `String`

**Description**

Operating mode of the built-in virtual keyboard

Specifies whether to show Elements' built-in alphanumeric keyboard instead of the OS software
keyboard when a text field ( `input_box`, etc. ) receives focus.
The possible values are as follows.

| Value | Meaning |
|---|---|
| `"auto"` | Default. Shown only when no physical keyboard is connected |
| `"always"` | Always shown even with a physical keyboard ( for testing; also shown on desktop ) |
| `"never"` | Not shown ( left to the OS ). Closed if currently shown |

The initial value is `"always"` if the environment variable `KRKRZ_FORCE_VIRTUAL_KEYBOARD=1` is set,
and `"auto"` otherwise.

It appears **when an Elements text field receives focus**; it does not appear for input fields
the game draws on its own. Key presses are not buffered but fed to the input target immediately,
so the input field updates in real time.
The current version supports only uppercase alphanumeric characters.

The core demo for trying it out is `softkey_ime`.

**See also:** [ElementsDialog.hasPhysicalKeyboard](ElementsDialog.md#hasphysicalkeyboard)

---

### hasPhysicalKeyboard

Property \ Access: `r`

**Type**: `Boolean`

**Description**

Whether a physical keyboard is present

Returns whether a physical ( hardware ) keyboard is connected. Read-only.
On desktop it is always true; on game consoles, etc., it reflects whether a USB keyboard is connected.
Use it to decide whether the game should show its own software keyboard.

**See also:** [ElementsDialog.virtualKeyboard](ElementsDialog.md#virtualkeyboard)

---

### focusRing

Property \ Access: `r/w`

**Type**: `Boolean`

**Description**

Focus ring display

Controls display of the generic ring ( blue rounded rectangle ) Elements draws around the focused element
( it acts like a static property for the whole class ). The default is true.

```tjs
global.ElementsDialog.focusRing = false;    // アプリ全体で消す
```

The rings on button / slider / dial / thumbwheel all disappear together. Turn it off for image UIs that have
per-state artwork ( normal / over / pressed / disabled ) as assets, where the generic ring overlaps the
artwork and gets in the way. **Focus itself remains active**, so
key/pad navigation and switching to the hilite frame keep working as before.

This is an application-wide setting, not per screen ( a global theme flag ).

When accessing it from inside a class, write `global.ElementsDialog.focusRing`. Inside a method of a class
that inherits ElementsDialog, a bare `ElementsDialog` refers to the parent class, and assigning to the static property
fails with "member not found".

---

### baseSize

Property \ Access: `r/w`

**Type**: `Array`

**Description**

Author base surface size of the UI

Specifies the size of the base surface used as the denominator of the overlay scale ( fit ), as a `[w, h]`
array. Setting void ( or an empty array ) reverts to the default =
the game's base surface ( the size of primaryLayer ). When not set, the
getter returns void.

For titles that author the UI at a different resolution from the game screen ( e.g. game screen
640x400 / UI 1920x1080 ), setting this makes partial panels scale according to the author basis,
and they are not affected by changes to the game's primaryLayer size ( such as emulating
low-resolution hardware ). It also applies to the displayed screen from the next frame.

**See also:** [ElementsDialog.renderScale](ElementsDialog.md#renderscale)

---

### renderScale

Property \ Access: `r/w`

**Description**

Overlay rendering density mode

The rendering density mode of the overlay ( it acts like a static property for the whole class ).

- 0 ( default ) = auto: rasterizes directly at the final present size.
- >0 = draws at the authored logical size × this factor and scales at present time ( 1.0 = render at native size, then scale for display;
2.0 = equivalent to supersampling ).

It also applies to the displayed screen from the next frame ( for comparing rendering quality / load ).

---

### renderCache

Property \ Access: `r/w`

**Description**

Suppresses overlay re-rasterization

While true ( the default ), frames with no changes skip re-rasterizing the dialog ( CPU ) and
re-uploading the texture, presenting the previous rendering result as is
( it acts like a static property for the whole class ). This greatly reduces CPU load while idle.

Redrawing happens automatically for input events, focus/hover changes, while part animations are playing, actual changes via setVar,
the blinking caret in text fields, during screen transition effects, and so on.
Setting false redraws every frame as before ( for load comparison and problem isolation ).

---

### partialRedraw

Property \ Access: `r/w`

**Description**

Partial redraw of the overlay

While true ( the default ), when the changed area can be identified as a rectangle, **only that rectangle** is
re-rasterized and partially transferred to the texture ( it acts like a static property for the whole class ).
A rectangle can be identified only in limited cases such as the blinking caret in a text field; input, focus
changes, part animations, setVar, etc. still redraw the whole area as before.

It only works when [ElementsDialog.renderCache](ElementsDialog.md#rendercache) is enabled
( it relies on the previous rendering result being kept ). Setting false makes changed frames
always redraw the whole area ( for load comparison and problem isolation ). The number of times a partial redraw
actually happened can be checked in "partials" of [ElementsDialog.renderStats](ElementsDialog.md#renderstats).

---

### renderCount

Property \ Access: `r/w`

**Description**

Cumulative rasterization count ( read-only )

The cumulative number of times rasterization ( redraw ) actually happened ( shared across the whole class ).
If it does not increase while idle, renderCache is working ( for verification and load comparison ).

---

### renderStats

Property \ Access: `r/w`

**Description**

Per-stage timing of the rendering pipeline ( read-only )

Returns a breakdown of overlay rendering load as a Dictionary ( cumulative values shared across the whole class ).
All times are in microseconds:
%[ "frames" => presented frame count, "updates" => state update count,
"rasters" => rasterization count, "partials" => how many of those were partial redraws,
"cachedPresents" => presents with rasterization skipped,
"presents" => present count, "totalUs" => entire rendering process, "updateUs" => state update,
"rasterUs" => CPU rasterization, "acquireUs" => buffer acquisition,
"uploadUs" => texture transfer, "presentUs" => present ]

Since the values are cumulative, read twice, take the difference, and divide by the elapsed real time to compute
"the time and share consumed by Elements"
( reset to 0 with [ElementsDialog.renderStatsReset](ElementsDialog.md#renderstatsreset) ).
A benchmark screen for measurement is in the core demo `elements_bench`
( scenario switching + renderCache A/B + breakdown display every 500ms ).

---

### a11yActive

Property \ Access: `r`

**Type**: `bool`

**Description**

Whether a screen reader is connected ( read-only )

True if the OS screen reader, etc. has already queried the accessibility tree
( shared across the whole class ). It becomes true on the first query. On Windows,
the query arrives when the window comes to the foreground, so it is still false right after startup.

When using it to decide "read the text if connected", do not cache the value; check this property
right before reading, or receive changes with
[onA11yActiveChanged](#ona11yactivechanged).
It is always false in builds with `KRKRZ_USE_A11Y=OFF` and when [a11yMode](#a11ymode) is `"off"`.

**See also:** [ElementsDialog.onA11yActiveChanged](ElementsDialog.md#ona11yactivechanged)

---

### a11yMode

Property \ Access: `r/w`

**Type**: `String`

**Description**

Whether to expose the accessibility tree to the OS

`"auto"` ( the default ) works only when a screen reader is connected. `"off"` does not
expose it to the OS ( it acts like a static property for the whole class ). Even with `"off"`,
verification interfaces such as [Agent.a11yTree](Agent.md#a11ytree) are available.
Assigning any other string is ignored with a warning in the log.

---

### a11yLabel

Property \ Access: `r/w`

**Type**: `String`

**Description**

Name of the accessibility tree root ( window )

Set it to the game name or scene name ( it acts like a static property for the whole class ). If it is an empty string ( the default ),
the name of the frontmost screen ( `title` in the screen JSON's `"a11y"` ) is used.

---

### a11yLayers

Property \ Access: `r/w`

**Type**: `bool`

**Description**

Automatically exposes Layers in the accessibility tree

When true, the tree under the main window's primary layer is traversed and added to the game's
nodes ( default false; it acts like a static property for the whole class ).

The following Layers are exposed.

- Layers in the focus chain ( `focusable` and `joinFocusChain` ).
The name is `hint` and the role is button ( check_box for `CheckBoxLayer`,
text_input for `EditLayer` )
- Layers with `a11yName` or `a11yRole` ( they need not be focusable )
- Layers drawing an [ElementsPanel](ElementsPanel.md) ( the panel's parts are placed
under it, and operations are delivered to the panel )

Layers whose `visible` is false and Layers whose `a11yHidden` is true are not exposed, including their children.
For the members you can add to a Layer ( `a11yName` / `a11yRole` / `a11yValue` /
`a11yDescription` / `a11yStates` / `a11yHidden` / `onA11yAction` ), see
the class description of [Layer](Layer.md).

It can be combined with [setGameA11y](#setgamea11y). setGameA11y's nodes come first in order,
and focus passed to setGameA11y also takes precedence. Re-reading happens at most once every 150ms
( immediately when the focused Layer changes ), and only while a screen reader is connected or
while the REPL screen reader log is being recorded. On WINVER, continuous events keep running during that time,
even when idle.

**See also:** [ElementsDialog.setGameA11y](ElementsDialog.md#setgamea11y)

---

### showJson

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `json` | `&nbsp;` | Layout definition string in JSON / JSONC format. |
| `grabFocus` | `true` | Whether to take keyboard focus ( default true ).<br>When true, the panel takes keyboard focus, allowing text<br>input into input_box, etc., and key / pad operation of widgets.<br>When false, it does not take focus and key input goes to the host ( Window ).<br>Use this for display-only resident HUD-style panels. In this case, text input into input_box, etc.<br>in the panel is not possible. Mouse operation works regardless of grabFocus. |
| `modal` | `grabFocus` | Whether to make it modal ( exclusive input ). If omitted, it takes the same value as<br>grabFocus for backward compatibility.<br>`showJson(json, true, false)` is the in-between state "non-modal + with focus":<br>keys / pad reach the panel and can operate widgets ( pad D-pad = focus<br>navigation / A = confirm ), and only keys the panel did not handle pass through to the host<br>( [Window.onKeyDown](Window.md#onkeydown) ). This is recommended for control panels.<br>Reserve keys the host must always receive with<br>[registerHotKey](#registerhotkey).<br>Three uses: modal dialog `showJson(json)` / control panel<br>`showJson(json, true, false)` / display-only HUD `showJson(json, false)`. |

**Return value**

True if the display started successfully.

**Description**

Shows a non-modal dialog from a JSON string

Builds a dialog from the given JSON / JSONC layout definition and
shows it as an overlay on the existing game screen. The main loop keeps running
while it is shown, and [onAction](#onaction) fires on each user operation.
Call [close](#close) to end the display.

**See also:** [ElementsDialog.showFile](ElementsDialog.md#showfile) / [ElementsDialog.registerHotKey](ElementsDialog.md#registerhotkey) / [ElementsDialog.onAction](ElementsDialog.md#onaction) / [ElementsDialog.close](ElementsDialog.md#close)

---

### showFile

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `path` | `&nbsp;` | Path of the JSON / JSONC file. |
| `grabFocus` | `true` | Whether to take keyboard focus ( default true ). See [showJson](#showjson) for details. |
| `modal` | `grabFocus` | Whether to make it modal ( follows grabFocus if omitted ). See [showJson](#showjson) for details. |

**Return value**

True if the display started successfully.

**Description**

Shows a non-modal dialog from a file

Loads a JSON / JSONC layout definition from the given path and shows it the same way as
[showJson](#showjson). Paths go through Storages.

**See also:** [ElementsDialog.showJson](ElementsDialog.md#showjson)

---

### showDict

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `dict` | `&nbsp;` | Layout definition Dictionary. |
| `grabFocus` | `true` | Whether to take keyboard focus ( default true ). See [showJson](#showjson) for details. |
| `modal` | `grabFocus` | Whether to make it modal ( follows grabFocus if omitted ). See [showJson](#showjson) for details. |

**Return value**

True if the display started successfully.

**Description**

Shows a non-modal dialog from a Dictionary

A version of [showJson](#showjson) that takes the layout directly as a TJS
Dictionary / Array instead of a JSON string. It is converted to JSON internally and
shown through the same path ( the conversion rules are the same as [dictToJson](#dicttojson) ).

**See also:** [ElementsDialog.showJson](ElementsDialog.md#showjson) / [ElementsDialog.dictToJson](ElementsDialog.md#dicttojson)

---

### showModalJson

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `json` | `&nbsp;` | Layout definition string in JSON / JSONC format. |
| `title` | `""` | Title of the separate window ( if omitted, overlay mode is used ). |
| `width` | `800` | Width of the separate window in pixels ( default 800 ). |
| `height` | `600` | Height of the separate window in pixels ( default 600 ). |

**Return value**

A Dictionary holding action and values.

**Description**

Shows a modal dialog from a JSON string

Builds a dialog from the given JSON / JSONC definition and shows it blocking,
stopping TJS execution until it is closed.

- Called with only the JSON argument, it is shown as an overlay on the existing game screen
( in-game modal ).
- Passing title and later arguments opens a new separate native window to show it.

The return value is a Dictionary with the following structure.

%[
action: <id of the button that closed it ( "" for Esc / × )>,
values: %[ <id>: <value>, ... ]   // map of final values of state widgets
]

[onAction](#onaction) fires during modal display too, but the dialog
closes only when a button with `"close_on_click": true` is pressed
( or when cancelled with Esc / × ).

**See also:** [ElementsDialog.showModalFile](ElementsDialog.md#showmodalfile) / [ElementsDialog.onAction](ElementsDialog.md#onaction)

---

### showModalFile

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `path` | `&nbsp;` | Path of the JSON / JSONC file. |
| `title` | `""` | Title of the separate window ( if omitted, overlay mode is used ). |
| `width` | `800` | Width of the separate window in pixels ( default 800 ). |
| `height` | `600` | Height of the separate window in pixels ( default 600 ). |

**Return value**

A Dictionary holding action and values.

**Description**

Shows a modal dialog from a file

Loads a JSON / JSONC layout definition from the given path and shows it the same way as
[showModalJson](#showmodaljson). Paths go through Storages.

**See also:** [ElementsDialog.showModalJson](ElementsDialog.md#showmodaljson)

---

### showModalDict

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `dict` | `&nbsp;` | Layout definition Dictionary. |
| `title` | `""` | Title of the separate window ( if omitted, overlay mode is used ). |
| `width` | `800` | Width of the separate window in pixels ( default 800 ). |
| `height` | `600` | Height of the separate window in pixels ( default 600 ). |

**Return value**

A Dictionary holding action and values.

**Description**

Shows a modal dialog from a Dictionary

A version of [showModalJson](#showmodaljson) that takes the layout directly as a TJS Dictionary /
Array. As with [showModalJson](#showmodaljson), calling it with one argument shows an overlay,
passing title and later arguments shows a separate window, and the return value has the same format.

**See also:** [ElementsDialog.showModalJson](ElementsDialog.md#showmodaljson) / [ElementsDialog.showDict](ElementsDialog.md#showdict)

---

### dictToJson

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `value` | `&nbsp;` | Value to convert ( Dictionary / Array / primitive type ). |

**Return value**

A JSON string.

**Description**

Converts a Dictionary / Array to a JSON string

A utility that directly invokes the conversion [showDict](#showdict) / [showModalDict](#showmodaldict)
perform internally. Use it to save a layout built as a Dictionary as a JSON asset,
or to check the conversion result. It can be called as `ElementsDialog.dictToJson(...)`
without creating an instance.

Supported value types are void / Integer / Real / String / Dictionary / Array.
Anything else ( Octet, general objects, circular references, non-finite reals )
throws an exception.

**See also:** [ElementsDialog.showDict](ElementsDialog.md#showdict)

---

### showFlow

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `manifestPath` | `&nbsp;` | Storages path of the app.jsonc manifest. |

**Return value**

A Dictionary holding action and values.

**Description**

Shows a multi-screen flow from a manifest, blocking

Loads a manifest in `app.jsonc` format ( a path through Storages ) and runs
a flow with transitions between multiple screens as an overlay on the existing game screen.
It stops TJS execution until the flow ends, and returns the Dictionary
`%[ action, values ]` of the last screen that closed.

[onScreen](#onscreen) / [onScreenLeave](#onscreenleave) fire on each screen switch,
and [onAction](#onaction) fires on each widget operation.

Writing a `transitions` entry in the screen JSON in object form declares
a transition effect for the screen switch ( `effect: "fade"` = crossfade /
`effect: "universal"` = universal transition using a rule image.
`duration` = time in ms ( 200 if omitted ); for universal, also specify `rule` =
rule image path ( relative to the declaring screen / Storages path / autopath search ),
and `vague` = edge blur width 0–255 ( 64 if omitted ) ).

```json
"transitions": {
"next": { "target": "s2", "effect": "fade", "duration": 300 },
"back": { "target": "<back>", "effect": "universal",
"rule": "rule.png", "vague": 64, "duration": 500 }
}
```

**See also:** [ElementsDialog.showFlowScreens](ElementsDialog.md#showflowscreens) / [ElementsDialog.startFlow](ElementsDialog.md#startflow)

---

### showFlowScreens

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `screensDict` | `&nbsp;` | Dictionary mapping screen names ( strings ) to layout definitions ( JSON strings, or Dictionary / Array ). Both forms can be mixed. |
| `entry` | `&nbsp;` | Name of the starting screen ( a key of screensDict ). |

**Return value**

A Dictionary holding action and values.

**Description**

Shows a multi-screen flow from inline definitions, blocking

An inline version of [showFlow](#showflow) that runs a flow from a Dictionary mapping
screen names to layout definitions, without file I/O.
Behavior and return value are the same as [showFlow](#showflow).

**See also:** [ElementsDialog.showFlow](ElementsDialog.md#showflow) / [ElementsDialog.startFlowScreens](ElementsDialog.md#startflowscreens)

---

### startFlow

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `manifestPath` | `&nbsp;` | Storages path of the app.jsonc manifest. |
| `grabFocus` | `true` | If true, takes keyboard / gamepad focus ( default true ). If false, it is shown as a resident HUD that does not take focus. |

**Return value**

True if it started successfully.

**Description**

Starts a non-modal ( resident ) multi-screen flow

Starts the same manifest as [showFlow](#showflow) non-modally ( non-blocking ) and
returns immediately. Because it can stay on the game screen while progressing,
it suits resident UI such as main menus and HUDs.

Screen transitions are defined by `transitions` on the JSON side. To handle button presses
and the like on the TJS side, dispatch in [onAction](#onaction) for buttons
without `"close_on_click"`. Call [close](#close) to end it explicitly,
and check [active](#active) to see whether teardown has completed.

**See also:** [ElementsDialog.startFlowScreens](ElementsDialog.md#startflowscreens) / [ElementsDialog.showFlow](ElementsDialog.md#showflow) / [ElementsDialog.active](ElementsDialog.md#active)

---

### startFlowScreens

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `screensDict` | `&nbsp;` | Dictionary mapping screen names ( strings ) to JSON strings. |
| `entry` | `&nbsp;` | Name of the starting screen ( a key of screensDict ). |
| `grabFocus` | `true` | If true, takes keyboard / gamepad focus ( default true ). If false, it is shown as a resident HUD that does not take focus. |

**Return value**

True if it started successfully.

**Description**

Starts a non-modal ( resident ) multi-screen flow from inline definitions

An inline version of [startFlow](#startflow) that starts screen definitions in the same Dictionary format as
[showFlowScreens](#showflowscreens) non-modally ( non-blocking ).

**See also:** [ElementsDialog.startFlow](ElementsDialog.md#startflow) / [ElementsDialog.showFlowScreens](ElementsDialog.md#showflowscreens)

---

### close

Method

**Description**

Closes the dialog

Closes the non-modal / modal dialog ( including flows ) opened by this instance.
It does not close dialogs opened by other instances.

The internal teardown happens on the next frame, so [active](#active) stays true
for a while even right after calling close. To safely start
the next modal, wait until [active](#active) becomes false.

If elements on the screen have `"animate"` with `"on": "exit"` ( an exit animation ),
close also plays the exit animation and closes after it finishes ( [active](#active)
stays true in the meantime ). close during a flow does not resolve screen transitions
( transitions ) and ends the whole flow.

**See also:** [ElementsDialog.active](ElementsDialog.md#active)

---

### registerFont

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `family` | `&nbsp;` | Family name to register under. |
| `path` | `&nbsp;` | Storages path of the font file ( .ttf / .otf ). |
| `weight` | `40` | weight value ( default 40 = normal ). |
| `slant` | `0` | slant value ( default 0 = normal ). |
| `stretch` | `50` | stretch value ( default 50 = normal ). |

**Return value**

The family name actually registered ( the ThorVG embedded name takes precedence ).

**Description**

Registers a font for Elements

Registers a font used by Elements dialogs through krkrz Storages.
Returns the embedded family name ThorVG read from the file ( an empty string if it
could not be read ). Scripts can use this return value
to incorporate the font into a theme or for logging.

weight / slant / stretch are integer values from font_constants ( see
`StoragesResourceLoader.h` for details ).

**See also:** [ElementsDialog.registerFontDir](ElementsDialog.md#registerfontdir)

---

### registerFontDir

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `dir` | `&nbsp;` | Storages path of the directory to register. |

**Return value**

The number of fonts registered. 0 = none were registered
( the directory or fonts do not exist ). No exception is thrown;
a warning is logged instead.

**Description**

Registers Elements fonts in bulk

Enumerates and registers all .ttf / .otf files under the given directory ( family / weight / slant / stretch
are inferred from the file names ). dir is a path through Storages;
both relative paths ( "font/" ) and normalized paths such as `System.exePath + "data/font/"`
work. To point to a directory inside an XP3, name the archive explicitly, as in
`"data.xp3>font/"`
( mounting it with addAutoPath alone does not allow directory enumeration ).
Passing an OS path ( "D:/foo/font/" ) as is registers 0 fonts.

**See also:** [ElementsDialog.registerFont](ElementsDialog.md#registerfont)

---

### registerHotKey

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `key` | `&nbsp;` | Virtual key code ( VK_ESCAPE, etc. ). Besides keys, pad buttons<br>( VK_PAD1 to VK_PAD12, etc. ) and mouse buttons ( VK_LBUTTON / VK_RBUTTON /<br>VK_MBUTTON / VK_XBUTTON1 / VK_XBUTTON2 ) can be specified in the same space.<br>Registering printable keys is not recommended ( the onKeyPress character event is not<br>suppressed ). |
| `shift` | `0` | Combination of modifier keys ( ssShift \| ssAlt \| ssCtrl, default 0 ).<br>Key down is matched exactly; the matching up is bypassed by key alone. |
| `duringTextInput` | `false` | If true, it stays active even while the caret is in a text input widget<br>( input_box, etc. ) in the dialog. With the default false, it is suppressed<br>during text input so it does not steal ESC / BackSpace, etc. from the input field. |

**Return value**

No return value. Registering the same ( key, shift ) again
overwrites duringTextInput.

**Description**

Registers a host hotkey

A bypass mechanism for "giving the dialog focus, while still always receiving certain keys
on the host side". Registered keys are not passed to the dialog and
go straight to the normal game input path
( [Window.onKeyDown](Window.md#onkeydown) /
[Window.onMouseDown](Window.md#onmousedown), etc. )
( there is no dedicated event ).

Input is delivered in the following priority order.

1. Modal dialogs ( take all input; take precedence over hotkeys )
2. Host hotkeys ( bypass dialogs and go to the host )
3. Non-modal panels with focus ( only unhandled keys pass through )
4. Game / layers

It is intended to make ESC for returning from a scene, or PageUp/Down for switching screens,
work reliably even while a control panel containing sliders etc. ( `showJson(json, true, false)` )
is shown.

**See also:** [ElementsDialog.unregisterHotKey](ElementsDialog.md#unregisterhotkey) / [ElementsDialog.clearHotKeys](ElementsDialog.md#clearhotkeys) / [ElementsDialog.showJson](ElementsDialog.md#showjson)

---

### unregisterHotKey

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `key` | `&nbsp;` | Virtual key code. |
| `shift` | `0` | Combination of modifier keys ( default 0 ). |

**Description**

Unregisters a host hotkey

Unregisters a hotkey registered with [registerHotKey](#registerhotkey)
( removes the entry whose key and shift both match ).

**See also:** [ElementsDialog.registerHotKey](ElementsDialog.md#registerhotkey)

---

### clearHotKeys

Method

**Description**

Unregisters all host hotkeys

Unregisters all hotkeys registered with [registerHotKey](#registerhotkey).

**See also:** [ElementsDialog.registerHotKey](ElementsDialog.md#registerhotkey)

---

### beginKeyCapture

Method

**Return value**

True if capture started. False when the dialog is not shown ( not active ).

**Description**

Starts key capture

A method for "receiving the next pressed key as is". Use it when you want TJS to decide
on a key instead of letting it operate widgets ( focus movement, confirm, closing with Esc, etc. ),
such as showing "Press the key to assign" on a key binding settings screen.

While the capturing dialog has keyboard focus, all key presses go to
[onKeyCapture](#onkeycapture) and are not passed to widgets.

- It takes precedence over keys registered with [registerHotKey](#registerhotkey), even on top of a modal.
However, top-level hotkeys from [System.registerHotKey](System.md#registerhotkey)
take effect first.
- Presses of Shift / Ctrl / Alt alone, gamepad buttons ( `VK_PAD*` ),
and auto-repeat ( with `ssRepeat` ) are also delivered. The receiver decides whether to ignore repeats.
- Presses of mouse buttons other than left ( right / middle / X ) are also delivered as `VK_RBUTTON`, etc.
( e.g. right-click to cancel ). Left clicks go to widgets as usual.
- Key release events and character input are discarded during capture.
- Even if capture ends ( or the dialog closes ) while the captured key is held down, repeats
do not leak to the screen behind.

Capture ends when you call [endKeyCapture](#endkeycapture) or close the dialog.

A typical use is to overlay a modal dialog containing only explanatory text on top of the settings screen
and capture in that dialog. You may call [close](#close) from within
[onKeyCapture](#onkeycapture).

```tjs
var dlg = new ElementsDialog();
dlg.onKeyCapture = function(key, shift) {
if (shift & ssRepeat) return;          // リピートは無視
if (key == VK_RBUTTON) { close(); return; }   // 右クリックで取り消し
assignKey(key);
close();
} incontextof dlg;
dlg.showJson(promptJson);
dlg.beginKeyCapture();
```

**See also:** [ElementsDialog.endKeyCapture](ElementsDialog.md#endkeycapture) / [ElementsDialog.onKeyCapture](ElementsDialog.md#onkeycapture)

---

### endKeyCapture

Method

**Return value**

True if it ended. False when the dialog is not shown ( not active ).

**Description**

Ends key capture

Ends the capture started with [beginKeyCapture](#beginkeycapture). It ends automatically
when the dialog closes, so you do not need to call it in that case.

**See also:** [ElementsDialog.beginKeyCapture](ElementsDialog.md#beginkeycapture)

---

### registerImage

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Name in the store ( referenced as `mem://<name>` ). |
| `path` | `&nbsp;` | Unified storage path of the image to register. |

**Return value**

Whether loading and registration succeeded.

**Description**

Registers a runtime image

Registers the file at unified storage path path in the runtime image store under name. From jsonc
image widgets, etc., refer to it as `"mem://<name>"`. This is the mechanism for passing images that change
at runtime, such as save thumbnails, to Elements. If the displayed screen has an image widget for
`mem://<name>`, it is re-decoded and updated immediately when re-registered
( no need to reopen the screen; panels are updated too ). Widgets built before registration
stay empty, so register the first time before opening the screen.

---

### registerLayerImage

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Name in the store (referenced as `mem://<name>`). |
| `layer` | `&nbsp;` | Layer to take the pixels from. Passing anything other than a Layer throws an exception. |
| `left` | `0` | Left edge of the range to take (default 0). |
| `top` | `0` | Top edge of the range to take (default 0). |
| `width` | `&nbsp;` | Width of the range to take (default: up to the right edge of the image). The range is clipped to the image. |
| `height` | `&nbsp;` | Height of the range to take (default: up to the bottom edge of the image). |

**Return value**

Whether the image was registered. False if there is no image or the range is empty.

**Description**

Registers a layer's pixels as a runtime image

Registers the pixels of the layer's image (its main image) in the runtime image store under name, without encoding them or going through a file. This is meant for passing pictures drawn in TJS (such as text drawn with TextRender in the same typeface as the message window) each time a list scrolls. Referencing it (`"mem://<name>"`), having a displayed image update immediately when re-registered, and removing it with [unregisterImage](#unregisterimage) all work the same as with [registerImage](#registerimage). One name holds either an image file or layer pixels, not both; registering again replaces it, including its kind.

How alpha is handled depends on the layer type. `ltAddAlpha` is taken as already premultiplied, `ltOpaque` ignores alpha and is treated as opaque, and any other type is treated as non-premultiplied alpha and is premultiplied when registered.

**See also:** [ElementsDialog.registerImage](ElementsDialog.md#registerimage)

---

### unregisterImage

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Name of the image to remove. |

**Description**

Removes a runtime image

Removes name registered with [registerImage](#registerimage) from the runtime image store.

---

### clearImages

Method

**Description**

Clears all runtime images

Clears the entire runtime image store.

---

### setSharedVar

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Variable name. |
| `value` | `&nbsp;` | Value to set ( string ). |

**Description**

Writes a session shared variable

Writes a "variable kept across screens" declared by `"shared_vars"` in the screen JSON.
The variable store is recreated for each screen, but variables matching a `"shared_vars"` pattern
( exact match, or prefix match with a trailing `*` ) are synchronized both ways with the session shared store
and carried over to the next screen opened. It can be written even before a screen is built.

The screen decides which values to carry, so no host implementation is needed, but use this method
when saving to game save data / feeding values back after loading.

---

### getSharedVars

Method

**Return value**

Dictionary of variable name => value.

**Description**

Gets all session shared variables

Returns the current values of session shared variables as a dictionary ( variable name => value ). Intended for
writing to save data. Values are strings.

Only values "written as a change" reach the shared side; widget initial values
( `"initial"` / `"value"` ) do not. This avoids "items nobody touched" being fixed
to the defaults of the first screen opened.

---

### clearSharedVars

Method

**Description**

Discards all session shared variables

Empties the session shared store. Call it when returning to the title screen, right before
loading save data, and so on.

---

### setAtlasImage

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Atlas name declared in the screen JSON. |
| `path` | `&nbsp;` | Path of the replacement image ( relative to the screen's `resource_base` ). |

**Return value**

Whether it was swapped ( false if not declared or loading failed; the display does not change ).

**Description**

Swaps the image of a swappable atlas

Swaps the image of an atlas declared with `"swappable": true` in the screen JSON's `"atlases"`
for another image at runtime. Widgets are not rebuilt, so layout and
focus are preserved. It is meant for switching "the same screen with a different set of pictures",
such as group tabs in a CG gallery.

The replacement must have **the same rectangle layout**. The frames / rect held by widgets
do not change, so if picture positions differ, the wrong picture is shown.

---

### swappableAtlases

Method

**Return value**

Array of atlas names.

**Description**

Gets the list of swappable atlas names

Returns an array of atlas names that can currently be swapped with [setAtlasImage](#setatlasimage).
Intended for checking from a verification panel or the REPL.

---

### setVar

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Variable name. |
| `value` | `&nbsp;` | Value to set ( string ). |

**Return value**

Whether it was written.

**Description**

Writes a variable of the displayed dialog

Writes a value to the variable store of the displayed dialog. Labels, etc. with `"text_var": name` in the JSON
are updated on the next frame. Returns false if this instance is not active.

---

### getVar

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Variable name. |

**Return value**

The variable's value ( string ). void for an unknown variable.

**Description**

Reads a variable of the displayed dialog

Reads a value from the variable store of the displayed dialog. Not only values written with [setVar](#setvar)
but also values written by the screen ( `"vars_on_hover"` /
`"vars_on_focus"` / a slider's `"value_var"` / `"drag_at_var"` /
a list's `"index_offset_var"`, etc. ) can be read from the same store.

Returns void for an unknown variable name or if this instance is not active
( distinguishable from an empty string ). To be notified when it changes,
implement [onVar](#onvar).

---

### listVars

Method

**Return value**

An array of variable descriptor Dictionaries. An empty array when not active.

**Description**

Gets the list of variables of the displayed dialog

Returns the variables used by the displayed dialog as an array sorted by name. Each element is a
Dictionary with `name` / `value` / `usedBy`; `usedBy` is an array of Dictionaries with
`id` ( the id of the nearest ancestor widget ) and `kind` ( the referencing JSON
key, such as `"text_var"` / `"visible_var"` / `"value_var"` ).

Variables that are referenced but never written, and conversely variables with no references that were
created with [setVar](#setvar), are also listed. Use it for debug panels and for verifying
screen JSON.

---

### focus

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` | id of the widget to focus. |

**Return value**

Whether the request was made. false when not active.

**Description**

Moves focus to the widget with the given id

Moves focus to a widget ( specified by `"id"` in the JSON ) of the displayed dialog.
An input_box receives editing focus ( caret shown + accepts text ).
It is intended for explicitly moving the input target after rearranging the screen,
such as with `at_var` park / unpark.

The return value indicates whether the focus move could be requested from the instance; it does not check
whether the id exists. Returns false if this instance is not active.

---

### activate

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` | id of the widget to activate. |

**Return value**

Whether it was activated. false for an unknown id or when not active.

**Description**

Activates the widget with the given id

Moves focus to a widget ( specified by `"id"` in the JSON ) of the displayed dialog and
activates it ( equivalent to Enter ). It is the instance version of [Agent.dialogClick](Agent.md#dialogclick)
and has the same shape as [ElementsPanel.activate](ElementsPanel.md#activate).

**See also:** [ElementsDialog.focus](ElementsDialog.md#focus)

---

### trimAtlasCache

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `budget` | `&nbsp;` | Upper limit to trim to ( bytes ). 0 / omitted releases everything not in use. |

**Return value**

The number of bytes freed.

**Description**

Trims the atlas decode cache

Trims the atlas decode cache down to `budget` bytes.
Passing 0 ( the default ) releases "everything not in use".
The return value is the number of bytes freed.

⚠ **Atlases used by the displayed screen are still referenced and cannot be discarded.**
Call it at scene boundaries ( after closing the screen ).

```tjs
dlg.close();
var freed = global.ElementsDialog.trimAtlasCache();   // 使っていない分を全部
```

The budget itself does not change ( a temporary trim ). To lower it permanently,
assign to [atlasCacheBudget](#atlascachebudget).

**See also:** [ElementsDialog.atlasCacheStats](ElementsDialog.md#atlascachestats)

---

### setPadIconBase

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `dir` | `&nbsp;` | Base directory of the pad_icon assets ( unified storage path ). |

**Description**

Sets the base directory for pad_icon

Sets the base directory for pad_icon ( Kenney input prompts ). dir is a unified storage
path ( may be inside an XP3 ). It expects xbox/ps/switch/keyboard directories, each with vector/*.svg,
under it. If left unset, pad_icon shows a gray placeholder.

---

### setPadTheme

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Theme name. |

**Return value**

Whether the name was recognized.

**Description**

Sets the global pad_icon theme

Sets the global pad_icon theme ( `"xbox"` / `"ps"` / `"switch"` / `"keyboard"` / `"none"` ).
Specifying `"auto"` selects the theme automatically from the family of the connected pad
( [System.padStyle](System.md#padstyle) ). On platforms where the family
cannot be determined ( such as Windows ), it becomes `"xbox"` if at least one pad
is connected, and `"keyboard"` if none
( showing pad pictures with no pad connected would not tell the user which keys to press ).

The `"auto"` decision watches the number and family of connected pads and **re-decides
as soon as they change**. Plugging or unplugging a controller does not require reopening the screen;
pad_icons on the displayed screen switch to the new theme's pictures on the next draw.
If the screen JSON specifies a top-level `"pad_theme"`, that takes precedence.

**See also:** [ElementsDialog.setPadIconAlias](ElementsDialog.md#setpadiconalias)

---

### setPadIconAlias

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `theme` | `&nbsp;` | Target theme name ( `"xbox"` / `"ps"` / `"switch"` / `"keyboard"` ). |
| `name` | `&nbsp;` | Logical name to override. An empty string removes all overrides for that theme. |
| `basename` | `&nbsp;` | Basename of the asset to assign. An empty string / omitted removes the override for that name. |

**Return value**

Whether the theme name was recognized.

**Description**

Overrides pad_icon name resolution per theme

Overrides, per theme, the mapping from pad_icon logical names ( `"a"` / `"b"` / `"dpad"`, etc. ) to actual asset file names
( basenames in the Kenney pack ). Use it when the default table
( `"a"` = Enter / `"b"` = Esc / `"dpad"` = arrows … ) differs from the title's actual key
bindings.

```tjs
// キャンセルが Esc ではなく BackSpace のタイトル
global.ElementsDialog.setPadIconAlias("keyboard", "b", "keyboard_backspace");
```

Overrides take precedence over the default table. Passing an empty basename removes only the override
for that name; passing an empty name removes all overrides for that theme. Either way,
the change applies to the displayed screen from the next draw.

**See also:** [ElementsDialog.setPadTheme](ElementsDialog.md#setpadtheme)

---

### renderStatsReset

Method

**Description**

Resets the rendering measurement counters

Resets the cumulative counters of [ElementsDialog.renderStats](ElementsDialog.md#renderstats) to 0.
Call it at the start of a measurement interval.

---

### announce

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `text` | `&nbsp;` | String to read. |
| `assertive` | `false` | If true, requests an interruption ( default false ). How it is actually handled<br>depends on the screen reader. |

**Description**

Makes the screen reader read text

Makes the screen reader read text aloud ( it acts like a static method for the whole class ).
The text goes into the live region of the frontmost dialog, or into the game's own
live region if there are no dialogs. The same text is read every time, even if passed repeatedly.

It is accepted even when no screen reader is connected ( the latest state is passed on
once one connects ). While the REPL is running, it is also recorded in the screen reader log ( [Agent.a11yLog](Agent.md#a11ylog) ).

```tjs
global.ElementsDialog.announce("セーブしました");
global.ElementsDialog.announce("体力が残りわずかです", true);   // 割り込み
```

For the full specification, see [Accessibility (screen reader) support](../specification/accessibility.md).

**See also:** [ElementsDialog.a11yActive](ElementsDialog.md#a11yactive)

---

### setGameA11y

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `nodes` | `&nbsp;` | Array of node dictionaries. |
| `focus` | `&nbsp;` | `id` of the node to place focus on ( none if omitted ). |

**Description**

Exposes the game's own UI in the accessibility tree

Choices, menus, settings screens, etc. drawn on Layers are outside Elements,
so scripts pass a table of nodes to expose them in the accessibility tree ( it acts like a static method
for the whole class ). Each call replaces the whole table ( the engine computes the differences ).

```tjs
global.ElementsDialog.setGameA11y([
%[ id:"choices", role:"list", name:"選択肢" ],
%[ id:"c1", role:"list_item", name:"北へ行く", parent:"choices", rect:[100,400,600,48] ],
%[ id:"c2", role:"list_item", name:"南へ行く", parent:"choices", rect:[100,460,600,48] ],
%[ id:"vol", role:"slider", name:"音量", value:"50%", num_value:50, num_min:0, num_max:100 ],
], "c1");
```

Keys of a node dictionary:

- `id` ... required. A unique string. Nodes with an empty or duplicate id are skipped with a log message
- `role` ... `button` / `toggle_button` / `check_box` / `radio_button` / `tab` /
`menu_item` / `list` / `list_item` / `slider` / `spin_button` / `text_input` /
`label` / `heading` / `image` / `status` / `group` ( omitted or unknown values become group )
- `name` / `value` / `description` ... name / value / supplementary description
- `states` ... an array or the form `"focusable,checked"`. `focusable` / `disabled` /
`checked` / `selected` / `expanded` / `read_only`
- `rect` ... primary layer coordinates `[x, y, w, h]`. If omitted, the rectangle enclosing the children.
The engine converts for window scaling and letterboxing
- `parent` ... `id` of the parent. Top level if omitted
- `num_value` / `num_min` / `num_max` / `num_step` ... numeric values for slider / spin_button

The game's nodes are placed below the dialogs and are hidden while a modal dialog
is shown. Operations from the screen reader are delivered to
[onGameA11yAction](#ongamea11yaction). The engine does not move focus or values
by itself, so have the script change the game state and then call
`setGameA11y` again. Only the main window is supported.

**See also:** [ElementsDialog.clearGameA11y](ElementsDialog.md#cleargamea11y) / [ElementsDialog.a11yLayers](ElementsDialog.md#a11ylayers)

---

### clearGameA11y

Method

**Description**

Removes all of the game's nodes

Removes all nodes exposed with [setGameA11y](#setgamea11y). The game's
container and the live region used by [announce](#announce) remain.

---

### onScreen

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Name of the entered screen ( the screen key in the manifest ). |

**Description**

Flow screen transition notification ( entered a screen )

Fires when a screen of a flow run with [showFlow](#showflow) / [startFlow](#startflow), etc.
is entered. Override it on the TJS side.

**See also:** [ElementsDialog.onScreenLeave](ElementsDialog.md#onscreenleave)

---

### onScreenLeave

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Name of the screen left ( the screen key in the manifest ). |
| `action` | `&nbsp;` | id of the button that caused leaving the screen ( empty string for Esc / × ). |

**Description**

Flow screen transition notification ( left a screen )

Fires when leaving a screen of a flow run with [showFlow](#showflow) / [startFlow](#startflow), etc.
Override it on the TJS side.

**See also:** [ElementsDialog.onScreen](ElementsDialog.md#onscreen)

---

### onAction

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` | id string of the source widget. |
| `payload` | `&nbsp;` | Value passed by the widget ( see above ). |

**Description**

Notification of operations on the dialog

An event that receives actions occurring on the dialog ( button clicks and value
changes of state widgets ). Override it on the TJS side.

In non-modal mode ( [showJson](#showjson) / [showFile](#showfile) ) it
fires the whole time the dialog is shown. In modal mode ( [showModalJson](#showmodaljson) /
[showModalFile](#showmodalfile) ) too, actions that occur before the dialog closes with
`"close_on_click": true` are notified to this event in order.

The content of payload depends on the widget type.

- button click ... void
- checkbox / toggle ... bool ( the new value )
- input_box ... string ( the edited text )
- slider, etc. ... the value each widget passes

---

### onDrag

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `payload` | `&nbsp;` | Dictionary describing the drag state ( see above ). |

**Description**

Drag notification

An event that receives press → move → release on widgets with
`"drag_events": true` in the screen JSON. Override it on the TJS side.

payload is a Dictionary with `id` ( id of the source widget ), `phase`
( `"begin"` / `"move"` / `"end"` ), `x` / `y` ( current position ), `dx` / `dy`
( delta from the previous event ), `startX` / `startY` ( press position ), and `modifiers`
( shift state ). Coordinates are in the coordinate system written in the screen JSON.

Accumulated `"move"` events are collapsed into the latest one ( `"begin"` / `"end"` are
not collapsed ).

**You do not need this event just to make a picture follow the drag**. Write
`"drag_at_var"` on the widget to output the drag position to a variable, and plug the same variable into
the canvas child's `"at_var"`; it is then handled entirely within the engine ( `"drag_bounds"` can also
limit the movable range ). Use this event when TJS needs to make decisions such as
"where was it released".

---

### onVar

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Name of the changed variable. |
| `value` | `&nbsp;` | The new value ( string ). |

**Description**

Variable change notification

An event delivered when a value in the variable store of the displayed dialog changes.
Override it on the TJS side. It fires not only for your own writes through [setVar](#setvar)
but also for values written by the screen ( `"vars_on_hover"` / `"vars_on_focus"` /
a slider's `"value_var"` / `"drag_at_var"` / a list's `"index_offset_var"`,
etc. ).

Use it in setups where "the picture is on a host-side layer and only hit testing is in the dialog",
to connect hover and selection changes to host processing ( e.g. a list of
large single images that are too big to fit in an atlas ).

Notifications are delayed by one frame, and consecutive changes to the same variable ( hover movement or
coordinate writes during a drag ) are collapsed into the latest one. When you need "the current value",
read it with [getVar](#getvar) instead of waiting for the notification.

**Only dialogs that implement this event are observed**.
Dialogs that do not implement it incur no cost at all. To narrow down
the variables you receive, use [watchVars](#watchvars).

---

### onClose

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `action` | `&nbsp;` | id of the button that triggered the close ( when closed via `close_on_click` / Esc;<br>empty string when closed explicitly with [close](#close), etc. ). |

**Description**

Dialog teardown completion notification

A non-blocking event that fires when this instance's dialog has fully closed
( teardown complete ). Override it on the TJS side.

---

### onKeyCapture

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `key` | `&nbsp;` | VK code. Mouse buttons other than left are `VK_RBUTTON` / `VK_MBUTTON` /<br>`VK_XBUTTON1` / `VK_XBUTTON2`; gamepad buttons are `VK_PAD*`. |
| `shift` | `&nbsp;` | Combination of `ss*`. Auto-repeat has `ssRepeat`. |

**Description**

Captured key

An event that receives keys pressed during capture started with [beginKeyCapture](#beginkeycapture).
Override it on the TJS side. By default it does nothing.

**See also:** [ElementsDialog.beginKeyCapture](ElementsDialog.md#beginkeycapture)

---

### onA11yActiveChanged

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `active` | `&nbsp;` | True if connected. |

**Description**

The screen reader connection state changed

Called when [a11yActive](#a11yactive) changes. Receive it by assigning a function to the `ElementsDialog` class
( it is called outside rendering, and immediately even on a static WINVER screen ).

```tjs
global.ElementsDialog.onA11yActiveChanged = function(active) {
Debug.message("スクリーンリーダー: " + (active ? "接続" : "切断"));
};
```

---

### onGameA11yAction

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` | `id` of the operated node. |
| `action` | `&nbsp;` | `"click"` / `"focus"` / `"increment"` / `"decrement"` / `"set_value"`. |
| `arg` | `&nbsp;` | Value for `"set_value"` ( string ). |

**Description**

Operation on a node of the game

Called when the screen reader operates a node from [setGameA11y](#setgamea11y).
Receive it by assigning a function to the `ElementsDialog` class. Regardless of which thread
the operation came from, it is called on the main thread outside rendering.

action is determined by the node's role. Pressable roles ( button / check_box /
list_item, etc. ) receive `"click"`; slider / spin_button receive `"increment"` /
`"decrement"` / `"set_value"`; text_input receives `"set_value"`. Every role
receives `"focus"`, and `disabled` nodes receive only `"focus"`.

```tjs
global.ElementsDialog.onGameA11yAction = function(id, action, arg) {
if (action == "focus") { selectChoice(id); updateA11y(); }
else if (action == "click") { decideChoice(id); }
};
```

---
