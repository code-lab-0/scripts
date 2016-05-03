#!/usr/bin/env python3

import numpy.random
import re
from subprocess import check_output,Popen,PIPE
import time

def main():
    while 1:
        submit_jobs("qsub -cwd -N probeS -b y \"sleep 13\"", 8.0, "probeS") # many small jobs.
        submit_jobs("qsub -cwd -N probeMPI -pe mpi 10 -b y \"sleep 23\"", 1.0, "probeMPI") # parallel jobs.
        time.sleep(5)

def submit_jobs(cmd, poisson_lambda, desc):

    r = re.compile(r'Your job ([0-9]+)')
    
    num = numpy.random.poisson(poisson_lambda, 1)
    for i in range(1,num[0]):
        result = check_output(cmd, shell=True)
        result = result.decode("utf-8")
        print(result)

        m = r.search(result)
        if m != None:
            jobID = m.group(1)
            print(jobID)
    



if __name__=="__main__":
    main()
