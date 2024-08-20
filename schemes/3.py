#!/usr/bin/env python
import math
import sys
import csv
from schemes import *
import os
DATASIZEUNIT = 8000*1000 # Megabytes
DATASIZERANGE = range (1,60,6)
def writeCSV(path ,d):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path , mode="w") as outfile:
        writer = csv.writer(outfile , delimiter=',')
        for x in d:
            writer.writerow ([x,d[x]])
# Writes the graphs for a given scheme
# into a csv file
def writeScheme(name ,makeScheme):
    commitment = {}
    commpq = {}
    commtotal = {}
    encoding = {}
    for s in DATASIZERANGE:
        datasize = s*DATASIZEUNIT
        scheme = makeScheme(datasize)
        commitment[s] = scheme["comsize"]/8000000
        commpq[s] =scheme["commpqsize"]/8000
        commtotal[s] = scheme["samples"]* scheme["commpqsize"]/8000000
        encoding[s] = (scheme["encodinglength"]* scheme["encodingsymbolsize"]) /8000000000
    writeCSV("./data/"+name+"_com.csv",commitment)
    writeCSV("./data/"+name+"_comm_pq.csv",commpq)
    writeCSV("./data/"+name+"_comm_total.csv",commtotal)
    writeCSV("./data/"+name+"_encoding.csv",encoding)
############################################
writeScheme("rs",makeKZGScheme)
writeScheme("tensor",makeTensorScheme)
writeScheme("hash",makeHashBasedScheme)
writeScheme("homhash",makeHomHashBasedScheme)