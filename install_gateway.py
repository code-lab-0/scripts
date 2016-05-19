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




def exec_lines(lines):
    for line in lines.split("\n"):
        line = line.strip()
        p = Popen(line, shell=True)
        p.wait()



def main():
    ps = PackageSet()

#    exec_lines(JDK)
#    exec_lines(other)

    p = Popen("sudo -E apt-get update", shell=True)
    p.wait()
    p = Popen("sudo -E apt-get upgrade", shell=True)
    p.wait()

    ps.install_packages(Japanese_IME)
    ps.install_packages(emacs)
    ps.install_packages(network_tools)


if __name__=="__main__":
    main()


