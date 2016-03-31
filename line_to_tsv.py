#!/usr/bin/env python3

import re
import sys


def main():
    line_to_tsv()


def line_to_tsv():
    p = re.compile(r'\s+')
    for line in sys.stdin:
        line = line.strip()
        col = p.split(line)
        print("\t".join(col))


if __name__=="__main__":
    main()
