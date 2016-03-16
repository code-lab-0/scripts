#!/usr/bin/env python

"""
process each files one by one.
"""
from subprocess import Popen
import sys

def process_each(args):
    for line in sys.stdin:
        line = line.strip()
        com = args.command[0].replace('@FILE', line, 100)

        if args.test or args.verbose:
            print(com)

        if not args.test:
            p = Popen(com, shell=True)
            p.wait()

#-----------------

import argparse
def getargs():
    parser = argparse.ArgumentParser(description='Process each line one by one.')

    parser.add_argument('--doctest',
                        action='store_true',
                        default=False,
                        help='doctest if this flag is set (default: False)')

    parser.add_argument('--verbose',
                        action='store_true',
                        default=False,
                        help='print each command')

    parser.add_argument('--test',
                        action='store_true',
                        default=False,
                        help='Test only. Do not run commands.')


    parser.add_argument('command',
                        action='store',
                        nargs=1,
                        const=None,
                        default="ls -l ",
                        type=str,
                        choices=None,
                        help='A command that processes each file.',
                        metavar=None)


    args = parser.parse_args()
    return args


def main():
    args = getargs()
    if args.doctest == True:
        import doctest
        doctest.testmod()
    else:
        print(args)
        process_each(args)


if __name__=="__main__":
    main()
