#!/usr/bin/python

import argparse
from itertools import zip_longest

parser = argparse.ArgumentParser()
parser.add_argument("--infile1", help="input file 1 of reference or shifted WYK encoded sequences in string")
parser.add_argument("--infile2", help="input file 2 of shifted WYK encoded sequences in string")
parser.add_argument("--isref", help="type true or false if input file 1 is a reference sequence")
parser.add_argument("--position", help="position of shifted infile 2 where ref seq is added to infile 2")
parser.add_argument("--outfile", help="outfile name (preferably mentions sum) in string")
args = parser.parse_args()

file1 = []
with open(args.infile1) as f1:
    file1 = [line.strip() for line in f1]
file1int = list(map(int, file1))

file1len = len(file1int)
    
file2 = []
with open(args.infile2) as f2:
    file2 = [line.strip() for line in f2] 
file2int = list(map(int, file2))

finalList = []
if args.isref == "true":
    position = int(args.position)
    slicedfile2 = file2int[position : position + file1len ]
    sumseq = [x+y for x,y in zip_longest(file1int, slicedfile2, fillvalue=0)]
    finalList = file2int
    finalList[position : position + file1len] = sumseq
elif args.isref == "false":
    finalList = [x+y for x,y in zip_longest(file1int, file2int, fillvalue=0)]

with open(args.outfile, "a") as f:
    for x in finalList:
        f.write(str(x) + "\n")

