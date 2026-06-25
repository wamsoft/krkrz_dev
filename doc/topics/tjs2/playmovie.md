# 動画の再生方法

吉里吉里Z TJS2 のサンプルスクリプト。
mixer(VMR9)モードで動画を再生する。
最前面で動画を再生する時はこの方法が標準の方法。


```
class MainWindow extends Window {
	var video;
	function MainWindow( width, height ) {
		super.Window();
		video = new VideoOverlay(this);
		video.mode = vomMixer;
		video.open("test.mpg");
		setInnerSize( video.originalWidth, video.originalHeight );
		video.play();
		video.width = video.originalWidth;
		video.height = video.originalHeight;
		video.visible = true;
		add( video );
	}
};
var win = new MainWindow(640,480);
win.visible = true;

```


