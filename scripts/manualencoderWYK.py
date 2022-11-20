#!/usr/bin/python

from Bio import SeqIO
import argparse
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("--infile", help="input file of sequences in fasta format")
parser.add_argument("--outfile", help="output file in WYK encoding, a string of  1 and -1 ")
args = parser.parse_args()

enc = []
for seq_record in SeqIO.parse(args.infile, "fasta"):
    lseq = len(seq_record)
    seq = seq_record.seq
    for i in range(lseq):
        if seq[i] == "A":
            enc = enc + [1, -1, -1]
        elif seq[i] == "C":
            enc = enc + [-1, 1, -1]
        elif seq[i] == "G":
            enc = enc + [-1, -1, 1]
        elif seq[i] == "T":
            enc = enc + [1, 1, 1]

plt.plot(enc)

np.savetxt(args.outfile,enc,fmt='%i')

