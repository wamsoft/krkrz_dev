# Timer

The Timer class raises events at regular intervals.

## Members

### Constructors

- [Timer](#timer)

### Properties

- [interval](#interval)
- [capacity](#capacity)
- [enabled](#enabled)
- [mode](#mode)

### Events

- [onTimer](#ontimer)

---

### Timer

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `owner` | `&nbsp;` | Target that receives the event. |
| `actionname` | `"action"` | Name of the method on the owner object that receives the event.<br>If you pass an empty string, owner itself is treated as a method and is called<br>directly at every interval. |

**Description**

Constructs a Timer object

Constructs an object of the Timer class.

Initially, the interval property is 1000 and the enabled property is false.

---

### interval

Property \ Access: `r/w`

**Description**

Event interval

Represents the event **interval**. This property can also be set.

The unit is ms (milliseconds); an event occurs each time the specified period elapses.

You can also specify the interval as a real number. In the current version it can be specified
with a precision of 1/65536 ms (fractional values are rounded to this precision).

Even with a precision of about 1/65536 ms, there is no guarantee that the event handler is actually called with that precision.
In practice, the timing of events jitters by about 3 to 10 ms.
However, the timing is adjusted automatically so that, on average and over the long term, events occur at the interval specified by this property.

---

### capacity

Property \ Access: `r/w`

**Description**

Maximum number of pending events

Specifies how many events can be raised at once. This property can also be set.

The timer may be unable to keep up with its events, for example when processing takes longer than the timer interval.
In that case the timer stores events in the event queue, but the number of events it can store there is limited.
This property specifies that maximum.

When it is time to process events, Kirikiri tries to process all the events in the queue at once.

If you specify 1, at most one event is stored in the event queue. If you specify 0, there is no limit to the number of
queued events, but note that if too many events pile up, the application may appear to freeze.

The default is 6.

---

### enabled

Property \ Access: `r/w`

**Description**

Whether events are raised

Indicates whether events are raised. This property can also be set.

If true, events are raised. If false, no events are raised.

---

### mode

Property \ Access: `r/w`

**Description**

Mode

Represents the operating mode. This property can also be set.

Specify one of the following values.

`**atmNormal**    : ` Events are delivered with normal event-delivery priority.

`**atmExclusive** : ` Events are delivered ahead of other asynchronous events.

`**atmAtIdle**    : ` Events are delivered when idle (when there are no other events to deliver).

**See also:** [AsyncTrigger.mode](AsyncTrigger.md#mode)

---

### onTimer

Event

**Description**

The timer interval has elapsed

Called at every timer interval.

---
