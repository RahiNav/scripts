import csv


with open('C:\\Users\\rsn13\\Anaconda3\\input_files\\reviewed.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    
    column_header=[]
            
    for line in csv_reader:
        for i in range(len(line)):              
            column_header.append(line[i])
        break
    
            
    for line in csv_reader:
        sourceFile=open('C:\\Users\\rsn13\\Anaconda3\\input_files\\final.txt', 'a')
        print('==='+line[0]+'===',file=sourceFile)
        for i in range(len(line)):
            print("'''"+column_header[i]+"'''",":",line[i],'<br>', file=sourceFile )
        print(file=sourceFile)
        print(file=sourceFile)
    sourceFile.close()  
    
    print("Done")
            
        
        
        
    
