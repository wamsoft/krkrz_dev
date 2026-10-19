---
source_hash: bb70fa85cceb
---

# Overview of the Elements UI System

Kirikiri Z's [ElementsDialog](../../reference/ElementsDialog.md) (the Elements-based UI) is built from **four stacked layers**.
This page summarizes what lives in each layer, which layer to change for a given task, and which
document to read. For how to use it, see [Dialog (guide)](../../guide/ElementsDialog.md);
for the API, see the [ElementsDialog class reference](../../reference/ElementsDialog.md).

## Layer structure

```
┌─────────────────────────────────────────────────────────────┐
│ ④ ゲーム / TJS 側の UI コード                                  │
│    画面の出し入れ、ゲーム状態との接続、画面遷移の方針           │
│    ※ 共有の枠組みは無く、プロジェクトごとに書かれている         │
├─────────────────────────────────────────────────────────────┤
│ ③ krkrz 本体 ( src/core/common/visual/elements/ )             │
│    TJS ElementsDialog クラス / DrawDevice への描画接続 / 入力ルーティング │
│    複数インスタンスと z-order / モーダルの nested ループ         │
│    ホスト資源との接続 ( Storages・フォント・ソフトキーボード )    │
├─────────────────────────────────────────────────────────────┤
│ ② elements_modal ( external/elements/external/elements_modal ) │
│    画面 JSON の仕様と構築、変数 store、named action、画面遷移     │
│    overlay_session ( 描画先バッファと入力を受け取るだけの口 )     │
│    ※ 吉里吉里に依存しない。単体アプリからも同じ JSON が動く      │
├─────────────────────────────────────────────────────────────┤
│ ① elements ( cycfi/elements の派生 )                          │
│    ウィジェットの土台、レイアウト計算、フォーカス、ThorVG 描画    │
└─────────────────────────────────────────────────────────────┘
```

- **④ Game / TJS-side UI code** — showing and hiding screens, wiring to game state, screen-transition policy.
  There is no shared framework; each project writes its own.
- **③ krkrz engine** (`src/core/common/visual/elements/`) — the TJS `ElementsDialog` class, rendering into the
  `DrawDevice`, input routing, multiple instances and z-order, nested loops for modals, and connections to host
  resources (Storages, fonts, the software keyboard).
- **② elements_modal** (`external/elements/external/elements_modal`) — the screen JSON specification and
  construction, the variable store, named actions, screen transitions, and `overlay_session` (an interface that
  only receives a target buffer and input). It does not depend on Kirikiri; the same JSON also runs in a standalone app.
- **① elements** (derived from cycfi/elements) — widget foundations, layout computation, focus, ThorVG rendering.

**Layers ① and ② work independently of Kirikiri Z.** A screen JSON can be displayed and operated the same way in a
standalone host application; layer ③'s job is to place it over the game screen and connect it to the game's input and resources.

## Which layer to change (quick reference)

| What you want to do | Layer to change | Where exactly |
|---|---|---|
| Change a screen's look, layout or text | Screen JSON | The project's screen JSON |
| Add a widget / add an attribute to an existing widget | ② | `json_layout.cpp` + elements_modal README |
| Change how variable binding, input binding or screen transitions work | ② | Same as above |
| Widget rendering itself, layout computation, focus movement | ① | The elements library itself (`lib/`) |
| Add TJS API (`ElementsDialog.*`) | ③ | `DialogIntf.cpp` + `doc/manual/ElementsDialog.manual.tjs` |
| Display target (DrawDevice), input path, handling of multiple instances | ③ | `ElementsDialogManager.cpp` |
| How screens are shown and hidden, how they connect to game state | ④ | Game-side scripts |

When in doubt, ask: "**Is this feature meaningful even without Kirikiri Z?**" If it is, it belongs in
② or ①; if game-specific concerns are involved, it belongs in ③ or ④.

## Data flow

**Rendering**: At the end of each game frame, `DrawDevice::Show()` calls `PaintOverlay`;
② draws into a pixel buffer, and ③ uploads it to a texture for each DrawDevice (SDL / OpenGL /
D3D11) and displays it over the game screen. Frames that need no redraw present the previous texture
as-is, and only changed rectangles are redrawn.

**Input**: ③ intercepts the window's mouse / key / pad input and passes it to the visible dialog.
Only input that ② did not handle flows on to the game (layers) (when non-modal).

**Values**: Variables in a screen JSON all hang off a single store. From TJS you write them with
[setVar](../../reference/ElementsDialog.md#setvar), read them with [getVar](../../reference/ElementsDialog.md#getvar),
and receive changes with [onVar](../../reference/ElementsDialog.md#onvar). Button presses and value changes arrive via
[onAction](../../reference/ElementsDialog.md#onaction). **For everyday use, these four are the entire
interface between ③ and ④** (there are also entry points for "things only the host can do", such as
replacing images or atlases and reading/writing session-shared variables; see the next section).

## Design policy: keep UI logic on the screen-data side

After several projects each began writing their own UI framework in ④,
we adopted the policy that **UI logic is completed within ② and the screen JSON, and ④ only
"invokes, supplies values, and executes actions"**. The dividing principle is "**does it touch
game state?**"

| Screen-data side (② + screen JSON) | Host side (③④) |
|---|---|
| Screen transitions, tabs, list scrolling and selection | The actual settings values and save data |
| Value formatting and conditional display, focus, effects | Executing save / load, actually playing sound effects |
| Keeping values across screens (`shared_vars`) | Coordinating with the host's dialog mechanism |

As a result, the following **work with the screen JSON alone, without writing host callbacks**.

- **`"shared_vars": ["cfg_*"]`** — keeps matching variables across screens
  (sliders don't reset as you move between tabs on a settings screen)
- **`"value_var"`** — binds the ON/OFF state of a `checkbox` / `toggle_button` / `slide_switch` to a variable
- **`"image_var"`** — replaces the picture of an `image` itself via a variable (e.g. paging through a save list)
- **Replaceable atlases** — swap only a set of pictures while keeping the same screen (e.g. group tabs in a CG gallery)

The only job left for the host is "persisting into save data"; the entry points for that are
[getSharedVars](../../reference/ElementsDialog.md#getsharedvars) /
[setSharedVar](../../reference/ElementsDialog.md#setsharedvar) /
[clearSharedVars](../../reference/ElementsDialog.md#clearsharedvars),
and atlas replacement is [setAtlasImage](../../reference/ElementsDialog.md#setatlasimage).

## Documentation map

| Document | Layer | Contents |
|---|---|---|
| [Dialog (guide)](../../guide/ElementsDialog.md) | ③④ | How to use display modes, flows, lists, variables and input bindings |
| [ElementsDialog class reference](../../reference/ElementsDialog.md) | ③ | All members of the TJS API |
| [ElementsDialog.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/ElementsDialog.md) | ③ | **SSOT for the engine-side implementation**. DrawDevice connection, input routing, multiple instances, partial redraw, measurement |
| [elements_modal README](https://github.com/wamsoft/elements/blob/develop/external/elements_modal/README.md) | ② | **SSOT for the screen JSON specification**. Widget list, variable binding, themes, atlases, transitions, effects |
| [elements repository](https://github.com/wamsoft/elements) | ① | The library itself (derived from cycfi/elements) |
| [Gamepad input](gamepad.md) | ③ | Pad-to-key conversion (dialog pad navigation is built on top of this) |
| [Virtual cursor position](https://github.com/wamsoft/krkrz_develop/blob/master/doc/VirtualCursor.md) | ③ | The basis for hover detection and cursor queries. Key / pad navigation does not move the real OS cursor |

## Terminology

- **overlay** … Displayed on top of the game screen. This is the default for both non-modal and modal dialogs
- **Separate-window modal** … Opens a separate OS window and displays the dialog as blocking
- **Flow (navigator)** … A mechanism for transitioning between multiple screen JSONs. Transition targets are determined
  by declarations in the screen JSON; the host does not write transitions
- **Screen JSON** … A layout definition for one screen. It can also be written as a TJS Dictionary
- **Variable store** … Named values shared within a screen. Values are held as strings
- **Session-shared variables** … Variables kept across screens. The screen JSON's
  `"shared_vars"` declares which ones are carried over (no host implementation needed)
- **named action** … A named operation assigned to keys / pad / mouse. Built-in names are
  handled inside the dialog; others are notified to the host
