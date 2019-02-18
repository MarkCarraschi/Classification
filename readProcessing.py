# -*- Coding: UTF-8 -*-
#coding: utf-8
import os
import shutil

#### Variables
var_path = "/home/mark/Documents/Dataset_Part/06_Junho/Particionamento_100mb"
array_variables = []
global_countBlack = 0

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

def function_processingData():

    for indice in range(varQuantitieFiles):
        with open(var_path + "/" + array_variables[int(indice)],'r') as f:
            linesFile = f.read().split("\n")

    for i,line in enumerate(linesFile):
         if searchBlack in line: #and searchMonkey in line.split():
             global global_countBlack
             global_countBlack = global_countBlack + 1
             #if searchMonkey in line:
             print(line)
             print("\nWord \"{}\" found in line {}".format(searchWord, i+1))

def function_createFolder():

    if not os.path.exists("/home/mark/Documents/resultadoCodigo/black"):
        os.makedirs("/home/mark/Documents/resultadoCodigo/black")

    if not os.path.exists("/home/mark/Documents/resultadoCodigo/white"):
        os.makedirs("/home/mark/Documents/resultadoCodigo/white")

def function_Filter():

    file_whiteFilter = "whiteFilter"
    file_blackFilter = "blackFilter"
    resultado_blackFilter = open("/home/mark/Documents/FilterEtnia/black/"+file_blackFilter+".txt", 'a')
    resultado_whiteFilter = open("/home/mark/Documents/FilterEtnia/white/"+file_whiteFilter+".txt", 'a')

    # convertendo para caixa baixa
    #nome_do_integrante = nome_do_integrante.lower();
    ####manipulador = open(nome_do_integrante+".txt",'r');
    contador = 0;

    #### NÃO ESQUECER DA CAIXA BAIXA
    for indice in range(varQuantitieFiles):
        with open(var_path + "/" + array_variables[int(indice)],'r') as f:
            linesFile = f.read().split("\n")
"""
        if indice >= 2

            indice_one = indice - 1
            indice_two = indice - 2

            with open(var_path + "/" + array_variables[int(indice_one)],'r') as f_one:
                previousLineOne = f_one.read().split("\n")

            with open(var_path + "/" + array_variables[int(indice_two)],'r') as f_two:
                previousLineTwo = f_two.read().split("\n")
"""
        for i,line in enumerate(linesFile):

            #### LOWER CASE
            line = line.lower()

            if "white" in line:
                contador = contador + 1;
                resultado_whiteFilter.write(line + '\n');

            elif "black" in line:
                contador=contador + 1;
                resultado_blackFilter.write(line + '\n');
"""

            if "white trash" in line or "black trash" in line:
                contador = contador + 1;
                #print(line)
                resultado.write(line + '\n');

            elif "white boy" in line or "white girl" in line or "white boys" in line or "white girls" in line:
                contador=contador + 1;
                resultado.write(line + '\n');
                #print(line)

            elif "nigga bitch" in line or "nigga bitches" in line:
                contador = contador + 1;
                resultado.write(line + '\n');
                #print(line)

            elif "white man" in line or "white men" in line or "white woman" in line or "white women" in line:
                contado = contador + 1;
                resultado.write(line  + '\n');
                #print(line)

            elif "black man" in line or "black men" in line or "black woman" in line or "black women" in line:
                contador = contador + 1;
                resultado.write(line + '\n');
                #print(line)

            elif "that monkey" in line or "this monkey" in line or "these monkey" in line:
                contador = contador + 1;
                resultado.write(line + '\n');
                #print(line)

            elif "black boyfriend" in line or "black girlfriend" in line or "black boyfriends" in line or "black girlfriends" in line:
                contador = contador + 1;
                resultado.write(line + '\n');
                #print(line)
"""

#function_renameDirectory(var_path,'tweets_12_part')
#function_processingData()
#print global_countBlack
function_Filter()
function_createFolder()
