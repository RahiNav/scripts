#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#The script parses a fasta file and finds the N glycosylation motif(s) in the protein sequence using the biopython package.
#The output file produces UniProtKB accession, matched motif and the starting position of the matched motif
#The script works on fasta file(s) downloaded from UniProtKB. e.g. input file: https://www.uniprot.org/uniprot/P04278.fasta



"""
Created on Thu May 27 13:05:55 2021

@author: rahinavelkar
"""
import re

infile = "/Users/rahinavelkar/Desktop/scripts/P04278.fasta"
outfile = "/Users/rahinavelkar/Desktop/scripts/N-Motifs_biopython.txt"

fasta = {}

from Bio import SeqIO
for seq_record in SeqIO.parse(infile, "fasta"):
    fasta[seq_record.id] = seq_record.seq

for name,seq in fasta.items():
    pattern = re.finditer('N\wS|N\wT', str(seq))
    for i in pattern:
        if i.group() != 'NPT' and i.group() != 'NPS':
            motif = i.group()
            motif_start_pos = i.start()+1
            sourceFile = open(outfile,'a')
            print(name, motif, motif_start_pos, file=sourceFile)
            sourceFile.close()
            
            
print('Done')            