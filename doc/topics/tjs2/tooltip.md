# ツールチップの表示方法

ツールチップとは、マウスオーバーで表示される簡単なヘルプのことです。  
具体的には Layer.hint で表示されるものです。  
吉里吉里内ではヒントと呼ばれています。  
吉里吉里2 では OS の機能(厳密にはVCL)によって表示されていましたが、吉里吉里Zでは任意レイヤーを表示させるように仕様が変更されています。  
なお、マウスオーバーはタッチパネルを持ったタブレットデバイスなどでは表示することが出来ないため、別の方法で表示できるようにする必要があります。  

## 仕様
* ヒントを設定し、カーソルが一定時間停止しヒント表示タイミングになると Window.onHintChanged(text:string,x:int,y:int,isshow:bool) イベントが発生する。  
* カーソル停止時間は、property:Window.hintDelay で指定可能。  
デフォルトは 500 (msec) 。  
従来は固定値だったものを変更可能にした。  
* ヒントを描画するレイヤーには property:Layer.ignoreHintSensing を有効にして、ヒント表示を無視させる。
* isshow が false でイベントが来たら非表示にする。

これで onHintChanged で isshow が true の時、ヒントを最前面レイヤーに描画し、ヒントレイヤーはマウスメッセージは無視されるように設定すれば従来と同じような表示が出来る。  

従来は、標準の味気ない表示のみだったが、レイヤーに任意に描画可能としたことで、文字のみではなく画像などを用いて表示も可能となった。

## サンプル
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

[GitHub にも同じサンプルが上げてある。
](https://github.com/krkrz/krkrz/blob/master/script/Sample/tooltip/startup.tjs)