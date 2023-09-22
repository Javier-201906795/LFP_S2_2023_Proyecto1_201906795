import json
from os import system
from tkinter import *
from tkinter import messagebox as MessageBox


from Archivojson import *



#         MessageBox.showerror('Error:[analizado.py][CG002]','No se pudo convertir un diccionario revise el texto introducido')

################################################################
#Variables Globales
tokens = []
linea = 1
columna = 1
listatocaracteresbuscados = ['{','}',':','[',']',',']
listaoperacionescon1valor = ['seno','coseno','tangente','inverso']
listaerrores = []
listainstrucciones = []

################################################################




def obtenertexto(text, a):
    #Texto
    string = ''
    #Evaluar caracter por carcater
    for newcaracter in text:
        if newcaracter == '"':
            #Si encuntra el cierre "
            return [string, a]
        #Forma el texto
        string += newcaracter
        a += 1
    print("Error: No se encontraron comillas doble que cerraran el texto.")

################################################################

def obtenernumero(texto, a):
    numero = ""
    isDecimal = False
    for newcaracter in texto:
        if newcaracter.isdigit():
            numero += newcaracter
            a += 1
        elif newcaracter == "." and not isDecimal:
            numero += newcaracter
            a += 1
            isDecimal = True
        else:
            break
    if isDecimal:
        return [float(numero), a]
    return [int(numero), a]


################################################################
def obtenertokens(texto):

    #Variables Globales
    global tokens, linea, columna, listatocaracteresbuscados
    #iterador
    c = 0
    #numero maximo de iteraciones
    maxiterc = len(texto)
    #Ciclo de iteraciones para evaluar y obtener tokens
    while c < maxiterc:
        #Obtener caracter
        caracter = texto[c]
        #Leyendo el siguiente texto
        textoaleer = texto[c:]
        
        #Evaluar
        if caracter.isspace():
            #Si es algun tipo de espacio
            if caracter == '\n':
                #Si es un Salto de linea
                #Aumenta la linea
                linea += 1
                #Reinicia columnas
                columna = 1
            elif caracter == '\t':
                #Si es un Tabulador
                #Aumenta la columna en 4
                columna += 4
            else:
                #Si es un espacio
                #Aumenta la columna
                columna += 1
            #Reporte
            #print('Caracter: ', caracter, ' Linea: ', linea, ' Columna: ',columna)
            #Contador
            c += 1
        elif caracter in listatocaracteresbuscados:
            #Aumenta columna
            columna += 1
            #Contador
            c += 1
            #Almacena token
            tokens.append(caracter)
            print('token: ', caracter, ' linea:', linea,' columna: ',columna)
        elif caracter == '"':
            #Si es un texto un posible token
            textoaevaluar = texto[c+1:]
            string, pos = obtenertexto(textoaevaluar, c)
            #Aumentar contador y columna
            c = pos + 2
            columna = len(string) + 1
            #Almacenar token
            tokens.append(string)
            print('token: ', string, ' linea:', linea,' columna: ',columna)
        elif caracter.isdigit():
            #Obtener numero
            textoaevaluar = texto[c:]
            numero, pos = obtenernumero(textoaevaluar, c)
            #Aumentar contador y columna
            c = pos
            txtnumero = str(numero) 
            columna += len(txtnumero) + 1
            #Almacenar token
            tokens.append(numero)
            print('token: ', numero, ' linea:', linea,' columna: ',columna)
        else:
            #Aumentar contador y columna
            c += 1
            columna += 1
            #Caracter Desconocido
            print("\033[1;31;40m Error: caracter desconocido:", caracter," |Linea:",linea," |Columna:",columna,"\033[0m")
            #Almacenar error
            error = [caracter, linea, columna]
            listaerrores.append(error)
        
    #Resultados
    print('\n')
    print('Iteraciones maxima: ', maxiterc)
    print(tokens)
    print('Tokens: ', len(tokens))
    print(listaerrores)
    print('Numero de Errores: ', len(listaerrores))
    if (len(listaerrores) > 0):
        print(listaerrores[0])
        print(listaerrores[0][0])
        print(listaerrores[0][1])
        print(listaerrores[0][2])

    #Evaluar token y formar instrucciones
    formar_instrucciones()
    

################################################################
def formar_instrucciones():
    global tokens, listainstrucciones

    while tokens:
        instruccion = obtener_instruccion()
        if instruccion:
            #Añadir nueva instruccion
            listainstrucciones.append(instruccion)
    
    print('\n###### [ Lista instrucciones ] #####')
    print(listainstrucciones,'\n')


################################################################
def lexico(texto):

    global tokens, listaerrores, linea, columna, listainstrucciones
    #Reiniciar valores
    linea = 1
    columna = 1
    tokens = []
    listaerrores = []
    listainstrucciones = []
    

    #Obtener Tokens
    obtenertokens(texto)
    
################################################################
def obtener_instruccion():
    global tokens
    operacion = ''
    valor1 = ''
    valor2 = ''
    #Recorrer valores
    while tokens:
        token = tokens.pop(0)
        print('Token: ', token)
        if token == 'operacion':
            #Eliminar el siguiente token : (dos puntos)
            tokens.pop(0)
            #Almacena el tipo de operacion
            operacion = tokens.pop(0)
        elif token == 'valor1':
            #Eliminar el siguiente token : (dos puntos)
            tokens.pop(0)
            #Obtine el valor 1
            valor1 = tokens.pop(0)
            #Evaluea si no hay mas instrucciones adentro del valor1
            if valor1 == '[':
                valor1 = obtener_instruccion()
        elif token == 'valor2':
            #Eliminar el siguiente token : (dos puntos) o , (coma)
            tokens.pop(0)
            #Evalua si hay comas
            #Obtine el valor 2
            valor2 = tokens.pop(0)
            #Evaluea si no hay mas instrucciones adentro del valor2
            if valor2 == '[':
                valor2 = obtener_instruccion()

        #Evaluar si es una operacion de un valor o dos
        if operacion and valor1 and valor2:
            #Operacion con dos Valores
            print('\n\noperacion:', operacion, '|valor1:', valor1, '|valor2:', valor2)
            return [operacion,valor1,valor2]
        if operacion and operacion in listaoperacionescon1valor and valor1:
            return [operacion,valor1,None]


    


def graphviz():
    #Crear imagen Graphviz
    system('dot -Tpng archivo.dot -o archivograph1.png')     

    