# デモ (ブラウザ実行)

吉里吉里Z のコアデモ + プラグイン横断デモを **ブラウザ上でそのまま実行**できます。
`krkrz_dev/data` の統合デモギャラリー（全 11 デモ）を Emscripten (wasm) でビルドし、
このページに埋め込んでいます。メニューからデモを選ぶと **再起動なし**で切り替わり、
**ESC でメニューに戻ります**（デスクトップ版とまったく同じ hub 動作）。

!!! note "動作環境"
    - **PC の Chrome / Edge / Firefox 最新版**で動作します（`SharedArrayBuffer` / wasm スレッドを使用。非同期処理は全ブラウザ対応の Asyncify でビルド）。
    - 初回アクセス時は Service Worker 登録のため **一度自動リロード**が入ります。
    - 起動時に **約 24 MB**（wasm + データ + 日本語フォント）を読み込みます。下の「▶ 実行」を押したときだけロードします。
    - Elements パネルを使うデモはマウス操作、その他は下部バーやキーボード（各デモの操作説明を参照）で動きます。

<div id="krkrz-demo-holder" markdown="0" style="margin:1.5em 0;">
  <button id="krkrz-demo-run"
          style="display:block;width:100%;aspect-ratio:16/9;border:0;border-radius:10px;
                 background:#14161c;color:#e6ebf5;font-size:1.2rem;cursor:pointer;
                 display:flex;align-items:center;justify-content:center;gap:.6em;">
    ▶ デモを実行（約 24 MB を読み込みます）
  </button>
</div>

<p>
  うまく表示されない場合は
  <a href="../_assets/demo/" target="_blank" rel="noopener">別タブでフルスクリーン表示</a>
  を試してください。
</p>

<script>
(function () {
  var btn = document.getElementById("krkrz-demo-run");
  if (!btn) return;
  btn.addEventListener("click", function () {
    var holder = document.getElementById("krkrz-demo-holder");
    var f = document.createElement("iframe");
    f.src = "../_assets/demo/";
    f.setAttribute("allow", "autoplay; fullscreen; gamepad");
    f.setAttribute("allowfullscreen", "");
    f.style.cssText =
      "width:100%;aspect-ratio:16/9;border:0;border-radius:10px;background:#000;";
    holder.innerHTML = "";
    holder.appendChild(f);
  });
})();
</script>

## 仕組み

- エンジン本体は **共有 wasm バイナリ 1 つ**、デモデータは preload（`krkrz.data`）で同梱しています。
- GitHub Pages は COOP/COEP レスポンスヘッダを設定できないため、`coi-serviceworker` で
  クライアント側に注入し `crossOriginIsolated` を成立させています（COEP は既定で
  `credentialless`）。
- ビルドは外枠リポジトリ [krkrz_web](https://github.com/wamsoft/krkrz_web) を使用し、
  成果物を `doc/_assets/demo/` に配置しています。エンジン更新時は krkrz_web で再ビルド
  して差し替えます。

各デモの内容・操作は [data/README](https://github.com/wamsoft/krkrz_dev/blob/develop/data/README.md)
と各デモフォルダの `readme.txt` を参照してください。
