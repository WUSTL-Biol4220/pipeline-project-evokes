The `scripts` directory contains the following scripts:
- `run_job.sh` is the entry point for the pipeline, and handles initial input handling and error checking
- `build_align.sh` generates multiple sequence alignments using MAFFT, MUSCLE, and PRANK
- `build_phylo.sh` generates molecular phylogenies from an alignment using FastTree and IQ-Tree (MLE and MP)
