import sys
import os

def clean(file):
    """	clean(file)

    Abre e limpa um arquivo de texto
    Entradas:
        file: caminho para o arquivo a partir do arquivo que chamou a função

    """
    tfile = os.path.join(sys.path[0], file)
    fileToClean = open(tfile, "w")
    fileToClean.write("")
    fileToClean.close()

def toLinesArray(file):
    """	toLinesArray(file)

    Converte um arquivo de texto em um array de suas linhas
    Entradas:
    	file: O arquivo a ser convertido

    Saída:
        array: Um array em cada elemento é uma liha do arquivo original

    """
    fileToConvert = os.path.join(sys.path[0], file)
    with open(fileToConvert) as f:
        temp_arr = f.readlines()
        array = [line.rstrip('\n') for line in temp_arr]
    return array

def toWordsArray(line):
    """	toWordsArray(line)

    Converte uma frase em um array composto das palavras da frase
    Entradas:
    	line: a frase a ser quebrada em array

    Saída:
        array: Um array em cada elemento é uma palavra da frase original

    """
    array = line.split(" ")
    return array

def toAppend(file):
    """	toAppend(file)

    Abre um arquivo no modo append
    Entradas:
    	file: o arquivo que se quer abrir

    Saída:
        returnFile: o arquivo aberto e pronto para receber informações adicionais

    """
    tfile = os.path.join(sys.path[0], file)
    returnFile = open(tfile, "a")
    return returnFile

def toCSV(input, output):
    """	toCSV(file)

    Converte um arquivo .txt em .csv, colocando virgulas no lugar dos espaços
    Entradas:
    	input: o arquivo a ser convertido
        output: o arquivo de saida

    """
    linesArray = toLinesArray(input)
    clean(output)
    returnFile = toAppend(output)
    for line in linesArray:
        returnFile.write(line.replace(' ', ', ') + '\n')
    return returnFile
