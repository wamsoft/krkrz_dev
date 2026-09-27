//---------------------------------------------------------------------------
// 詰め合わせプラグインの共通実装 (packinone / packinoneWin32 で共有)
//
//   使い方: PACKINONE_PLUGINS(f) を定義してから include する。
//
//     #define PACKINONE_PLUGINS(f) f(csvParser) f(scriptsEx)
//     #include "bundle_impl.h"
//
//   取り込むプラグインのソースは個別プラグインのものをそのまま使う (二重管理しない)。
//   各ソースは TVP_STATIC_PLUGIN 付きでコンパイルするので、
//     - バインダ (ncbind / simplebinder) の自動登録リストがプラグインごとに
//       別名になり、同じ DLL に同居できる
//     - krkrz_plugin_<名前>() という登録エントリが生える
//   ようになる。 その登録エントリは本体の TVPRegisterPlugin() を呼ぶ想定だが、
//   ここでは **自前の TVPRegisterPlugin をリンクさせて横取り**し、
//   自分の V2Link から各プラグインの link を順に呼ぶ。
//
//   併せて TVPRegisterBundledPlugin() で「この名前は自分が持っている」と本体に申告する。
//   これにより Plugins.link("csvParser.dll") は何もせず成功する (旧 PackinOne が
//   Plugins.link を自前で差し替えてやっていたことの本体公式版)。
//---------------------------------------------------------------------------
#ifndef PACKINONE_PLUGINS
# error "PACKINONE_PLUGINS(f) を定義してから include すること"
#endif

#include <windows.h>
#include "tp_stub.h"

#include <vector>

//---------------------------------------------------------------------------
// 取り込んだプラグインの登録エントリ (各ソースが TVP_STATIC_PLUGIN で生やす)
//---------------------------------------------------------------------------
#define PACKINONE_DECL(name) extern "C" void STDCALL krkrz_plugin_##name();
PACKINONE_PLUGINS(PACKINONE_DECL)
#undef PACKINONE_DECL

//---------------------------------------------------------------------------
// TVPRegisterPlugin の横取り。
//   本体 (exe) 側の同名関数は「本体に静的リンクされたプラグイン」用で、
//   DLL からは呼べない (宣言だけがヘッダにある)。 ここで定義しておくと
//   取り込んだプラグインの登録エントリはこちらへ入ってくる。
//---------------------------------------------------------------------------
static std::vector<const iTVPStaticPlugin *> PackedPlugins;

extern "C" void TVPRegisterPlugin(const iTVPStaticPlugin *plugin)
{
	if(plugin) PackedPlugins.push_back(plugin);
}

//---------------------------------------------------------------------------
static void CollectPackedPlugins()
{
	if(!PackedPlugins.empty()) return;
#define PACKINONE_CALL(name) krkrz_plugin_##name();
	PACKINONE_PLUGINS(PACKINONE_CALL)
#undef PACKINONE_CALL
}
//---------------------------------------------------------------------------

#ifdef _MSC_VER
# if defined(_M_AMD64) || defined(_M_X64)
#  pragma comment(linker, "/EXPORT:V2Link")
#  pragma comment(linker, "/EXPORT:V2Unlink")
# else
#  pragma comment(linker, "/EXPORT:V2Link=_V2Link@4")
#  pragma comment(linker, "/EXPORT:V2Unlink=_V2Unlink@0")
# endif
#endif

extern "C" __declspec(dllexport) HRESULT STDCALL V2Link(iTVPFunctionExporter *exporter)
{
	TVPInitImportStub(exporter);

	CollectPackedPlugins();
	for(std::vector<const iTVPStaticPlugin *>::iterator i = PackedPlugins.begin();
		i != PackedPlugins.end(); i++)
	{
		const iTVPStaticPlugin *p = *i;
		if(!p) continue;
		if(p->link) p->link(exporter);
		// 「このプラグインは同梱済み」と本体へ申告する
		if(p->name) TVPRegisterBundledPlugin(ttstr(p->name) + TJS_W(".dll"));
	}
	return S_OK;
}
//---------------------------------------------------------------------------
extern "C" __declspec(dllexport) HRESULT STDCALL V2Unlink()
{
	for(std::vector<const iTVPStaticPlugin *>::reverse_iterator i = PackedPlugins.rbegin();
		i != PackedPlugins.rend(); i++)
	{
		const iTVPStaticPlugin *p = *i;
		if(!p) continue;
		if(p->name) TVPUnregisterBundledPlugin(ttstr(p->name) + TJS_W(".dll"));
		if(p->unlink) p->unlink();
	}
	TVPUninitImportStub();
	return S_OK;
}
//---------------------------------------------------------------------------
