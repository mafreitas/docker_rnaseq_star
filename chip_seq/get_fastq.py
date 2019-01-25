#!/usr/bin/env python

import csv
import sys
import subprocess

print (sys.argv)

first_line = True
with open(sys.argv[1]) as f:
    for line in f:
        lis = line.split("\t")       # create a list of lists
        if first_line:
            header = lis
            first_line = False
            print("Header Found")
            fastq_index = header.index("fastq_ftp")
            print("fastq_ftp index located in column {}".format(fastq_index))

        else:
            print(lis[fastq_index])
            subprocess.run(["wget", "--continue", "--progress=bar", lis[fastq_index]])
