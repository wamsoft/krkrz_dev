# VertexBinder

VertexBinder associates a VertexBuffer with the vertex attributes fed to a shader.
Instances of this class are assigned to ShaderProgram properties.
A VertexBinder set on a ShaderProgram is passed to the shader as vertex data when Canvas.drawMesh is called.

## Members

### Constructors

- [VertexBinder](#vertexbinder)

### Properties

- [vertexBuffer](#vertexbuffer)
- [stride](#stride)
- [componentCount](#componentcount)
- [offset](#offset)
- [normalize](#normalize)

---

### VertexBinder

Constructor

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `vertex` | `VertexBuffer` | `&nbsp;` | The VertexBuffer to associate. |
| `stride` | `int` | `0` | Per-vertex stride in bytes. For XY coordinates as floats this is sizeof(float)*2, so specify 8. |
| `componentCount` | `int` | `4` | Number of components per vertex. Specify 2 for XY coordinates, or 4 for an RGBA color. |
| `offset` | `int` | `0` | Offset in bytes from the start of the VertexBuffer. Use this when a single VertexBuffer stores several kinds of vertex data. |
| `normalize` | `bool` | `false` | Whether to normalize. If true, non-float values are normalized to the range [-1.0 to 0.0 to 1.0] before being sent to the shader. |

**Description**

Constructor

---

### vertexBuffer

Property \ Access: `r/w`

**Description**

Vertex buffer (VertexBuffer class, read-only)

---

### stride

Property \ Access: `r/w`

**Description**

Per-vertex stride (bytes)

Defaults to 0.

---

### componentCount

Property \ Access: `r/w`

**Description**

Number of components per vertex (1 to 4)

Defaults to 4.
Specify 2 for XY coordinates.

---

### offset

Property \ Access: `r/w`

**Description**

Vertex buffer offset (bytes)

Defaults to 0.
Specifies the byte offset from the start of the VertexBuffer.
Use this when a single VertexBuffer stores several kinds of vertex data.

---

### normalize

Property \ Access: `r/w`

**Description**

Whether to normalize

Defaults to false.
If true, non-float values are normalized to the range [-1.0 to 0.0 to 1.0] before being sent to the shader.
Use this, for example, when you specify colors as ubyte values from 0 to 255 and want the shader to receive them normalized to 0.0 to 1.0.

---
