# AsyncTrigger

The AsyncTrigger class fires an event at the next event-delivery point, right after control returns to Kirikiri. This feature is called an **asynchronous trigger**.

In an event-driven programming model like Kirikiri's, this is useful when you want to do something outside an event handler that cannot be done inside it (for example, invalidating the object that raised the event from within its own handler).

## Members

### Constructors

- [AsyncTrigger](#asynctrigger)

### Properties

- [cached](#cached)
- [mode](#mode)

### Methods

- [trigger](#trigger)
- [cancel](#cancel)

### Events

- [onFire](#onfire)

---

### AsyncTrigger

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `owner` | `&nbsp;` | Target that receives the event. |
| `actionname` | `"action"` | Name of the method on the owner object that receives the event.<br>If you pass an empty string, owner itself is treated as a method and is called<br>directly each time the event fires. |

**Description**

Constructs an AsyncTrigger object

Constructs an object of the AsyncTrigger class.

---

### cached

Property \ Access: `r/w`

**Description**

Whether events are cached

Indicates whether events are cached. This property can also be set.

If true, the trigger fires only once no matter how many times
[AsyncTrigger.trigger](AsyncTrigger.md#trigger) is called before it fires.

If false, it fires as many times as it was called before firing.

---

### mode

Property \ Access: `r/w`

**Description**

Mode

Represents the operating mode. This property can also be set.

Specify one of the following values.

`**atmNormal**    : ` Fires at the normal event-delivery stage.

`**atmExclusive** : ` Fires ahead of other asynchronous events.

`**atmAtIdle**    : ` Fires when idle (when there are no other events to deliver).

Triggers pulled at the same time fire in the order atmExclusive, atmNormal, atmIdle.

When several triggers of the same mode have been pulled, they fire in the order they were pulled.

**See also:** [Timer.mode](Timer.md#mode)

---

### trigger

Method

**Description**

Pulls the trigger

Raises the event.

After this method is called, control returns to the Kirikiri engine, and the [AsyncTrigger.onFire](AsyncTrigger.md#onfire) event
occurs when the engine delivers its pending asynchronous events.

---

### cancel

Method

**Description**

Cancels the trigger

Cancels a trigger pulled with the [AsyncTrigger.trigger](AsyncTrigger.md#trigger) method.

You can cancel at any time before it fires.

---

### onFire

Event

**Description**

When the trigger fires

Occurs after the trigger has been pulled with the [AsyncTrigger.trigger](AsyncTrigger.md#trigger) method.

---
