import os
import json


def jsonabrirarchivo(ruta):
    nombre, extension = os.path.splitext(ruta)
    
    try:
        textoarchivo = ''
        try:
            with open(ruta, "r") as archivo:
                textoarchivo = archivo.read()
                return textoarchivo
        except:
            print("♦ Error[SJSON.py][CD001]: no se pudo abrir el archivo.")
    except:
        print("♦ Error[SJSON.py][CD002]: no se pudo abrir el archivo.")





