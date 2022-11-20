#!/bin/bash

INPUTDIR=$1
cwd=$(pwd)
cd ..
parentwd=$(pwd)
OUTDIRNAME=$2
mkdir $OUTDIRNAME

for file in $(ls ${INPUTDIR}/*.fasta)
do
  testname=""
  testname="$(echo ${file})"
  name=""
  name="$(echo ${testname} | rev | cut -f1 -d '/' | rev)"
  id="$(echo ${name} | cut -f1 -d '.')"
  infilename=""
  infilename="${INPUTDIR}/${name}"
  outfilename=""
  outfilename="${parentwd}/${OUTDIRNAME}/wyk_${id}.txt"
  cd ${cwd}
  python3 encodeWYK.py --infile "${infilename}" --outfile "${outfilename}"
done
