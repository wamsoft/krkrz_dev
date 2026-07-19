======================================================================
 トランジション表示サンプル (Elements UI / Dialog 版)
======================================================================

■ 概要

  吉里吉里Z の標準トランジション + extrans + extNagano プラグインの
  各トランジションを、組込 Elements UI (Dialog クラス) のパネルから
  「選択 → パラメータ設定 → 実行」して確認できるデモです。

  画面 A ⇔ 画面 B を、選んだトランジションで切り替えます。実行のたびに
  A→B→A… と向きが交互になります。

  収録トランジション (計 21 種):
    [標準]     crossfade / universal / scroll
    [extrans]  wave / mosaic / turn / rotatezoom / rotatevanish /
               rotateswap / ripple
    [extNagano] 3duniversal / blurfade / scanline / zoomfade / rgbfade /
               spin / flutter / book / imagewipe / honeyturn / multiripple
    ※ extNagano の morphing は座標配列指定が必要なためスライダ UI に
      馴染まず、本デモでは除外しています。


■ 動作要件

  - Elements Dialog は SDL3 ビルド + KRKRZ_USE_ELEMENTS=ON でのみ動作
    します (既定 ON)。WINVER ビルドでは Dialog クラスが登録されず、
    起動時に警告が出ます。
      → プリセット x64-windows (SDL) のビルドを使用してください。

  - extrans / extNagano のトランジションを使うには extrans.dll /
    extNagano.dll が読み込める必要があります。実行ファイルと同じ
    フォルダ、または実行ファイル配下の plugin64/ (32bit は plugin/)
    にあれば読まれます。`make install` した bin/ 以下にはプラグインが
    揃うので、そのまま利用できます。
    プラグインが見つからない場合は自動判定 (Plugins.canLink) で該当
    項目をメニューから除外し、標準トランジションのみで動作します。


■ 実行方法

  make install 済みの bin/ を使う場合 (推奨):

    bin/<preset>/<config>/krkrz64.exe  <このフォルダのパス>

  例 (umbrella リポジトリのルートから):
    bin/x64-windows/Release/krkrz64.exe  data/transition_demo


■ 操作

  - 左上パネルの「種類」でトランジションを選択
  - 「パラメータ」の各スライダ / メニューで値を調整
  - 「▶ 実行」ボタン (またはキー R) でトランジション再生
  - SPACE : パネル再表示
  - ESC   : パネルを閉じる
  - ←→   : 種類を前後に切替

  実行した beginTransition の内容は画面下部の帯 (HUD) と
  Debug ログ (Debug.message) に出力されます。


■ 構成ファイル

  startup.tjs      デモ本体 (トランジション定義テーブル + UI + 実行)
  image/rule.png   universal 用ルール画像 (本デモ独自生成。中心から広がる
                   放射グラデーションの 256 階調グレースケール)
  image/rule4.png  3duniversal 用ルール画像 (本デモ独自生成。画面サイズ
                   1280x720。ステンドグラス状の Voronoi セル分割で、セル毎に
                   R=落下開始時間(上ほど早い) を均一化し領域ごとまとまって落下。
                   G=落下速度 / B=方向(64=真下)。緑の境界線は高速セル境界で
                   割れ目が先に裂ける)
  image/rule5.png  imagewipe 用ルール画像 (本デモ独自生成。幅=ワイプ帯の厚み・
                   高=画面高の RGBA。アルファの波状右端がワイプ境界の輪郭に、
                   RGB(白→金の暖色グロー)が縁の装飾になる)
  readme.txt       このファイル
