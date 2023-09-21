import json
from tkinter import *
from tkinter import messagebox as MessageBox


from Archivojson import *



#         MessageBox.showerror('Error:[analizado.py][CG002]','No se pudo convertir un diccionario revise el texto introducido')


def lexico(texto):


   
    
    #Leer Linea por linea
    linea = 1
    columna = 1
    for caracter in texto:
        #Print estado
        print('Ascii: ', ord(caracter), ' Caracter: ', caracter, 'Linea: ', linea, ' Columna: ', columna)
        #Contador columna
        columna = columna + 1
        #Salto de linea
        if ord(caracter) == 10:
            linea = linea + 1
            columna = 0

        

    