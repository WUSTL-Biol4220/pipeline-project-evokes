#!/bin/bash

INPUTDIR=$1
cwd=$(pwd)
cd ..
parentwd=$(pwd)
OUTDIRNAME=$2
mkdir $OUTDIRNAME
ref=$3
refstring="$(echo ${ref})"
for file in $(ls ${INPUTDIR}/*.txt)
do
  testname=""
  testname="$(echo ${file})"
  cd ${parentwd}
  if [ $refstring != $testname ]
  then
    name=""
    name="$(echo ${testname} | rev | cut -f1 -d '/' | rev)"
    id="$(echo ${name} | cut -f1 -d '.')"
    infilename=""
    infilename="${INPUTDIR}/${name}"
    outfilename=""
    outfilename="${parentwd}/${OUTDIRNAME}/shifted_${id}.txt"
    cd ${cwd}
    python3 corrshift.py --ref "${refstring}" --infile "${infilename}" --outfile "${outfilename}"
  fi
done
