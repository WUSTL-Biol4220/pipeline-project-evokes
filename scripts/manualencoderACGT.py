#!/usr/bin/python

import argparse
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


parser = argparse.ArgumentParser()
parser.add_argument("--infile", help="input file of reference total sum WYK encoded sequences in string")
parser.add_argument("--number", help="number of files used to generate the reference total sum from previous steps")
parser.add_argument("--outfile", help="outfile name (preferably mentions ACGT) in string with a .csv extension")
args = parser.parse_args()

numberint = int(args.number)


sumfinal = []
with open(args.infile) as f1:
    sumfinal = [line.strip() for line in f1]
sumint = list(map(int, sumfinal))



squaredint = [x ** 2 for x in sumint]
plt.plot(squaredint)
plt.show()



relsqint = [x / numberint for x in squaredint]
plt.plot(relsqint)
plt.show()


divided = []
for i in range(len(sumint)):
  divided.append((sumint[i] / numberint))
plt.plot(divided)
plt.show()

npthree = np.array_split(divided, len(divided)/3)
npfour = np.append(npthree, np.ones([len(npthree),1]),1)

converter = np.array([[1, -1, -1, 1],
                     [-1, 1, -1, 1],
                     [-1, -1, 1, 1],
                     [1, 1, 1, 1]])

results = np.dot(npfour, converter)
results = results.round(decimals = 2)
resultsf = results/4
resultsf = resultsf.round(decimals = 2)

df = pd.DataFrame(data=resultsf.astype(float))
dfnew = pd.DataFrame([['A', 'C', 'G', 'T']])
dfinal = pd.concat([dfnew, df])
dfinal.to_csv(args.outfile, sep='\t', header=False, float_format='%.2f', index=False)


