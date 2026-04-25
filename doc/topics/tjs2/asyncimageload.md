# 非同期画像読み込み
標準の画像読み込みは読み込みを要求した時、その読み込みの完了を待って処理をするが、非同期読み込みでは画像の読み込みをバックグラウンドで行いながら他の処理を出来る。  
このためディスクからの読み込みと言う遅い処理をあまり感じさせないような作りにすることも可能になる。  

## 仕様
* 非同期読込みは Bitmap.loadAsync(filename) と Bitmap.onLoaded(meta,async,error,message) を使って行う。
* loadAsync で読込みを要求し、onLoaded で読込み完了を受ける。
* 非同期読込み中かどうかは Bitmap.loading で判定できる。
* 非同期読込み中は Bitmap の他のメンバへアクセスすると例外が発生する。
* loadAsync の引数 filename は拡張子を含んだものとなり、省略できる Layer.loadImages とは異なるので注意。

### onLoaded で受け取る各値 (meta,async,error,message) はそれぞれ以下の通り。
* meta : Layer.loadImages の戻り値で受け取れるものと同じ。タグ情報の辞書配列。
* async : 非同期で読み込まれたものかどうか。キャッシュに入っていた場合は、読込み要求した後そのまま onLoaded で返ってくる。
* error : 読込みエラーが発生したかどうか。
* message : エラーメッセージ。エラーが発生した場合、エラーメッセージが渡される。

読み込んだ画像は Layer.copyFromBitmapToMainImage(Bitmap) によって、Bitmap から Layer にコピーできる。  
コピーと言っても、変更されるまでは共有されているので、一瞬で終わる。  
読込み処理は非同期であるため、読込みが完了した時に、その画像を渡す Layer が既に無効化されている可能性がある。  
onLoaded で他のオブジェクトへアクセスする場合は、無効化されていないか確認した方が良い。  
もしくは、onLoaded が完了するまで無効化されないようにする必要がある。  

## サンプルスクリプト
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

[GitHubに入っているものと同じ](https://github.com/krkrz/krkrz/blob/master/script/Sample/asyncimageload/startup.tjs)

