#!/bin/bash

INPUTDIR=$1
cwd=$(pwd)
cd ..
parentwd=$(pwd)
OUTDIRNAME=$2
mkdir $OUTDIRNAME
ref=$3
refstring="$(echo ${ref})"
ref2=$4
ref2string="$(echo ${ref2})"

outfilefirst="${parentwd}/${OUTDIRNAME}/sum1.txt"
cd ${cwd}
python3 sumcreator.py --infile1 "${refstring}" --infile2 "${ref2string}" --outfile "${outfilefirst}"
cd ${parentwd}

i=1
for file in $(ls ${INPUTDIR}/*.txt)
do
  testname=""
  testname="$(echo ${file})"
  cd ${parentwd}
  if [[ $refstring != $testname && $ref2string != $testname ]]
  then
    name=""
    name="$(echo ${testname} | rev | cut -f1 -d '/' | rev)"
    id="$(echo ${name} | cut -f1 -d '.')"
    infile1name=""
    infile1name="${parentwd}/${OUTDIRNAME}/sum${i}.txt"
    infile2name=""
    infile2name="${INPUTDIR}/${name}"
    i=$((${i}+1))
    outfilename=""
    outfilename="${parentwd}/${OUTDIRNAME}/sum${i}.txt"
    cd ${cwd}
    python3 sumcreator.py --infile1 "${infile1name}" --infile2 "${infile2name}" --outfile "${outfilename}"
  fi
done
