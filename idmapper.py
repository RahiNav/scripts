#The script uses panda to merge two file based on a anchor (common) column between the two file.
# The merge type can be inner/left/right/outer. for descriptions please see https://www.geeksforgeeks.org/how-to-do-a-vlookup-in-python-using-pandas/

import pandas as pd

infile1='/Users/rsn13/Desktop/scripts/input/glycan_chebi.csv'
infile2='/Users/rsn13/Desktop/scripts/input/glycan_xref_reactome.csv'
outfile='/Users/rsn13/Desktop/scripts/output/mapped1.txt'
anchor_column = 'glytoucan_ac'
merge_type = 'inner'

df1 = pd.read_csv(infile1)
df2 = pd.read_csv(infile2)
    
inner_join = pd.merge(df1,df2,on=anchor_column,how=merge_type)

sourceFile = open(outfile, 'a')
print(inner_join, file=sourceFile)

sourceFile.close()

print('Done')
