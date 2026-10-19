# EffekseerEffect

Effect asset

Holds a loaded effect. It can be shared by multiple EffekseerPlayer objects, so
reuse it when playing the same effect many times simultaneously.

## Members

### Constructors

- [EffekseerEffect](#effekseereffect)

### Properties

- [device](#device)
- [meta](#meta)
- [loaded](#loaded)
- [filename](#filename)
- [magnification](#magnification)
- [termMin](#termmin)
- [termMax](#termmax)

### Methods

- [load](#load)
- [clear](#clear)
- [unloadResources](#unloadresources)
- [reloadResources](#reloadresources)
- [readMeta](#readmeta)
- [setDynamicInputNames](#setdynamicinputnames)
- [findDynamicInput](#finddynamicinput)

---

### EffekseerEffect

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `device` | `&nbsp;` | EffekseerDevice instance |

**Description**

Constructor

---

### device

Property \ Access: `r/w`

**Description**

Read-only

---

### meta

Property \ Access: `r/w`

**Description**

Supplementary information (effect.json) bundled in the .efkzip; void if absent

The effect binary does not retain the names of dynamic parameters. It contains only
default values and compiled code, so normally they can be accessed only by index. The convention,
therefore, is to provide the name-to-index mapping and similar data as JSON.
It is parsed automatically when the .efkzip is loaded, so no extra steps are needed on the loading side.

Only the following two keys have defined meanings; everything else is passed through as is:
dynamicInputs … [ %[ name:"emitter.x", index:0 ], ... ]
automatically imported as the mapping table for setDynamicInputByName()
motions       … [ %[ name:"...", file:"motion/....json", ... ], ... ]

var meta = effect.meta;
if (meta !== void && meta.motions !== void)
var path = effect.readMeta(meta.motions[0].file);

---

### loaded

Property \ Access: `r/w`

**Description**

Read-only: whether an effect is loaded

---

### filename

Property \ Access: `r/w`

**Description**

Read-only: normalized storage name

---

### magnification

Property \ Access: `r/w`

**Description**

Read-only: magnification at load time

---

### termMin

Property \ Access: `r/w`

**Description**

Read-only: minimum expected playback length (frames)

---

### termMax

Property \ Access: `r/w`

**Description**

Read-only: maximum expected playback length (frames)

---

### load

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `&nbsp;` | Storage name (.efkzip / .efkefc / .efk) |
| `magnification` | `&nbsp;` | Magnification at load time (1.0 if omitted) |
| `entry` | `&nbsp;` | Effect file name inside the .efkzip (optional)<br>- .efkzip … a ZIP bundling the effect together with its textures/models.<br>Effekseer effects split their assets across multiple files, so this format is normally used<br>(the same idea as Live2D's .l2d). Assets are resolved by their relative paths inside the ZIP.<br>If entry is omitted, the first .efkefc in the ZIP (or .efk if none) is used.<br>- .efkefc / .efk … a single file. Assets are resolved relative to the directory of filename;<br>if not found there, the file name alone is also looked up in the auto search path<br>(to cope with directory structures flattened when packed into an XP3).<br>An exception is thrown on failure. |

**Description**

Loads an effect file

---

### clear

Method

**Description**

Clears the contents

---

### unloadResources

Method

**Description**

Releases / reloads assets (textures, models, etc.)

---

### reloadResources

Method

---

### readMeta

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Path inside the ZIP |

**Return value**

void if it cannot be parsed

**Description**

Reads a JSON file inside the .efkzip as a dictionary / array

---

### setDynamicInputNames

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `names` | `&nbsp;` |  |

**Description**

Replaces the mapping between dynamic parameter names and input indices

For .efkzip files the mapping comes from effect.json automatically, so you normally do not need this.
Use it when loading .efk / .efkefc directly, or when you want to rename entries.

effect.setDynamicInputNames(%[ "emitter.x" => 0, "emitter.y" => 1 ]);
effect.setDynamicInputNames(["emitter.x", "emitter.y"]);  // 並び順が番号
effect.setDynamicInputNames([ %[ name:"emitter.x", index:0 ] ]);

Passing void clears the registration.

---

### findDynamicInput

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

**Return value**

-1 if not found

**Description**

Looks up an input index from the registered mapping

---
