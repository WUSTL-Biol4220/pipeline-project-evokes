#!/usr/bin/python

import argparse
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("--ref", help="ref file of WYK encoded sequences in string")
parser.add_argument("--infile", help="input file 1 of WYK encoded sequences in string")

args = parser.parse_args()

ref = np.loadtxt(args.ref)
x1 = np.loadtxt(args.infile)

c12 = signal.correlate(ref, x1, mode='full', method='auto')

c12s2=c12[2::3]
#print(c12s2)
plt.plot(c12s2)
plt.show()

cmax = np.amax(c12s2)
#print(cmax)

#print(c12s2.argmax())

shift = c12s2.argmax() - (len(ref) /3) + 1
#print(shift)
print(shift * 3)
