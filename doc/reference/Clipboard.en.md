# Clipboard

The Clipboard class provides access to the OS **clipboard**. You cannot create objects of this class.

Available in both the native Windows (WINVER) build and the SDL3 build
(the SDL3 build gained support on 2026-08-16; before that it was an empty implementation that did nothing).
In builds for platforms without a clipboard, writes are ignored,
reads always return void, and [hasFormat](#hasformat) always returns false.

Bitmaps ([setAsBitmap](#setasbitmap) / [getAsBitmap](#getasbitmap)) are
currently supported only in the native Windows (WINVER) build;
in other builds they always return false and do nothing.

## Members

### Properties

- [asText](#astext)

### Methods

- [hasFormat](#hasformat)
- [setAsBitmap](#setasbitmap)
- [getAsBitmap](#getasbitmap)

---

### asText

Property \ Access: `r/w`

**Description**

Text format

Represents the text data currently on the clipboard. This property can also be written.

Reading it returns the text data currently on the clipboard. If the clipboard has no text data, void is returned.

Writing it stores text data on the clipboard.

---

### hasFormat

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `format` | `&nbsp;` | Format to check for.<br>You can specify `cbfText` (text) or `cbfBitmap` (bitmap). |

**Return value**

true if the clipboard contains the specified format, false otherwise

**Description**

Checks whether the clipboard contains the specified format

Checks whether the clipboard contains data in the specified **format**.

The OS clipboard can hold several formats at once, so use this method to check whether a particular format is among them.

---

### setAsBitmap

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `layer` | `&nbsp;` | [Layer](Layer.md) object holding the image to write. |

**Return value**

true if the image was written to the clipboard, false otherwise

**Description**

Writes a layer's image to the clipboard

Stores the main image of the specified layer on the clipboard as a bitmap.

Because the data is handed to other applications, alpha values are flattened to 255 (opaque).

---

### getAsBitmap

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `layer` | `&nbsp;` | [Layer](Layer.md) object to read the image into. |

**Return value**

true if the image was read from the clipboard; false if, for example, there is no bitmap data

**Description**

Reads the clipboard image into a layer

Reads bitmap data on the clipboard into the specified layer.

The layer's **image size** is changed to match the image on the clipboard
(the layer's display size does not change, so call [Layer.setSizeToImageSize](Layer.md#setsizetoimagesize) if needed).

---
