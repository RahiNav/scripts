#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 18:20:54 2021

@author: rahinavelkar
"""

#The script take single or multiple fasta sequences and prints the desired amino acid and the respective position in the fasta sequence
# To match a single position add aa = 'S', for multiple amino acid residues use aa = 'S|T|K'
#generates a space seperated file with accession, matched amino acid, position of the matched amino acid
# Uses Biopython module.

import re

infile = "/Users/rahinavelkar/Desktop/scripts/input.fasta"
outfile = "/Users/rahinavelkar/Desktop/scripts/get_aa_pos_biopython.txt"
amino_acid = []
pos = []
fasta = {}
aa = 'K|T|S'  


from Bio import SeqIO
for seq_record in SeqIO.parse(infile, "fasta"):
    fasta[seq_record.id] = seq_record.seq

for name,seq in fasta.items():
    pattern = re.finditer(aa, str(seq))
    for i in pattern:
        match_location = i.start() + 1
        pos.append(str(match_location))
        match_amino_acid = i.group()
        amino_acid.append(match_amino_acid)
    sourceFile = open(outfile,'a')    
    print(name, ("|").join(amino_acid), ("|").join(pos), file=sourceFile)
    sourceFile.close()
    
print('Done')    
