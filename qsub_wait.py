
import os
import sys
import subprocess
import time

def main():
    job_id = sys.argv[1]
    while True:
        if not is_running(job_id):
            break
        else:
            time.sleep(60)


def is_running(job_id):

    qstat = subprocess.check_output(["qstat", "-j " + str(job_id)], shell=True)
    if qstat.startswith("Following jobs do not exists"):
        return True
    else:
        return False




if __name__=="__main__":
    main()
