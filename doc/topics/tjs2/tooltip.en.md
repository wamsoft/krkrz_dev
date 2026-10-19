---
source_hash: 4285c5b28367
---

# Showing Tooltips

A tooltip is a short piece of help shown on mouseover.  
Specifically, it is what Layer.hint displays.  
Within Kirikiri it is called a hint.  
Kirikiri 2 displayed it through an OS feature (strictly speaking, VCL), but Kirikiri Z changed this so that it displays an arbitrary layer.  
Note that mouseover cannot be used on tablet devices with touch panels and the like, so you need to provide another way to show hints there.  

## Specification
* When a hint is set and the cursor stays still long enough for the hint to appear, the Window.onHintChanged(text:string,x:int,y:int,isshow:bool) event fires.  
* The cursor idle time can be set with property:Window.hintDelay.  
The default is 500 (msec).  
This used to be a fixed value and is now configurable.  
* Enable property:Layer.ignoreHintSensing on the layer that draws the hint so that it is ignored for hint display.
* When the event arrives with isshow set to false, hide the hint.

With this, when isshow is true in onHintChanged, draw the hint on the frontmost layer and make the hint layer ignore mouse messages, and you get the same display as before.  

Previously only the plain standard display was available, but since you can now draw anything on a layer, hints can use images and more, not just text.

## Sample
```
class MainWindow extends Window {
	var base;
	var layer;
	var hintlayer;

	function MainWindow( width, height ) {
		super.Window();
		setSize( width, height );
		setInnerSize( width, height );

		base = new Layer(this, null);
		base.setSize(width,height);
		base.setSizeToImageSize();
		base.name = "base";
		base.visible = true;

		layer = new Layer(this,base);
		layer.setPos(100,200);
		layer.setSize(100,100);
		layer.setSizeToImageSize();
		layer.colorRect(0,0,100,100,0xff0000,128);
		layer.drawText( 0, 40, "Draw Sample Text", 0xffffff );
		layer.hint = "Show Hint";
		layer.visible = true;

		// Hint Layer
		hintlayer = new Layer(this,base);
		hintlayer.visible = false;
		hintlayer.ignoreHintSensing = true;
		hintlayer.font.height = 14;
		hintlayer.hitThreshold = 256;

		// hintDelay = 500; // default
		// hintDelay = 0; // immediate
		// hintDelay = -1; // never
		// hintDelay = 1000; // slow
	}
	function onHintChanged(text,x,y,isshow) {
		if( isshow ) {
			var w = hintlayer.font.getTextWidth( text ) + 6;
			var h = hintlayer.font.getTextHeight( text ) + 4 + 4;
			hintlayer.setImageSize( w, h );
			hintlayer.setSizeToImageSize();

			if( (x+w) > innerWidth ) { x = innerWidth - w; }
			if( (y+h) > innerHeight ) { y = innerHeight - h; }
			hintlayer.setPos( x, y );

			hintlayer.fillRect( 0, 0, w, h, 0 );
			hintlayer.colorRect( 0, 0, w, h, clInfoBk, 196 );

			hintlayer.colorRect( 0, 0, 1, h, 0xFFFFFF );
			hintlayer.colorRect( 0, 0, w, 1, 0xFFFFFF );
			hintlayer.colorRect( w-1, 0, 1, h, 0xFFFFFF );
			hintlayer.colorRect( 0, h-1, w, 1, 0xFFFFFF );

			hintlayer.drawText( 2, 2, text, clInfoText, 220 );
			hintlayer.visible = true;
		} else {
			hintlayer.visible = false;
		}
	}
}
var win = new MainWindow(640,480);
win.visible = true;
```

[The same sample is also available on GitHub.
](https://github.com/krkrz/SampleScript/blob/master/tooltip/startup.tjs)
