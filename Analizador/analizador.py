import json
from os import system
from tkinter import *
from tkinter import messagebox as MessageBox


from Archivojson import *
from Operaciones import *


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
contadorinstrucciones = 0
listaresultados = []

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


    

################################################################
def formar_instrucciones():
    global tokens, listainstrucciones

    while tokens:
        instruccion = obtener_instruccion()
        if instruccion:
            #Añadir nueva instruccion
            listainstrucciones.append(instruccion)
    
    print('#######################################')
    print('\n###### [ Lista instrucciones ] #####')
    print(listainstrucciones,'\n')
    print('#######################################\n')


################################################################

def esunnumero(posiblenumero):
    try:
        int(posiblenumero)
        return True
    except:
        try:
            float(posiblenumero)
            return True
        except:
            return False

################################################################

def interpretar_instruccion(operacion, valor1, valor2):
    global listainstrucciones
    
    resultado = None
    while listainstrucciones:
        
        #Obtener Valores
        if operacion == None and valor1 == None and valor2 == None:
            instruccion = listainstrucciones.pop(0)
            operacion = instruccion[0]
            valor1 = instruccion[1]
            valor2 = instruccion[2]
            print('\n###### [ Instruccion ] #######')
            print(operacion, valor1, valor2)
            print('-----------------------------------')
        
        #Hay operaciones adentro del valor
        if esunnumero(valor1) == False:
            operacion = valor1[0]
            valor1 = valor1[1]
            valor2 = valor1[2]
            valor1 = interpretar_instruccion(operacion,valor1,valor2)
        if esunnumero(valor2) == False:
            newoperacion = valor2[0]
            newvalor1 = valor2[1]
            newvalor2 = valor2[2]
            valor2 = interpretar_instruccion(newoperacion,newvalor1,newvalor2)
        #Intentar Resolver
        if esunnumero(valor1) and esunnumero(valor2):
            #Operar
            resultado = evaluar_tipo_operacion(operacion,valor1,valor2)
            return resultado   

################################################################    
def evaluar_tipo_operacion(operacion, valor1, valor2):
    # aritmetica.suma(5,6)
    # aritmetica.resta(3,1)
    # aritmetica.multiplicacion(5,5)
    # aritmetica.division(15,5)
    # aritmetica.potencia(5,2)
    # aritmetica.raiz(25,2)
    # aritmetica.inverso(5,3)
    # aritmetica.seno(45)
    # aritmetica.coseno(45)
    # aritmetica.tangente(45)

    #Convertir texto a minusculas
    operacion = operacion.lower()

    #Evaluar
    if operacion == 'suma':
        resultado = aritmetica.suma(valor1,valor2)
    elif operacion == 'resta':
        resultado = aritmetica.resta(valor1,valor2)
    elif operacion == 'multiplicacion':
        resultado = aritmetica.multiplicacion(valor1,valor2)
    elif operacion == 'division':
        resultado = aritmetica.division(valor1,valor2)
    elif operacion == 'potencia':
        resultado = aritmetica.potencia(valor1,valor2)
    elif operacion == 'raiz':
        resultado = aritmetica.raiz(valor1,valor2)
    elif operacion == 'inverso':
        resultado = aritmetica.inverso(valor1)
    elif operacion == 'seno':
        resultado = aritmetica.seno(valor1)
    elif operacion == 'coseno':
        resultado = aritmetica.coseno(valor1)
    elif operacion == 'tangente':
        resultado = aritmetica.tangente(valor1)
    elif operacion == 'mod':
        resultado = aritmetica.mod(valor1,valor2)
    else:
        resultado = -1
    
    #Envia el resultado    
    print('operar: ', operacion, '|valor1:',valor1,'|valor2:',valor2,'|Resultado:',resultado), 
    return resultado



################################################################
#Inicia
def realizar_instruccion():
    global listainstrucciones, listaresultados
    # # interpretar_instruccion()
    a = 0
    while listainstrucciones:
        a += 1
        operacion = None
        valor1 = None
        valor2 = None
        resultado = interpretar_instruccion(operacion,valor1,valor2)
        #Almacenar resultado
        listaresultados.append(resultado)
        print('♦♦ ',a,'Resultado:', resultado)
        print('-----------------------------------\n')
    
    print('Lista Resultados',listaresultados)
################################################################



################################################################
def lexico(texto):

    global tokens, listaerrores, linea, columna, listainstrucciones, contadorinstrucciones
    #Reiniciar valores
    linea = 1
    columna = 1
    tokens = []
    listaerrores = []
    listainstrucciones = []
    contadorinstrucciones = 0
    

    #Obtener Tokens -> tokens
    obtenertokens(texto)

    #Evaluar token y formar instrucciones -> listainstrucciones
    formar_instrucciones()

    #Interpretar instrucciones
    realizar_instruccion()



def graphviz():
    #Crear imagen Graphviz
    system('dot -Tpng archivo.dot -o archivograph1.png')     

    