# PSD

Manual written as pseudo-code

PSD file storage
Layer images in a PSD file can be loaded directly as files using the following paths:

psd://PSDfilename/root/foldername/.../layername.bmp
psd://PSDfilename/id/layerID.bmp

- The PSD file name is the base name only, normalized to lowercase
- Folder and layer names are all normalized to lowercase, and any "/" they contain is replaced with "_"
- If names collide, the later one takes precedence

## Members

### Properties

- [width](#width)
- [height](#height)
- [channels](#channels)
- [depth](#depth)
- [color_mode](#color_mode)
- [layer_count](#layer_count)
- [hresolution](#hresolution)
- [vresolution](#vresolution)
- [merged_alpha](#merged_alpha)

### Methods

- [load](#load)
- [loadOctet](#loadoctet)
- [clear](#clear)
- [assignAutoIds](#assignautoids)
- [getLayerType](#getlayertype)
- [getLayerName](#getlayername)
- [getLayerInfo](#getlayerinfo)
- [getLayerData](#getlayerdata)
- [getLayerDataRaw](#getlayerdataraw)
- [getLayerDataMask](#getlayerdatamask)
- [getSlices](#getslices)
- [getGuides](#getguides)
- [getBlend](#getblend)
- [getLayerComp](#getlayercomp)
- [getLayerMask](#getlayermask)
- [getLayerBlendingRanges](#getlayerblendingranges)
- [getLayerSheetColor](#getlayersheetcolor)
- [getLayerInfoKeys](#getlayerinfokeys)
- [getLayerDescriptor](#getlayerdescriptor)
- [getLayerDescriptorBytes](#getlayerdescriptorbytes)
- [getLayerEffects](#getlayereffects)
- [getLayerFill](#getlayerfill)
- [getColorTable](#getcolortable)
- [getGlobalLayerMask](#getgloballayermask)
- [getImageResourceIds](#getimageresourceids)
- [getImageResource](#getimageresource)
- [getICCProfile](#geticcprofile)
- [getEXIF](#getexif)
- [getXMP](#getxmp)
- [getThumbnail](#getthumbnail)
- [save](#save)
- [createBlank](#createblank)
- [deleteLayer](#deletelayer)
- [moveLayer](#movelayer)
- [groupSpan](#groupspan)
- [moveLayerSibling](#movelayersibling)
- [moveLayerRange](#movelayerrange)
- [duplicateLayer](#duplicatelayer)
- [copyLayerFrom](#copylayerfrom)
- [setLayerName](#setlayername)
- [setFillOpacity](#setfillopacity)
- [setLayerOpacity](#setlayeropacity)
- [setLayerClipping](#setlayerclipping)
- [setLayerVisible](#setlayervisible)
- [setLayerBlendMode](#setlayerblendmode)
- [setLayerEffects](#setlayereffects)
- [setLayerDescriptor](#setlayerdescriptor)
- [setMaskDisabled](#setmaskdisabled)
- [setMaskDensity](#setmaskdensity)
- [setMaskFeather](#setmaskfeather)
- [setMaskDefaultColor](#setmaskdefaultcolor)
- [setLayerPixels](#setlayerpixels)
- [setLayerMaskPixels](#setlayermaskpixels)
- [addLayer](#addlayer)
- [setMergedImage](#setmergedimage)
- [setLayerText](#setlayertext)
- [setLayerRunStyle](#setlayerrunstyle)
- [setLayerRichText](#setlayerrichtext)
- [setLayerJustification](#setlayerjustification)
- [getLayerFonts](#getlayerfonts)
- [getLayerTextTransform](#getlayertexttransform)
- [setLayerTextTransform](#setlayertexttransform)
- [moveTextLayer](#movetextlayer)
- [getLayerTextBounds](#getlayertextbounds)
- [setLayerTextBounds](#setlayertextbounds)
- [clearStorageCache](#clearstoragecache)
- [getComposite](#getcomposite)
- [renderLayer](#renderlayer)
- [getVectorMask](#getvectormask)
- [getPaths](#getpaths)
- [getLayerShape](#getlayershape)
- [getShapeMask](#getshapemask)
- [flattenPath](#flattenpath)
- [rasterizePath](#rasterizepath)
- [strokePath](#strokepath)
- [setThreads](#setthreads)
- [getThreads](#getthreads)

---

### width

Property \ Access: `r`

**Description**

Image width

---

### height

Property \ Access: `r`

**Description**

Image height

---

### channels

Property \ Access: `r`

**Description**

Number of channels

---

### depth

Property \ Access: `r`

**Description**

Bits per channel (1/8/16/32)

---

### color_mode

Property \ Access: `r`

**Description**

Color mode

---

### layer_count

Property \ Access: `r`

**Description**

Number of layers

---

### hresolution

Property \ Access: `r`

**Description**

Horizontal resolution (dpi, default 72, image resource 1005)

---

### vresolution

Property \ Access: `r`

**Description**

Vertical resolution (dpi, default 72)

---

### merged_alpha

Property \ Access: `r`

**Description**

Whether the merged image contains an alpha channel

---

### load

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `&nbsp;` | File name. |

**Return value**

true if loading succeeded.

**Description**

Loads a PSD image

---

### loadOctet

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `data` | `&nbsp;` | An octet containing the entire PSD file. |

**Return value**

true if loading succeeded.

**Description**

Loads PSD data held in an octet

The byte sequence is copied into an internal buffer, so the octet may be discarded
after the call. Since there is no file name, it is not registered in the psd:// storage.

---

### clear

Method

**Description**

Explicitly discards the data held

Object lifetime in Kirikiri depends on GC, so call this when you do not want to keep
a large PSD held. Subsequent queries throw a "no data" exception.

---

### assignAutoIds

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `base_id` | `0` | The smallest ID to assign, minus 1 (if any existing layer ID is larger than this, that value is used instead). |

**Return value**

Number of layers that were assigned an ID.

**Description**

Automatically assigns IDs to layers without a LayerID (from base_id+1, in layer_no order)

Some Photoshop-compatible tools save PSD files without assigning layer IDs, so psd://~/id/ cannot load them correctly.
It is generally recommended to call this right after load.

---

### getLayerType

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `no` | `&nbsp;` | Layer index. |

**Return value**

The layer type.

**Description**

Gets the layer type

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

Gets the layer name

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
layer_type   layer type
top          top coordinate
left         left coordinate
bottom       bottom coordinate
right        right coordinate
width        width
height       height
blend_mode   blend mode (blend_mode_*; unknown modes are blend_mode_invalid)
blend_mode_key raw blend mode key in the PSD (4 characters; note that 3-character keys have
a trailing space, as in "mul "). Unknown modes are returned as is, so
to write back the value you read, pass this to setLayerBlendMode
opacity      opacity
fill_opacity fill opacity
visible      visibility
name         layer name
layer_id     layer ID
group_layer_id parent layer ID
parent_index layer index of the parent folder (-1 at the top level). layer_id may be
unset (-1) in some PSD files, so this is more reliable for building the hierarchy.
It is recalculated after structural edits
(deleteLayer/moveLayer/duplicateLayer/addLayer, etc.)
type         blend mode (the corresponding Kirikiri mode)
clipping	whether the layer is the target of a clipping mask
mask		whether the layer has a layer mask
mask_params  mask parameters (density/feather). Present only for layers that have a mask
and an actual parameter block. Contains only the items specified
%[ user_density:   // user mask density 0..255
user_feather:   // user mask feather (px)
vector_density: // vector mask density 0..255
vector_feather: // vector mask feather (px)
]
layer_comp    layer comp information (a dictionary keyed by comp ID)
%[ <id>: [ id,       // comp ID (see getLayerComp())
offset_x, // X offset of the layer
offset_y, // Y offset of the layer
enable,   // visibility flag
],... ]
text         text layer information (present only for text layers, layer_type==layer_type_text;
for other layers the key itself does not exist)
%[ text:          // entire body text (line breaks are carriage returns, CR)
orientation:   // "horizontal" or "vertical" (vertical text)
justification: // alignment of the first paragraph 0=left 1=right 2=center
transform:     // affine transform `[ xx, xy, yx, yy, tx, ty ]` (tx,ty=translation)
runs: [        // array of character style runs (in body text order)
%[ length:       // number of characters it applies to (UTF-16 code units; surrogates such as emoji count as 2)
font:         // resolved font name
size_px:      // font size (pt)
color:        // RGBA array, each 0..1, `[ r, g, b, a ]` (absent if unspecified)
tracking:     // tracking (1/1000 em)
kerning:      // manual kerning
auto_kerning: // whether automatic kerning (metrics/optical) is enabled
bold:         // faux bold (FauxBold)
italic:       // faux italic (FauxItalic)
underline:    // underline (Underline)
],... ]
paragraphs: [   // per-paragraph alignment (for box text whose alignment varies per paragraph)
%[ length:        // number of characters in the paragraph (UTF-16 code units)
justification: // alignment 0=left 1=right 2=center
],... ]
]
Additional information follows (see the PSD specification for details)
obsolete
transparency_protected
pixel_data_irrelevant

**Description**

Gets layer information

---

### getLayerData

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `layer` | `&nbsp;` | Destination layer. |
| `no` | `&nbsp;` | Layer index.<br>Can be read only when layer_type is layer_type_normal.<br>Reads the image with the mask applied.<br>In addition to the image data, the following properties are set on the layer automatically:<br>left          left coordinate<br>top           top coordinate<br>width         width<br>height        height<br>type          blend mode<br>opacity       opacity<br>fill_opacity	 fill opacity<br>visible       visibility<br>imageLeft     set to 0<br>imageTop      set to 0<br>imageWidth    set to width<br>imageHeight   set to height<br>name          set to the layer name |

**Description**

Reads layer data

---

### getLayerDataRaw

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `layer` | `&nbsp;` | Destination layer. |
| `no` | `&nbsp;` | Layer index.<br>Can be read only when layer_type is layer_type_normal.<br>Reads only the image.<br>In addition to the image data, the following properties are set on the layer automatically:<br>left          left coordinate<br>top           top coordinate<br>width         width<br>height        height<br>type          blend mode<br>opacity       opacity<br>fill_opacity	 fill opacity<br>visible       visibility<br>imageLeft     set to 0<br>imageTop      set to 0<br>imageWidth    set to width<br>imageHeight   set to height<br>name          set to the layer name |

**Description**

Reads layer data

---

### getLayerDataMask

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `layer` | `&nbsp;` | Destination layer. |
| `no` | `&nbsp;` | Layer index.<br>Can be read only when layer_type is layer_type_normal.<br>Reads only the mask.<br>If the mask image size is 0 and only defualtMaskColor is set,<br>then to work around Kirikiri's restriction that a layer size cannot be 0,<br>a dummy layer of the minimum size (0,0)-(1,1) is created, filled with defaultMaskColor, and returned.<br>In addition to the image data, the following properties are set on the layer automatically:<br>left          left coordinate<br>top           top coordinate<br>width         width<br>height        height<br>type          blend mode<br>opacity       opacity<br>fill_opacity	 fill opacity<br>visible       visibility<br>imageLeft     set to 0<br>imageTop      set to 0<br>imageWidth    set to width<br>imageHeight   set to height<br>name          set to the layer name<br>defaultMaskColor  mask color outside the stored area (always either 0 or 255) |

**Description**

Reads layer data

---

### getSlices

Method

**Return value**

Slice information dictionary %[ top, left, bottom, right, slices:[ %[ id, group_id, left, top, bottom, right ], ... ] ]
Returns void if there is no slice information.
The last slice appears to be one whose size covers all slices.

**Description**

Reads slice data

---

### getGuides

Method

**Return value**

Guide information dictionary %[ vertical:[ x1, x2, ... ], horizontal:[ y1, y2, ... ] ]
Returns void if there is no guide information.

**Description**

Reads guide data

---

### getBlend

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `layer` | `&nbsp;` | Destination layer. |

**Return value**

true on success.

**Description**

Gets the composited result

The library does not composite anything itself; it reads the composited result saved in the PSD.
Depending on how the file was saved, this image may not exist.
For color modes without layers (bitmap, indexed color),
the image data must be obtained with this method.

---

### getLayerComp

Method

**Return value**

Comp information dictionary %[ last_applied_id,  // ID of the comp last applied in Photoshop
comps:[ %[ id,                // comp ID
record_visibility, // whether visibility is recorded
record_position,   // whether position is recorded
record_appearance, // whether appearance (layer effects) is recorded
name,              // comp name
comment,           // comment
],... ] ]
Returns void if there is no comp information.

- If a record_xxx flag is not set, the state of the last applied comp (the comp last applied
by the program, not last_applied_id) carries over
- The visibility information of each layer for each comp ID is stored in the layer_comp
property of the layer information, as a dictionary keyed by comp ID.

**Description**

Reads layer comp data

---

### getLayerMask

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `no` | `&nbsp;` | Layer index. |

**Return value**

%[ top:, left:, bottom:, right:, // mask rectangle
width:, height:,
default_color:  // value outside the mask area 0..255
flags:          // raw flag byte
relative:       // whether the position is relative to the layer (bit0)
disabled:       // whether the mask is disabled (bit1)
inverted:       // inverted (bit2, obsolete)
from_render:    // whether it comes from rendering other data (bit3)
has_parameters: // whether it has a density/feather block (bit4)
user_density:   // user mask density 0..255 (the key is absent if none)
user_feather:   // user mask feather (px; same as above)
vector_density: // vector mask density (same as above)
vector_feather: // vector mask feather (same as above)
real: %[        // real/user mask (the key is absent if none)
flags:, background:,
top:, left:, bottom:, right:, // enclosing rectangle
]
]  void if the layer has no mask

**Description**

Gets the details of a layer mask

---

### getLayerBlendingRanges

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `no` | `&nbsp;` | Layer index. |

**Return value**

%[ gray:     %[ source:, dest: ],
channels: [ %[ source:, dest: ],... ]
]  void if there is no blending ranges block

**Description**

Gets the layer's blending ranges.

source/dest are raw 32-bit values, with the black and white ranges packed into the upper and lower 16 bits (see the PSD specification for details).

---

### getLayerSheetColor

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `no` | `&nbsp;` | Layer index. |

**Return value**

%[ index: // 0..11
name:  // "none" "red" "orange" "yellow" "green" "blue"
// "violet" "gray" "seafoam" "indigo" "magenta" "fuschia"
]  void if there is no lclr block
(index 0/"none" means "explicitly no label", so it is distinguished from void)

**Description**

Gets the color label of the Layers panel ('lclr')

---

### getLayerInfoKeys

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `no` | `&nbsp;` | Layer index. |

**Return value**

Array of key strings (4 characters each).

**Description**

Gets the list of 4CC keys of the additional layer information blocks in the layer

Useful for finding keys to pass to getLayerDescriptor / getLayerDescriptorBytes.

---

### getLayerDescriptor

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `no` | `&nbsp;` | Layer index. |
| `key` | `&nbsp;` | 4-character key ("lfx2", etc.). |
| `skip` | `-1` | Number of version prefix bytes before the descriptor body.<br>-1 detects it automatically for known keys (lfx2/SoCo/GdFl/PtFl/SoLd/SoLE/vstk/CgEd/vscg/vogk)<br>and uses 0 for others. Defaults to -1. |

**Return value**

A dictionary, or void if the key does not exist or cannot be parsed.

**Description**

Converts an additional layer information block, as a Photoshop descriptor, into a dictionary

Values are converted according to their type:
Integer/Double → number
Boolean        → 1/0
String         → string
UnitFloat      → %[ value:, unit: ]  unit is one of "points" "millimeters" "angle"
"density" "distance" "none" "percent"
"pixels"
Enumerated     → %[ type:, value: ]
List           → array
Descriptor     → dictionary (nested)
RawData        → octet
Class/Alias    → string
Reference      → void

---

### getLayerDescriptorBytes

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `no` | `&nbsp;` | Layer index. |
| `key` | `&nbsp;` | 4-character key. |

**Return value**

An octet, or void if the key does not exist.

**Description**

Gets the raw bytes of an additional layer information block

---

### getLayerEffects

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `no` | `&nbsp;` | Layer index. |

**Return value**

A dictionary, or void if there are no effects.

**Description**

Gets the descriptor dictionary of the layer effects ('lfx2')

Drop shadow, glow, overlay, stroke, bevel and so on are stored as nested dictionaries.
Same as getLayerDescriptor(no, "lfx2").

---

### getLayerFill

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `no` | `&nbsp;` | Layer index. |

**Return value**

%[ type: // "solid" / "gradient" / "pattern"
data: // descriptor dictionary
]  void if the layer is not a fill layer

**Description**

Gets the contents of a fill layer ('SoCo' solid color / 'GdFl' gradient / 'PtFl' pattern)

---

### getColorTable

Method

**Return value**

%[ valid_count:        // number of valid entries
transparency_index: // transparent color index (-1 if none)
colors: [ 0xAARRGGBB, ... ] // always 256 entries
]  void if there is no color table

**Description**

Gets the color table (the palette of an indexed color document)

---

### getGlobalLayerMask

Method

**Return value**

%[ overlay_color_space:,
color: [ c1, c2, c3, c4 ],
opacity: // 0..100
kind:    // 0=inverted / 1=color selected / 128=per layer
]  void if the block is empty or absent

**Description**

Gets the global layer mask info (the overlay color used to display masks)

---

### getImageResourceIds

Method

**Return value**

Array of IDs (integers).

**Description**

Gets the list of image resource IDs in the document

---

### getImageResource

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` | Resource ID (1039=ICC profile, 1058=EXIF, 1060=XMP,<br>1036/1033=thumbnail, 1005=resolution, 1032=grid/guides, etc.). |

**Return value**

An octet, or void if the resource does not exist.

**Description**

Gets the raw bytes of an image resource. Decoding is up to the caller

---

### getICCProfile

Method

**Description**

Raw bytes of the ICC profile (resource 1039). void if none

---

### getEXIF

Method

**Description**

Raw bytes of EXIF (resource 1058). void if none

---

### getXMP

Method

**Return value**

A string, or void if none.

**Description**

Gets the XMP packet (resource 1060) as a string. The contents are UTF-8 XML

If the data might contain invalid UTF-8, get the raw bytes with
getImageResource(1060) instead.

---

### getThumbnail

Method

**Return value**

%[ format:      // "jpeg" (JFIF JPEG) or "raw"
width:, height:,
bits:        // bits per pixel
resource_id: // 1036 or 1033
data:        // payload octet (excluding the 28-byte header)
]  void if there is no thumbnail

**Description**

Gets the embedded thumbnail (resource 1036 = RGB order / legacy 1033 = BGR order)

---

### save

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `&nbsp;` | Destination file name (local path). |

**Return value**

true on success.

**Description**

Writes the current contents as a PSD file

---

### createBlank

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `width` | `&nbsp;` | Width. |
| `height` | `&nbsp;` | Height. |
| `mode` | `color_mode_rgb` | Color mode (color_mode_*, defaults to color_mode_rgb).<br>**Currently returns false for anything other than color_mode_rgb**<br>(only 8-bit RGB is supported for new documents).<br>Pixel editing (addLayer/setLayerPixels/setMergedImage) likewise<br>supports only 8-bit RGB documents. |

**Return value**

true on success.

**Description**

Initializes this PSD as an empty 8-bit document (with a white merged image)

You can then add layers with addLayer(...) and save().

---

### deleteLayer

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` | Layer index. |

**Return value**

true on success (false if out of range).

**Description**

Deletes one layer

---

### moveLayer

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `from` | `&nbsp;` | Source layer index. |
| `to` | `&nbsp;` | Destination (insertion position in the list after removal). |

**Return value**

true on success.

**Description**

Moves a layer from from to to

---

### groupSpan

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` | Layer index. |

**Return value**

%[ start: // first layer index of the block
count: // number of layers in the block
]  void if out of range

**Description**

Returns the "block" a layer occupies in the layer list

For a folder (layer_type_folder), the range from the corresponding divider (layer_type_hidden)
to the folder itself (including nested content); for anything else, just the layer itself.
Use it with moveLayerRange to move a whole folder.

---

### moveLayerSibling

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` | Layer index. |
| `up` | `true` | true moves one step up as shown in the Layers panel (later in the layer list).<br>Defaults to true. |

**Return value**

The layer index after moving. -1 if it is already at the end and cannot move, or if out of range.

**Description**

Swaps a layer with its adjacent sibling at the same level

A folder moves as one block (divider plus contents), and if the neighbor is a folder, it jumps over
that whole block. It does not move across hierarchy levels.

---

### moveLayerRange

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `from` | `&nbsp;` | First layer index to move. |
| `count` | `&nbsp;` | Number of layers to move. |
| `to` | `&nbsp;` | Destination (index in the layer list before removal). |

**Return value**

true on success (false if the arguments are invalid).

**Description**

Moves the range [from, from+count) of the layer list to position to as a group

A low-level operation. To move a whole folder, pass the return value of groupSpan.

---

### duplicateLayer

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` | Layer index. |

**Return value**

New layer index of the duplicate (-1 on failure).

**Description**

Duplicates a layer (inserted right after the original)

---

### copyLayerFrom

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `src` | `&nbsp;` | Source PSD instance. |
| `srcIndex` | `&nbsp;` | Source layer index. |
| `destIndex` | `&nbsp;` | Insertion position (a negative value appends at the end). |

**Return value**

New layer index (-1 on failure).

**Description**

Copies and inserts a layer from another PSD instance

The color mode and bit depth must match. The source PSD must stay alive
until save() on this PSD has finished.

---

### setLayerName

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` | Layer index. |
| `name` | `&nbsp;` | New name. |

**Return value**

true on success.

**Description**

Renames a layer (updates both the Pascal name and the luni name)

---

### setFillOpacity

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` | Layer index. |
| `opacity` | `&nbsp;` | 0..255 |

**Return value**

true on success.

**Description**

Edits the fill opacity

---

### setLayerOpacity

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` | Layer index. |
| `opacity` | `&nbsp;` | 0..255 (out-of-range values are clamped). |

**Return value**

true on success (false if the layer index is out of range).

**Description**

Edits the opacity

---

### setLayerClipping

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` | Layer index. |
| `clipping` | `&nbsp;` | 0=base / 1=non-base (clipped). |

**Return value**

true on success.

**Description**

Edits whether the layer is the target of a clipping mask

---

### setLayerVisible

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` | Layer index. |
| `visible` | `&nbsp;` | Whether to show the layer. |

**Return value**

true on success.

**Description**

Edits the visibility

---

### setLayerBlendMode

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` | Layer index. |
| `mode` | `&nbsp;` | A blend_mode_* constant, or the raw key string in the PSD (4 characters,<br>such as "norm" "mul " "scrn"; 3-character keys require the trailing space).<br>The value of getLayerInfo().blend_mode_key can be passed as is. |

**Return value**

true on success.

**Description**

Edits the blend mode

---

### setLayerEffects

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` | Layer index. |
| `changes` | `&nbsp;` | Partial dictionary. |

**Description**

Edits the values of the layer effects ('lfx2')

changes is a "partial dictionary" in the same shape as getLayerEffects(); only the leaf values given
are overwritten. The structure, class IDs, types and key order are kept as they are, and items not given
or keys that do not exist in the descriptor are ignored (so the bytes otherwise stay identical).
How to give values:
number/string/boolean → as is
UnitFloat             → %[ value: ] or a raw number (the unit is not changed)
Enumerated            → %[ type:, value: ] or just the value string
List                  → array (overwrites existing elements in order, up to the existing count)
Descriptor            → dictionary (merged recursively)
Throws an exception if the layer has no lfx2 block.

---

### setLayerDescriptor

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` | Layer index. |
| `key` | `&nbsp;` | 4-character key. |
| `changes` | `&nbsp;` | Partial dictionary. |
| `skip` | `-1` | Number of version prefix bytes before the descriptor body<br>(-1 detects it automatically for known keys. Defaults to -1). |

**Description**

General version of setLayerEffects for any additional layer information key

Used for things such as 'SoCo'/'GdFl'/'PtFl' of fill layers.
Throws an exception if the layer does not have the key.

---

### setMaskDisabled

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` | Layer index. |
| `disabled` | `&nbsp;` | Whether to disable the mask. |

**Return value**

true on success.

**Description**

Edits the mask disabled flag (layers with a mask only)

---

### setMaskDensity

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` | Layer index. |
| `density` | `&nbsp;` | 0..255 |

**Return value**

true on success.

**Description**

Edits the user mask density (layers with a mask only)

---

### setMaskFeather

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` | Layer index. |
| `feather` | `&nbsp;` | Feather radius (px). |

**Return value**

true on success.

**Description**

Edits the user mask feather (layers with a mask only)

---

### setMaskDefaultColor

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` | Layer index. |
| `color` | `&nbsp;` | 0..255 |

**Return value**

true on success.

**Description**

Edits the mask default color (layers with a mask only)

---

### setLayerPixels

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` | Layer index. |
| `layer` | `&nbsp;` | Layer that supplies the pixels. |

**Return value**

true on success.

**Description**

Replaces the pixels of an existing layer with the contents of a Layer object

Takes in imageWidth×imageHeight of the Layer as BGRA. left/top are kept and
width/height are updated. 8-bit RGB documents only.

---

### setLayerMaskPixels

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` | Layer index. |
| `layer` | `&nbsp;` | Layer that supplies the mask. |
| `top` | `&nbsp;` | Top edge of the mask. |
| `left` | `&nbsp;` | Left edge of the mask. |

**Return value**

true on success.

**Description**

Replaces a layer's mask pixels with the contents of a Layer object (the B component is used as gray).

Also sets the mask rectangle to (top,left,imageWidth,imageHeight).
Creates a mask if there is none. 8-bit documents only.

---

### addLayer

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Layer name. |
| `left` | `&nbsp;` | Left coordinate. |
| `top` | `&nbsp;` | Top coordinate. |
| `layer` | `&nbsp;` | Layer that supplies the pixels. |
| `blendMode` | `blend_mode_normal` | Blend mode (blend_mode_*, defaults to blend_mode_normal). |
| `opacity` | `255` | Opacity 0..255 (defaults to 255). |
| `destIndex` | `-1` | Insertion position (a negative value appends at the end). |

**Return value**

New layer index (-1 on failure).

**Description**

Adds a new image layer. Takes in imageWidth×imageHeight of the Layer as BGRA

8-bit RGB documents only.

---

### setMergedImage

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `layer` | `&nbsp;` | Layer that supplies the pixels. |

**Return value**

true on success.

**Description**

Replaces the merged image (the source of the preview and getBlend) with the contents of a Layer

The Layer size must match the canvas size (width×height).
8-bit RGB documents only.

---

### setLayerText

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` | Layer index. |
| `text` | `&nbsp;` | New body text (line breaks are \\r). |

**Description**

Replaces the body text of a text layer (styles collapse into the first run)

Throws an exception for non-text layers or if there is no TySh block.

---

### setLayerRunStyle

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` | Layer index. |
| `runIndex` | `&nbsp;` | Run index. |
| `style` | `&nbsp;` | Style dictionary. |

**Description**

Edits the style of run runIndex of a text layer (corresponding to getLayerInfo().text.runs).

Only the keys given in the style dictionary are overwritten.
%[ font:      // font name; added to the document's font set if missing
// (the PostScript-style name returned by getLayerFonts(), not the
//  display name. Names not available locally are substituted by Photoshop)
size_px:   // font size (px)
color:     // RGBA array, each 0..1, `[ r, g, b, a ]` (`[ r, g, b ]` without a is also accepted)
tracking:  // tracking (1/1000 em)
kerning:   // manual kerning
bold:      // faux bold (FauxBold) true/false
italic:    // faux italic (FauxItalic) true/false
underline: // underline (Underline) true/false
]
The body text and run lengths do not change. Keys are added to runs that lack them through inheritance.
Throws an exception for non-text layers or if runIndex is out of range.

---

### setLayerRichText

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` | Layer index. |
| `text` | `&nbsp;` | New body text (line breaks are \\r). |
| `runs` | `void` | [ %[ length: // number of characters it applies to<br>...the same keys as style in setLayerRunStyle<br>],... ]   optional |
| `paragraphs` | `void` | [ %[ length:        // number of characters in the paragraph<br>justification: // alignment 0=left 1=right 2=center<br>],... ]   optional |

**Description**

Replaces the body text, run structure and paragraph structure of a text layer at once

setLayerText collapses styles into the first run, so use this when you want to change the body text
while formatting parts of it differently.

The length of runs / paragraphs is in UTF-16 code units (surrogate pairs such as emoji
count as 2). If the lengths do not add up to the body text length, the last element absorbs the difference
(extended or truncated). Zero-length elements are discarded. Passing void or an empty array
collapses into a single run / single paragraph. A trailing line break (\r) is added if missing.
Each run's style is "the original first run used as a template, with only the given keys overwritten",
so formatting you do not specify keeps its original appearance.

Throws an exception for non-text layers.

---

### setLayerJustification

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` | Layer index. |
| `justification` | `&nbsp;` | Alignment 0=left 1=right 2=center. |
| `paraIndex` | `-1` | Target paragraph index (corresponding to getLayerInfo().text.paragraphs).<br>A negative value means all paragraphs. Defaults to -1. |

**Description**

Changes only the paragraph alignment of a text layer (the body text and runs are unchanged)

Throws an exception for non-text layers or if paraIndex is out of range.

---

### getLayerFonts

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` | Layer index. |

**Return value**

Array of font names.

**Description**

Returns the list of font names in a text layer (candidates for a font selection UI)

Names that can be passed as font to setLayerRunStyle / setLayerRichText.
Throws an exception for non-text layers.

---

### getLayerTextTransform

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` | Layer index. |

**Return value**

`[ xx, xy, yx, yy, tx, ty ]` (tx,ty=translation)

**Description**

Gets the placement (affine transform) of a text layer

Same value as getLayerInfo().text.transform. Throws an exception for non-text layers.

---

### setLayerTextTransform

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` | Layer index. |
| `matrix` | `&nbsp;` | 6-element array [ xx, xy, yx, yy, tx, ty ]. |

**Description**

Replaces the placement (affine transform) of a text layer

Only the text information is rewritten; the layer rectangle (the baked raster)
does not move. Use moveTextLayer for a simple translation.
Throws an exception for non-text layers or if there are too few elements.

---

### moveTextLayer

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` | Layer index. |
| `dx` | `&nbsp;` | Amount to move in X (px). |
| `dy` | `&nbsp;` | Amount to move in Y (px). |

**Description**

Translates a text layer.

Shifts tx/ty of the affine transform and the layer rectangle (and the mask rectangle, if any) by the same amount,
so the raster stored in the PSD moves along with it. Throws an exception for non-text layers.

---

### getLayerTextBounds

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` | Layer index. |

**Return value**

%[ left:, top:, right:, bottom: ]

**Description**

Gets the text frame of a text layer (in the local coordinates of the affine transform;

the position in the document is obtained by adding tx/ty of transform).
Throws an exception for non-text layers.

---

### setLayerTextBounds

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` | Layer index. |
| `left` | `&nbsp;` | Left. |
| `top` | `&nbsp;` | Top. |
| `right` | `&nbsp;` | Right. |
| `bottom` | `&nbsp;` | Bottom. |

**Description**

Replaces the text frame of a text layer (in the local coordinates of the affine transform)

The text flow actually changes only for paragraph text (box text);
for point text, Photoshop rebuilds the frame from the glyphs.
Throws an exception for non-text layers.

---

### clearStorageCache

Method

**Description**

Clears the cache held for the storage

A static method.

---

### getComposite

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `layer` | `&nbsp;` | Destination layer (resized to the document size). |
| `effects` | `true` | Whether to draw layer effects (defaults to true). |
| `background` | `void` | Opaque background color 0xRRGGBB (transparent if omitted / void). |

**Return value**

Counts of things that could not be reproduced:
%[ skipped_adjustments, unsupported_clip_base, unsupported_effects ]

**Description**

Composites the document from its layers

---

### renderLayer

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `layer` | `&nbsp;` | Destination layer. |
| `no` | `&nbsp;` | Layer index. |
| `effects` | `true` | Whether to draw layer effects (defaults to true). |

**Return value**

true if something was drawn. false for groups, dividers, adjustment layers and empty layers.

**Description**

Draws a single layer, with effects, onto a transparent surface (not stacked on the layers below)

Applies the mask, the contents of fill and shape layers, opacity and effects.
left/top of the destination layer are its position in the document, and the rectangle includes
any overflow from effects (shadows, glows, strokes).

---

### getVectorMask

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `no` | `&nbsp;` | Layer index. |

**Return value**

%[ key, inverted, not_linked, disabled, path ], or void if none.
path = %[ subpaths:[ %[ closed, operation, index,
knots:[ %[ anchor:[x,y], preceding:[x,y], leaving:[x,y], linked ], ... ] ], ... ],
initial_fill, clipboard ]
operation is how the subpath is combined (-1 grouped with the previous one / 0 exclude overlapping /
1 combine / 2 subtract front shape / 3 intersect). preceding is the control point of the previous segment,
and leaving the control point of the next segment.

**Description**

Vector mask ('vsms' for shape layers). Coordinates are in document pixels

---

### getPaths

Method

**Return value**

[ %[ id, kind:"saved"|"work", name:<octet>, unicode_name, path ], ... ]
path has the same shape as in getVectorMask.

**Description**

Saved paths (resources 2000 to 2997) and the work path (1025)

---

### getLayerShape

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `no` | `&nbsp;` | Layer index. |

**Return value**

%[ fill_enabled, stroke_enabled,
fill:%[ kind:"solid"|"gradient"|"pattern", descriptor ],
stroke:%[ width (px), alignment:"inside"|"center"|"outside",
cap:"butt"|"round"|"square", join:"miter"|"round"|"bevel",
miter_limit, dashes:[px...], dash_offset (px), opacity (0..1),
blend_mode, content_kind, content ],
origins:[ %[ type:"rectangle"|"rounded_rectangle"|"line"|"ellipse",
type_id, index, box:[l,t,r,b], radii:[top-left,top-right,bottom-right,bottom-left],
line:[x0,y0,x1,y1], line_weight, invalidated ], ... ],
path ]
void if none of these exist. Stroke widths given in pt are converted to px using the document resolution.

**Description**

Shape layer information ('vscg' fill / 'vstk' stroke / 'vogk' live shape)

---

### getShapeMask

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `layer` | `&nbsp;` | Destination layer (left/top are its position in the document; it may extend outside the document). |
| `no` | `&nbsp;` | Layer index. |
| `part` | `"both"` | "fill" (inside of the path) / "stroke" (the shape's stroke) / "both" (default). |

**Return value**

%[ left, top, width, height ]. void if there is no vector mask (for stroke, if there is no stroke).

**Description**

Rasterizes the path of a shape / vector mask (with anti-aliasing)

The coverage is stored in the destination layer as B=G=R=value, A=255 (the same form as getLayerDataMask).
The mask density and feather are not applied.

---

### flattenPath

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `path` | `&nbsp;` | A dictionary in the same shape as path in getVectorMask, or an array of subpaths.<br>A knot may be just [x, y] (a straight-line vertex). closed defaults to true and<br>operation to -1. |
| `tolerance` | `0.1` | Maximum deviation from the curve (px, defaults to 0.1). |

**Return value**

[ %[ closed, operation, points:[ [x,y], ... ] ], ... ]

**Description**

Converts a path into polylines.

A static method.

---

### rasterizePath

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `layer` | `&nbsp;` | Destination layer (resized to width x height). |
| `path` | `&nbsp;` | Same as flattenPath. |
| `width` | `&nbsp;` | Width. |
| `height` | `&nbsp;` | Height. |
| `left` | `0` | Path coordinate corresponding to the top-left of the destination (defaults to 0). |
| `top` | `0` | Same as above (defaults to 0). |

**Description**

Rasterizes the fill of a path (coverage as B=G=R=value, A=255).

A static method.

---

### strokePath

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `layer` | `&nbsp;` | Destination layer (resized to width x height). |
| `path` | `&nbsp;` | Same as flattenPath. |
| `width` | `&nbsp;` | Width. |
| `height` | `&nbsp;` | Height. |
| `style` | `void` | %[ left, top, line_width (defaults to 1), alignment:"center"\|"inside"\|"outside",<br>cap:"butt"\|"round"\|"square", join:"miter"\|"round"\|"bevel",<br>miter_limit (ratio to the line width, defaults to 4), dashes:[dash,gap,...] (px),<br>dash_offset (px) ]<br>inside / outside draw the full line width on only one side of closed subpaths. |

**Description**

Rasterizes the stroke of a path (coverage as B=G=R=value, A=255).

A static method.

---

### setThreads

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `count` | `&nbsp;` | Number of threads to use (including the caller). 0 = automatic (number of logical cores, up to 16),<br>1 = no splitting. The worker threads are stopped when the plugin is unregistered. |

**Description**

Number of threads used for parallel processing in rendering (getComposite / renderLayer / rasterization).

A static method.
Large images are split by rows across multiple threads (the result does not depend on the thread count).
On CPUs with AVX2, compositing for the main blend modes uses a SIMD version that processes 8 pixels at a time.

---

### getThreads

Method

**Return value**

Number of threads actually used for rendering.

**Description**

static method

---
