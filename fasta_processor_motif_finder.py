#The script parses a fasta file and finds the N glycosylation motif(s) in the protein sequence.
#The output file produces UniProtKB accession, matched motif and the starting position of the matched motif
#The script works on fasta file(s) downloaded from UniProtKB. e.g. input file: https://www.uniprot.org/uniprot/P04278.fasta

import re


fasta_file = '/Users/rahinavelkar/Desktop/scripts/P04278.fasta'
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
    pattern = re.finditer('N\wS|N\wT', seq)
    for i in pattern:
        if i.group() != 'NPT' and i.group() != 'NPS':
            motif = i.group()
            motif_start_pos = i.start()+1
            sourceFile = open(outfile,'a')
            print(name, motif, motif_start_pos, file=sourceFile)
            sourceFile.close()
    
        

print('Done')   


       

