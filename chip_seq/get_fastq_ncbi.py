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
            run_accession = header.index("run_accession")
            sra_ftp = header.index("sra_ftp")
            print("fastq_ftp index located in column {}".format(sra_ftp))

        else:
            sra = lis[run_accession]

            loc = "/sra/sra-instant/reads/ByRun/sra/{}/{}/{}/{}.sra".format(sra[0:3],sra[0:6],sra,sra)
            wget_loc = "ftp://ftp-trace.ncbi.nih.gov" + loc
            ascp_loc = "anonftp@ftp.ncbi.nlm.nih.gov:" + loc
            ascp_rsa = "/root/.aspera/connect/etc/asperaweb_id_dsa.openssh"

            #subprocess.run(["wget", "--continue", "--progress=bar", wget_loc])
            ascp_cmd = ["ascp", "-T", "-k", "1", "-l","100m","-i",ascp_rsa,ascp_loc,"."]
            fastq_dump_cmd = ["fastq-dump","--gzip","-I","--split-files","./"+sra+".sra"]
            print("downloading sra file {}".format(sra))
            subprocess.run(ascp_cmd)
            print("Converting sra file {} to fastq.gz".format(sra))
            subprocess.run(fastq_dump_cmd)
