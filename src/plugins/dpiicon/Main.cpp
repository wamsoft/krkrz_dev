//---------------------------------------------------------------------------
// dpiicon - DPI に合わせた大きさのウィンドウアイコンを扱う (DpiIcon クラス)
//
//   旧 PackinOne の DpiIconManager.cpp を個別プラグインとして起こし直したもの。
//   中身は Win32 の HICON / WM_SETICON そのものなので WINVER 専用
//   (packinoneWin32 に入る)。
//
//   comctl32 の LoadIconWithScaleDown と user32 の GetDpiForWindow /
//   GetDpiForSystem を実行時に解決するので、古い Windows でも読み込みは通る。
//---------------------------------------------------------------------------
#define ISOLATION_AWARE_ENABLED 1
#pragma comment(lib, "comctl32.lib")
// [NOTE] exe側にmanifestが無いと意味がない
#pragma comment(linker,"/manifestdependency:\"type='win32' name='Microsoft.Windows.Common-Controls' version='6.0.0.0' processorArchitecture='*' publicKeyToken='6595b64144ccf1df' language='*'\"")

#include <windows.h>
#include "tp_stub.h"
#include "simplebinder.hpp"

#include <map>

#ifndef IDI_TVPWIN32
#define IDI_TVPWIN32 107
#endif

//#include <commctrl.h>
//#include <winuser.h>


class ModuleHolder {
	HMODULE module;
	bool autoloaded;

	bool load_without_unload(LPCWSTR dll, DWORD flags, bool autoload) {
		if (!::GetModuleHandleExW(flags, dll, &module)) {
			if (autoload) {
				module = ::LoadLibraryW(dll);
				if (module) autoloaded = true;
			}
		}
		return module != nullptr;
	}
public:
	ModuleHolder() : module(nullptr), autoloaded(false) {}
	ModuleHolder(LPCWSTR dll, DWORD flags = GET_MODULE_HANDLE_EX_FLAG_UNCHANGED_REFCOUNT, bool autoload = false) : module(nullptr), autoloaded(false) {
		load_without_unload(dll, flags, autoload);
	}
	~ModuleHolder() { unload(); }

	bool load(LPCWSTR dll, DWORD flags = GET_MODULE_HANDLE_EX_FLAG_UNCHANGED_REFCOUNT, bool autoload = false) {
		unload();
		return load_without_unload(dll, flags, autoload);
	}
	void unload() {
		if (autoloaded) ::FreeLibrary(module);
		module = nullptr;
		autoloaded = false;
	}

	template <typename HOLDER>
	typename HOLDER::Proc get(HOLDER &holder) {
		typedef typename HOLDER::Proc ProcType;
		if (holder.cached) return holder.proc;
		if (!module) return nullptr;
		ProcType proc = holder.proc = reinterpret_cast<ProcType>(::GetProcAddress(module, holder.name));
		holder.cached = true;
		return proc;
	}
};
template <typename PROC>
struct ProcAddress {
	typedef PROC Proc;
	Proc proc;
	const char *name;
	bool cached;
	ProcAddress(const char *name) : proc(nullptr), name(name), cached(false) {}
};

typedef HRESULT (WINAPI *LoadIconWithScaleDownProcType)(HINSTANCE,PCWSTR,int,int,HICON*);
static ProcAddress<LoadIconWithScaleDownProcType> LoadIconWithScaleDownProc("LoadIconWithScaleDown");
static ModuleHolder ModuleComCtl32;

typedef UINT (WINAPI *GetDpiForSystemProcType)();
typedef UINT (WINAPI *GetDpiForWindowProcType)(HWND hwnd);
static ProcAddress<GetDpiForSystemProcType> GetDpiForSystemProc("GetDpiForSystem");
static ProcAddress<GetDpiForWindowProcType> GetDpiForWindowProc("GetDpiForWindow");
static ModuleHolder ModuleUser32;


class IconMap {
	struct IconEntry {
		HICON hIcon;
		int refCount;
	};
	std::map<int, IconEntry> icons;

	HINSTANCE hinst;
	PCWSTR resid;
	UINT flags;
public:
	IconMap() : hinst(nullptr), resid(nullptr), flags(0) {}
	~IconMap() { clear(); }

	void reset(HINSTANCE hinst, PCWSTR resid, UINT flags) {
		this->hinst = hinst;
		this->resid = resid;
		this->flags = flags;
	}

	void clear() {
		for (auto& it : icons) ::DestroyIcon(it.second.hIcon);
		icons.clear();
	}

	HICON acquire(int cxy) {
		auto it = icons.find(cxy);
		if (it != icons.end()) {
			++it->second.refCount;
			return it->second.hIcon;
		}
		HICON icon = Load(hinst, resid, cxy, cxy, flags);
		if (icon) {
			IconEntry const entry = { icon, 1 };
			icons[cxy] = entry;
		}
		return icon;
	}

	void release(int cxy) {
		auto it = icons.find(cxy);
		if (it == icons.end()) return;

		if (--it->second.refCount <= 0) {
			::DestroyIcon(it->second.hIcon);
			it->second.hIcon = nullptr;
			icons.erase(it);
		}
	}

	static HICON Load(HINSTANCE hinst,
					  PCWSTR    pszName,
					  int       cx,
					  int       cy,
					  UINT      fuLoad = LR_DEFAULTCOLOR)
	{
		if ((fuLoad & LR_LOADFROMFILE) == 0) {
			const LoadIconWithScaleDownProcType proc = ModuleComCtl32.get(LoadIconWithScaleDownProc);
			if (proc) {
				HICON hIcon = nullptr;
				HRESULT hr = (*proc)(hinst, pszName, cx, cy, &hIcon);
				if (SUCCEEDED(hr) && hIcon) {
#if _DEBUG
					ttstr log(TJS_W("LoadIconWithScaleDown: "));
					if (IS_INTRESOURCE(pszName)) {
						log += ttstr(reinterpret_cast<tjs_int>(pszName));
					} else {
						log += ttstr(pszName);
					}
					log += TJS_W(", ");
					log += ttstr((tjs_int)cx);
					log += TJS_W(", ");
					log += ttstr((tjs_int)cy);
					TVPAddLog(log);
#endif
					return hIcon;
				}
			}
		}
		return (HICON)::LoadImageW(hinst, pszName, IMAGE_ICON, cx, cy, fuLoad);
	}
};

class DpiIconManager {
	typedef DpiIconManager Self;

	IconMap iconMap;
	ttstr resname;
protected:
	static inline tjs_int ScaleForDpi(tjs_int basePx, tjs_int dpi) {
		return ::MulDiv(basePx, dpi, USER_DEFAULT_SCREEN_DPI); // 96
	}
	static inline tjs_error GetHWND(tTJSVariant const &vwin, HWND &hwnd) {
		switch (vwin.Type()) {
		case tvtInteger: hwnd = reinterpret_cast<HWND>(vwin.AsInteger()); break;
		case tvtObject: {
			tTJSVariantClosure const clo(vwin.AsObjectClosureNoAddRef());
			if (clo.Object) {
				tTJSVariant val;
				if (TJS_FAILED(clo.PropGet(TJS_MEMBERMUSTEXIST, TJS_W("HWND"), 0, &val, nullptr))) return TJS_E_MEMBERNOTFOUND;
				hwnd = reinterpret_cast<HWND>(val.AsInteger());
			} else {
				hwnd = TVPGetApplicationWindowHandle();
			}
		} break;
		default: return TJS_E_INVALIDPARAM;
		}
		return TJS_S_OK;
	}
	static inline HICON CastIcon(tTJSVariant const &v) {
		return (v.Type() == tvtInteger) ? reinterpret_cast<HICON>(v.AsInteger()) : NULL;
	}

	static inline PCWSTR FindIcon(PCWSTR pszName) {
		HICON icon = ::LoadIconW(::GetModuleHandleW(NULL), pszName);
		return icon != NULL ? pszName : NULL;
	}

	DpiIconManager() {
		static PCWSTR appicon = nullptr;
		if(!appicon) {
			/**/          appicon = FindIcon(MAKEINTRESOURCEW(IDI_TVPWIN32));
			if (!appicon) appicon = FindIcon(L"MAINICON");
			if (!appicon) appicon = IDI_APPLICATION;
		}
		iconMap.reset(appicon != IDI_APPLICATION ? ::GetModuleHandleW(NULL) : NULL,
					  appicon, LR_DEFAULTCOLOR);
	}
	void setup(tTJSVariant *vresid, bool is_file, tTJSVariant *vmod) {
		HMODULE hmod = ::GetModuleHandleW(NULL);
		if (vmod) {
			if (vmod->Type() == tvtString) {
				const ttstr name(*vmod);
				hmod = !name.IsEmpty() ? ::GetModuleHandleW(name.c_str()) : NULL;
			} else {
				hmod = reinterpret_cast<HMODULE>(vmod->AsInteger());
			}
		}
		if (vresid->Type() == tvtString) {
			resname = *vresid;
			if (is_file) {
				iconMap.reset(hmod, resname.c_str(), LR_DEFAULTCOLOR|LR_LOADFROMFILE);
			} else {
				iconMap.reset(hmod, resname.c_str(), LR_DEFAULTCOLOR);
			}
		} else {
			iconMap.reset(hmod, MAKEINTRESOURCEW((tjs_int)*vresid), LR_DEFAULTCOLOR);
		}
	}

public:
	~DpiIconManager() {}

	static tjs_error CreateNew(Self* &inst, tjs_int optnum, tTJSVariant **optargs) {
		inst = new Self();
		if (optnum > 0) inst->setup(optargs[0], optnum>1 && optargs[1]->operator bool(), optnum>2?optargs[2]:nullptr);
		return TJS_S_OK;
	}

	// setIcon(win, big, small);
	static tjs_error SetIcon(tTJSVariant *r, tTJSVariant *vwin, tjs_int optnum, tTJSVariant **optargs) {
		HWND hwnd = nullptr;
		const tjs_error st = GetHWND(*vwin, hwnd);
		if (TJS_FAILED(st)) return st;
		if (hwnd) {
			if (optnum > 0 && optargs[0]->Type() != tvtVoid) ::SendMessage(hwnd, WM_SETICON, ICON_BIG,   (LPARAM)CastIcon(*optargs[0]));
			if (optnum > 1 && optargs[1]->Type() != tvtVoid) ::SendMessage(hwnd, WM_SETICON, ICON_SMALL, (LPARAM)CastIcon(*optargs[1]));
			if (r) *r = 1;
		} else {
			if (r) *r = 0;
		}
		return TJS_S_OK;
	}

	static tjs_error GetDPI(tTJSVariant *r, tjs_int optnum, tTJSVariant **optargs) {
		UINT dpi = 96;
		if (optnum > 0 && optargs[0]->Type() != tvtVoid) {
			HWND hwnd = nullptr;
			const tjs_error st = GetHWND(*optargs[0], hwnd);
			if (TJS_FAILED(st)) return st;
			if (!hwnd) return TJS_E_INVALIDPARAM;

			const GetDpiForWindowProcType proc = ModuleUser32.get(GetDpiForWindowProc);
			if (proc) dpi = (*proc)(hwnd);
		} else {
			const GetDpiForSystemProcType proc = ModuleUser32.get(GetDpiForSystemProc);
			if (proc) dpi = (*proc)();
		}
		if (r) *r = (tjs_int)dpi;
		return TJS_S_OK;
	}

	// acquire(size);
	tjs_error acquire(tTJSVariant *r, tTJSVariant *vcxy) {
		HICON icon = iconMap.acquire((tjs_int)*vcxy);
		if (r) *r = reinterpret_cast<tTVInteger>(icon);
		return TJS_S_OK;
	}
	// release(size);
	tjs_error release(tTJSVariant *r, tTJSVariant *vcxy) {
		iconMap.release((tjs_int)*vcxy);
		if (r) r->Clear();
		return TJS_S_OK;
	}
	// calcSize(size, dpi); // -> px
	tjs_error calcSize(tTJSVariant *r, tTJSVariant *vsz, tTJSVariant *vdpi) {
		if (r) *r = ScaleForDpi((tjs_int)*vsz, (tjs_int)*vdpi);
		return TJS_S_OK;
	}
	// clear();
	tjs_error clear(tTJSVariant *r) {
		iconMap.clear();
		if (r) r->Clear();
		return TJS_S_OK;
	}

	static bool Entry(bool link) {
		return (SimpleBinder::BindUtil(link)
				.Class   (TJS_W("DpiIcon"),  &CreateNew)
				.Function(TJS_W("acquire"),  &acquire)
				.Function(TJS_W("release"),  &release)
				.Function(TJS_W("clear"),    &clear)
				.Function(TJS_W("calcSize"), &calcSize)
				.Function(TJS_W("setIcon"),  &SetIcon)
				.Function(TJS_W("getDpi"),   &GetDPI)
				.IsValid());
	}
};

////////////////////////////////////////////////////////////////
bool DpiIconManagerEntry(bool link) {
	if (link) {
		ModuleComCtl32.load(L"comctl32.dll");
		ModuleUser32  .load(L"user32.dll");
	} else {
		ModuleComCtl32.unload();
		ModuleUser32  .unload();
	}
	return DpiIconManager::Entry(link);
}

// ⚠ TVP_STATIC_PLUGIN (詰め合わせ) では simplebinder が TVP_PLUGIN_NAME で
//   onV2Link_<名前> へ改名するので、直書きせずマクロを使う。
bool ONV2LINK()   { return DpiIconManagerEntry(true);  }
bool ONV2UNLINK() { return DpiIconManagerEntry(false); }
