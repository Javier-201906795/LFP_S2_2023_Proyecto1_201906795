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






################################################################
def obtenertokens(texto):

    #Variables Globales
    global tokens, linea, columna
    #iterador
    c = 0
    #numero maximo de iteraciones
    maxiterc = len(texto)
    #Ciclo de iteraciones para evaluar y obtener tokens
    while c < maxiterc:
        #Obtener caracter
        caracter = texto[c]
        


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

    