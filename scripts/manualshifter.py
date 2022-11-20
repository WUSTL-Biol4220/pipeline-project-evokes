#!/usr/bin/python

import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--infile", help="input file of WYK encoded sequences in string/.txt extensions")
parser.add_argument("--shiftright", help="true if shift right (shift is +), false if shift left (-)")
parser.add_argument("--number", help="number of zeroes to add")
parser.add_argument("--outfile", help="outfile name (preferably mentions sequence) in string with a .txt extension")
args = parser.parse_args()

numberint = int(args.number)
shiftdir = True
if (args.shiftright == "true"): 
    shiftdir = True
elif (args.shiftright == "false"):
    shiftdir = False

seq = []
with open(args.infile) as f1:
    seq = [line.strip() for line in f1]
seqint = list(map(int, seq))

if shiftdir:
    for x in range(numberint):
        seqint.insert(0,0)
        seqint.pop()
else :
    for x in range(numberint):
        seqint.append(0)
        seqint.pop(0)
        
with open(args.outfile, "a") as f:
    for x in seqint:
        f.write(str(x) + "\n")

