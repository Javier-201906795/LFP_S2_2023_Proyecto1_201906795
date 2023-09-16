import os
import json


def jsonabrirarchivo(ruta):
    nombre, extension = os.path.splitext(ruta)
    
    if (extension == '.json' or extension == '.JSON' or extension == '.Json'):
        textoarchivo = ''
        try:
            with open(ruta, "r") as archivo:
                textoarchivo = archivo.read()
                return textoarchivo
        except:
            print("♦ Error: no se pudo abrir el archivo.")
    else:
        print("♦ Error: no se pudo abrir el archivo porque no es un archivo JSON.")




def diccionarioJSON(ruta):
    try:
        txtjson = jsonabrirarchivo(ruta)
        datosdiccionario = json.loads(txtjson)
        return datosdiccionario
    except:
        print("♦ Error: no se pudo convertir en un diccionario el texto proporcionado")