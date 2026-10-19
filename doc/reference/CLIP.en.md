# CLIP

Manual written as pseudo-code

clipfile.dll: a plugin for reading and editing CLIP STUDIO PAINT (.clip) files

CLIP file storage
Layer images in a CLIP file can be loaded directly as files using the following paths:

clip://CLIPfilename/root/foldername/.../layername.bmp
clip://CLIPfilename/id/LayerId.bmp

- The CLIP file name is the base name only, normalized to lowercase
- Folder and layer names are all normalized to lowercase, and any "/" they contain is replaced with "_"
- If names collide, the later one takes precedence
- Layers without an image (folders, adjustment layers, empty layers) are not listed

The rules are the same as psd:// in the psdfile plugin.

## Members

### Properties

- [width](#width)
- [height](#height)
- [resolution](#resolution)
- [layer_count](#layer_count)
- [root_layer](#root_layer)
- [is_loaded](#is_loaded)
- [error](#error)

### Methods

- [load](#load)
- [loadOctet](#loadoctet)
- [clearData](#cleardata)
- [getLayerName](#getlayername)
- [getLayerInfo](#getlayerinfo)
- [getRoots](#getroots)
- [getChildren](#getchildren)
- [getLayerIndexById](#getlayerindexbyid)
- [getLayerAttribute](#getlayerattribute)
- [getLayerData](#getlayerdata)
- [getLayerDataRaw](#getlayerdataraw)
- [getLayerDataMask](#getlayerdatamask)
- [getLayerRegion](#getlayerregion)
- [getBlend](#getblend)
- [getPreviewPNG](#getpreviewpng)
- [check](#check)
- [clearStorageCache](#clearstoragecache)

---

### width

Property \ Access: `r`

**Description**

Canvas width (in actual pixels)

CLIP's Canvas.CanvasWidth depends on CanvasUnit, and files in mm units do exist,
so this returns the actual pixel value derived from the attributes of the 100% mipmap. -1 if not loaded.

---

### height

Property \ Access: `r`

**Description**

Canvas height (in actual pixels). -1 if not loaded

---

### resolution

Property \ Access: `r`

**Description**

Resolution (dpi). 0 if not loaded

---

### layer_count

Property \ Access: `r`

**Description**

Number of layers. -1 if not loaded

---

### root_layer

Property \ Access: `r`

**Description**

LayerId of the root folder. -1 if not loaded

---

### is_loaded

Property \ Access: `r`

**Description**

Whether a file is loaded

---

### error

Property \ Access: `r`

**Description**

Reason for the most recent failure. An empty string if none

---

### load

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `&nbsp;` | File name. |

**Return value**

true if loading succeeded (the reason for failure is in the error property).

**Description**

Loads a CLIP file

Files that exist locally are opened with mmap, and pixels are read in 256x256 blocks only
when needed (so load itself is cheap even for large files).
If the file does not resolve to a local path (for example inside an archive), the whole stream
is read into memory and then parsed.

---

### loadOctet

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `data` | `&nbsp;` | An octet containing the entire file. |

**Return value**

true if loading succeeded.

**Description**

Loads CLIP data held in an octet

This object keeps the byte sequence. Since there is no file name,
it is not registered in the clip:// storage.

---

### clearData

Method

**Description**

Explicitly discards the data held

Object lifetime in Kirikiri depends on GC, so call this when you do not want to keep
a large file held.

---

### getLayerName

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `no` | `&nbsp;` | Layer index. |

**Return value**

The layer name.

**Description**

Gets a layer name

---

### getLayerInfo

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `no` | `&nbsp;` | Layer index. |

**Return value**

A dictionary containing the layer information.
Contents:
left         left coordinate (canvas coordinates)
top          top coordinate
right        right coordinate
bottom       bottom coordinate
width        width
height       height
name         layer name
layer_id     LayerId (CLIP's Layer.MainId). This is the value used by CLIPWriter's methods
and by clip://~/id/
visible      visibility
opacity      opacity 0..255 (matching PSD / Kirikiri)
opacity_raw  raw opacity 0..**256** (CLIP uses 256 levels)
clipping     whether to clip to the layer below (0/1)
composite    raw blend mode (CLIP's LayerComposite; the same values as CLIPWriter's
composite_* constants)
type         blend mode (the corresponding Kirikiri mode). Modes without an equivalent
fall back to ltPsNormal, so use composite when you need the exact mode
blend_mode_key blend mode as a PSD four-character code, for comparing with psdfile's
getLayerInfo().blend_mode_key
is_group     whether it is a folder layer
is_filter    whether it is an adjustment layer (has no pixels of its own)
is_text      whether it is a text layer
has_mask     whether it has a layer mask
folder       raw folder attributes (bit0=folder / bit4=collapsed)
collapsed    whether the folder is collapsed
layer_type_raw raw LayerType (bit12(4096)=adjustment layer / bit1(2)=has mask)
parent_index layer index of the parent folder (-1 at the top level)
children     array of layer indices of the direct children (bottom to top). An empty array for non-folders

**Description**

Gets layer information

The layer index no ranges from 0 to layer_count-1, in the same flattened order as psdfile:
"contents first, folder after, bottom to top".

---

### getRoots

Method

**Return value**

Array of layer indices.

**Description**

Gets the array of top-level layer indices (directly under the root), bottom to top

---

### getChildren

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `no` | `&nbsp;` | Layer index. |

**Return value**

Array of layer indices (an empty array for non-folders).

**Description**

Gets the array of layer indices of a folder's direct children, bottom to top

---

### getLayerIndexById

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `layerId` | `&nbsp;` | Value of getLayerInfo().layer_id. |

**Return value**

The layer index, or -1 if not found.

**Description**

Looks up a layer index from a LayerId

---

### getLayerAttribute

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `no` | `&nbsp;` | Layer index. |
| `mask` | `false` | true examines the mask's mip chain. Defaults to false. |

**Return value**

%[ width:, height:,        // logical size
cols:, rows:,           // block grid
color_mode:             // 33=RGBA / 17=gray, monochrome / 1=mask
num_channels:           // 4 / 1 / 0
bit_depth:              // 5=8bpp RGBA / 2=8bpp / 1=1bpp
plane_bytes:,
block_width:, block_height:,
has_init_color:,
init_color:             // packed RGBA value
block_count:            // number of blocks
]  void if there is no data

**The width / height returned here are not necessarily the canvas size.** CSP stores pixels
for some layers rounded up to 256x256 block boundaries (for example 512x512 even on a
300x400 canvas). The size of the Layer passed to `CLIPWriter.setPixels` must match this value,
so check it here when rewriting a layer.

**Description**

Gets the Offscreen attributes of the 100% mipmap (for checking the block grid and expression color)

---

### getLayerData

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `layer` | `&nbsp;` | Destination layer. |
| `no` | `&nbsp;` | Layer index.<br>Folders, adjustment layers and empty layers have no image, so nothing is done<br>(a Kirikiri Layer cannot have zero size).<br>In addition to the image data, the following properties are set on the layer automatically:<br>left          left coordinate<br>top           top coordinate<br>width         width<br>height        height<br>type          blend mode<br>opacity       opacity (normalized to 0..255)<br>visible       visibility<br>imageLeft     set to 0<br>imageTop      set to 0<br>imageWidth    set to width<br>imageHeight   set to height<br>name          set to the layer name |

**Description**

Reads a layer image (with the mask folded into alpha)

---

### getLayerDataRaw

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `layer` | `&nbsp;` | Destination layer. |
| `no` | `&nbsp;` | Layer index. |

**Description**

Reads a layer image (the raw image, without folding in the mask)

The properties set are the same as getLayerData.

---

### getLayerDataMask

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `layer` | `&nbsp;` | Destination layer. |
| `no` | `&nbsp;` | Layer index. |

**Description**

Reads only the layer's mask (grayscale)

Does nothing for layers without a mask.
opacity is set to 255 and type to ltPsNormal.

---

### getLayerRegion

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `layer` | `&nbsp;` | Destination layer. |
| `no` | `&nbsp;` | Layer index. |
| `x` | `&nbsp;` | Left of the rectangle (canvas coordinates). |
| `y` | `&nbsp;` | Top of the rectangle. |
| `w` | `&nbsp;` | Width of the rectangle. |
| `h` | `&nbsp;` | Height of the rectangle. |
| `mode` | `image_mode_masked` | image_mode_* (defaults to image_mode_masked). |

**Description**

Reads only the given rectangle (canvas coordinates) of a layer image

CLIP stores pixels in 256x256 tiles, so **only the overlapping tiles are
decoded**. This is cheaper when you only need part of a large layer
(PSD uses row RLE and cannot do the same, so this is specific to clipparse).
The left/top of the destination Layer are set to x/y.

---

### getBlend

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `layer` | `&nbsp;` | Destination layer (resized to the canvas size). |

**Return value**

true on success.

**Description**

Gets the image of all layers composited from the bottom up

Unlike psdfile's getBlend, which only reads the composited result saved in the PSD,
this one actually composites the layers in clipparse (the correct result matches CSP's
CanvasPreview). It supports 27 blend modes, 4 expression colors, masks, clipping,
pass-through folders and 5 kinds of adjustment layers.
If you just want the saved finished image as is, getPreviewPNG() is cheaper.

---

### getPreviewPNG

Method

**Return value**

An octet of PNG data, or void if there is none.

**Description**

Returns the finished image embedded in the file (CanvasPreview) as a PNG octet

It is the image CSP saved, so no compositing is needed, but **it is not necessarily at full size**.

---

### check

Method

**Return value**

A report string if there are problems, or void if there are none.

**Description**

Runs structural assertions over all blocks (for diagnostics)

---

### clearStorageCache

Method

**Description**

Clears the cache held for the storage

A static method.

---
