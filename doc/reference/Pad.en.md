# Pad

Pad extensions

## Members

### Methods

- [registerExEvent](#registerexevent)

---

### registerExEvent

Method

**Description**

Enables extended events (throws an exception if registration fails)

The following extended event is raised:
onClose  The close button was pressed

Note: if the window is recreated (for example by changing borderStyle), the events stop firing.
In that case, call registerExEvent() again.

---
