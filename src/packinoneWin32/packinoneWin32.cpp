//---------------------------------------------------------------------------
// packinoneWin32 - WINVER 専用の機能を 1 つの DLL に詰め合わせる
//
//   本体 (generic) に同等の口があるものは packinone / 本体側へ寄せてあるので、
//   ここに入るのは **Win32 でしか成り立たない機能**だけ。
//   仕組みは ../packinone/bundle_impl.h を参照。
//
//   ⚠ 取り込んだプラグインは「本体に無い分だけ補完する」形で登録してある
//     (ncbind は NCB_METHOD_IF_MISSING / RawCallbackIfMissing、
//      simplebinder は FunctionIfMissing)。 本体を上書きしないので、
//      本体が同じものを持てばプラグイン側は自動的に身を引く。
//
//     fstat    … ローカルファイル操作。16 個は本体 (common) へ移した
//     systemEx … レジストリ / 多重起動ロック / DPI / OS バージョン /
//                 既知フォルダ / メッセージポンプ / DLL 検索パス。
//                 環境変数と URL エンコードは本体へ移した
//     process  … メッセージ専用ウィンドウを作って子プロセスと遣り取りする
//     dpiicon  … DPI に合わせた大きさのウィンドウアイコン (DpiIcon クラス)
//---------------------------------------------------------------------------
#define PACKINONE_PLUGINS(f) \
	f(fstat)                 \
	f(systemEx)              \
	f(process)               \
	f(dpiicon)

#define PACKINONE_SELF_NAME TJS_W("PackinOneWin32.dll")

#include "bundle_impl.h"
