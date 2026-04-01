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
CMAKEOPT?=
INSTALL_PREFIX=bin/$(PRESET)/$(BUILD_TYPE)

DATAPATH?=src/core/data

DATAPATH_ABS=$(shell $(FIXPATH) "$(DATAPATH)")

BUILD_PATH=$(shell cmake --preset $(PRESET) -N | grep BUILD_DIR | sed 's/.*BUILD_DIR="\(.*\)"/\1/')

.PHONY: build prebuild install clean

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
