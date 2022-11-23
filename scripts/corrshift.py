#!/usr/bin/python

import argparse
import numpy as np
from scipy import signal

parser = argparse.ArgumentParser()
parser.add_argument("--ref", help="ref file of WYK encoded sequences in string")
parser.add_argument("--infile", help="input file of WYK encoded sequences in string")
parser.add_argument("--outfile", help="outfile name (preferably mentions sequence) in string with a .txt extension")
args = parser.parse_args()

ref = np.loadtxt(args.ref)
x1 = np.loadtxt(args.infile)

c12 = signal.correlate(ref, x1, mode='full', method='auto')

c12s2=c12[2::3]

cmax = np.amax(c12s2)

shift = c12s2.argmax() - (len(ref) /3) + 1
wykshift = shift * 3

shiftdir = True
if (wykshift >= 0):
    shiftdir = True
elif (wykshift < 0):
    shiftdir = False

abswykshift = int(abs(wykshift))

seq = []
with open(args.infile) as f1:
    seq = [line.strip() for line in f1]
seqint = list(map(int, seq))

if shiftdir:
    for x in range(abswykshift):
        seqint.insert(0,0)
        seqint.pop()
else :
    for x in range(abswykshift):
        seqint.append(0)
        seqint.pop(0)
        
with open(args.outfile, "a") as f:
    for x in seqint:
        f.write(str(x) + "\n")
