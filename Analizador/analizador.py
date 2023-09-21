import json
from os import system
from tkinter import *
from tkinter import messagebox as MessageBox


from Archivojson import *



#         MessageBox.showerror('Error:[analizado.py][CG002]','No se pudo convertir un diccionario revise el texto introducido')

################################################################
#Variables Globales
tokens = []
linea = 1
columna = 1
listatocaracteresbuscados = ['{','}',':','[',']',',']

################################################################




def obtenertexto(text, c):
    #Texto
    string = ''
    #Evaluar caracter por carcater
    for caracter in text:
        if caracter == '"':
            #Si encuntra el cierre "
            return [string, c]
        #Forma el texto
        string += caracter
        c += 1
    print("Error: No se encontraron comillas doble que cerraran el texto.")




################################################################
def obtenertokens(texto):

    #Variables Globales
    global tokens, linea, columna, listatocaracteresbuscados
    #iterador
    c = 0
    #numero maximo de iteraciones
    maxiterc = len(texto)
    #Ciclo de iteraciones para evaluar y obtener tokens
    while c < maxiterc:
        #Obtener caracter
        caracter = texto[c]
        
        #Evaluar
        if caracter.isspace():
            #Si es algun tipo de espacio
            if caracter == '\n':
                #Si es un Salto de linea
                #Aumenta la linea
                linea += 1
                #Reinicia columnas
                columna = 1
            elif caracter == '\t':
                #Si es un Tabulador
                #Aumenta la columna en 4
                columna += 4
            else:
                #Si es un espacio
                #Aumenta la columna
                columna += 1
            #Reporte
            #print('Caracter: ', caracter, ' Linea: ', linea, ' Columna: ',columna)
            #Contador
            c += 1
        elif caracter in listatocaracteresbuscados:
            #Aumenta columna
            columna += 1
            #Contador
            c += 1
            #Almacena token
            print('token: ', caracter, ' linea:', linea,' columna: ',columna)
        elif caracter == '"':
            #Si es un texto un posible token
            textoaevaluar = texto[c+1:]
            string, pos = obtenertexto(textoaevaluar, c)
            #Aumentar contador
            c += pos + 2
            #Almacenar token
            print('token: ', string, ' linea:', linea,' columna: ',columna)
        c += 1
    #Resultados
    print('Iteraciones maxima: ', maxiterc)







################################################################
def lexico(texto):

    #Obtener Tokens
    obtenertokens(texto)
    


def graphviz():
    #Crear imagen Graphviz
    system('dot -Tpng archivo.dot -o archivograph1.png')     

    