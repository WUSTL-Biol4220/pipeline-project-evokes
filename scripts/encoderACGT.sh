#!/bin/bash

INPUTFILE=$1
cwd=$(pwd)
cd ..
parentwd=$(pwd)
OUTDIRNAME=$2
mkdir $OUTDIRNAME
NUMBER=$3
outfilename="${parentwd}/${OUTDIRNAME}/acgt.csv"

cd ${cwd}

python3 encodeACGT.py --infile "${INPUTFILE}" --number "${NUMBER}" --outfile "${outfilename}"
