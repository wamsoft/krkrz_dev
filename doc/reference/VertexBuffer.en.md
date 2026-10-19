# VertexBuffer

VertexBuffer holds vertex data.

Use it when you want fine control over positions, UV coordinates, vertex colors, and so on.
It is also used for things other than simple rectangles, such as mesh deformation or point sprites.

Pointer access is also available so that plugins can modify the vertex array directly (OpenGL ES 3.0 or later only).
Combining shaders, TJS2 script, and vertex manipulation in plugins keeps the kind of Layer extensibility available before.
This is somewhat more complex than the previous approach, where almost everything was contained within a plugin.

## Members

### Constructors

- [VertexBuffer](#vertexbuffer)
- [VertexBuffer](#vertexbuffer)

### Properties

- [size](#size)
- [dataType](#datatype)
- [updateType](#updatetype)
- [isIndex](#isindex)
- [nativeHandle](#nativehandle)

### Methods

- [setVertex](#setvertex)
- [lock](#lock)
- [unlock](#unlock)

### Constants

- [dtByte](#dtbyte)
- [dtUByte](#dtubyte)
- [dtShort](#dtshort)
- [dtUShort](#dtushort)
- [dtInt](#dtint)
- [dtUInt](#dtuint)
- [dtFixed](#dtfixed)
- [dtFloat](#dtfloat)
- [utStream](#utstream)
- [utStatic](#utstatic)
- [utDynamic](#utdynamic)
- [ptPoints](#ptpoints)
- [ptLineStrip](#ptlinestrip)
- [ptLineLoop](#ptlineloop)
- [ptLines](#ptlines)
- [ptTriangleStrip](#pttrianglestrip)
- [ptTriangleFan](#pttrianglefan)
- [ptTriangles](#pttriangles)

---

### VertexBuffer

Constructor

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `size` | `int` | `&nbsp;` | Size of the buffer in bytes. |
| `dataType` | `int` | `&nbsp;` | Data type: dtByte/dtUByte/dtShort/dtUShort/dtInt/dtFloat. |
| `updateType` | `int` | `&nbsp;` | Update frequency: utStream/utStatic/utDynamic. |
| `isIndex` | `bool` | `false` | Whether this is an index buffer. false for a vertex buffer. |

**Description**

Creates an uninitialized vertex buffer

---

### VertexBuffer

Constructor

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `data` | `Array` | `&nbsp;` | Vertex array. The buffer size is the number of elements in this array times the size of the data type. |
| `dataType` | `int` | `&nbsp;` | Data type: dtByte/dtUByte/dtShort/dtUShort/dtInt/dtFloat. |
| `updateType` | `int` | `&nbsp;` | Update frequency: utStream/utStatic/utDynamic. |
| `isIndex` | `bool` | `false` | Whether this is an index buffer. false for a vertex buffer. |

**Description**

Creates a vertex buffer from a vertex array

---

### size

Property \ Access: `r/w`

**Description**

Buffer size (read-only)

---

### dataType

Property \ Access: `r/w`

**Description**

Vertex data type (read-only)

---

### updateType

Property \ Access: `r/w`

**Description**

Update frequency (read-only)

---

### isIndex

Property \ Access: `r/w`

**Description**

Whether this is an index buffer (read-only)

---

### nativeHandle

Property \ Access: `r/w`

**Description**

Native handle

---

### setVertex

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `array` | `Array` | `&nbsp;` | Vertex array. |
| `offset` | `int` | `0` | Array index at which to start the update (in elements, not bytes). |

**Description**

Sets or updates vertex data

Fails (throws an exception) for a static buffer.

---

### lock

Method

**Return value**

A pointer to the vertex data, or null if locking fails.

**Description**

Locks the vertex data and returns a pointer to it (read/write)

For plugins (requires OpenGL ES 3.0 or later).

---

### unlock

Method

**Description**

Unlocks the vertex data

For plugins (requires OpenGL ES 3.0 or later).
Call this after you finish passing data and before the buffer is used.
Rather than keeping the buffer locked, unlock it immediately after updating.

---

### dtByte

Constant

**Description**

Data type constant (byte)

---

### dtUByte

Constant

**Description**

Data type constant (unsigned byte)

---

### dtShort

Constant

**Description**

Data type constant (short)

---

### dtUShort

Constant

**Description**

Data type constant (unsigned short)

---

### dtInt

Constant

**Description**

Data type constant (int); requires ES 3.0 or later

---

### dtUInt

Constant

**Description**

Data type constant (unsigned int); requires ES 3.0 or later

---

### dtFixed

Constant

**Description**

Data type constant (fixed: fixed-point)

---

### dtFloat

Constant

**Description**

Data type constant (float)

---

### utStream

Constant

**Description**

Update frequency constant: updated every frame

---

### utStatic

Constant

**Description**

Update frequency constant: never changes

---

### utDynamic

Constant

**Description**

Update frequency constant: updated frequently

---

### ptPoints

Constant

**Description**

Primitive type constant (point list)

---

### ptLineStrip

Constant

**Description**

Primitive type constant (line strip)

---

### ptLineLoop

Constant

**Description**

Primitive type constant (line loop)

---

### ptLines

Constant

**Description**

Primitive type constant (line list)

---

### ptTriangleStrip

Constant

**Description**

Primitive type constant (triangle strip)

---

### ptTriangleFan

Constant

**Description**

Primitive type constant (triangle fan)

---

### ptTriangles

Constant

**Description**

Primitive type constant (triangle list)

---
