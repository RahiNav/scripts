import csv

#original_stdout = sys.stdout

with open('C:\\Users\\rsn13\\Anaconda3\\input_files\\reviewed.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    
    column_header=[]
            
    for line in csv_reader:
        for i in range(len(line)):
            #print(line[i])               
            column_header.append(line[i])
        break
    
#    print(column_header[0])
            
    for line in csv_reader:
        for i in range(len(line)):
            sourceFile=open('C:\\Users\\rsn13\\Anaconda3\\input_files\\output.txt', 'a')
            print(column_header[i],":",line[i], file=sourceFile )
        print(file=sourceFile)
        print(file=sourceFile)
    sourceFile.close()     
            
        
        
        
    