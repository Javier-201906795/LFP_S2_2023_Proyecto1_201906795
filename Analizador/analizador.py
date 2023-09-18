import json


from Archivojson import *



def convertiradiccionario(texto):
    try:
        newdiccionario = Sjson.diccionarioJSON(texto)
        print('\n',newdiccionario,'\n')
        return newdiccionario
    except:
        print('♦ Error: no se pudo convertir el texto en un diccionario')


def lexico(texto):
    #Convertir texto a diccionario
    diccionario = convertiradiccionario(texto)
    
    