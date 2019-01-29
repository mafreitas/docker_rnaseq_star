#!/usr/bin/env python

import csv
import sys
import subprocess
import pandas as pd
import os 
import multiprocessing as mp

THREADS = 8

# for index, row in data.iterrows():
    
#     sra = row['run_accession']

#     exists = os.path.isfile("./"+sra+".conversion_complete")
#     if exists:
#         print("Skipping previously converted sra file {}".format(sra))
#     else:
#         try:
#             fastq_dump_cmd = ["fastq-dump","--gzip","-I","--split-files","./"+sra+".sra"]
#             print("Converting sra file {} to fastq.gz".format(sra))   
#             subprocess.run(fastq_dump_cmd)  
#             touch("./"+sra+".conversion_complete")
#         except:
#             continue

def run_sra(sra): 

    print("downloading sra file {}".format(sra))
    loc = "/sra/sra-instant/reads/ByRun/sra/{}/{}/{}/{}.sra".format(sra[0:3],sra[0:6],sra,sra)
    wget_loc = "ftp://ftp-trace.ncbi.nih.gov" + loc
    ascp_loc = "anonftp@ftp.ncbi.nlm.nih.gov:" + loc
    ascp_rsa = "/root/.aspera/connect/etc/asperaweb_id_dsa.openssh"
    ascp_cmd = ["ascp", "-T", "-k", "1", "-l","50m","-i",ascp_rsa,ascp_loc,"."]
    subprocess.run(ascp_cmd)

def safe_run_sra(*args, **kwargs):
    """Call run(), catch exceptions."""
    try: run_sra(*args, **kwargs)
    except Exception as e:
        print("error: %s run(*%r, **%r)" % (e, args, kwargs))

def run_fastq_dump(sra): 
    print("Converting sra file {} to fastq".format(sra))   
    fastq_dump_cmd = ["fasterq-dump","./"+sra+".sra"]
    subprocess.run(fastq_dump_cmd)  

def safe_run_fastq_dump(*args, **kwargs):
    """Call run(), catch exceptions."""
    try: run_fastq_dump(*args, **kwargs)
    except Exception as e:
        print("error: %s run(*%r, **%r)" % (e, args, kwargs))

def main():
    df= pd.read_csv(sys.argv[1],sep='\t', header=0)
    # Preview the first 5 lines of the loaded data 
    print(df.head())
    sra = df["run_accession"].tolist()

    # start processes
    pool = mp.Pool(THREADS) # use all available CPUs
    pool.map(safe_run_sra, sra)
    pool.map(safe_run_fastq_dump, sra)

if __name__=="__main__":
    mp.freeze_support() # optional if the program is not frozen
    main()