# Live2DDevice

## Members

### Constructors

- [Live2DDevice](#live2ddevice)

### Methods

- [onBeginScene](#onbeginscene)
- [onEndScene](#onendscene)
- [prepareShaders](#prepareshaders)

---

### Live2DDevice

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `oglbase` | `&nbsp;` | Object that holds GetProcAddress.<br>One of the following can be specified:<br>- The OpenGL context object provided by the krkrgles plugin<br>- The OGLDrawDevice of newer Kirikiri Z versions (the engine's built-in OpenGL draw device)<br>The device is initialized for the current OpenGL context. |

---

### onBeginScene

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `width` | `&nbsp;` |  |
| `height` | `&nbsp;` |  |

**Description**

Call once at the start of drawing the whole scene

Note: call this in the context the device was created in.

---

### onEndScene

Method

**Description**

Call once when drawing the whole scene is finished

---

### prepareShaders

Method

**Description**

Precompiles the shaders

If not called, the shaders are compiled all at once on the first draw,
causing a wait of a few seconds, so calling it at startup or similar is recommended.
Note: call this in the context the device was created in.

---
