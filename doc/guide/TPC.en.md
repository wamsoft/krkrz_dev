---
source_hash: b04e9e09eb14
---

# Image Format Converter

## About the image format converter

The image format converter ( `krkrimg` ) converts images used in Kirikiri between formats.
It succeeds the Kirikiri 2 image format converter ( krkrtpc.exe ), and its conversion rules (separate formats for opaque images and images with transparent areas, handling of the color in fully transparent areas, conversion to ltAddAlpha, and tag information) are the same as the old version.

Like the other [standard tools](Tools.md), it opens its GUI in a browser window when launched. It can also be used on the command line without opening the GUI (see "Using the command line" below).

Input file formats are BMP, PNG, JPEG, TLG5, TLG6, PSD, and CLIP STUDIO (.clip); the output file format can be BMP, PNG, TLG5, TLG6, or JPEG.

It can also read and write transparent images in the separate main/mask format that Kirikiri uses. The term "mask" here is synonymous with alpha channel.

It can also export the layers of PSD / CLIP files one by one as images (see "Exporting layers" below).

Since it basically just converts image formats, images it outputs (other than TLG) can be used with other software and tools as well.

And, though this is not specific to this tool, **don't forget to make backups!**

## Input image formats

The following input file formats can be used. The format is determined from the file contents.

- **BMP**  
  The standard Windows bitmap format. 32-bit (bpp) BMPs are treated as BMPs with an alpha channel.
  
  BMPs in other formats are treated as opaque images (images without transparency information), except when used in the separate main/mask format described below.
- **PNG**  
  The Portable Network Graphics format. PNGs with transparent areas (with an alpha channel or transparency information) can also be read.
  
  For PNGs with oFFs / vpAg / pHYs chunks, that information is carried over as tag information (see "Tag information" below).
- **JPEG**  
  Common full-color and grayscale JPEGs can be read. JPEG can also be used as input in the separate main/mask format described below.
- **TLG5 / TLG6**  
  Kirikiri's TLG format. Tag information is also read.
  
  A TLG whose tag information has mode=alpha or mode=addalpha is treated as an ltAlpha / ltAddAlpha image according to that mode (this takes precedence over the "Treat input as ltAddAlpha" setting described below).
- **PSD**  
  The Adobe Photoshop format (PSB can also be read).
  
  The image is read by compositing it from the layers. Compositing uses psdparse and includes blend modes other than "Normal", layer effects, and adjustment layers. For a PSD without layers, or one that cannot be composited from its layers, the composite image saved in the file is used.
  
  The composited result is converted as a single image (whatever blend modes the layers use, the output mode tag is one of opaque / alpha / addalpha, described below). To make use of each layer's blend mode, use "Exporting layers".
  
  This format cannot be read as the separate main/mask format.
- **CLIP STUDIO (.clip)**  
  The CLIP STUDIO PAINT format. The image is read by compositing it from the layers using clipparse.
  
  This format cannot be read as the separate main/mask format.
- **Separate main/mask format**  
  In the separate main/mask format, the main image (color information) and the mask image (transparency information) are separate files.
  
  The mask image's file name is the main image's file name with _m appended (for example, test_m.jpg for test.jpg). The brightness of the mask image becomes the opacity.
  
  The valid input image formats for the separate main/mask format are BMP, JPEG, and PNG. The main and mask may be in different formats (such as test_m.png for test.jpg). The main and mask images must be the same size.
  
  If a mask image corresponding to a main image exists, the pair is automatically read as the separate main/mask format. If you specify both the main image and the mask image as conversion targets, the mask image is removed from the targets, since it will be "read as the main image's mask".

> **Note:**
> The ERI format is not supported.

## Output image formats

The following output image formats can be used.

- **24-bit/32-bit BMP**  
  A 24-bit BMP has no alpha channel.
  
  A 32-bit BMP has an alpha channel, holding both main and mask in a single file.
- **PNG**  
  A full-color PNG, or a PNG with an alpha channel.
- **TLG5**  
  A full-color TLG5, or a TLG5 with an alpha channel. The extension is .tlg.
- **TLG6**  
  A full-color TLG6, or a TLG6 with an alpha channel. The extension is .tlg.
  
  As with TLG5 images, tag information is written for TLG6 images.
- **JPEG**  
  Can be chosen only as the output format for opaque images. You can specify the compression quality (1 to 100, default 90).
- **Separate main/mask format**  
  For images with transparent areas, records the main and mask in separate files. BMP, JPEG, or PNG can be chosen for each. For JPEG, the compression quality (default 90) can be specified separately for the main and mask.
  
  The mask image's file name is the main image's file name with _m appended (for example, test_m.jpg for test.jpg). The mask image is written in grayscale.
  
  The main and mask can be in different image formats, but the BMP + BMP and PNG + PNG combinations make little sense; it is better to choose the 32-bit BMP or PNG with an alpha channel described above.
  
  Using JPEG for either or both saves file size but lowers image quality.
  
  TLG5 or TLG6 cannot be specified for the separate main/mask format.

TLG5 / TLG6 writing is ported from the Kirikiri Z engine code, and for the same image it outputs a TLG with exactly the same bytes as the engine would.

## Opaque images and images with transparent areas

You can specify different formats for opaque images and for images with transparent areas.

An "opaque image" here means an image that is fully opaque over its entire area (for example, a background image). An "image with transparent areas" means an image that has areas that become transparent (for example, a foreground image).

Even if the image format can hold transparency information, an image in which every pixel ends up fully opaque is treated as an "opaque image".

By default, both opaque images and images with transparent areas are output as TLG5.

## Options for images with transparent areas

### Color in fully transparent areas

Specifies how fully transparent areas of the image are processed.

Normally, an ltAlpha image holds color information even in fully transparent areas. Since those areas are fully transparent, they are simply ignored when displayed, but they are not ignored when the image is processed (including compression such as JPEG).

This setting specifies how these fully transparent areas are processed.

- **除去 (Remove)** (default)  
  The color information in fully transparent areas is removed (more precisely, filled with black).
  
  This setting is normally fine.
- **そのまま (Keep)**  
  No processing is done. The original image is left as is.
  
  If there is garbage in the fully transparent areas, that garbage gets compressed too, which worsens the compression ratio.
- **合成 (Blend)** (blend with surrounding colors)  
  Estimates the color of fully transparent areas from the colors of the surrounding opaque areas and blends them in.
  
  In the GUI, you can choose the blend strength from 1, 2, 3, 5, or 8 pixels. The color of a fully transparent area is blended from the colors of opaque pixels within the specified distance in pixels. Larger values take longer to process. Colors in fully transparent areas beyond the specified distance are removed.
  
  For example, when compressing the main image with JPEG, the nature of JPEG causes mosquito noise where colors change abruptly. In a foreground image, this tends to occur at the boundary between fully transparent and opaque areas if there is an abrupt color change there and no blending is done. Blending derives the color of fully transparent areas from the colors of opaque areas, which reduces the color difference and suppresses mosquito noise. Also, in typical JPEG, color information mixes with neighboring pixels; blending also prevents unintended colors of fully transparent areas (as they would be without blending) from mixing with the colors of opaque areas.
  
  Normally, choose "Remove". Fully transparent areas need no color information, and removing it also makes the compressed file smaller.

This option is not used when outputting in ltAddAlpha format, because "fully transparent" in ltAddAlpha can only mean opacity 0 with pure black color.

### Treat input as ltAddAlpha

When this option is specified, the input image is treated as being in ltAddAlpha format, that is, the additive alpha compositing format suitable for display with ltAddAlpha set in Kirikiri's [Layer.type](../reference/Layer.md#type) property.

Without this option, input images are treated as ltAlpha. Most graphics software outputs ltAlpha, and the PNG specification is also ltAlpha, so normally do not specify this option.

However, TLG images follow their own mode tag (alpha / addalpha).

Specifying this option automatically specifies "Output in ltAddAlpha format" as well. In addition, the "Color in fully transparent areas" option is no longer used (neither alpha nor color information is processed by the image format converter).

### Output in ltAddAlpha format

When this option is specified, the output image is written in ltAddAlpha format.

If the input is ltAlpha, it is converted from ltAlpha to ltAddAlpha (the color is multiplied by the opacity).

Without this option, the output image has the same format as the input (normally ltAlpha).

Various graphics software and the PNG specification accept only ltAlpha images, so unless the output image is for use in Kirikiri, normally do not specify this option.

When this option is specified, the "Color in fully transparent areas" option is no longer used (neither alpha nor color information is processed by the image format converter).

## Tag information

The image format converter writes "tag information" to TLG and PNG images. Tag information includes things such as how the image should be displayed. It can be obtained as the return value of the [Layer.loadImages](../reference/Layer.md#loadimages) method.

The following tag information is written.

- **mode** (TLG only)  
  The display mode of the image. It writes mode=opaque for an "opaque image", mode=alpha for an "image with transparent areas", and mode=addalpha when output in ltAddAlpha format.
  
  "Exporting layers" writes the mode corresponding to each layer's blend mode (psmul and so on).
  
  Kirikiri has a dictionary named imageTagLayerType in the TJS global object, which describes how the mode in a TLG image's tag information maps to the layer type. It is defined as follows.
  
  ```
  global.imageTagLayerType = %[
      opaque      :%[type:ltOpaque            ],
      rect        :%[type:ltOpaque            ],
      alpha       :%[type:ltAlpha             ],
      transparent :%[type:ltAlpha             ],
      addalpha    :%[type:ltAddAlpha          ],
      add         :%[type:ltAdditive          ],
      sub         :%[type:ltSubtractive       ],
      mul         :%[type:ltMultiplicative    ],
      dodge       :%[type:ltDodge             ],
      darken      :%[type:ltDarken            ],
      lighten     :%[type:ltLighten           ],
      screen      :%[type:ltScreen            ],
      psnormal    :%[type:ltPsNormal          ],
      psadd       :%[type:ltPsAdditive        ],
      pssub       :%[type:ltPsSubtractive     ],
      psmul       :%[type:ltPsMultiplicative  ],
      psscreen    :%[type:ltPsScreen          ],
      psoverlay   :%[type:ltPsOverlay         ],
      pshlight    :%[type:ltPsHardLight       ],
      psslight    :%[type:ltPsSoftLight       ],
      psdodge     :%[type:ltPsColorDodge      ],
      psdodge5    :%[type:ltPsColorDodge5     ],
      psburn      :%[type:ltPsColorBurn       ],
      pslighten   :%[type:ltPsLighten         ],
      psdarken    :%[type:ltPsDarken          ],
      psdiff      :%[type:ltPsDifference      ],
      psdiff5     :%[type:ltPsDifference5     ],
      psexcl      :%[type:ltPsExclusion       ],
  ]
  ```
  
  For each layer type, see [Layer.type](../reference/Layer.md#type).
- **offs_x** **offs_y** **offs_unit** (TLG, PNG)  
  These are output only when the source is a PNG containing offset information from the image's top-left corner (an oFFs chunk).
  
  offs_x is the horizontal distance from the left edge, and offs_y is the vertical distance from the top edge. offs_unit is either **pixel** or **micrometer** and indicates the unit of distance.
- **vpag_w** **vpag_h** **vpag_unit** (TLG, PNG)  
  These are output only when the source is a PNG containing Virtual PAGe information, that is, the size of the whole image (a vpAg chunk).
  
  [ImageMagick](https://imagemagick.org/) is one piece of software that writes this information to PNGs; when you trim an image with ImageMagick, this information is written as the image size before trimming. The caNv chunk written by ImageMagick is also read and treated as vpag_* and offs_* (in pixels).
  
  vpag_w is the width of the whole image, vpag_h is the height of the whole image, and vpag_unit is either **pixel** or **micrometer** and indicates the unit of size.
- **reso_x** **reso_y** **reso_unit** (TLG, PNG)  
  These are output only when the source is a PNG containing the image's resolution information (a pHYs chunk).
  
  reso_x is the horizontal resolution and reso_y is the vertical resolution. reso_unit is **meter** and indicates the unit of resolution.

When the input is a TLG, the tag information it had is carried over. When outputting to PNG, offs_* / vpag_* / reso_* are written as oFFs / vpAg / pHYs chunks, respectively. Other tags such as mode are not written to PNG.

## Exporting layers

The layers of PSD / CLIP files can be exported one by one as image files (currently only with the command-line `layers` command).

- A folder named after the source file (without the extension) is created in the output destination, and layers are written into it as "number_layername.png" (numbers start at 000, from the bottom layer up). The format can be chosen from PNG (default) / TLG5 / TLG6.
- Each image is written at the size of the rectangle the layer occupies. For PSD, layers are written with layer effects applied (if an effect extends beyond the layer, the rectangle grows accordingly).
- Folders (groups), adjustment layers, and layers without pixels are not exported. Hidden layers (including those whose parent folder is hidden) are exported only when requested.
- For each image, the position in the document is written to the tag information as offs_x / offs_y (in pixels), and the size of the whole document as vpag_w / vpag_h (in pixels). For TLG, a mode tag corresponding to the layer's blend mode is also written. For PSD, the mapping is as follows (no mode tag is written for blend modes without a counterpart). For CLIP, mode=alpha is written only for "Normal" layers.

| PSD blend mode | mode |
|---|---|
| Normal | alpha |
| Linear Dodge (Add) | psadd |
| Linear Burn | pssub |
| Multiply | psmul |
| Screen | psscreen |
| Overlay | psoverlay |
| Hard Light | pshlight |
| Soft Light | psslight |
| Color Dodge | psdodge |
| Color Burn | psburn |
| Lighten | pslighten |
| Darken | psdarken |
| Difference | psdiff |
| Exclusion | psexcl |

- The "Color in fully transparent areas" setting (default: remove) also applies to exported layers.
- The list of layers is written to the same folder as `layers.json`.

```
{
 "source": "chara.psd",
 "width": 32,
 "height": 24,
 "layers": [
  {
   "file": "000_red.png",
   "name": "red",
   "folder": "",
   "index": 0,
   "visible": true,
   "left": 3,
   "top": 2,
   "width": 10,
   "height": 8,
   "opacity": 255,
   "blend": "norm",
   "mode": "alpha"
  },
  ...
 ]
}
```

width / height are the size of the whole document. The fields of each layer are as follows.

| Field | Content |
|---|---|
| file | File name of the exported image |
| name | Layer name |
| folder | Names of the parent folders joined with / (empty at the top level) |
| index | Layer number in the source file |
| visible | Whether the layer and all its parent folders are visible |
| left / top | Position in the document |
| width / height | Size of the exported image |
| opacity | Layer opacity (0 to 255) |
| blend | Original blend mode (a 4-character key for PSD, a number for CLIP) |
| mode | Corresponding Kirikiri mode (empty if none) |

## Using the GUI

Launching `krkrimg` shows the GUI in a browser window. If you pass files as arguments at launch, they are opened as conversion targets.

- **「ファイル」 (Files)**  
  Choose files to convert with 「追加…」 (Add...) (multiple files can be selected). 「クリア」 (Clear) empties the list.
  
  The list shows each file's format, width and height, whether it has transparent areas, and notes (the mask image of the separate main/mask format, the number of layers in a PSD / CLIP, the mode tag of a TLG, and so on). Files that will be read as another file's mask image are marked as such.
- **「不透明な画像」 (Opaque images)**  
  Choose the output format for opaque images from TLG5 / TLG6 / PNG / BMP (24-bit) / JPEG. For JPEG, the quality can also be specified.
- **「透明部分のある画像」 (Images with transparent areas)**  
  Choose the output format for images with transparent areas from TLG5 / TLG6 / PNG / BMP (32-bit) / separate main/mask. For separate main/mask, you can specify the main and mask formats (JPEG / PNG / BMP) and the JPEG quality.
  
  Here you also specify 「完全透明部分の色」 (Color in fully transparent areas) (remove / keep / blend with surrounding colors (1, 2, 3, 5, 8px)), 「入力を ltAddAlpha 形式とみなす」 (Treat input as ltAddAlpha), and 「ltAddAlpha 形式で出力する」 (Output in ltAddAlpha format).
- **「出力フォルダ」 (Output folder)**  
  When empty, output goes to the same folder as the input file. When a folder is specified, output goes to that folder. You can also choose a folder with 「参照…」 (Browse...).
  
  A relative path is resolved relative to the folder containing the input file (same as the old version).
  
  When 「上書き」 (Overwrite) is checked, files with the same name are overwritten. When unchecked, a file with the same name causes the conversion of that file to fail with an error.
- **「変換する」 (Convert)**  
  Starts the conversion. While it is running, you can stop it with 「中断」 (Abort).
  
  After the conversion, a list shows whether each file was converted successfully or failed (along with the output file name and the mode written), so check it.

> **Note:**
> If the output would be the same file as the input file (for example, outputting a TLG as TLG in the same folder), an error occurs. Specify a different folder as the output folder.

## Using the command line

With `--cli`, the tool processes on the command line without opening the GUI and then exits.

```
krkrimg --cli info    <ファイル>...
krkrimg --cli convert <ファイル>... [オプション]
krkrimg --cli layers  <PSD / CLIP>... [オプション]
```

- **info**  
  Shows the image format, size, whether it has transparent areas, the number of layers in a PSD / CLIP, the mask image of the separate main/mask format, and the tag information.
- **convert**  
  Converts images. This is the same processing as conversion in the GUI.
- **layers**  
  Exports the layers of PSD / CLIP files (see "Exporting layers" above).

Options that take a value are specified as `--name=value`.

| Option | Description |
|---|---|
| `--opaque=FORMAT` | Format for opaque images: `tlg5` / `tlg6` / `png` / `bmp` / `jpg` (default `tlg5`) |
| `--alpha=FORMAT` | Format for images with transparent areas: `tlg5` / `tlg6` / `png` / `bmp` / `sep` (default `tlg5`; `sep` is the separate main/mask format) |
| `--sep-main=FORMAT` | Main format for the separate format: `jpg` / `png` / `bmp` (default `jpg`) |
| `--sep-mask=FORMAT` | Mask format for the separate format: `jpg` / `png` / `bmp` (default `jpg`) |
| `--quality=Q` | Quality when writing opaque images as JPEG, 1 to 100 (default 90) |
| `--main-quality=Q` | JPEG quality of the main image in the separate format (default 90) |
| `--mask-quality=Q` | JPEG quality of the mask image in the separate format (default 90) |
| `--transparent=METHOD` | Color in fully transparent areas: `remove` (default) / `keep` / `expand1` to `expand8` (blend with the colors of the surrounding N pixels) |
| `--input-addalpha` | Treats input as ltAddAlpha (also implies `--addalpha`) |
| `--addalpha` | Outputs in ltAddAlpha format |
| `--format=FORMAT` | layers: export format `png` / `tlg5` / `tlg6` (default `png`) |
| `--hidden` | layers: also exports hidden layers |
| `--out=DIR` | Output folder. If omitted, the same folder as the input file |
| `--force` | Overwrites files with the same name in the output destination |
| `--json` | Outputs the results as JSON |
| `--quiet` | Does not show progress |

> **Note:**
> A relative path given to `--out` on the command line is resolved relative to the **current folder** (the same as the other standard tools). Note that this differs from the GUI's 「出力フォルダ」 (Output folder) field, which is relative to the input file's folder.

For example:

```
# 背景は TLG5、立ち絵は TLG6 にして out フォルダへ
krkrimg --cli convert bg01.png chara01.png --opaque=tlg5 --alpha=tlg6 --out=out

# 透明部分のある画像をメイン JPEG + マスク PNG の分離形式に (周囲 3 ピクセルの色で合成)
krkrimg --cli convert chara01.png --alpha=sep --sep-main=jpg --sep-mask=png --transparent=expand3

# ltAddAlpha 形式の TLG5 を作る
krkrimg --cli convert effect.png --addalpha

# PSD のレイヤを TLG6 で書き出す (非表示のレイヤも含める)
krkrimg --cli layers chara.psd --format=tlg6 --hidden --out=layers
```

convert prints one line per file, in the form 「変換 (tab) input (tab) → output (tab) (mode)」 on success or 「失敗 (tab) input (tab) reason」 on failure.

### Exit codes

| Value | Meaning |
|---|---|
| 0 | All files succeeded |
| 2 | Some files failed (could not be read, the output already exists, invalid options, and so on) |
