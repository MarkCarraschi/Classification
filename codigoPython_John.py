print("HA 5 TXT'S, CADA UM COM O NOME DE UM DOS INTEGRANTES. CADA UM DELES TEM A BASE COM 1080 FRASES");
print("O ARQUIVO GERADO TERÁ O SEGUINTE NOME: resultado-NOME_DO_INTEGRANTE_DO_GRUPO");
nome_do_integrante = input("DIGITE O NOME DO INTEGRANTE DO GRUPO QUE DESEJA ANALISAR A BASE EM TXT:\n");

# convertendo para caixa baixa
nome_do_integrante = nome_do_integrante.lower();

manipulador = open(nome_do_integrante+".txt",'r');
contador = 0;

for it in range(1080):
    palavra = manipulador.readline();
    palavra = palavra.rstrip();
    resultado = open("resultado-"+nome_do_integrante+".txt", 'a');

    if "white trash" in palavra or "black trash" in palavra:
        contador = contador + 1;
        resultado.write(palavra+'\n');

    elif "white boy" in palavra or "white girl" in palavra or "white boys" in palavra or "white girls" in palavra:
        contador=contador+1;
        resultado.write(palavra+'\n');

    elif "nigga bitch" in palavra or "nigga bitches" in palavra:
        contador = contador+1;
        resultado.write(palavra+'\n');

    elif "white man" in palavra or "white men" in palavra or "white woman" in palavra or "white women" in palavra:
        contado=contador|+1;
        resultado.write(palavra+'\n');

    elif "black man" in palavra or "black men" in palavra or "black woman" in palavra or "black women" in palavra:
        contador=contador+1;
        resultado.write(palavra+'\n');

    elif "that monkey" in palavra or "this monkey" in palavra or "these monkey" in palavra:
        contador = contador + 1;
        resultado.write(palavra+'\n');

    elif "black boyfriend" in palavra or "black girlfriend" in palavra or "black boyfriends" in palavra or \
         "black girlfriends" in palavra:
        contador = contador + 1;
        resultado.write(palavra+'\n');

    resultado.close();

print("\nQTD DE PALAVRAS RACISTAS: ",contador);
print("DIVIDIDO EM CINCO PESSOAS PARA ANALISAR: ",(contador/5));

#criando o arquivo com o resultado da análise
resultado = open("resultado-"+nome_do_integrante+".txt", 'a');
#imprime a frase total no arquivo criado como resultado-NOME_DO_INTEGRANTE_DO_GRUPO
resultado.write("\n\n\nTotal de frases: ");
#A função abaixo coloca no arquivo criado, o resultado de quantas linhas foram selecionadas, convertendo um inteiro para string
resultado.write(str(contador));
resultado.close();

#manipulador.seek(0); #retorna o ponteiro para o início do arquivo txt
manipulador.close(); #fechando o arquivo