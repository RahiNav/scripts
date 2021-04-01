import csv

#input file should be the glycan reviewed dictionary in the csv format.
#output file needs to be in a txt format.

#The program takes a csv file and parsers the columns into a specific text format 
#which is used to generate the Wikipedia page https://wiki.glygen.org/index.php/Glycan_structure_dictionary




with open('C:\\Users\\rsn13\\Anaconda3\\input_files\\glycan_dictionary.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    
    column_header=[]
            
    for line in csv_reader:
        for i in range(len(line)):            
            column_header.append(line[i])
        break
    

            
    for line in csv_reader:
        sourceFile=open('C:\\Users\\rsn13\\Anaconda3\\input_files\\glycan_dictionary.txt', 'a')
        print('==='+line[0]+'===',file=sourceFile)
        for i in range(len(line)):
            print("'''"+column_header[i]+"'''",":",line[i],'<br>', file=sourceFile )
        print(file=sourceFile)
        print(file=sourceFile)
    sourceFile.close()  
    
    print("Done")
            
        
        
        
    
