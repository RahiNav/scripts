#The script parses a fasta file and finds the N glycosylation motif(s) in the protein sequence.
#The output file produces UniProtKB accession, matched motif and the starting position of the matched motif

import re


fasta_file = '/Users/rahinavelkar/Desktop/scripts/input.fasta'
outfile = '/Users/rahinavelkar/Desktop/scripts/N_motifs.txt'


fh=open(fasta_file)

fasta={}
counter=0

for line in fh:
    line=line.rstrip()
    if line[0]=='>':
        words=line.split()
        name=words[0][4:]
        fasta[name]=''
    else:
        fasta[name]= fasta[name]+line


for name,seq in fasta.items():
    motif = re.finditer('N\wS|N\wT', seq)
    for i in motif:
        if i.group() != 'NPT' and i.group() != 'NPS':
            sourceFile = open(outfile,'a')
            print(name, i.group(), i.start(), file=sourceFile)
            sourceFile.close()
    
        

print('Done')   


       

