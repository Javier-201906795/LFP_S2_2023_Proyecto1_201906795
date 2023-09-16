import os


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
    
    