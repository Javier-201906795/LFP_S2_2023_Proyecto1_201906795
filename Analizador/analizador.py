import json
from tkinter import *
from tkinter import messagebox as MessageBox


from Archivojson import *



# def convertiradiccionario(texto):
#     try:
#         newdiccionario = Sjson.diccionarioJSON(texto)
#         #Evaluar si es un error
#         mensaje = str(newdiccionario)[2:7]
#         if mensaje == 'Error':
#             #causar un error
#             x = 1/0
#         else:
#             #Retornar
#             return newdiccionario
#     except Exception:
#         print('Error:[analizado.py][CG002] ', Exception)
#         MessageBox.showerror('Error:[analizado.py][CG002]','No se pudo convertir un diccionario revise el texto introducido')


def lexico(texto):


    # #Convertir texto a diccionario
    # diccionario = convertiradiccionario(texto)
    # #Obtener operaciones
    # listaOperaciones = diccionario['operaciones']
    # print(listaOperaciones)
    
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

        

    