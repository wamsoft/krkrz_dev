# ライセンス

このリポジトリは 吉里吉里Z (Kirikiri Z) の開発用アンブレラリポジトリです。
エンジン本体・各プラグイン・スクリプトライブラリを git submodule として束ねており、
ライセンスはそれぞれの構成要素側で定義されています。

## エンジン本体 (src/core)

[src/core/LICENSE](src/core/LICENSE) を参照してください。
本体条項と、ソースツリーに含まれる第三者コードの notice が記載されています。

リンクされる外部ライブラリ・同梱フォント等のライセンス全文は
`src/core/licenses/` に個別に保持され、エンジン実行時に
`System.getLicenseList()` / `System.getLicenseText()` で参照できます。
仕組みの詳細は [src/core/doc/LicenseSystem.md](src/core/doc/LicenseSystem.md) を
参照してください。

## プラグイン (src/plugins/*)

各プラグインはそれぞれ独立したリポジトリです。ライセンスは各フォルダの
LICENSE / README を参照してください。

## スクリプトライブラリ (script/*)

KAG3 ほか script/ 以下の各フォルダも同様に、それぞれのフォルダ内の
LICENSE / README を参照してください。
