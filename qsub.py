#!/usr/bin/env python3


__doc__ = """{f}

Usage:
    {f} [-q | --qsubopts <qsub_options>] <command>
    {f} -h | --help

Options:
    -q --qsubopts <qsub_options>  Set qsub options 
    -h --help                     Show this screen and exit.
""".format(f=__file__)

from docopt import docopt


def parse():
    args = docopt(__doc__)
    return args




from subprocess import Popen
import hashlib

def qsub(args):
    com = args['<command>']
    md5 = hashlib.md5(com.encode('utf-8')).hexdigest()
    fname = "qsub_" + str(md5)[0:15] + ".sh"

    fout = open(fname, "w")
    fout.write(com + "\n")
    fout.close()

    if len(args['--qsubopts']) == 0:
        com = "qsub -cwd -V -l short -S /bin/bash " + fname
    else:
        com = "qsub -cwd -V " + " ".join(args['--qsubopts']) + " -S /bin/bash " + fname

    print(com)
    p = Popen(com, shell=True)
    p.wait()



def main(args):
    qsub(args)


if __name__=="__main__":
    result = parse()
    main(result)
