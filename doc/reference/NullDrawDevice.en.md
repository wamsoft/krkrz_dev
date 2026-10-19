# NullDrawDevice

NullDrawDevice is a DrawDevice that you register in [Window.drawDevice](Window.md#drawdevice); it is a dummy implementation that draws nothing.

Use it for headless execution, or when you want to control the entire drawing path yourself from outside.

## Members

### Constructors

- [NullDrawDevice](#nulldrawdevice)

### Properties

- [interface](#interface)

### Methods

- [recreate](#recreate)

---

### NullDrawDevice

Constructor

**Description**

Constructs a NullDrawDevice object

Constructs an object of the NullDrawDevice class.

---

### interface

Property \ Access: `r`

**Description**

Gets the interface object

Provided so that plugins and the like can use the DrawDevice object.

---

### recreate

Method

**Description**

Recreates the internal device

Recreates the internal device.

You normally do not need to call this.

---
