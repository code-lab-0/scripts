#!/usr/bin/env python

import getopt
import subprocess
import sys
import time

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hn:", ["help","name="])
        take_stats(opts, args)
    except getopt.GetoptError:
        usage()
        sys.exit(2)


def take_stats(opts, args):
    print opts
    print args

    name = "xxx"

    for o,a in opts:
        if o == "--name" or "-n":
            name = a



    p0 = subprocess.Popen("mpstat -P ALL 10 > mpstat." + name + ".out", shell=True)
    p1 = subprocess.Popen(args)
    p2 = subprocess.Popen("pidstat -urdh -t -p " + str(p1.pid) + " 10 > pidstat." + name + ".out", shell=True)
    p1.wait()
    time.sleep(10)
    p0.kill()
    p2.kill()


if __name__=="__main__":
    main(sys.argv[1:])
