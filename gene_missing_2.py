#!/usr/bin/env python
"""
"""

import sys
import gff_toolkit as gt


def main(gff_file, namemap):
	gff = gt.parser(gff_file = gff_file)
	with open('namemap.tsv','r') as namemap:
		genes = gff.getitems(featuretype = 'gene')
		sorted_genes = sorted(genes, key = lambda sub: sub.get_start())
		genefind = namemap.read() 
		for gene in sorted_genes:
			number = genefind.find(gene.ID) 
			print "%s : %s " % (gene.ID, number) 			
				
if __name__ == '__main__':
	if len(sys.argv) == 3:
		main(*sys.argv[1:])
	else:
		print 'Usage: python {0} <annotation gff> <namemap>'.format(sys.argv[0])
