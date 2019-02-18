############### Autoria : Johnatan
#### Ajustes para classe

import shutil

####print("O ARQUIVO GERADO TERÁ O SEGUINTE NOME: resultado-NOME_DO_INTEGRANTE_DO_GRUPO");

##nome_do_arquivo = input("DIGITE O NOME DO ARQUIVO  QUE ESTÁ EM UMA DAS TRÊS PASTAS(BLACK, WHITE E MONKEY: \n");
##nome_da_pasta = input("DIGITE O NOME DA PASTA ONDE ESTÁ O ARQUIVO ESCOLHIDO(monkey, white ou black: ")

nome_do_arquivo = 'black'
nome_da_pasta = 'black'

# convertendo para caixa baixa
nome_do_arquivo = nome_do_arquivo.lower();
# abrindo o arquivo com a base das 1080 palavras do integrante selecionado


###### Joga o valor para a variavel
manipulador = open("c:/python/"+nome_da_pasta+"/"+nome_do_arquivo+".txt", 'r');

contador = 0;
contadorMonkey = 0
contadorBlack = 0
contadorWhite = 0

for palavra in manipulador:
    palavra = palavra.rstrip()
    palavra = palavra.lower()
    resultado = open("c:/python/bases/resultados/resultado-"+nome_do_arquivo+".txt", 'a')

    if "white trash" in palavra or "black trash" in palavra:
        contador = contador + 1;
        resultado.write(palavra + '\n');

    elif " white boy" in palavra or "white girl" in palavra\
        or "white boys" in palavra or "white girls" in palavra:
        contador +=1;
        resultado.write(palavra + '\n');

    elif "black kid" in palavra or "black kids" in palavra or "white kids" in palavra or "white kid" in palavra:
        contador = contador + 1;
        resultado.write(palavra + '\n');

    elif "nigga bitch" in palavra or "niggah bitches" in palavra\
            or "nigger" in palavra:
        contador = contador + 1
        resultado.write(palavra + '\n')

    elif "black bitch" in palavra or "black bitches" in palavra or "white bitch" in palavra\
         or "white bitches" in palavra:
        contador +=1
        resultado.write(palavra + '\n')

    elif "white man" in palavra or "black men" in palavra\
        or "white woman" in palavra or "black women" in palavra:
        contador +=1
        resultado.write(palavra + '\n')


    elif "that monkey" in palavra or "this monkey" in palavra or "these monkeys" in palavra or "that monkeys" in palavra\
         or "this monkeys" in palavra:
        contador +=1
        resultado.write(palavra+'\n')

    elif "white boyfriend" in palavra or "black girlfriend" in palavra\
        or "white boyfriends" in palavra or "black girlfriends" in palavra:
        contador +=1
        resultado.write(palavra + '\n')

    elif "white people" in palavra or "black people" in palavra or "white person" in palavra\
          or "black person" in palavra:
        contador+=1
        resultado.write(palavra+'\n')

    elif "older black" in palavra or "old black" in palavra or "older white" in palavra or "old white" in palavra:
        contador+=1
        resultado.write(palavra+'\n')

    elif "black hand" in palavra or "black hands " in palavra or "white hand" in palavra or "white hands" in palavra:
        contador+=1
        resultado.write(palavra+'\n')

    elif "black arm" in palavra or "black arms" in palavra or "white arm" in palavra or "white arms" in palavra:
        contador += 1
        resultado.write(palavra + '\n')

    elif "black body" in palavra or "black bodies" in palavra or "white body" in palavra or "white bodies" in palavra:
        contador += 1
        resultado.write(palavra + '\n')

resultado.close();
"""
    elif "kid" in palavra or "kids" in palavra:
        monkey = open("monkey.txt", 'a')
        contadorMonkey += 1
        contado = contador + 1
        monkey.write(palavra + '\n')
        monkey.close()

    elif "man" in palavra or "men" in palavra:
        white = open('white.txt', 'a')
        contadorWhite += 1
        white.write(palavra + '\n')
        white.close()

    elif "woman" in palavra or "women" in palavra:
        black = open('black.txt', 'a')
        contadorBlack += 1
        black.write(palavra + '\n')
        black.close()
"""

# abrindo o arquivo com o resultado da análise para inserir o total de freases analisadas
resultado = open("c:/python/bases/resultados/resultado-"+nome_do_arquivo + ".txt", 'a');

# escreve a frase total no arquivo criado como resultado-NOME_DO_INTEGRANTE_DO_GRUPO
resultado.write("\n\n\nTotal de frases: ");
# A função abaixo coloca, no arquivo criado, o total de frases analisadas.
resultado.write(str(contador))

# fechando arquivos
resultado.close();
manipulador.close();  # fechando o arquivo como nome do integrante
