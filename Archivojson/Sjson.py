import os
import json


def jsonabrirarchivo(ruta):
    nombre, extension = os.path.splitext(ruta)
    print('Nombre: ',nombre,' | Extension: ', extension)

    textoarchivo = ''
    try:
        with open(ruta, "r") as archivo:
            textoarchivo = archivo.read()
            return textoarchivo
    except:
        print("♦ Error: no se pudo abrir el archivo.")
    

def textoajson():
    try:
        txtjson = jsonabrirarchivo('test.json')
        print(txtjson)
        datosdiccionario = json.loads(txtjson)
        print(datosdiccionario)
    except:
        print("♦ Error: no se pudo convertir en un diccionario el texto proporcionado")