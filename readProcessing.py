# -*- Coding: UTF-8 -*-
#coding: utf-8
import os

#### Variables
var_path = "/home/mark/Documents/Dataset_Part/12_Dezembro/Particionamento_100mb"
array_variables = []

####### Filtros
searchBlack = 'black'
searchMonkey = 'monkey'
searchWord  =  'Found !!! '

countIndice = 0

def function_renameDirectory(pathName, preFx):
    i = 0
    for filename in os.listdir(pathName):
        os.rename(os.path.join(pathName,filename), os.path.join(pathName,preFx+str(i)+'.txt'))
        i = i +1

for dirname, dirnames, filenames in os.walk(var_path):
    #print path to all filenames.
    for filename in filenames:
        #array_variables.append(filename[:-4])
        array_variables.append(filename)

varQuantitieFiles = len(array_variables)
#function_renameDirectory(var_path,'tweets_08_part')

#print varQuantitieFiles

#def function_processingData():
for indice in range(varQuantitieFiles):
    with open(array_variables[int(indice)],'r') as f:
        linesFile = f.read().split("\n")

for i,line in enumerate(linesFile):
    if searchBlack in line and searchMonkey in line.split():
        #if searchMonkey in line:
        print(line)
        print("\nWord \"{}\" found in line {}".format(searchWord, i+1))

#function_renameDirectory(var_path,'tweets_12_part')
#function_processingData()
