# -*- Coding: UTF-8 -*-
#coding: utf-8

# varFrase = 'VARIABLE WORD theme music SounD ... @ !'
#
# #### Test open file on python
variablePathFile = '/home/mark/Documents/Datasets/tweets2009Part00'
arrayVariablePathFile = [28]
arrayVariablePathFile[0] = "/home/mark/Documents/Datasets/tweets2009Part00"

########## Better to get a quantitie on the directory
quantitieFiles = 28

for indice in range(quantitieFiles):
    arrayVariablePathFile.append("/home/mark/Documents/Datasets/tweets2009Part0"+str(indice))

for j in arrayVariablePathFile:
    print (j)
######## Contagem de quantas linhas há no arquivo
# def file_lengthy(fname):
#         with open(fname) as f:
#                 for i, l in enumerate(f):
#                         pass
#         return i + 1
#
###linesFile = file_lengthy(variablePathFile)

searchBlack = 'black'
searchMonkey = 'monkey'
searchWord  =  'Found !!! '

for indice in range(quantitieFiles):
    with open(arrayVariablePathFile[int(indice)],'r') as f:
        linesFile = f.read().split("\n")

    for i,line in enumerate(linesFile):
        if searchBlack in line and searchMonkey in line.split():
            #if searchMonkey in line:
            print(line)
            print("\nWord \"{}\" found in line {}".format(searchWord, i+1))
#print("Number of lines in the file: ",file_lengthy(variablePathFile
