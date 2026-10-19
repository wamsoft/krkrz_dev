# ShaderProgram

Holds a compiled and linked pair of vertex and fragment shaders.
Compilation and linking happen in the constructor; if there is an error, an exception is thrown, so check the log and fix the shader.
The parameters used as shader inputs are added as members, so you can set their values through those members.
Variable names are obtained from the shader through reflection.
Inputs such as textures use predefined reserved names, and the shader is written using those names.
Attribute values (vertex data) can be set through members only when drawMesh is used with VertexBuffer/VertexBinder.
The member functions and properties that ShaderProgram already has naturally cannot be used as input variable names in a shader (which is why only a minimal set of members has been added so far).

If you set a value on a property added for an input name defined in the shader, that value is applied when drawing.
Added properties can only be set, not read.
Values persist, so when reusing the same shader you need to change them to the desired values before drawing.
Property types are obtained from the shader source.
Types such as vec4 are passed as an Array of real values.

Reserved names are set automatically and internally at draw time, so you do not need to set them explicitly (except with drawMesh).
For example, s_tex0 receives the first texture ID.
Which values are set automatically depends on the drawing command.

If shaders can be specified from script and swapped freely, effects that previously required writing a plugin to extend Layer can be added with TJS2 script alone, and they are expected to run faster than conventional CPU processing.
There is currently no Layer-equivalent functionality, but by enriching the supporting features needed to implement things like Layer/Sprite in TJS2 script, those parts can be written in script, reducing the need for native (C++) plugins.
Distributing a shader together with the TJS2 script that implements a Sprite (or similar) using it is enough to enhance effects.

When loading shader source from a file, write it in UTF-8.


Variable names that cannot be used in shaders (defined internally)

+ ShaderProgram
+ finalize

Names of values that are set automatically

+ Textures: s_tex0, s_tex1, s_tex2, s_tex3...
+ Vertex position: a_pos(vec2)
+ Texture coordinates: a_texCoord(vec2)
+ Matrix: a_modelMat4(mat4)


GLSL structs and arrays are not supported in this initial stage.

## Members

### Constructors

- [ShaderProgram](#shaderprogram)

---

### ShaderProgram

Constructor

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `vertex` | `string` | `&nbsp;` | The vertex shader.<br>When file is true, specify a file name; when false, specify the source string directly. |
| `fragment` | `string` | `&nbsp;` | The fragment shader.<br>When file is true, specify a file name; when false, specify the source string directly. |
| `vsfile` | `boolean` | `true` | Selects whether the string given in vertex is a file name or the shader source itself. |
| `fsfile` | `boolean` | `true` | Selects whether the string given in fragment is a file name or the shader source itself. |

**Description**

Constructor

---
