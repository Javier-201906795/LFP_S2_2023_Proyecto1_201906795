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
            print("♦ Error[SJSON.py][CD001]: no se pudo abrir el archivo.")
    else:
        print("♦ Error[SJSON.py][CD002]: no se pudo abrir el archivo porque no es un archivo JSON.")




def diccionarioJSON(txtjson):
    try:
        datosdiccionario = json.loads(txtjson)
        return datosdiccionario
    except:
        errmensaje = "♦ Error[SJSON.py][CD003]: no se pudo convertir en un diccionario el texto proporcionado"
        print(errmensaje)
        return ValueError(errmensaje)



