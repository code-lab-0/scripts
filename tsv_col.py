#!/usr/bin/env python3

import re
import sys

def main():

    p = re.compile(r'\t')

    for line in sys.stdin:
        line = line.strip()
        col = p.split(line)
        c = join_columns(col, sys.argv[1])
        if c != None:
            print(c)

def join_columns(col, ns):
    
    result = []
    s = ns.split(",")
    for c in s:
        if len(col) > int(c):
            result.append(col[int(c)])


    if len(s) == len(result):
        return "\t".join(result)
    else:
        return None


if __name__=="__main__":
    main()
