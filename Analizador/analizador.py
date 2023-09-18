import json
from tkinter import *
from tkinter import messagebox as MessageBox


from Archivojson import *



def convertiradiccionario(texto):
    
    print('paso aqui1')
    newdiccionario = Sjson.diccionarioJSON(texto)
    print('\n',newdiccionario,'\n')
    return newdiccionario
    


def lexico(texto):
    #Convertir texto a diccionario
    diccionario = convertiradiccionario(texto)
    print('holamundo')
    
    
    