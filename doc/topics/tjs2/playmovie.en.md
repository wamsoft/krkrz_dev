---
source_hash: e90d7c39929d
---

# Playing a Movie

A Kirikiri Z TJS2 sample script.
It plays a movie in mixer (VMR9) mode.
This is the standard way to play a movie in front of everything else.


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


