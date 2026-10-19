---
source_hash: c833111d89e0
---

# Adding/Editing Engine Settings
## The old method
In Kirikiri 2, the engine obtained a "|"-delimited string (other delimiters were also used) from TVPGetCommandDesc and displayed the engine setting items based on it.  
Plugins put --has-option-- in their comment section and exported a GetOptionDesc function that returned the setting details in the same string format as the engine.  
--has-option-- was added with the linker's /COMMENT: option, but recent versions of Visual Studio ignore it, so it could no longer be embedded in a DLL binary the usual way.

## The method since Kirikiri Z
In Kirikiri Z, the list of setting items is JSON and is stored in resources instead of being embedded in source code.  
The JSON format should be mostly self-explanatory from the files.

### Engine definition files (SSOT) and language selection

The engine's definitions live in four files that are the SSOT: `src/core/resource/optiondesc.json` ( Japanese = base ) and its per-language
files `optiondesc-en.json` / `optiondesc-chs.json` / `optiondesc-cht.json` ( the `win32/vcproj/option_desc_*.json`
files formerly maintained separately for WINVER were removed in 2026-08 and merged into these ). When editing, keep the structure
( order of categories and options ) consistent across all four languages.

The language is chosen at load time ( OS language = `System.systemLanguage`, or the
command-line option `-language`. If no file exists for that language, it falls back to en and then to the base ):

- SDL3 build … reads `resource/optiondesc<language suffix>.json` directly
- WINVER build … `resource/*` is embedded in the exe as **BINARY** resources under
  their file names, and one is chosen by the same rules. If none is found, it falls back to the old
  TEXT resource ( `IDR_OPTION_DESC_JSON`, whose content is `resource/optiondesc.json` )
  ( a safeguard for when `KRKRZ_RESOURCE_DIR` is pointed at a different resource set )

### Plugins

Plugins need a little care.  
Store the data in the DLL as a resource of type TEXT with the string ID IDR_OPTION_DESC_JSON.  

Specifically, add it to the resources by writing the following in the *.rc file.  
IDR_OPTION_DESC_JSON TEXT "option_desc_ja.json"

Do not define IDR_OPTION_DESC_JSON in resource.h.  
If you define IDR_OPTION_DESC_JSON, the resource is added with a numeric ID.

For SDL3 / generic build plugins ( .so and other formats that cannot carry Win32 resources ),
place `<basename>.options.json` ( e.g. `myplugin.options.json` ) next to the DLL
and it is loaded. If it is absent, the plugin is simply treated as having no setting items.

### JSON format

The top level is an **array of categories**, and each category has an array of option definitions in `options`.
For the real thing, see the engine's `src/core/resource/optiondesc.json` ( 7 categories / 66 options ).

```json
[
  {
    "category": "システム全般",
    "options": [
      {
        "caption":     "データ保存場所",
        "description": "吉里吉里が様々なデータを保存する場所を指定します。\n\n...",
        "name":        "datapath",
        "type":        "string",
        "length":      255,
        "user":        false,
        "value":       "$(exepath)\\savedata"
      },
      {
        "caption":     "処理ウェイト",
        "description": "...",
        "name":        "contfreq",
        "type":        "select",
        "user":        true,
        "values": [
          { "value": "0",  "desc": "ウェイトをかけない", "default": true },
          { "value": "60", "desc": "60Hz" }
        ]
      }
    ]
  }
]
```

#### Categories

| Key | Description |
|---|---|
| `category` | Category name shown as a tab / heading in the configuration tool |
| `options`  | Array of option definitions in this category |

#### Option definitions

| Key | Required | Description |
|---|---|---|
| `caption`     | ○ | Item name shown in the configuration tool |
| `description` | ○ | Description text. Use `\n` for a line break |
| `name`        | ○ | Command-line option name ( without the leading `-`; `datapath` means `-datapath=` ) |
| `type`        | ○ | `"select"` ( choose from options ) or `"string"` ( free input ) |
| `user`        | ○ | Whether to show it in the end-user configuration tool ( `-userconf` ). If `false`, it appears only in the Releaser's settings for developers |
| `values`      | `select` only | Array of choices |
| `value`       | `string` only | Initial value |
| `length`      | `string` only | Maximum length of the input field |

#### Choices (elements of `values`)

| Key | Required | Description |
|---|---|---|
| `value`   | ○ | Value actually passed to the option ( e.g. `"60"` ) |
| `desc`    | ○ | String shown for the choice |
| `default` | | If `true`, this is the default. Specify only one per category |

!!! note "Relation to the command-line option descriptions"
    The `description` here is **the text shown in the configuration tool** and is maintained
    separately from the [command-line options](../../guide/CommandLine.md) documentation.
    When you add or change an option, both need updating.
