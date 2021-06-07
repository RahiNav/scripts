# Takes a column from a file and calculates its frequency in the column. #prints the item and frequency in the output file. 
# sorts the output file by highest frequency

infile = '/Users/rsn13/Desktop/scripts/input/pubs.csv'
outfile = '/Users/rsn13/Desktop/scripts/output/freq.txt'

with open(infile) as file:
    items=[]
    frequency = {}
    
    for line in file:
        line = line.strip()
        items.append(line)
                   
    for item in items:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
            
    #print(frequency)
    sort_orders = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    
    for i in sort_orders:
        sourceFile = open(outfile,'a')
        print(i[0], i[1], file=sourceFile)
        sourceFile.close()
        
print('Done')        


            
        
        
        