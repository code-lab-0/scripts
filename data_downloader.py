#!/usr/bin/python3
# coding: UTF-8

from datetime import date
import getopt
import json
import multiprocessing
import os
import subprocess
import sys
import time

"""
Usage:
    python3 data_downloader.py download_conf.json

Example of the download_conf.json:

[
{"name": "db-name",
 "base_dir": "/home/oogasawa/data2",
 "urls": [
    "wget http://examples.com",
    "wget https://www.ogalab.net"],
"download_type": "overwrite"},
{"name": "db-name2",
 "base_dir": "/home/oogasawa/data2",
 "urls": [
    "wget http://examples.com",
    "wget https://www.ogalab.net"],
"download_type": "snapshot"}

]
"""


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "h", ["help"])
        data_download(opts, args)
    except getopt.GetoptError:
        usage()
        sys.exit(2)



def data_download(opts, args):
    jobs = []
    for json_file in args:
        j = json.loads(open(json_file, "r").read())
        for item in j:
            print(item)
            p = multiprocessing.Process(target=download, args=(item,))
            jobs.append(p)
            p.start()
            
    for job in jobs:
        job.join()



def download(item):

    os.chdir(item["base_dir"])

    if item["download_type"] == "snapshot":
        dir_name = make_snapshot_dir(item)
    elif item["download_type"] == "overwrite":
        dir_name = make_overwritten_dir(item)

    os.chdir(dir_name)

    for u in item['urls']:
        print(u)
        p0 = subprocess.Popen(u, shell=True)
        p0.wait()


def make_snapshot_dir(item):
    t = date.today()
    t0 = t.isoformat()

    dir_name = item["name"] + "/download/" + t0
    os.makedirs(dir_name, exist_ok=True)

    os.chdir(item["name"])
    p0 = subprocess.Popen("rm -f current", shell=True)
    p0.wait()
    dir_name = "download/" + t0    
    p0 = subprocess.Popen("ln -s " + dir_name + " current", shell=True)
    p0.wait()
    os.chdir("..")

    return dir_name


def make_overwritten_dir(item):
    dir_name = item["name"] + "/download"
    os.makedirs(dir_name, exist_ok=True)
    return dir_name



if __name__ == "__main__":
    main(sys.argv[1:])

