//---------------------------------------------------------------------------
// packinoneWin32 - WINVER 専用の機能を 1 つの DLL に詰め合わせる
//
//   本体 (generic) に同等の口があるものは packinone / 本体側へ寄せてあるので、
//   ここに入るのは **Win32 でしか成り立たない機能**だけ。
//   仕組みは ../packinone/bundle_impl.h を参照。
//
//   ⚠ fstat は「本体に無い分だけ補完する」形で登録する (IF_MISSING)。
//     generic の本体は dirlist / dirtree / isExistentDirectory / moveFile /
//     deleteFile を持っているが WINVER の本体は持っていないので、そこを埋める。
//     将来 WINVER の本体が持てば、プラグイン側は自動的に身を引く。
//---------------------------------------------------------------------------
#define PACKINONE_PLUGINS(f) \
	f(fstat)

#include "bundle_impl.h"
