#!/usr/bin/env python


import subprocess
import sys
import time

def main():
    print sys.argv[1:]
    p0 = subprocess.Popen("mpstat -P ALL 10 > mpstat.out", shell=True)
    p1 = subprocess.Popen(sys.argv[1:])
    p2 = subprocess.Popen("pidstat -urdh -t -p " + str(p1.pid) + " 10 > pidstat.out", shell=True)
    p1.wait()
    time.sleep(10)
    p0.kill()
    p2.kill()


if __name__=="__main__":
    main()
