---
source_hash: e1225b0d81c2
---

# Event System

## About the event system

TJS scripts written for Kirikiri follow an event-driven programming model.

An event is raised when "something happens", to notify other objects or the object itself. Event handlers contain the code that responds to it.

In Kirikiri, a single event handler should not take longer than necessary. If you need to wait for some time, use the [Timer](../reference/Timer.md) class.

## Synchronous and asynchronous events

A synchronous event is raised immediately, on the spot, when you operate on an object. For example, when you start playback on a sound buffer, the onStatusChanged event is raised inside the play method.

An asynchronous event, in contrast, is stored temporarily in the event queue inside Kirikiri (a place that holds events waiting to be raised). Such an event is not raised until all other event handlers have finished, and it is never raised inside another event handler (with an exception; see the note below). The onTimer event raised when a timer period elapses, and every event caused by user input, are asynchronous events.

> **Note:**
> Some features that wait for user input, such as Window.showModal, may run the event queue (deliver events). As a result, another asynchronous event can be raised inside an event handler.

The [AsyncTrigger](../reference/AsyncTrigger.md) class lets a script raise asynchronous events.

## When the screen is updated

The screen update that shows layers in a window happens at the same timing as asynchronous events: after all other event handlers have been processed. No matter how many times you draw inside one event handler, the drawing goes to the internal image buffer and is not reflected on screen right away. Only after the event handler returns and Kirikiri gets a chance to draw is the content drawn to the window and shown.

## Event handlers in a class

An event raised in a class can be handled within that class by overriding the superclass's event handler.

For example, you can create a subclass of the Timer class and write an event handler like this:

```
class MyTimer extends Timer
{
	function MyTimer()
	{
		super.Timer(...);
	}

	function onTimer()
	{
		// ( ここに onTimer の処理 )
		super.onTimer(...); // スーパークラスのメソッドは一応呼び出す
	}
}
```

Calling the superclass method is not required, but it is usually done. Also, if you do not call it, event handling through the action method (described below) does not work.

## The action method

Classes such as [Layer](../reference/Layer.md) and [WaveSoundBuffer](../reference/WaveSoundBuffer.md) can deliver events to the action method of the owner specified in the constructor.

The action method receives one argument, a dictionary object that holds the event information.

Among the dictionary members, target is the object that raised the event, and type is the event name.

Other members depend on the event. For example, the [Layer.onClick](../reference/Layer.md#onclick) event has the members x and y, which give the position clicked on the layer.

```
例:
class MyWindow extends Window
{
	var layer;
	(略)
	function MyWindow()
	{
		super.Window(...);
		add(layer = new Layer(this /* this = オーナー */, null));
		layer.visible = true;
	}
	(略)
	function action(ev)
	{
		if(ev.type == "onClick" && ev.target == layer)
		{
			// layer がクリックされた
			System.inform(ev.x, ev.y);
		}
	}
}
```
