#!/usr/bin/env python3

"""
qsub.py --command="gunzip your_file.seq.gz"
"""

from subprocess import Popen
import hashlib

def qsub(args):
    com = " ".join(args.command)
    md5 = hashlib.md5(com.encode('utf-8')).hexdigest()
    fname = "qsub_" + str(md5)[0:15] + ".sh"
    print(fname)

    fout = open(fname, "w")
    fout.write(com + "\n")
    fout.close()

    if args.sge_options == None:
        com = "qsub -cwd -V -S /bin/bash " + fname
    else:
        com = "qsub -cwd -V " + args.sge_options + " -S /bin/bash " + fname

    print(com)
    p = Popen(com, shell=True)
    p.wait()


#-----------------

import argparse
def getargs():
    parser = argparse.ArgumentParser(description='Return factorial of a given argument n.')

    parser.add_argument('--doctest',
                        action='store_true',
                        default=False,
                        help='doctest if this flag is set (default: False)')

    parser.add_argument('command',
                        action='store',
                        nargs='+',
                        const=None,
                        default=None,
                        type=str,
                        choices=None,
                        help='A data file name.',
                        metavar=None)

    parser.add_argument('-o', '--sge-options',
                        action='store',
                        nargs='?',
                        const=None,
                        default=None,
                        type=str,
                        choices=None,
                        help='qsub options',
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
        qsub(args)


if __name__=="__main__":
    main()
