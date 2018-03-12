# index-after-Braker
this pipeline will re-index annotation produced by Braker.
It includes adjusted python scripts that are eveloped by Rens Homler.
The scripts will print new gff3 annotation including 'gene','mRNA' and 'CDS' feature with the replaced ID name according to your input.
Reminder：the scripts can only run under python2.x version. Before running, make sure the sequence IDs from fasta and gff file are identical.


process_braker_gff.py: change the ID of all gff feature type according to your input

process_braker_gff_limited:will only generate a annotation with 'gene', 'mRNA' and 'CDS' feature types

process_braker_gff_all_transcript: generate a annotation including all transcript from one gene.

gene_missing_1.py and gene_missing_2.py: sometime, the script could skip genes that are too short. By running these two scripts orderly, you can find the missing genes ID labelled as -1 in the output file of gene_missing_2.py.
