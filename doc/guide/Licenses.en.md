---
source_hash: 6790ab6c5f72
---

# Getting and Displaying License Information

Kirikiri Z keeps the license texts of the third-party components ( libraries,
fonts, etc. ) built into the engine and plugins inside the executable. You can
get both the list and the full texts from TJS, so you are free to build in-game
credit screens or license screens in script.

## Three Sources

The list merges the following three sources. From a script, the only
difference is the value of the `source` member; they are all retrieved the
same way.

| `source` | Contents | How it is supplied |
|---|---|---|
| `builtin` | Built into the engine ( libraries the engine uses, bundled fonts ) | Compressed and embedded in the executable |
| `plugin` | Registered by plugins | The plugin DLL registers them when loaded |
| `storage` | Provided by the project | Text files placed in the project's `licenses` folder |

If the same name exists in more than one source, they are merged into one entry
( priority: `plugin` > `builtin` > `storage` ).

## Getting Them from TJS

### Getting the List

[System.getLicenseList](../reference/System.md#getlicenselist) returns an array
of dictionaries. Each element has `name` ( display name ), `group` ( category ),
and `source` ( source ).

```tjs
var list = System.getLicenseList();
for (var i = 0; i < list.count; i++) {
	var e = list[i];
	Debug.message(e.name + " / " + e.group + " / " + e.source);
}
```

`group` is a string for categorization. The entries built into the engine use
the values below. Entries registered by plugins or by a title can be any
string, so **do not write a `switch` that assumes the list is exhaustive**
( handle unknown values by, for example, displaying them as is ).

| `group` | Contents |
|---|---|
| `engine` | Engine foundation ( zlib / libpng / Oniguruma, etc. ) |
| `font-engine` | Font engine ( FreeType / HarfBuzz, etc. ) |
| `audio` | Audio ( libogg / libvorbis / Opus, etc. ) |
| `video` | Movie ( libvpx / libyuv, etc. ) |
| `ui` | UI rendering ( Elements / ThorVG ) |
| `platform` | Platform ( SDL3 / ANGLE, etc. ) |
| `font` | Bundled fonts |
| `data` | Entries placed in the project's `licenses` folder |

### Getting the Full Text

Pass a `name` to [System.getLicenseText](../reference/System.md#getlicensetext)
and the entire license text is returned as a string. **If it is not found, it
returns void.**

```tjs
var text = System.getLicenseText("FreeType");
if (text !== void) {
	Debug.message(text);
}
```

!!! warning "Do not test with `if (text)`"
    In TJS2, a string that cannot be converted to a number is **always false**
    when used as a condition. Test strings such as license texts with `text !== void`.

### Combining the List and Full Texts into One String

An example for outputting all the credits as text at once.

```tjs
function buildLicenseText()
{
	var list = System.getLicenseList();
	var buf = [];
	for (var i = 0; i < list.count; i++) {
		var name = list[i].name;
		var text = System.getLicenseText(name);
		if (text === void) continue;
		buf.add("======== " + name + " ========");
		buf.add(text);
	}
	return buf.join("\n");
}
```

### Grouping by Category

```tjs
var byGroup = %[];
var list = System.getLicenseList();
for (var i = 0; i < list.count; i++) {
	var e = list[i];
	if (byGroup[e.group] === void) byGroup[e.group] = [];
	byGroup[e.group].add(e.name);
}
```

Reading a member that is not in the dictionary returns void, so you can
initialize it as shown above.

### When to Use System.licenseText

[System.licenseText](../reference/System.md#licensetext) is a single string
made of "the version line + the Kirikiri Z engine's terms + the list of bundled
components", intended for **displaying as is**. It does not include the full
text of each component, so use `getLicenseText` when you need the full texts.

| Goal | Use |
|---|---|
| Show the engine's terms as is | `System.licenseText` |
| List what is included | `System.getLicenseList()` |
| Get the full text of a specific component | `System.getLicenseText(name)` |

## Using the Built-in Viewer

In builds where ElementsDialog is available, you can use the sample
implementation `data/ui/license_dialog.tjs` as is. It has a two-pane layout:
the left pane is the item list grouped by category, and the right pane is the
license text.

```tjs
Scripts.execStorage("ui/license_dialog.tjs");
showLicenseDialog(win);          // モーダル。閉じるまでブロック
showLicenseDialog(win, false);   // 非モーダル ( 戻り値 = ElementsDialog )
```

Feel free to copy it into your project and modify it. In builds without
ElementsDialog ( `KRKRZ_USE_ELEMENTS=OFF` ), it does nothing and returns void.

## Adding Your Project's Assets to the List

If you put **one text file per asset** in the project's `licenses` folder,
they are automatically merged into the list at startup ( `source` is
`storage`, `group` is `data` ). Files with the extensions `.txt` and `.md`
are included.

```
licenses/kenney-input-prompts.txt
licenses/myfont-regular.txt
```

- **The display name ( `name` ) is the file name without the extension, in
  lowercase.** `MyFont-Regular.txt` is listed as `myfont-regular`. If you want
  a nicer title for display, it helps to write the asset name on the first line
  of the file.
- `System.getLicenseText(name)` looks it up by the same name
  ( it searches `licenses/<name>.txt`, then `.md` if not found ).
- Save the files in UTF-8 ( a BOM is fine ).

### Example

To bundle [Kenney Input Prompts](https://kenney.nl/assets/input-prompts)
( CC0 ), which is often used for gamepad button prompts, as
`licenses/kenney-input-prompts.txt`:

```
Input Prompts (Kenney)

This product includes "Input Prompts" by Kenney (www.kenney.nl),
released under Creative Commons Zero (CC0 1.0 Universal).

  https://kenney.nl/assets/input-prompts
  https://creativecommons.org/publicdomain/zero/1.0/

Attribution is not required, but appreciated:
  "Input Prompts" by Kenney (www.kenney.nl)
```

You can also put the pack's own License.txt there as is. CC0 does not require
attribution, but listing it makes it easier to track where assets came from
and to display credits.

## Checking from a Command-Line Option

To check the contents without writing a script, use the
[-license](CommandLine.md) command-line option. It is handy for checks during
development and for inspecting what a distribution contains.

```
krkrz64.exe -license            # 一覧
krkrz64.exe -license=FreeType   # 1 件の全文
krkrz64.exe -license=all        # 全件の全文
```

If you launch with a project specified, the entries in that project's
`licenses` folder are also listed. The same list is also shown in the
"version, copyright, and environment information" dialog of `-about`.

## Files Included in the Distribution

In the distribution created by `make install`, the original license texts are
also written out as files, separately from the runtime list.

| Path | Contents |
|---|---|
| `license.txt` | The Kirikiri Z engine's terms |
| `licenses/<name>.txt` | Original texts of third-party components built into the engine |
| `licenses/plugins/<name>.txt` | Original texts of components built into the bundled plugins |

A table of which component uses which license is in
[Bundled Licenses](BundledLicenses.md).

## Registering from a Plugin

License texts built into a plugin are merged into the list using the
registration functions exposed through `tp_stub` ( once registered, they
appear as entries whose `source` is `plugin` ).

| Function | Purpose |
|---|---|
| `TVPRegisterLicense(name, group, deflated, deflatedSize, originalSize)` | Registers compressed text ( the data is held by reference ) |
| `TVPRegisterLicenseText(name, group, text)` | Registers raw text ( for short texts ) |
| `TVPGetLicenseText(name, &text)` | Gets the full text by name |
| `TVPEnumLicenses(sink)` | Enumerates all entries |

The registration source can be generated from a manifest. For the mechanism
and the generation steps, see `src/core/doc/LicenseSystem.md` on the engine side.
