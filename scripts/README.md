The `scripts` directory contains the following scripts. All files that do not have `manual` in their name are scripts used in the pipeline:
## *WYK* Encoding
- `encoderWYK.sh` is the entry point for the pipeline, and handles encoding of *.fasta* files.
- `encodeWYK.py` is the corresponding *.py* file for `encoderWYK.sh`.
- `manualencoderWYK.py` is a file not used in the pipeline and has similar content to `encodeWYK.py` but this is used for troubleshooting and user-changes through python as it contains code to plot the WYK file and will not affect the rest of the pipeline if manipulated.
## Sliding Score Generation and Shifting Sequences
- `shifter.sh` shifts *wyk* files from `encoderWYK.sh` based upon a sliding score algorithm.
- `corrshift.py` is the *.py* file for `shifter.sh`.
- `manualscorer.py` is the file used to generate and visualize the sliding scores separately from the pipeline.
- `manualshifter.py` is the file used to shift sequences separately from the pipeline.
## Summation
- `summer.sh` is used to sum the *wyk* files in a directory.
- `sumcreator.py` is the corresponding *.py* file for `summer.sh`.
- `manualsummer.py` is used to visualize and troubleshoot the summation of the sequences for this step.
## Nucleotide Probability Matrix (ACGT) Encoding
- `encoderACGT.sh` is the file that converts a file with the total summed *wyk* files in this pipeline into a nucleotide probability matrix.
- `encodeACGT.py` is the corresponding *.py* file used for `encoderACGT.sh`.
- `manualencoderACGT.py` is the file used for manual troubleshooting and visualizing of this step.
