# Rect

The Rect class holds a rectangle.

## Members

### Constructors

- [Rect](#rect)
- [Rect](#rect)
- [Rect](#rect)

### Properties

- [width](#width)
- [height](#height)
- [left](#left)
- [top](#top)
- [right](#right)
- [bottom](#bottom)
- [nativeArray](#nativearray)

### Methods

- [setSize](#setsize)
- [setOffset](#setoffset)
- [addOffset](#addoffset)
- [clear](#clear)
- [set](#set)
- [isEmpty](#isempty)
- [clip](#clip)
- [union](#union)
- [intersects](#intersects)
- [included](#included)
- [includedPos](#includedpos)
- [equal](#equal)

---

### Rect

Constructor

**Description**

Constructs a Rect object

Constructs an object of the Rect class.

---

### Rect

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `left` | `&nbsp;` | Left edge. |
| `top` | `&nbsp;` | Top edge. |
| `right` | `&nbsp;` | Right edge. |
| `bottom` | `&nbsp;` | Bottom edge. |

**Description**

Constructs a Rect object

Constructs an object of the Rect class with the given size.

---

### Rect

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `src` | `&nbsp;` | Rect object to copy from. |

**Description**

Constructs a Rect object

Constructs an object of the Rect class from another Rect object.

---

### width

Property \ Access: `r/w`

**Description**

Rectangle width

Width of the rectangle.

The value can also be set.

**See also:** [Rect.setSize](Rect.md#setsize)

---

### height

Property \ Access: `r/w`

**Description**

Rectangle height

Height of the rectangle.

The value can also be set.

**See also:** [Rect.setSize](Rect.md#setsize)

---

### left

Property \ Access: `r/w`

**Description**

Left edge

Left edge of the rectangle.

The value can also be set.

**See also:** [Rect.setOffset](Rect.md#setoffset)

---

### top

Property \ Access: `r/w`

**Description**

Top edge

Top edge of the rectangle.

The value can also be set.

**See also:** [Rect.setOffset](Rect.md#setoffset)

---

### right

Property \ Access: `r/w`

**Description**

Right edge

Right edge of the rectangle.

The value can also be set.

---

### bottom

Property \ Access: `r/w`

**Description**

Bottom edge

Bottom edge of the rectangle.

The value can also be set.

---

### nativeArray

Property \ Access: `r`

**Description**

Pointer to the rectangle buffer

A pointer to the coordinate array of the rectangle.

This property exists to give plugins and similar code direct access to the coordinate
array buffer.

It is returned as an integer; in a plugin, cast it to a suitable type (such as int[4])
before use.

---

### setSize

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `width` | `&nbsp;` | Width of the rectangle.<br>This value can also be read and set with the [Rect.width](Rect.md#width) property. |
| `height` | `&nbsp;` | Height of the rectangle.<br>This value can also be read and set with the [Rect.height](Rect.md#height) property. |

**Description**

Sets the rectangle size

Sets the size of the rectangle.

---

### setOffset

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | X coordinate of the rectangle.<br>This value can also be read and set with the [Rect.left](Rect.md#left) property. |
| `y` | `&nbsp;` | Y coordinate of the rectangle.<br>This value can also be read and set with the [Rect.top](Rect.md#top) property. |

**Description**

Sets the rectangle position

Sets the position of the rectangle.

---

### addOffset

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | Horizontal amount to move. |
| `y` | `&nbsp;` | Vertical amount to move. |

**Description**

Moves the rectangle

Moves the rectangle.

The rectangle is moved by the given x and y amounts.

---

### clear

Method

**Description**

Clears the rectangle

Sets every edge of the rectangle to zero.

---

### set

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `left` | `&nbsp;` | Left edge. |
| `top` | `&nbsp;` | Top edge. |
| `right` | `&nbsp;` | Right edge. |
| `bottom` | `&nbsp;` | Bottom edge. |

**Description**

Sets the rectangle coordinates

Sets the rectangle to the given edges.

---

### isEmpty

Method

**Return value**

Whether the area is empty

**Description**

Whether the rectangle is empty

Checks whether the rectangle has a width and a height.

Returns true if either of them is 0 or less.

---

### clip

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `r` | `&nbsp;` | Rectangle object to clip with. |

**Return value**

Whether clipping was done

**Description**

Clips the rectangle

Clips the rectangle with the given rectangle.

Clipping is done only if the result is not empty.

If the result would be empty, false is returned and the rectangle is left unchanged.

**See also:** [Rect.isEmpty](Rect.md#isempty)

---

### union

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `r` | `&nbsp;` | Rectangle object to unite with. |

**Return value**

Whether the union was done

**Description**

Unites rectangles

Extends the rectangle with the given rectangle object.

The rectangle becomes the smallest one that contains both rectangles.

This is done only if the target rectangle is not empty; if it is empty, nothing is done and false is returned.

**See also:** [Rect.isEmpty](Rect.md#isempty)

---

### intersects

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `r` | `&nbsp;` | Rectangle object to test. |

**Return value**

Whether they intersect

**Description**

Tests intersection

Tests whether the rectangle intersects the given rectangle object.

Returns true if they intersect.

---

### included

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `r` | `&nbsp;` | Rectangle object to test. |

**Return value**

Whether it is contained

**Description**

Tests containment

Tests whether the given rectangle object is inside this rectangle.

Returns true if it is.

If even one edge is outside, it is not considered contained.

---

### includedPos

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | X coordinate to test. |
| `y` | `&nbsp;` | Y coordinate to test. |

**Return value**

Whether it is contained

**Description**

Tests containment of a point

Tests whether the given position is inside the rectangle.

Returns true if it is.

right and bottom themselves are not included in the range.

---

### equal

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `r` | `&nbsp;` | Rectangle object to compare with. |

**Return value**

Whether they are equal

**Description**

Tests equality

Tests whether the rectangles are equal.

Returns true if they are.

The four edge values are compared.

---
