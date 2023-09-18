import json
from tkinter import *
from tkinter import messagebox as MessageBox


from Archivojson import *



def convertiradiccionario(texto):
    try:
        newdiccionario = Sjson.diccionarioJSON(texto)
        #Evaluar si es un error
        mensaje = str(newdiccionario)[2:7]
        if mensaje == 'Error':
            #causar un error
            x = 1/0
        else:
            #Retornar
            return newdiccionario
    except Exception:
        print('Error:[analizado.py][CG002] ', Exception)
        MessageBox.showerror('Error:[analizado.py][CG002]','No se pudo convertir un diccionario revise el texto introducido')


def lexico(texto):
    #Convertir texto a diccionario
    diccionario = convertiradiccionario(texto)
    print(diccionario)
    
    
    