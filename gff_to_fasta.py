#!/usr/bin/python
"""
"""

__author__ = 'rensholmer'

import sys
import gff_toolkit as gt

def splitter(string,n):
	while string:
		yield string[:n]
		string = string[n:]

def main(gff_file,fasta_file):
	gff = gt.parser(gff_file,fasta_file=fasta_file)
	cds_file = '{0}.CDS.fasta'.format(gff_file)
	pep_file = '{0}.PEP.fasta'.format(gff_file)
	transcripts = gff.getitems(featuretype='mRNA')
	sorted_transcripts = sorted(transcripts, key = lambda t: t.ID)
	with open(cds_file,'w') as cds_handle, open(pep_file,'w') as pep_handle:
		for transcript in sorted_transcripts:
			if len(transcript.seq) == 0:
				continue
			name = transcript.attributes.get('Name',[''])[0]
			header = '>{0} {1}\n'.format(transcript.ID, name)

			seq = splitter(transcript.seq,60)
			pep = splitter(transcript.pep,60)
			cds_handle.write(header)
			for s in seq:
				cds_handle.write(s+'\n')
			pep_handle.write(header)
			for p in pep:
				pep_handle.write(p+'\n')
if __name__ == '__main__':
	if len(sys.argv) == 3:
		main(*sys.argv[1:])
	else:
		print 'Usage: python {0} <annotation gff> <genome fasta file>'.format(sys.argv[0])
