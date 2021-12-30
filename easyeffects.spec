#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : easyeffects
Version  : 6.1.5
Release  : 241
URL      : file:///aot/build/clearlinux/packages/easyeffects/easyeffects-v6.1.5.tar.gz
Source0  : file:///aot/build/clearlinux/packages/easyeffects/easyeffects-v6.1.5.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: easyeffects-bin = %{version}-%{release}
Requires: easyeffects-data = %{version}-%{release}
Requires: easyeffects-locales = %{version}-%{release}
BuildRequires : PyYAML
BuildRequires : Pygments
BuildRequires : SDL2
BuildRequires : SDL2-dev
BuildRequires : Sphinx
BuildRequires : Vulkan-Headers-dev
BuildRequires : Vulkan-Loader-dev
BuildRequires : alsa-lib
BuildRequires : alsa-lib-dev
BuildRequires : alsa-lib-dev32
BuildRequires : alsa-plugins
BuildRequires : alsa-tools
BuildRequires : alsa-tools-dev
BuildRequires : alsa-ucm-conf
BuildRequires : alsa-utils
BuildRequires : appstream-glib
BuildRequires : appstream-glib-dev
BuildRequires : atk
BuildRequires : atk-dev
BuildRequires : atkmm-dev
BuildRequires : autogen
BuildRequires : autogen-dev
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : binutils-dev
BuildRequires : binutils-extras
BuildRequires : bison
BuildRequires : breeze
BuildRequires : breeze-gtk
BuildRequires : breeze-icons
BuildRequires : buildreq-cmake
BuildRequires : buildreq-configure
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : buildreq-qmake
BuildRequires : bzip2-dev
BuildRequires : bzip2-staticdev
BuildRequires : cairo
BuildRequires : cairo-dev
BuildRequires : cairomm-dev
BuildRequires : calf
BuildRequires : calf-dev
BuildRequires : calf-staticdev
BuildRequires : clr-avx-tools
BuildRequires : clr-rpm-config
BuildRequires : cmake
BuildRequires : cmake-dev
BuildRequires : colord-dev
BuildRequires : cups
BuildRequires : cups-dev
BuildRequires : curl
BuildRequires : curl-dev
BuildRequires : curl-lib
BuildRequires : dbus
BuildRequires : dbus-dev
BuildRequires : dejagnu
BuildRequires : docbook-utils
BuildRequires : docbook-xml
BuildRequires : docutils
BuildRequires : doxygen
BuildRequires : elfutils-dev
BuildRequires : expat
BuildRequires : expat-dev
BuildRequires : expat-staticdev
BuildRequires : expect
BuildRequires : extra-cmake-modules-data
BuildRequires : fftw-dev
BuildRequires : fftw-staticdev
BuildRequires : findutils
BuildRequires : flac
BuildRequires : flac-dev
BuildRequires : flac-dev32
BuildRequires : flac-staticdev
BuildRequires : flac-staticdev32
BuildRequires : flex
BuildRequires : fluidsynth
BuildRequires : fluidsynth-dev
BuildRequires : fluidsynth-staticdev
BuildRequires : fmt
BuildRequires : fmt-dev
BuildRequires : fmt-staticdev
BuildRequires : fomp
BuildRequires : fomp-dev
BuildRequires : fontconfig
BuildRequires : fontconfig-dev
BuildRequires : fonts-clear
BuildRequires : freetype
BuildRequires : freetype-dev
BuildRequires : fribidi-dev
BuildRequires : gcc
BuildRequires : gcc-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-doc
BuildRequires : gcc-go
BuildRequires : gcc-go-lib
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libs-math
BuildRequires : gcc-libstdc++32
BuildRequires : gcc-libubsan
BuildRequires : gcc-locale
BuildRequires : gdb-dev
BuildRequires : gdk-pixbuf
BuildRequires : gdk-pixbuf-dev
BuildRequires : git
BuildRequires : glib
BuildRequires : glib-bin
BuildRequires : glib-dev
BuildRequires : glib-networking
BuildRequires : glibc-bin
BuildRequires : glibc-dev
BuildRequires : glibc-dev32
BuildRequires : glibc-doc
BuildRequires : glibc-extras
BuildRequires : glibc-lib-avx2
BuildRequires : glibc-libc32
BuildRequires : glibc-locale
BuildRequires : glibc-nscd
BuildRequires : glibc-staticdev
BuildRequires : glibc-utils
BuildRequires : glslang
BuildRequires : gmp-dev
BuildRequires : gnutls
BuildRequires : gnutls-dev
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : googletest-dev
BuildRequires : gperf
BuildRequires : graphite
BuildRequires : graphite-dev
BuildRequires : graphviz
BuildRequires : graphviz-extras
BuildRequires : gtk+-dev
BuildRequires : gtk3
BuildRequires : gtk3-dev
BuildRequires : gtk4
BuildRequires : gtk4-dev
BuildRequires : gtkmm4
BuildRequires : gtkmm4-dev
BuildRequires : gtkmm4-staticdev
BuildRequires : guile
BuildRequires : harfbuzz-dev
BuildRequires : icu4c-dev
BuildRequires : icu4c-lib
BuildRequires : json
BuildRequires : json-dev
BuildRequires : keyutils
BuildRequires : keyutils-dev
BuildRequires : krb5
BuildRequires : krb5-dev
BuildRequires : ladspa_sdk
BuildRequires : ladspa_sdk-dev
BuildRequires : ladspa_sdk-staticdev
BuildRequires : libICE-dev
BuildRequires : libSM-dev
BuildRequires : libX11-data
BuildRequires : libX11-dev
BuildRequires : libX11-lib
BuildRequires : libXScrnSaver
BuildRequires : libXScrnSaver-dev
BuildRequires : libXScrnSaver-lib
BuildRequires : libXau-dev
BuildRequires : libXau-lib
BuildRequires : libXcomposite-dev
BuildRequires : libXcursor-dev
BuildRequires : libXcursor-lib
BuildRequires : libXdamage-dev
BuildRequires : libXdamage-lib
BuildRequires : libXdmcp-dev
BuildRequires : libXdmcp-lib
BuildRequires : libXext-dev
BuildRequires : libXext-lib
BuildRequires : libXfixes-dev
BuildRequires : libXfont2-dev
BuildRequires : libXft
BuildRequires : libXft-dev
BuildRequires : libXft-lib
BuildRequires : libXi-dev
BuildRequires : libXi-lib
BuildRequires : libXinerama-dev
BuildRequires : libXmu-dev
BuildRequires : libXpm-dev
BuildRequires : libXrandr-dev
BuildRequires : libXrender-dev
BuildRequires : libXrender-lib
BuildRequires : libXres-dev
BuildRequires : libXt-dev
BuildRequires : libXtst-dev
BuildRequires : libXtst-lib
BuildRequires : libXv-dev
BuildRequires : libXxf86vm-dev
BuildRequires : libXxf86vm-lib
BuildRequires : libadwaita
BuildRequires : libadwaita-dev
BuildRequires : libadwaita-staticdev
BuildRequires : libbs2b
BuildRequires : libbs2b-dev
BuildRequires : libbs2b-staticdev
BuildRequires : libcanberra-dev
BuildRequires : libcap-dev
BuildRequires : libcap-ng-dev
BuildRequires : libcap-staticdev
BuildRequires : libebur128
BuildRequires : libebur128-dev
BuildRequires : libebur128-staticdev
BuildRequires : libedit
BuildRequires : libedit-dev
BuildRequires : libfdk_aac-dev
BuildRequires : libfdk_aac-staticdev
BuildRequires : libffi-dev
BuildRequires : libffi-staticdev
BuildRequires : libgcc1
BuildRequires : libgcrypt-dev
BuildRequires : libgit2
BuildRequires : libgit2-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libjpeg-turbo-dev32
BuildRequires : libjpeg-turbo-lib
BuildRequires : libjpeg-turbo-lib32
BuildRequires : libjpeg-turbo-staticdev
BuildRequires : liblo
BuildRequires : liblo-dev
BuildRequires : liblo-staticdev
BuildRequires : libogg-dev
BuildRequires : libogg-dev32
BuildRequires : libogg-staticdev
BuildRequires : libogg-staticdev32
BuildRequires : libpng
BuildRequires : libpng-dev
BuildRequires : libpng-staticdev
BuildRequires : libpthread-stubs-dev
BuildRequires : librsvg-dev
BuildRequires : libsamplerate-dev
BuildRequires : libsamplerate-staticdev
BuildRequires : libsigc++-dev
BuildRequires : libsigc++-staticdev
BuildRequires : libsndfile-dev
BuildRequires : libsndfile-staticdev
BuildRequires : libstdc++
BuildRequires : libtool-dev
BuildRequires : libunwind-dev
BuildRequires : libusb-dev
BuildRequires : libvorbis-dev
BuildRequires : libvorbis-dev32
BuildRequires : libvorbis-staticdev
BuildRequires : libvorbis-staticdev32
BuildRequires : libwebp-dev
BuildRequires : libwebp-staticdev
BuildRequires : libxcb-dev
BuildRequires : libxcb-lib
BuildRequires : libxml2
BuildRequires : libxml2-dev
BuildRequires : libxml2-staticdev
BuildRequires : libxslt
BuildRequires : libxslt-bin
BuildRequires : lilv
BuildRequires : lilv-dev
BuildRequires : lilv-staticdev
BuildRequires : lsp-plugins
BuildRequires : lsp-plugins-dev
BuildRequires : lsp-plugins-staticdev
BuildRequires : lua-dev
BuildRequires : lua-staticdev
BuildRequires : lv2
BuildRequires : lv2-dev
BuildRequires : lxml
BuildRequires : m4
BuildRequires : mda-lv2
BuildRequires : mda-lv2-dev
BuildRequires : mesa
BuildRequires : mesa-dev
BuildRequires : meson
BuildRequires : mpc-dev
BuildRequires : mpfr-dev
BuildRequires : ncurses
BuildRequires : ncurses-dev
BuildRequires : ninja
BuildRequires : octave-dev
BuildRequires : openssh
BuildRequires : openssl-dev
BuildRequires : openssl-staticdev
BuildRequires : opus
BuildRequires : opus-dev
BuildRequires : opus-lib
BuildRequires : opus-staticdev
BuildRequires : pango-dev
BuildRequires : pangomm-dev
BuildRequires : pcre-dev
BuildRequires : pcre-staticdev
BuildRequires : pcre2-dev
BuildRequires : pcre2-staticdev
BuildRequires : perl
BuildRequires : perl(Test::More)
BuildRequires : perl(XML::Parser)
BuildRequires : pipewire
BuildRequires : pipewire-dev
BuildRequires : pipewire-tests
BuildRequires : pixman-dev
BuildRequires : pixman-staticdev
BuildRequires : pkg-config
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(fftw3f)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gstreamer-player-1.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(gtk4)
BuildRequires : pkgconfig(gtk4-unix-print)
BuildRequires : pkgconfig(gtk4-x11)
BuildRequires : pkgconfig(gtkmm-4.0)
BuildRequires : pkgconfig(iso-codes)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libarchive)
BuildRequires : pkgconfig(libgcab-1.0)
BuildRequires : pkgconfig(librsvg-2.0)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(lv2)
BuildRequires : pkgconfig(rubberband)
BuildRequires : pkgconfig(samplerate)
BuildRequires : pkgconfig(sndfile)
BuildRequires : pkgconfig(uuid)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(x11-xcb)
BuildRequires : procps-ng
BuildRequires : pulseaudio
BuildRequires : pulseaudio-dev
BuildRequires : pygobject
BuildRequires : pypi(html5lib)
BuildRequires : pypi(importlib_metadata)
BuildRequires : pypi(isodate)
BuildRequires : pypi(pyparsing)
BuildRequires : python-graphviz
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : python3-staticdev
BuildRequires : rdflib
BuildRequires : readline-dev
BuildRequires : requests
BuildRequires : rnnoise
BuildRequires : rnnoise-dev
BuildRequires : rnnoise-staticdev
BuildRequires : rpm
BuildRequires : rpm-dev
BuildRequires : rtkit
BuildRequires : rtkit-bin
BuildRequires : rtkit-data
BuildRequires : rtkit-libexec
BuildRequires : rtkit-services
BuildRequires : rubberband-dev
BuildRequires : rubberband-staticdev
BuildRequires : sassc
BuildRequires : sed
BuildRequires : serd
BuildRequires : serd-dev
BuildRequires : serd-staticdev
BuildRequires : setxkbmap
BuildRequires : shared-mime-info
BuildRequires : shared-mime-info-dev
BuildRequires : sord
BuildRequires : sord-dev
BuildRequires : sord-staticdev
BuildRequires : speex-dev
BuildRequires : speex-staticdev
BuildRequires : speexdsp-dev
BuildRequires : speexdsp-staticdev
BuildRequires : sqlite-autoconf-dev
BuildRequires : sratom
BuildRequires : sratom-dev
BuildRequires : sratom-staticdev
BuildRequires : systemd
BuildRequires : systemd-dev
BuildRequires : tbb
BuildRequires : tbb-dev
BuildRequires : tbb-staticdev
BuildRequires : tcl
BuildRequires : texinfo
BuildRequires : tiff-dev
BuildRequires : tiff-staticdev
BuildRequires : util-linux
BuildRequires : util-linux-dev
BuildRequires : valgrind
BuildRequires : valgrind-dev
BuildRequires : vamp-sdk
BuildRequires : vamp-sdk-dev
BuildRequires : vamp-sdk-staticdev
BuildRequires : wayland
BuildRequires : wayland-dev
BuildRequires : xauth
BuildRequires : xclip
BuildRequires : xdg-dbus-proxy
BuildRequires : xdg-desktop-portal
BuildRequires : xdg-desktop-portal-dev
BuildRequires : xdg-desktop-portal-gtk
BuildRequires : xdg-desktop-portal-kde
BuildRequires : xdg-user-dirs
BuildRequires : xdg-user-dirs-gtk
BuildRequires : xdg-utils
BuildRequires : xdotool
BuildRequires : xdpyinfo
BuildRequires : xf86-input-libinput
BuildRequires : xf86-video-amdgpu
BuildRequires : xf86-video-ati
BuildRequires : xf86-video-fbdev
BuildRequires : xf86-video-nouveau
BuildRequires : xf86-video-qxl
BuildRequires : xf86-video-vboxvideo
BuildRequires : xf86-video-vesa
BuildRequires : xf86-video-vmware
BuildRequires : xfontsel
BuildRequires : xhost
BuildRequires : xinit
BuildRequires : xinput
BuildRequires : xkbcomp
BuildRequires : xkeyboard-config
BuildRequires : xkill
BuildRequires : xmodmap
BuildRequires : xorg-server
BuildRequires : xorg-server-dev
BuildRequires : xorgproto
BuildRequires : xorgproto-dev
BuildRequires : xprop
BuildRequires : xrandr
BuildRequires : xrdb
BuildRequires : xrdp
BuildRequires : xrestop
BuildRequires : xscreensaver
BuildRequires : xsel
BuildRequires : xset
BuildRequires : xsetroot
BuildRequires : xvfb-run
BuildRequires : xwd
BuildRequires : xwininfo
BuildRequires : xz
BuildRequires : xz-dev
BuildRequires : xz-staticdev
BuildRequires : yaml
BuildRequires : yaml-cpp
BuildRequires : yaml-cpp-dev
BuildRequires : zita-convolver
BuildRequires : zita-convolver-dev
BuildRequires : zita-convolver-staticdev
BuildRequires : zlib-dev
BuildRequires : zlib-staticdev
BuildRequires : zstd-dev
BuildRequires : zstd-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Fix-libadwaita-req.patch

%description
# EasyEffects
[![CircleCI](https://circleci.com/gh/wwmm/easyeffects.svg?style=shield)](https://circleci.com/gh/wwmm/easyeffects)
[![Donate](https://liberapay.com/assets/widgets/donate.svg)](https://liberapay.com/wwmm/donate)

%package bin
Summary: bin components for the easyeffects package.
Group: Binaries
Requires: easyeffects-data = %{version}-%{release}

%description bin
bin components for the easyeffects package.


%package data
Summary: data components for the easyeffects package.
Group: Data

%description data
data components for the easyeffects package.


%package doc
Summary: doc components for the easyeffects package.
Group: Documentation

%description doc
doc components for the easyeffects package.


%package locales
Summary: locales components for the easyeffects package.
Group: Default

%description locales
locales components for the easyeffects package.


%prep
%setup -q -n easyeffects
cd %{_builddir}/easyeffects
%patch1 -p1

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640831607
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags_pgo content
## pgo generate
unset ASFLAGS
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage -fprofile-partial-training -fprofile-correction -freorder-functions --coverage -lgcov"
export CFLAGS_GENERATE="-O3 -ggdb3 -ggnu-pubnames --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export ASMFLAGS_GENERATE="-O3 -ggdb3 -ggnu-pubnames --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export FCFLAGS_GENERATE="-O3 -ggdb3 -ggnu-pubnames --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export FFLAGS_GENERATE="-O3 -ggdb3 -ggnu-pubnames --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export CXXFLAGS_GENERATE="-O3 -ggdb3 -ggnu-pubnames --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export LDFLAGS_GENERATE="-O3 -ggdb3 -ggnu-pubnames --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export LIBS_GENERATE="-lgcov"
## pgo use
## -fno-tree-vectorize: disable -ftree-vectorize thus disable -ftree-loop-vectorize and -ftree-slp-vectorize -fopt-info-vec
## -O3 -ffast-math
## -funroll-loops maybe dangerous
## -Wl,-z,max-page-size=0x1000
## -pthread -lpthread
## -Wl,-Bsymbolic-functions
export PGO_USE="-Wmissing-profile -Wcoverage-mismatch -fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-partial-training -fprofile-correction -freorder-functions"
export CFLAGS_USE="-ggdb3 -ggnu-pubnames -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export ASMFLAGS_USE="-ggdb3 -ggnu-pubnames -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export FCFLAGS_USE="-ggdb3 -ggnu-pubnames -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export FFLAGS_USE="-ggdb3 -ggnu-pubnames -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export CXXFLAGS_USE="-ggdb3 -ggnu-pubnames -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export LDFLAGS_USE="-ggdb3 -ggnu-pubnames -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
#
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:/usr/share/pkgconfig"
#
export LD_LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/gbm:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/gbm:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
#
export CPATH="/usr/local/cuda/include"
#
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=1
export __GL_SYNC_DISPLAY_DEVICE=HDMI-0
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=HDMI-0
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH="/usr/share/defaults/fonts"
export GTK_IM_MODULE="xim"
export QT_IM_MODULE="cedilla"
export FREETYPE_PROPERTIES="truetype:interpreter-version=40"
export PLASMA_USE_QT_SCALING=1
export QT_AUTO_SCREEN_SCALE_FACTOR=1
export GSETTINGS_SCHEMA_DIR="/usr/share/glib-2.0/schemas"
## altflags_pgo end
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
export ASMFLAGS="${ASMFLAGS_GENERATE}"
export LIBS="${LIBS_GENERATE}"
echo PGO Phase 1
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" LIBS="$LIBS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Ddefault_library=both  -Ddefault_library=both builddir
## make_prepend content
sd '(LINK_ARGS.+)(\s/usr/lib64/libfftw3f\.so)' -- '$1 -Wl,--whole-archive,--as-needed,--allow-multiple-definition,/usr/lib64/libfftw3f.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive' $(fd -uu --glob *.ninja)
sd '(LINK_ARGS.+)(\s/usr/lib64/libfftw3\.so)' -- '$1 -Wl,--whole-archive,--as-needed,--allow-multiple-definition,/usr/lib64/libfftw3.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive' $(fd -uu --glob *.ninja)
sd '(LINK_ARGS.+)(\s/usr/lib64/libsamplerate\.so)' -- '$1 -Wl,--whole-archive,--as-needed,--allow-multiple-definition,/usr/lib64/libsamplerate.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive' $(fd -uu --glob *.ninja)
sd '(LINK_ARGS.+)(\s/usr/lib64/libsndfile\.so)' -- '$1 -Wl,--whole-archive,--as-needed,--allow-multiple-definition,/usr/lib64/libsndfile.a,/usr/lib64/libFLAC.a,/usr/lib64/libopus.a,/usr/lib64/libvorbis.a,/usr/lib64/libvorbisenc.a,/usr/lib64/libvorbisfile.a,/usr/lib64/libogg.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive' $(fd -uu --glob *.ninja)
sd '(LINK_ARGS.+)(\s/usr/lib64/libsigc\-3\.0\.so)' -- '$1 -Wl,--whole-archive,--as-needed,--allow-multiple-definition,/usr/lib64/libsigc-3.0.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive' $(fd -uu --glob *.ninja)
sd '(LINK_ARGS.+)(\s/usr/lib64/libbs2b\.so)' -- '$1 -Wl,--whole-archive,--as-needed,--allow-multiple-definition,/usr/lib64/libbs2b.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive' $(fd -uu --glob *.ninja)
sd '(LINK_ARGS.+)(\s/usr/lib64/libfmt\.so)' -- '$1 -Wl,--whole-archive,--as-needed,--allow-multiple-definition,/usr/lib64/libfmt.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive' $(fd -uu --glob *.ninja)
sd '(LINK_ARGS.+)(\s/usr/lib64/libtbb\.so)' -- '$1 -Wl,--whole-archive,--as-needed,--allow-multiple-definition,/usr/lib64/libtbb.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive' $(fd -uu --glob *.ninja)
sd '(LINK_ARGS.+)(\s\-ltbb)' -- '$1 -Wl,--whole-archive,--as-needed,--allow-multiple-definition,/usr/lib64/libtbb.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive' $(fd -uu --glob *.ninja)
sd '(LINK_ARGS.+)(\s/usr/lib64/libzita-convolver\.so)' -- '$1 -Wl,--whole-archive,--as-needed,--allow-multiple-definition,/usr/lib64/libzita-convolver.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive' $(fd -uu --glob *.ninja)
sd '(LINK_ARGS.+)(\s\-lzita\-convolver)' -- '$1 -Wl,--whole-archive,--as-needed,--allow-multiple-definition,/usr/lib64/libzita-convolver.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive' $(fd -uu --glob *.ninja)
sd '(LINK_ARGS.+)(\s/usr/lib64/libspeexdsp\.so)' -- '$1 -Wl,--whole-archive,--as-needed,--allow-multiple-definition,/usr/lib64/libspeexdsp.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive' $(fd -uu --glob *.ninja)
sd '(LINK_ARGS.+)(\s/usr/lib64/librubberband\.so)' -- '$1 -Wl,--whole-archive,--as-needed,--allow-multiple-definition,/usr/lib64/librubberband.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive' $(fd -uu --glob *.ninja)
sd '(LINK_ARGS.+)(\s/usr/lib64/librnnoise\.so)' -- '$1 -Wl,--whole-archive,--as-needed,--allow-multiple-definition,/usr/lib64/librnnoise.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive' $(fd -uu --glob *.ninja)
sd '(LINK_ARGS.+)(\s/usr/lib64/libebur128\.so)' -- '$1 -Wl,--whole-archive,--as-needed,--allow-multiple-definition,/usr/lib64/libebur128.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive' $(fd -uu --glob *.ninja)
sd '(LINK_ARGS.+)(\s/usr/lib64/\.\./lib64/libebur128\.so)' -- '$1 -Wl,--whole-archive,--as-needed,--allow-multiple-definition,/usr/lib64/libebur128.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive' $(fd -uu --glob *.ninja)
sd '(LINK_ARGS.+)(\s/usr/lib64/liblilv\-0\.so)' -- '$1 -Wl,--whole-archive,--as-needed,--allow-multiple-definition,/usr/lib64/liblilv-0.a,/usr/lib64/libsratom-0.a,/usr/lib64/libserd-0.a,/usr/lib64/libsord-0.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive' $(fd -uu --glob *.ninja)
sd '(LINK_ARGS.+)(\s/usr/lib64/libsratom\-0\.so)' -- '$1 -Wl,--whole-archive,--as-needed,--allow-multiple-definition,/usr/lib64/libsratom-0.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive' $(fd -uu --glob *.ninja)
sd '(LINK_ARGS.+)(\s/usr/lib64/libserd\-0\.so)' -- '$1 -Wl,--whole-archive,--as-needed,--allow-multiple-definition,/usr/lib64/libserd-0.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive' $(fd -uu --glob *.ninja)
sd '(LINK_ARGS.+)(\s/usr/lib64/libsord\-0\.so)' -- '$1 -Wl,--whole-archive,--as-needed,--allow-multiple-definition,/usr/lib64/libsord-0.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive' $(fd -uu --glob *.ninja)
## make_prepend end
ninja --verbose %{?_smp_mflags} -C builddir

%install
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang easyeffects

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/easyeffects

%files data
%defattr(-,root,root,-)
/usr/share/applications/com.github.wwmm.easyeffects.desktop
/usr/share/dbus-1/services/com.github.wwmm.easyeffects.service
/usr/share/glib-2.0/schemas/com.github.wwmm.easyeffects.autogain.gschema.xml
/usr/share/glib-2.0/schemas/com.github.wwmm.easyeffects.bassenhancer.gschema.xml
/usr/share/glib-2.0/schemas/com.github.wwmm.easyeffects.bassloudness.gschema.xml
/usr/share/glib-2.0/schemas/com.github.wwmm.easyeffects.compressor.gschema.xml
/usr/share/glib-2.0/schemas/com.github.wwmm.easyeffects.convolver.gschema.xml
/usr/share/glib-2.0/schemas/com.github.wwmm.easyeffects.crossfeed.gschema.xml
/usr/share/glib-2.0/schemas/com.github.wwmm.easyeffects.crystalizer.gschema.xml
/usr/share/glib-2.0/schemas/com.github.wwmm.easyeffects.deesser.gschema.xml
/usr/share/glib-2.0/schemas/com.github.wwmm.easyeffects.delay.gschema.xml
/usr/share/glib-2.0/schemas/com.github.wwmm.easyeffects.echo_canceller.gschema.xml
/usr/share/glib-2.0/schemas/com.github.wwmm.easyeffects.equalizer.channel.gschema.xml
/usr/share/glib-2.0/schemas/com.github.wwmm.easyeffects.equalizer.gschema.xml
/usr/share/glib-2.0/schemas/com.github.wwmm.easyeffects.exciter.gschema.xml
/usr/share/glib-2.0/schemas/com.github.wwmm.easyeffects.filter.gschema.xml
/usr/share/glib-2.0/schemas/com.github.wwmm.easyeffects.gate.gschema.xml
/usr/share/glib-2.0/schemas/com.github.wwmm.easyeffects.gschema.xml
/usr/share/glib-2.0/schemas/com.github.wwmm.easyeffects.limiter.gschema.xml
/usr/share/glib-2.0/schemas/com.github.wwmm.easyeffects.loudness.gschema.xml
/usr/share/glib-2.0/schemas/com.github.wwmm.easyeffects.maximizer.gschema.xml
/usr/share/glib-2.0/schemas/com.github.wwmm.easyeffects.multibandcompressor.gschema.xml
/usr/share/glib-2.0/schemas/com.github.wwmm.easyeffects.multibandgate.gschema.xml
/usr/share/glib-2.0/schemas/com.github.wwmm.easyeffects.outputlevel.gschema.xml
/usr/share/glib-2.0/schemas/com.github.wwmm.easyeffects.pitch.gschema.xml
/usr/share/glib-2.0/schemas/com.github.wwmm.easyeffects.reverb.gschema.xml
/usr/share/glib-2.0/schemas/com.github.wwmm.easyeffects.rnnoise.gschema.xml
/usr/share/glib-2.0/schemas/com.github.wwmm.easyeffects.spectrum.gschema.xml
/usr/share/glib-2.0/schemas/com.github.wwmm.easyeffects.stereotools.gschema.xml
/usr/share/glib-2.0/schemas/com.github.wwmm.easyeffects.streaminputs.gschema.xml
/usr/share/glib-2.0/schemas/com.github.wwmm.easyeffects.streamoutputs.gschema.xml
/usr/share/icons/hicolor/scalable/apps/easyeffects.svg
/usr/share/metainfo/com.github.wwmm.easyeffects.metainfo.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/help/C/easyeffects/advancedinfo.page
/usr/share/help/C/easyeffects/autogain.page
/usr/share/help/C/easyeffects/bassenhancer.page
/usr/share/help/C/easyeffects/bassloudness.page
/usr/share/help/C/easyeffects/blocklist.page
/usr/share/help/C/easyeffects/compressor.page
/usr/share/help/C/easyeffects/convolver.page
/usr/share/help/C/easyeffects/crossfeed.page
/usr/share/help/C/easyeffects/crystalizer.page
/usr/share/help/C/easyeffects/deesser.page
/usr/share/help/C/easyeffects/delay.page
/usr/share/help/C/easyeffects/echocanceller.page
/usr/share/help/C/easyeffects/effectsorder.page
/usr/share/help/C/easyeffects/enableapp.page
/usr/share/help/C/easyeffects/equalizer.page
/usr/share/help/C/easyeffects/exciter.page
/usr/share/help/C/easyeffects/filter.page
/usr/share/help/C/easyeffects/gate.page
/usr/share/help/C/easyeffects/general.page
/usr/share/help/C/easyeffects/guide_1.page
/usr/share/help/C/easyeffects/index.page
/usr/share/help/C/easyeffects/limiter.page
/usr/share/help/C/easyeffects/loudness.page
/usr/share/help/C/easyeffects/maximizer.page
/usr/share/help/C/easyeffects/multibandcompressor.page
/usr/share/help/C/easyeffects/multibandgate.page
/usr/share/help/C/easyeffects/pipewire.page
/usr/share/help/C/easyeffects/pitch.page
/usr/share/help/C/easyeffects/reverb.page
/usr/share/help/C/easyeffects/rnnoise.page
/usr/share/help/C/easyeffects/saturated.page
/usr/share/help/C/easyeffects/settingsmenu.page
/usr/share/help/C/easyeffects/spectrum.page
/usr/share/help/C/easyeffects/stereotools.page
/usr/share/help/C/easyeffects/testsignals.page
/usr/share/help/C/easyeffects/userpresets.page

%files locales -f easyeffects.lang
%defattr(-,root,root,-)
