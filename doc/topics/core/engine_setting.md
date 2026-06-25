# エンジン設定の追加/編集
## 従来の方法
吉里吉里2 では、本体は TVPGetCommandDesc で得られる "|" 区切り(他の区切り文字もあり)の文字列を得て、それを元にエンジン設定の項目を表示していた。  
また、プラグインでは、コメント部に --has-option-- を入れて、GetOptionDesc 関数を公開し、その中で本体と同じ文字列フォーマットで設定の詳細を入れていた。  
リンカに /COMMENT: で --has-option-- を追加していたが、最近の Visual Studio では無視されるので、通常の方法ではこれを DLL バイナリに入れることは出来なくなっていた。

## 吉里吉里Zからの方法
吉里吉里Z では、設定項目のリストは JSON にし、ソースに埋め込むのではなくリソースに入れる方法に変更した。  
JSON の具体的なフォーマットは、ファイルを見ればだいたい分かるはず。  
本体の方はリソースの option_desc_ja.json を編集してもらえば反映されるのでいいとして、プラグイン側は少し注意が必要。  
リソースの種類は、TEXT で、ID は文字列 IDR_OPTION_DESC_JSON で DLL に格納する。  

具体的には *.rc ファイルに、以下のように記述してリソースに追加する。  
IDR_OPTION_DESC_JSON TEXT "option_desc_ja.json"

resource.h では、IDR_OPTION_DESC_JSON を定義しない。  
IDR_OPTION_DESC_JSON を定義するとリソース ID が数値で追加される。

### JSON のフォーマット
まだ書いていない……