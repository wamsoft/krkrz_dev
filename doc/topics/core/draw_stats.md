# DrawThreadPool 利用率の計測 (DrawStats)

吉里吉里Z の描画は内部で **DrawThreadPool** ( `TVPBeginThreadTask` /
`TVPExecThreadTask` / `TVPEndThreadTask` ) という並列スレッドプールを
通って実行されます。`KRKRZ_DRAW_STATS=ON` ビルドではこれの利用率を
atomic カウンタで採取し、画面オーバレイとログから観察できます。

主な用途は **「メイン CPU だけ詰まって他コアが空いている」現象の原因
特定**。Switch 等の組み込み環境で典型的に起こるこの状況を、外から
見ているだけで切り分けるための装備です。

詳細な使い方・読み方は src/core 側のガイドにまとまっています:

- [doc/DrawStats.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/DrawStats.md)

---

## ビルド

CMake オプションで OFF/ON を切替。**デフォルト OFF (本番ビルドに影響なし)**。

```bash
cmake --preset x64-windows -DKRKRZ_DRAW_STATS=ON
cmake --build build/x64-windows --config Release
```

OFF 時は計測マクロが空展開され、atomic 操作が一切生成されません。

### 閾値チューニング

`GetAdaptiveThreadNum` の閾値判定 `pixelNum >= factor * SCALE` の **SCALE**
をビルド時に上書きできます。

```bash
# 旧 PC 挙動 (1T 多め) で動かしたい場合
cmake --preset x64-windows -DKRKRZ_THREAD_PIXEL_SCALE=500
```

- **デフォルト 100** ( Switch 実機での比較から決定 )
- 500 (旧仕様) では Switch で 1T 利用率が支配的になり、ワーカが活用されません

---

## 表示と読み方

[`-memoverlay=1`](../../guide/CommandLine.md) を有効にすると、画面右上に
DrawStats が同時に表示されます。

実機などで画面表示が速く流れて読めない場合は
[System.setDrawStatsLog](../../reference/System.md#setdrawstatslog) で
500ms 周期のログ出力に切替できます ( OFF ビルドや MemoryOverlay 非表示時
には実害なく何も起こりません )。

---

## 関連 API

- [System.setDrawStatsLog](../../reference/System.md#setdrawstatslog) — DrawStats ログ出力の動的切替
- [System.setMemoryOverlay](../../reference/System.md#setmemoryoverlay) — 同時表示の MemoryOverlay 切替
- [System.drawThreadNum](../../reference/System.md#drawthreadnum) — 描画スレッド数の取得・設定
