#!/usr/bin/env python
# coding : utf-8

import re
from subprocess import Popen, PIPE

Japanese_IME="""
fcitx - Flexible Input Method Framework
fcitx-mozc - Mozc engine for fcitx - Client of the Mozc input method
fcitx-frontend-gtk2 - Flexible Input Method Framework - GTK+ 2 IM Module frontend
fcitx-frontend-gtk3 - Flexible Input Method Framework - GTK+ 3 IM Module frontend
fcitx-frontend-qt4 - Flexible Input Method Framework - Qt4 IM Module frontend
fcitx-frontend-qt5 - Free Chinese Input Toy of X - Qt5 IM Module frontend
fcitx-ui-classic - Flexible Input Method Framework - Classic user interface
fcitx-config-gtk - graphic Fcitx configuration tool - Gtk+ 3 version
mozc-utils-gui - GUI utilities of the Mozc input method
"""

emacs="""
emacs24 - GNU Emacs editor (with GTK+ user interface)
ess - 統計プログラミングおよびデータ分析用 Emacs モード
anthy-el - 日本語入力メソッド - elisp フロントエンド
emacs-goodies-el - Miscellaneous add-ons for Emacs
scala-mode-el - Emacs major mode for editing scala source code
eldav - interface to the WebDAV servers for Emacs.
w3m-el - w3m のシンプルな Emacs インタフェース
"""

development_tools="""
maven - Java software project management and comprehension tool
libc6-i386 - 組込用 GNU C ライブラリ: AMD64 用 32 ビット共有ライブラリ
gcc - GNU C コンパイラ
gfortran - GNU Fortran 95 コンパイラ
g++ - GNU C++ コンパイラ
libc6-dev-amd64 - Embedded GNU C Library: 64bit Development Libraries for AMD64
libpng3 - PNG ライブラリ - ランタイム
netpbm - グラフィックの画像フォーマット間変換ツール
libnetpbm10 - グラフィック変換ツールの共有ライブラリ
libnetpbm10-dev - グラフィック変換ツールの開発用ライブラリおよびヘッダファイル
flex - 高速な字句解析器生成プログラム
perl-doc - Perl ドキュメント
tcl-dev - Tool Command Language (default version) - development files
tk-dev - Toolkit for Tcl and X11 (default version) - development files
xorg-dev - X.Org X Window System development libraries
bison - YACC 互換なパーサジェネレータ
cmake - cross-platform, open-source make system
libwww-mechanize-perl - module to automate interaction with websites
libjson-perl - module for manipulating JSON-formatted data
libset-intspan-perl - module to manage sets of integers
libset-scalar-perl - Perl interface for operations on finite sets
"""

latex="""
texlive-base
ptex-bin - TeX Live: 移行用ダミーパッケージ
xdvik-ja - X Window System 向けの日本語化版 DVI プレビューア
dvipsk-ja - 日本語をサポートした DVI から PostScript への変換器
texlive-fonts-recommended - TeX Live: Recommended fonts
texlive-fonts-extra - TeX Live: Additional fonts
texlive-bibtex-extra - TeX Live: BibTeX additional styles
"""

mysql="""
mysql-client-5.6 - MySQL database client binaries
mysql-server-5.6 - MySQL database server binaries and system database setup
"""

network_tools="""
openssh-client - リモートマシンへの安全なアクセスを可能にする secure shell (SSH) クライアント
openssh-server - secure shell (SSH) server, for secure access from remote machines
firefox - Safe and easy web browser from Mozilla
apache2 - Apache HTTP Server
apache2-mpm-prefork - transitional prefork MPM package for apache2
apache2-utils - Apache HTTP Server (utility programs for web servers)
cadaver - コマンドライン WebDAV クライアント
ntp - Network Time Protocol デーモンおよびユーティリティプログラム
libapache2-svn - Apache Subversion server modules for Apache httpd (dummy package)
subversion - 先進的なバージョン管理システム
subversion-tools - Assorted tools related to Apache Subversion
libapache2-mod-encoding - Apache2 module for non-ascii filename interoperability
"""

misc_tools="""
xdiskusage - du コマンドによるディスク使用量をグラフィカルに表示
ncdu - ncurses ディスク利用状況ビューア
recoll - Personal full text search package with a Qt GUI
task-spooler - personal job scheduler
inkscape - ベクターベースのドローイングプログラム
libclucene-dev - library for full-featured text search engine (development)
imagemagick - 画像編集プログラム
lftp - Sophisticated command-line FTP/HTTP client programs
task-spooler - personal job scheduler
sysstat - system performance tools for Linux
"""


RGM="""
imagemagick - 画像編集プログラム
libxt-dev - X11 toolkit intrinsics library (development headers)
libgtk2.0-dev - development files for the GTK+ library
netcdf-bin - NetCDF ファイル読み書き用プログラム
libiodbc2-dev - iODBC Driver Manager (development files)
libtiff4-dev - Tag Image File Format library (TIFF), transitional package
libgmp3-dev - Multiprecision arithmetic library developers tools
libgd2-xpm-dev - GD Graphics Library (transitional package)
libgd-tools - GD コマンドラインツールとサンプルコード
hdf5-tools - 階層化データ形式 5 (HDF5) - ランタイムツール集
h5utils - HDF5 ファイル可視化ツール
ggobi - 高次元データ用データ可視化システム
libgl1-mesa-dev - free implementation of the OpenGL API -- GLX development files
libgl1-mesa-dri - OpenGL API のフリーな実装 -- DRI モジュール
libglu1-mesa-dev - Mesa OpenGL utility library -- development files
fftw-dev - library for computing Fast Fourier Transforms
libgtk2.0-dev - development files for the GTK+ library
libgsl0-dev - GNU Scientific Library (GSL) -- development package
gsl-bin - GNU 科学ライブラリ (GSL) -- バイナリパッケージ
h5utils - HDF5 ファイル可視化ツール
hdf5-tools - 階層化データ形式 5 (HDF5) - ランタイムツール集
tcllib - Standard Tcl Library
libboost-dev - Boost C++ Libraries development files (default version)
libquantlib0-dev - Quantitative Finance Library -- development package
curl - command line tool for transferring data with URL syntax
libcurl4-gnutls-dev - development files and documentation for libcurl (GnuTLS flavour)
libnetcdf-dev - Development kit for NetCDF
libxml2 - GNOME XML ライブラリ
libxml2-dev - Development files for the GNOME XML library
libgeos-dev - Geometry engine for GIS - Development files
libgdal-dev - Geospatial Data Abstraction Library - Development files
libproj-dev - Cartographic projection library (development files)
libmpfr-dev - multiple precision floating-point computation developers tools
cl-fftw3 - Common Lisp package for using the FFTW3 library
libfftw3-dev - Library for computing Fast Fourier Transforms - development
libqtcore4 - Qt 4 コアモジュール
libqt4-core - Qt 4 の非 GUI のコアランタイムライブラリのための移行用パッケージ
libsoqt4-dev - Qt4 GUI component toolkit for Inventor - development
coinor-libclp-dev - Coin-or linear programming solver (developer files)
libudunits2-dev - Development files for the libunits physical units package
libdb-dev - Berkeley Database Libraries [development]
mpc - command-line tool to interface MPD
libmpc-dev - multiple precision complex floating-point library development package
octave - 数値計算向けの GNU Octave 言語
liboctave-dev - Development files for the GNU Octave language
libdieharder-dev - Random-number generator test library -- development package
liblua5.2-dev - Development files for the Lua language version 5.2
libsprng2-dev - SPRNG Scalable Parallel RNG library -- development package
"""


class PackageSet:

    def __init__(self):
        #self.apt_string = None
        pass

    def apt_cache_search(self, keyword):
        p = Popen("apt-cache search " + keyword + " > pkg_list.txt", shell=True)
        p.wait()
        
        f = open("pkg_list.txt")
        result = f.read()
        f.close()
        return result


    def get_package_name(self, line):
        result = ""
        m = re.search(r"^(\S+) - ", line)
        if m != None:
            result = m.group(1)

        return result
        

    def get_package_list(self, lines):
        result = []
        
        for line in lines.split("\n"):
            result.append(self.get_package_name(line))

        return result


    def check_package(self, pkg):
        p = Popen("apt-cache search " + pkg + " > pkg_list.txt" , shell=True)
        p.wait()

        pattern = re.compile(r"^(\S+) - ")
        for line in open("pkg_list.txt"):
            line = line.strip()
            m = pattern.search(line)
            if m != None:
                if m.group(1) == pkg:
                    return line

        return False


    def check_package_list(self, pkgs):
        result = []
        for p in pkgs:
            r = self.check_package(p)
            if type(r) is str:
                result.append(r)
            else:
                r = "** " + p + " is not found. **"
                result.append(r)

        return result


    def install_package(self, pkg):
        com = "sudo -E apt-get --install-recommends  -y install " + pkg
        print(com)
        p = Popen(com, shell=True)
        p.wait()


    def install_packages(self, lines):
        for pkg in self.get_package_list(lines):
            self.install_package(pkg)


JDK="""
sudo apt-get -y install python-software-properties
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install oracle-java8-installer
"""

# Used by Apache Mesos
other="""
sudo apt-get -y install build-essential python-dev python3-dev 
sudo apt-get -y install python-boto libcurl4-nss-dev libsasl2-dev
sudo apt-get -y install libapr1-dev libsvn-dev maven
"""


def exec_lines(lines):
    for line in lines.split("\n"):
        line = line.strip()
        p = Popen(line, shell=True)
        p.wait()



def main2():
    ps = PackageSet()

    exec_lines(JDK)
    exec_lines(other)

    p = Popen("sudo -E apt-get update", shell=True)
    p.wait()
    p = Popen("sudo -E apt-get upgrade", shell=True)
    p.wait()

    ps.install_packages(Japanese_IME)
    ps.install_packages(emacs)
    ps.install_packages(development_tools)
    ps.install_packages(latex)
    ps.install_packages(mysql)
    ps.install_packages(network_tools)
    ps.install_packages(misc_tools)

    ps.install_packages(RGM)

    for pkg in ps.get_package_list(ps.apt_cache_search("r-cran-*")):
        ps.install_package(pkg)


if __name__=="__main__":
    main()


