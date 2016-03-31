#!/usr/bin/env python3

"""
process each files one by one.
"""
from subprocess import Popen
import sys

def process_each(command):
    for line in sys.stdin:
        line = line.strip()
        com = command.replace('@FILE', line, 100)

        p = Popen(com, shell=True)
        p.wait()


def main():
    process_each(sys.argv[1])


if __name__=="__main__":
    main()
