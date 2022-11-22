The `output` directory contains the results from the various pipeline analyses. The name of the subdirectory signifies not only what data set the output is from but what are the specific intermediate or final steps from which the contents of the subdirectory has.

## Data Set Tags
- `dummy` represents the dummy data output.
- `ecoli` represents the ecoli data output.
- `ecoli_bad` represents the ecoli_bad data output.
- `ecoli_good` represents the ecoli_good data output.
- `ecoli_hardshift` represents the ecoli data where all genes except for `ecoblgr1.fasta` were hardshifted using `manualshifter.py` from hand-counted values explained in the presentation. Files that correspond to here correspond to what the ideal `ecoli` output should have been but could not due to the algorithm of selecting the right shift being a work in progress.
- `ecoli_okay` represents the ecoli_okay data output.
- `test1` represents the test1 data output.
- `test2` represents the test2 data output.
- `test3` represents the test3 data output.

## Pipeline Content Tags
- `acgt` represents the **FINAL** output. In these subdirectories contain an `acgt.csv` file that is used to input into a DNA energy normalized logo generator to visualize output. This .csv file is the nucleotide probability document and comes from executing `encoderACGT.sh`.
- `wyk` represents the *wyk* encoded output. These subdirectories contain *.txt* files with the information of the *.fasta* file from which it was generated that have encoded nucleotides into *wyk* format. These were a result of executing `encoderWYK.sh`.
- `shift_wyk` represents *wyk* output that were shifted to a reference which was user-inputted. These were results obtained from executing `shifter.sh`.
- `sums` represents directories that contain different *.txt* files labeled from sum1 and onwards depending upon the amount of files assessed. The important file in these subdirectories are `sumN.txt` where N = the largest number in the subdirectory, and this file is used for further analysis. N + 1 represents the total number of sequences in this analysis/run of the pipeline. These were generated from `summer.sh`.
