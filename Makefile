ifeq ($(VCPKG_ROOT),)
$(error Variables VCPKG_ROOT not set correctly.)
endif

ifeq ($(shell type cygpath > /dev/null && echo true),true)
FIXPATH = cygpath -ma
else
FIXPATH = realpath
endif

VCPKG=$(shell $(FIXPATH) "$(VCPKG_ROOT)/vcpkg")

# Detect OS and set default PRESET accordingly
ifeq ($(OS),Windows_NT)
	PRESET?=x64-windows
else
	UNAME_S := $(shell uname -s)
	UNAME_M := $(shell uname -m)
	ifeq ($(UNAME_S),Linux)
		ifeq ($(UNAME_M),aarch64)
			PRESET?=arm64-linux
		else
			PRESET?=x64-linux
		endif
	else ifeq ($(UNAME_S),Darwin)
		ifeq ($(UNAME_M),arm64)
			PRESET?=arm64-osx
		else
			PRESET?=x64-osx
		endif
	else
		PRESET?=x64-windows
	endif
endif

BUILD_TYPE?=Release
CMAKEOPT?="-DKRKRZ_USE_SJIS=YES"
INSTALL_PREFIX=bin/$(PRESET)/$(BUILD_TYPE)

DATAPATH?=src/core/data

DATAPATH_ABS=$(shell $(FIXPATH) "$(DATAPATH)")

BUILD_PATH=$(shell cmake --preset $(PRESET) -N | grep BUILD_DIR | sed 's/.*BUILD_DIR="\(.*\)"/\1/')

.PHONY: build prebuild install clean docs docs-scan docs-diff

all: build

# cmake 処理実行
# CMAKEOPT で引数定義追加
prebuild:
	cmake --preset $(PRESET) ${CMAKEOPT}

# ビルド実行
build:
	cmake --build $(BUILD_PATH) --config $(BUILD_TYPE)

install:
	cmake --install $(BUILD_PATH) --config $(BUILD_TYPE) --prefix $(INSTALL_PREFIX)

clean:
	cmake --build $(BUILD_PATH) --config $(BUILD_TYPE) --target clean

# ===== ドキュメント生成（doc/ 配下） =====
# いずれのターゲットも .venv の python を使用する前提。
# 仮想環境が無い場合は以下で作成:
#   python -m venv .venv
# stdlib のみ使用しているので追加 pip install は不要。
#
# Windows と Unix 系で python 実行パスが異なるので自動判定。
ifeq ($(OS),Windows_NT)
VENV_PY=.venv/Scripts/python.exe
else
VENV_PY=.venv/bin/python
endif

# src/core のバインドと doc/reference/*.md の差分を更新する通常フロー。
# 1) scan_tjs.py で TJS ネイティブクラスのメンバー一覧を _inventory.json に抽出
# 2) diff_docs.py で _missing.md（未記載 / 廃止メンバー一覧）を再生成
# 実行後に doc/_missing.md を見て doc/reference/<Class>.md を手編集し、
# 再度 `make docs` を走らせてレポートが空に近づくまで繰り返す。
docs: docs-scan docs-diff

# src/core から TJS メンバー一覧を抽出 -> doc/_inventory.json
docs-scan:
	$(VENV_PY) tools/docgen/scan_tjs.py

# _inventory.json と doc/reference/*.md を突き合わせて doc/_missing.md を再生成
docs-diff:
	$(VENV_PY) tools/docgen/diff_docs.py

# WIN版用ルール
ifeq (windows,$(findstring windows,$(PRESET)))

ifeq (x64,$(findstring x64,$(PRESET)))
PLUGINS_SRC_DIR=plugin64
PLUGINS_DST_DIR=$(BUILD_PATH)/$(BUILD_TYPE)/plugin64
EXEFILE=$(BUILD_PATH)/core/$(BUILD_TYPE)/krkrz64.exe
else
ifeq (x86,$(findstring x86,$(PRESET)))
PLUGINS_SRC_DIR=plugin
PLUGINS_DST_DIR=$(BUILD_PATH)/$(BUILD_TYPE)/plugin
EXEFILE=$(BUILD_PATH)/core/$(BUILD_TYPE)/krkrz.exe
endif
endif

PLUGINS = $(patsubst $(PLUGINS_SRC_DIR)/%.dll, $(PLUGINS_DST_DIR)/%.dll, $(wildcard $(PLUGINS_SRC_DIR)/*.dll))

$(PLUGINS_DST_DIR)/%.dll : $(PLUGINS_SRC_DIR)/%.dll
	@mkdir -p `dirname $@`
	cp $< $@

$(EXEFILE): build

run: $(EXEFILE) $(PLUGINS)
	$(EXEFILE) $(DATAPATH_ABS)

endif
