vector_demo — ベクタ描画 + 画像効果 (複数プラグイン横断)
======================================================

■ 概要

複数プラグインをまたぐ横断デモ (data/ 直置き):

  layerExVector … Layer に GdiPlus 互換のベクタ描画を追加
                  (プリミティブ / グラデーション / パス / アウトライン文字)
  layerExImage  … 描いた結果に画像効果 (ブラー / 明度 / カラー化 / ノイズ)
  Elements      … パラメータ操作パネル

ベクタ描画ギャラリーを描き、Elements パネルで 線幅 / 回転 / グラデ色相 /
画像効果 を変更する。画像効果 ON のときは描画結果を複製レイヤへコピーして
layerExImage で加工した結果を重ねて表示する (= ベクタ→画像効果の連携)。

■ 使用しているプラグイン API

  layerExVector (Layer に付与):
    clear / drawRectangle / drawEllipse / drawLine / drawPolygon /
    drawArc / drawPie / drawLines / drawPath / drawString
    GdiPlus.Appearance (addBrush / addPen、グラデ辞書指定) / GdiPlus.Path /
    GdiPlus.loadFont / GdiPlus.Font
  layerExImage (Layer に付与):
    gaussianBlur / light / colorize / noise

■ 実行方法 (umbrella ルートから)

  bin/<preset>/<config>/krkrz64.exe  data/vector_demo

layerExVector.dll / layerExImage.dll を exe の隣か plugin64/ に置く
(make install 済みの bin/ にはある)。SDL3 + KRKRZ_USE_ELEMENTS でパネル表示。

■ 操作

  パネル : 線幅 / 回転 / グラデ色相 / 画像効果 を変更、再描画
  R      : 再描画
  ESC    : 終了

■ フォント (アウトライン文字)

  アウトライン文字は容量の都合でフォントを同梱していない。表示したい場合は
  font/ フォルダに .ttf を置く (候補名: NotoSansJP-VF.ttf / NotoSans.ttf /
  font.ttf)。無ければその部分だけスキップする。

■ ヘッドレステスト

  krkrz64.exe data/vector_demo -demotest
  → "@demotest:vector_demo vector=.. image=.. font=.." と "@demotest:ok"

■ 対応ドキュメント

  src/plugins/layerExVector/manual.tjs / src/plugins/layerExImage/manual.tjs
