# The script takes two csv files and maps the said column together based on the anhor(common)colum.
# The script only workks when there is one-to-one mapping between the anchor column and said column in files
#anchor_file1 and anchor_file2 needs to be the common column. same format. 

import csv

infile1='/Users/rsn13/Desktop/scripts/input/glycan_chebi.csv'
infile2='/Users/rsn13/Desktop/scripts/input/glycan_xref_reactome.csv'
outfile = '/Users/rsn13/Desktop/scripts/output/mapped.txt'

dct1 ={}
dct2 = {}

anchor_file1 = 0
anchor_file2 = 0 
column_file1 = 1
column_file2 = 1

with open(infile1) as csv_file1:
    csv_reader1 = csv.reader(csv_file1, delimiter=',')
    
    for line in csv_reader1:
        dct1[line[anchor_file1]] = line[column_file1]
    
with open(infile2) as csv_file2:
    csv_reader2 = csv.reader(csv_file2, delimiter=',')  
    
    for line in csv_reader2:
        dct2[line[anchor_file2]] = line[column_file2]    
    

for anchor1,id1 in dct1.items():
    sourceFile = open(outfile,'a')
    for anchor2,id2 in dct2.items():
        if anchor1 == anchor2:
            print(anchor1,anchor2,id1,id2,file=sourceFile)

sourceFile.close()            
    
csv_file1.close()
csv_file2.close()

print('Done')  
