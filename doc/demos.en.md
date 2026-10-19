---
source_hash: 320fb9e6b87f
---

# Demos (Run in Your Browser)

You can run the Kirikiri Z core demos and cross-plugin demos **directly in your browser**.
The integrated demo gallery in `krkrz_dev/data` (21 demos in total) is built with Emscripten (wasm)
and embedded in this page. Selecting a demo from the menu switches to it **without restarting**,
and **ESC returns to the menu** (exactly the same hub behavior as the desktop version).

!!! note "Requirements"
    - Works on **the latest desktop Chrome / Edge / Firefox** (uses `SharedArrayBuffer` / wasm threads; asynchronous processing is built with Asyncify, which works in all browsers).
    - On your first visit, the page **reloads once automatically** to register a Service Worker.
    - Startup loads **about 47 MB** (wasm + data + Japanese/emoji fonts). Nothing is loaded until you press "▶ Run" below.
    - Demos that use Elements panels are operated with the mouse; the others use the bottom bar or the keyboard (see each demo's instructions).
    - The embedded build is the **2026-10-19 build (all 21 demos, Japanese / English)**. When the engine or the demos
      are updated, the wasm must be rebuilt and replaced (the latest list is in
      `data/ROADMAP.md` in the repository).

<div id="krkrz-demo-holder" markdown="0" style="margin:1.5em 0;">
  <button id="krkrz-demo-run"
          style="display:block;width:100%;aspect-ratio:16/9;border:0;border-radius:10px;
                 background:#14161c;color:#e6ebf5;font-size:1.2rem;cursor:pointer;
                 display:flex;align-items:center;justify-content:center;gap:.6em;">
    ▶ Run the demos (loads about 47 MB)
  </button>
</div>

<p>
  If it does not display correctly, try
  <a href="../../_assets/demo/?language=en" target="_blank" rel="noopener">opening it full screen in a separate tab</a>.
</p>

<script>
(function () {
  var btn = document.getElementById("krkrz-demo-run");
  if (!btn) return;
  btn.addEventListener("click", function () {
    var holder = document.getElementById("krkrz-demo-holder");
    var f = document.createElement("iframe");
    // 英語版は /en/demos/ に出るので 1 階層深い。デモ本体は既定言語側 (/_assets/demo/) にだけある。
    // ?language=en で埋め込みデモも英語表示にする (krkrz_web の pre.js が -language= へ渡す)
    f.src = "../../_assets/demo/?language=en";
    f.setAttribute("allow", "autoplay; fullscreen; gamepad");
    f.setAttribute("allowfullscreen", "");
    f.style.cssText =
      "width:100%;aspect-ratio:16/9;border:0;border-radius:10px;background:#000;";
    holder.innerHTML = "";
    holder.appendChild(f);
  });
})();
</script>

## How It Works

- The engine is **a single shared wasm binary**, and the demo data is bundled as a preload (`krkrz.data`).
- GitHub Pages cannot set COOP/COEP response headers, so `coi-serviceworker` injects them
  on the client side to establish `crossOriginIsolated` (COEP defaults to
  `credentialless`).
- The build uses the wrapper repository [krkrz_web](https://github.com/wamsoft/krkrz_web),
  and the output is placed in `doc/_assets/demo/`. When the engine is updated, it is rebuilt
  with krkrz_web and replaced.

For the contents and controls of each demo, see [data/README](https://github.com/wamsoft/krkrz_dev/blob/develop/data/README.md)
and the `readme.txt` in each demo folder.
