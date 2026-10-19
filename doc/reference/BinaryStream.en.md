# BinaryStream

## Members

### Constructors

- [BinaryStream](#binarystream)

### Properties

- [storage](#storage)
- [mode](#mode)

### Methods

- [finalize](#finalize)
- [open](#open)
- [close](#close)
- [read](#read)
- [write](#write)
- [readI8](#readi8)
- [readI16LE](#readi16le)
- [readI32LE](#readi32le)
- [readI64LE](#readi64le)
- [readI16BE](#readi16be)
- [readI32BE](#readi32be)
- [readI64BE](#readi64be)
- [writeI8](#writei8)
- [writeI16LE](#writei16le)
- [writeI32LE](#writei32le)
- [writeI64LE](#writei64le)
- [writeI16BE](#writei16be)
- [writeI32BE](#writei32be)
- [writeI64BE](#writei64be)
- [copy](#copy)
- [compress](#compress)
- [decompress](#decompress)
- [setProgressCallback](#setprogresscallback)
- [setFilter](#setfilter)
- [seek](#seek)
- [tell](#tell)

### Constants

- [bsRead](#bsread)
- [bsWrite](#bswrite)
- [bsAppend](#bsappend)
- [bsUpdate](#bsupdate)
- [bsSeekSet](#bsseekset)
- [bsSeekCur](#bsseekcur)
- [bsSeekEnd](#bsseekend)

---

### BinaryStream

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `storage` | `&nbsp;` |  |
| `mode` | `&nbsp;` |  |

**Description**

Constructor / destructor

---

### storage

Property \ Access: `r`

**Description**

Storage currently open

void if nothing is open.

---

### mode

Property \ Access: `r`

**Description**

Current mode

-1 if nothing is open.

---

### finalize

Method

---

### open

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `storage` | `&nbsp;` | Target storage. |
| `mode` | `&nbsp;` | Mode (bsRead, bsWrite, bsAppend, bsUpdate). |

**Description**

Opens a storage

---

### close

Method

**Description**

Closes the open storage

---

### read

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `size` | `&nbsp;` | Number of bytes to read. |

**Return value**

The data read (as an octet). void if nothing could be read, for example at the end (note: not a zero-length octet).

**Description**

Reads the given number of bytes

---

### write

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `data` | `&nbsp;` | Data to write (an octet or a string). |

**Return value**

Number of bytes written.

**Description**

Writes data

If data is a string, it is written as wchar (no encoding conversion is supported).

---

### readI8

Method

**Return value**

The number read, or void if nothing could be read (for example at the end).

**Description**

Reads {1,2,4,8} bytes as a number

Note: except for 8 bytes, numbers are read as unsigned (no sign extension).
Note: void is returned only if not even 1 byte could be read.
If at least 1 byte but fewer than the requested bytes could be read, the missing part is filled with 0.

---

### readI16LE

Method

**Description**

Reads 2 bytes (little endian)

---

### readI32LE

Method

**Description**

Reads 4 bytes (little endian)

---

### readI64LE

Method

**Description**

Reads 8 bytes (little endian)

---

### readI16BE

Method

**Description**

Reads 2 bytes (big endian)

---

### readI32BE

Method

**Description**

Reads 4 bytes (big endian)

---

### readI64BE

Method

**Description**

Reads 8 bytes (big endian)

---

### writeI8

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `num` | `&nbsp;` | Number to write. |

**Return value**

Number of bytes written.

**Description**

Writes a number as {1,2,4,8} bytes

---

### writeI16LE

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `num` | `&nbsp;` |  |

**Description**

Writes 2 bytes (little endian)

---

### writeI32LE

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `num` | `&nbsp;` |  |

**Description**

Writes 4 bytes (little endian)

---

### writeI64LE

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `num` | `&nbsp;` |  |

**Description**

Writes 8 bytes (little endian)

---

### writeI16BE

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `num` | `&nbsp;` |  |

**Description**

Writes 2 bytes (big endian)

---

### writeI32BE

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `num` | `&nbsp;` |  |

**Description**

Writes 4 bytes (big endian)

---

### writeI64BE

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `num` | `&nbsp;` |  |

**Description**

Writes 8 bytes (big endian)

---

### copy

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `storage` | `&nbsp;` | Source storage (an exception is thrown if it is the storage currently open). |
| `elm` | `void` | Dictionary of options (in/out) with the following members (if omitted, a plain copy with no [out]):<br>offset  :[in] Offset in the source storage to start reading from (defaults to the beginning)<br>length  :[in] Maximum number of bytes to read from the source storage (defaults to the file size)<br>filter  :[in] Name of the filter function (no filtering if omitted)<br>fparam  :[in] Parameter value passed to the filter (int)<br>nocopy  :[in] If true, no output is written (defaults to false; use it when you only want the hash, for example)<br>md5     :[in] If true, returns the MD5 digest of the output<br>hash    :[out] Hash of the data read (Adler32)<br>read    :[out] Number of bytes read<br>digest  :[out] MD5 digest of the data written (octet); only valid when md5 is true |

**Return value**

Number of bytes written.

**Description**

Copies data from another storage

length bytes starting at offset in the source storage are written at the current stream position.
See setFilter() for details on filters.

---

### compress

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `storage` | `&nbsp;` | Source storage (an exception is thrown if it is the storage currently open). |
| `elm` | `void` | Dictionary of options (in/out): the same members as copy(), plus:<br>comp_lv :[in] zlib compression level (1 to 9). 9 if omitted or if elm itself is not given. |

**Return value**

Number of bytes written.

**Description**

Copies data from another storage while compressing it

Compresses the source storage with zlib/deflate and writes it at the current stream position.
The filter function is applied to the data before compression.

---

### decompress

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `storage` | `&nbsp;` | Source storage (an exception is thrown if it is the storage currently open). |
| `elm` | `void` | Dictionary of options (in/out): the same as copy(). |

**Return value**

Number of bytes written.

**Description**

Copies data from another storage while decompressing it

Decompresses the source storage with zlib/inflate and writes it at the current stream position.
An exception is thrown if decompression fails.
The filter function is applied to the decompressed data.
hash [out] is computed over the decompressed and filtered data.

---

### setProgressCallback

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `callback` | `&nbsp;` | Callback function: function(storage, read_size) { return true_if_cancel; }<br>void removes it. |

**Description**

Sets a progress callback

Sets a function that is called back during copy/compress/decompress.
In the current implementation, the callback is called every 1 MiB read and when the end is reached.
Returning true from the callback cancels the operation.
Note: the callback interval may change.

From TJS's point of view the script blocks during the operation, by design, but using something like
the windowExProgress plugin lets the user cancel it.

---

### setFilter

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `dll` | `&nbsp;` | Target DLL file (void removes the setting). |

**Description**

Sets a filter DLL

Sets a filter, implemented in an external DLL, applied to the data of copy/compress/decompress.
When a function name is given in elm.filter, the function exported from this DLL in the following form is used as the filter:
void (__stdcall *FilterProc)(uint32 hash, uint64 offset, void *buffer, uint32 length);

---

### seek

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `pos` | `&nbsp;` | Position. |
| `whence` | `&nbsp;` | Reference point (bsSeekSet, bsSeekCur, bsSeekEnd). |

**Return value**

The position after moving.

**Description**

Changes the stream position

---

### tell

Method

**Return value**

Position.

**Description**

Gets the current stream position

---

### bsRead

Constant

Value: `0`

**Description**

Read

---

### bsWrite

Constant

Value: `1`

**Description**

Write

---

### bsAppend

Constant

Value: `2`

**Description**

Append

---

### bsUpdate

Constant

Value: `3`

**Description**

Update

---

### bsSeekSet

Constant

Value: `0`

**Description**

From the beginning

---

### bsSeekCur

Constant

Value: `1`

**Description**

From the current position

---

### bsSeekEnd

Constant

Value: `2`

**Description**

From the end

---
