import os

def hola():
    print("hola mundo")


def abrirarchivo():
    ruta = 'test.json'
    nombre, extension = os.path.splitext(ruta)
    print(nombre, extension)

    try:
        with open(ruta, "r") as archivo:
            print(archivo.read())
    except:
        print("♦ Error: no se pudo abrir el archivo.")