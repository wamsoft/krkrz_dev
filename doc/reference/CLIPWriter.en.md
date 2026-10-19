# CLIPWriter

Class for editing and writing CLIP files

A separate class from the reader (CLIP). It reads the whole source file into memory (no mmap),
so it can write back to the same path.

**Run written files through validate() before opening them in CSP.**
clipparse takes care of the kinds of mistakes that "our reader accepts but CSP rejects"
(storage types, mip level counts, checksums, thumbnail generation numbers, CanvasPreview),
but broken referential integrity can only be detected by validate(). Files in such a state
crash CSP or show up fully transparent.

Example:
var w = new CLIPWriter();
w.load("in.clip");
w.setLayerAttr(5, %[ opacity: 128, composite: CLIPWriter.composite_multiply ]);
w.save("out.clip");
var problems = CLIPWriter.validate("out.clip");
if (problems.count) Debug.message(problems.join("\n"));

## Members

### Properties

- [error](#error)
- [external_count](#external_count)

### Methods

- [load](#load)
- [save](#save)
- [clearData](#cleardata)
- [setLayerAttr](#setlayerattr)
- [setPixels](#setpixels)
- [addLayer](#addlayer)
- [deleteLayer](#deletelayer)
- [dropThumbnail](#dropthumbnail)
- [setCanvasPreview](#setcanvaspreview)
- [resizeCanvas](#resizecanvas)
- [setSeed](#setseed)
- [validate](#validate)

---

### error

Property \ Access: `r`

**Description**

Reason for the most recent failure. An empty string if none

**It is not cleared on success, so read it only when the return value is false.**

---

### external_count

Property \ Access: `r`

**Description**

Number of external chunks (CHNKExta)

---

### load

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `&nbsp;` | File name (must resolve to a local path.<br>Files inside archives cannot be edited and throw an exception). |

**Return value**

true on success (the reason for failure is in the error property).

**Description**

Reads the CLIP file to edit

---

### save

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `&nbsp;` | Destination file name (local path). |

**Return value**

Number of bytes written. 0 on failure.

**Description**

Builds the file from the current state and writes it

If written back without changes, the sha256 matches the original file.

---

### clearData

Method

**Description**

Explicitly discards the data held

---

### setLayerAttr

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `layerId` | `&nbsp;` | LayerId (the value of CLIP.getLayerInfo().layer_id). |
| `attr` | `&nbsp;` | Attribute dictionary. |

**Return value**

true on success.

**Description**

Edits layer attributes. Only the keys given in the attr dictionary are changed

%[ name:       // layer name
opacity:    // opacity 0..**256** (CLIP uses 256 levels, not 0..255)
visibility: // visibility 0/1
composite:  // blend mode (composite_* constants)
clipping:   // whether to clip to the layer below
folder:     // folder attributes (bit0=folder / bit4=collapsed)
]

---

### setPixels

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `layerId` | `&nbsp;` | LayerId. |
| `layer` | `&nbsp;` | Layer that supplies the pixels. |

**Return value**

true on success.

**Description**

Replaces a layer's pixels with the contents of a Layer object

**The Layer size must match the dimensions of that layer's 100% mipmap, which is not
necessarily the canvas size.** CSP may store some layers rounded up to 256x256 block
boundaries (for example 512x512 even on a 300x400 canvas). You can find the required
dimensions from width / height of the reader's
`CLIP.getLayerAttribute(layer index)`:

var a = clip.getLayerAttribute(3);
lay.setImageSize(a.width, a.height);
lay.setSizeToImageSize();
// ... draw into lay ...
w.setPixels(clip.getLayerInfo(3).layer_id, lay);

If the dimensions do not match, false is returned and error is set to
"pixel size does not match the 100% mipmap".
Only RGBA plane layers are supported (getLayerAttribute().num_channels == 4).

---

### addLayer

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Name of the new layer. |
| `copyFrom` | `&nbsp;` | LayerId of the existing layer to use as the template. |
| `layer` | `void` | Layer that supplies the pixels (omitted / void makes it fully transparent). |
| `after` | `-1` | Inserts directly above this LayerId. A negative value means the top. Defaults to -1. |
| `parent` | `0` | LayerId of the parent folder. 0 means directly under the root. Defaults to 0. |

**Return value**

LayerId of the new layer. 0 on failure.

**Description**

Adds a layer using an existing layer as a template

Attributes such as the expression color are inherited from the template, so you need to choose the source layer.

---

### deleteLayer

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `layerId` | `&nbsp;` | LayerId. |

**Return value**

true on success.

**Description**

Deletes a layer

---

### dropThumbnail

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `layerId` | `&nbsp;` | LayerId. |

**Return value**

true on success.

**Description**

Drops only the thumbnail data and sets the generation number (CSP regenerates it when opening the file)

Intended for avoiding a stale thumbnail after replacing pixels, but
setPixels / addLayer handle this internally, so you normally do not need to call it.

---

### setCanvasPreview

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `layer` | `&nbsp;` | Layer that supplies the pixels. |

**Return value**

true on success.

**Description**

Replaces the image shown right after opening (CanvasPreview)

---

### resizeCanvas

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `width` | `&nbsp;` | New width. |
| `height` | `&nbsp;` | New height. |
| `dpi` | `0` | Resolution (0 keeps it unchanged). Defaults to 0. |

**Return value**

true on success.

**Description**

Rebuilds the canvas at new dimensions (scales the mip chain)

**All pixel data is dropped, so put it back with setPixels afterwards.**

---

### setSeed

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `seed` | `&nbsp;` | Random seed. |

**Description**

Fixes the random seed for external IDs (when tests need reproducible output)

---

### validate

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `&nbsp;` | File to check (local path). |

**Return value**

An array of strings describing problems. An empty array means no problems.

**Description**

Checks referential integrity

A static method. **Always run this before opening a file in CSP.**
Checks mip level counts, cycles, orphan rows, storage types and references to deleted layers.

---
