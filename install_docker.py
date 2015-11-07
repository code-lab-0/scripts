#!/usr/bin/env python
# coding : utf-8

import re
from subprocess import Popen, PIPE


COMMANDS="""
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install apparmor
sudo apt-get install docker.io
source /etc/bash_completion.d/docker.io
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
sudo apt-get update
sudo apt-get install lxc-docker
sudo apt-get install docker.io
"""


def exec_lines(lines):
    for line in lines.split("\n"):
        line = line.strip()
        p = Popen(line, shell=True)
        p.wait()


def main():
    exec_lines(COMMANDS)


if __name__ == "__main__":
    main()
