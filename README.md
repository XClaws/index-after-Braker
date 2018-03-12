# index-after-Braker
this is a pipeline to re-index annotation produced by Braker including adjusted python scripts developed by Rens Homler.
the original script can only run under python2.x which will produce a new gff3 annotation including 'gene','mRNA' and 'CDS' gene with the new replaced ID name according to your input.

process_braker_gff.py: change the ID of all gff feature type according to your input

process_braker_gff_limited:will only generate a annotation with 'gene', 'mRNA' and 'CDS' feature types

process_braker_gff_all_transcript: generate a annotation including all transcript from one gene.

gene_missing_1.py and gene_missing_2.py: sometime, the script could skip genes that are too short. By running these two scripts orderly, you can find the missing genes ID labelled as -1 in the output file of gene_missing_2.py.
