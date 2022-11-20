#!/bin/bash

INPUTDIR=$1
cwd=$(pwd)
cd ..
parentwd=$(pwd)
mkdir wyk

for file in $(ls ${INPUTDIR}/*.fasta)
do
  testname=""
  testname="$(echo ${file})"
  name=""
  name="$(echo ${testname} | rev | cut -f1 -d '/' | rev)"
  infilename=""
  infilename="${INPUTDIR}/${name}"
  outfilename=""
  outfilename="${parentwd}/wyk/wyk_${name}"
  cd ${cwd}
  python3 encodeWYK.py --infile "${infilename}" --outfile "${outfilename}"
done
