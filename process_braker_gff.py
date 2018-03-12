#!/usr/bin/env python
"""
"""

import sys
import gff_toolkit as gt

def format_id(prefix, counter, max_padding = 5):
	counter_string = str(counter)
	padding = '0' * (max_padding + 1 - len(counter_string))
	return prefix + padding + counter_string + '0'



def main(gff_file, fasta_file, prefix, min_len = 50):
	gff = gt.parser(gff_file = gff_file, fasta_file = fasta_file)
	scaffolds = sorted(gff.seq.items(), key = lambda x: len(x[1]), reverse = True)
	gene_counter = 0
	for seqid,seq in scaffolds:
		genes = gff.getitems(featuretype = 'gene', seqid = seqid)
		sorted_genes = sorted(genes, key = lambda sub: sub.get_start())
		for gene in sorted_genes:
			transcript = list(gff.get_children(gene, featuretype = 'mRNA'))[0]
			if len(transcript.pep) < min_len:
				continue
			gene_counter += 1
			gene_id = format_id(prefix, gene_counter)
			gene.ID = gene_id
			gene.source = 'BRAKER'
			print '\t'.join(gene.gff_fields)
			transcript_id = '{0}.1'.format(gene_id)
			transcript.ID = transcript_id
			transcript.parents = [gene_id]
			transcript.source = 'BRAKER'
			print '\t'.join(transcript.gff_fields)
			cds_counter = 0
			for cds in gff.get_children(transcript, featuretype = 'CDS'):
				cds_counter += 1
				cds_id = '{0}.CDS{1}'.format(gene_id, cds_counter)
				cds.ID = cds_id
				cds.source = 'BRAKER'
				cds.parents = [transcript_id]
				print '\t'.join(cds.gff_fields)

if __name__ == '__main__':
	if len(sys.argv) == 4:
		main(*sys.argv[1:])
	else:
		print 'Usage: python {0} <annotation gff> <genome fasta file> <prefix>'.format(sys.argv[0])