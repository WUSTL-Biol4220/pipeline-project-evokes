The `data` directory contains the following subdirectories:
- `dummy` contains man-made sequences that mimic the experimental *E.coli* data set in terms of the motif, as *fasta* files for a cumulative dummy data set. The four sequences in this data set have the same motif but all other nucleotides are different from one another (e.g. dummy1.fasta only has the motif and the rest are A's, dummy2.fasta has the motif and the rest are C's etc.)
- `ecoli` contains seven *E.coli* genes, each as separate *fasta* files. This is the core data set used for the pipeline as well as practical, biological implications.
- `ecoli_bad` contains three *E.coli* genes, each as separate *fasta* files that were used to represent the little to no consensus in the presentation.
- `ecoli_good` contains three *E.coli* genes, each as separate *fasta* files that were used to represent the good consensus in the presentation.
- `ecoli_okay` contains three *E.coli* genes, each as separate *fasta* files that were used to represent the close consensus in the presentation.
- `test1` contains two *fasta* files used to represent the first test of the pipeline (if it can align only the motif region and everything else is different).
- `test2` contains two *fasta* files used to represent the second test of the pipeline (what if the data has no similarities).
- `test3` containst two *fasta* files used to represent the third test of the pipeline (what if the data is entirely the same between two sequences).
