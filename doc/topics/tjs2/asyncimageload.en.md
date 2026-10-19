---
source_hash: cb7ac2883cf7
---

# Asynchronous Image Loading
Standard image loading waits for the load to finish when you request it, but asynchronous loading reads the image in the background while you do other work.  
This lets you build programs where the slow process of reading from disk is hardly noticeable.  

## Specification
* Asynchronous loading uses Bitmap.loadAsync(filename) and Bitmap.onLoaded(meta,async,error,message).
* Request the load with loadAsync, and receive completion in onLoaded.
* Bitmap.loading tells you whether an asynchronous load is in progress.
* Accessing other members of the Bitmap during an asynchronous load throws an exception.
* The filename argument of loadAsync must include the extension. Note that this differs from Layer.loadImages, where it can be omitted.

### The values received in onLoaded (meta,async,error,message) are as follows.
* meta : The same as the return value of Layer.loadImages. A dictionary of tag information.
* async : Whether the image was loaded asynchronously. If it was in the cache, onLoaded is called right away after the load request.
* error : Whether a load error occurred.
* message : Error message. Passed when an error occurs.

A loaded image can be copied from the Bitmap to a Layer with Layer.copyFromBitmapToMainImage(Bitmap).  
Although it is called a copy, the data is shared until it is modified, so it finishes instantly.  
Because loading is asynchronous, the Layer that should receive the image may already be invalidated by the time loading completes.  
When accessing other objects in onLoaded, check that they have not been invalidated.  
Alternatively, make sure they are not invalidated until onLoaded completes.  

## Sample script
```
/*
image0.png ～ image9.png を10回非同期で読み込む
*/
System.setArgument("-contfreq", 60);
System.graphicCacheLimit = 0;
// キャッシュが有効だと無意味なので画像キャッシュ切る

class Bitmap2Layer extends Bitmap {
	var target;
	var tag;
	function Bitmap2Layer(layer,filename) {
		super.Bitmap();
		this.target = layer;
		this.tag = filename;
	}
	function onLoaded(meta,async,error,message) {
		Debug.message("Exit load async:"+async+", error:"+error+", message:"+message);
		if( !error && isvalid(target) ) { // 非同期なので、既に無効化されいないことを確認する
			target.copyFromBitmapToMainImage(this);
			target.setSizeToImageSize();
		}
	}
};

class MainWindow extends Window {
	var base;
	var layer;
	var layermove;
	var addval;
	var bmps;

	function MainWindow( width, height ) {
		super.Window();
		setSize( width, height );
		setInnerSize( width, height );

		base = new Layer(this, null);
		base.setSize(width,height);
		base.setSizeToImageSize();
		base.name = "base";
		base.visible = true;
		add( base );

		layer = new Layer(this,base);
		layer.setSize(100,100);
		layer.setSizeToImageSize();
		layer.colorRect(0,0,100,100,0x00ff00,128);
		layer.visible = true;
		add( layer );

		layermove = new Layer(this,base);
		layermove.setSize(100,100);
		layermove.setPos(0,height-100);
		layermove.setSizeToImageSize();
		layermove.colorRect(0,0,100,100,0xff0000,128);
		layermove.drawText( 0, 40, "テスト文字列描画", 0xffffff );
		layermove.visible = true;
		add( layermove );

		bmps = new Array();
		for( var j = 0; j < 10; j++ ) {
		for( var i = 0; i < 10; i++ ) {
			var filename = "image"+i+".png";
			var bmp = new Bitmap2Layer(layer,filename);
			bmp.loadAsync(filename);
			bmps.add(bmp);
		}
		}
		add( bmps );

		addval = 1;
		System.addContinuousHandler(onMoveImage);
	}
	function finalize() {
		System.removeContinuousHandler(onMoveImage);
		super.finalize();
	}
	function onMoveImage() {
		layermove.left += addval;
		if( addval > 0 ) {
			if( layermove.left >= (this.width-layermove.width) ) {
				addval = -1;
			}
		} else {
			if( layermove.left <= 0 ) {
				addval = 1;
			}
		}
	}
};

var win = new MainWindow(640,480);
win.visible = true;
```

[Same as the one on GitHub](https://github.com/krkrz/SampleScript/blob/master/asyncimageload/startup.tjs)


