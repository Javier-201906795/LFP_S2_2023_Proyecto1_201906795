import math



def suma(num1,num2):
    sumar = float(num1 + num2)
    print('• Sumando:   ',str(num1),' + ',str(num2), ' = ', sumar)
    return sumar

def resta(num1,num2):
    restar = float(num1 - num2)
    print('• Restando:  ',str(num1),' - ',str(num2), ' = ', restar)
    return restar

def multiplicacion(num1,num2):
    multiplicar = float(num1 * num2)
    print('• Multiplicando:  ',str(num1),' * ',str(num2), ' = ', multiplicar)
    return multiplicar

def division(num1,num2):
    dividir = float(num1 / num2)
    print('• Dividiendo:  ',str(num1),' / ',str(num2), ' = ', dividir)
    return dividir

def potencia(num,numpotencia):
    potenciar = float(pow(num,numpotencia))
    print('• Potencia:  ',str(num),' ^ ',str(numpotencia), ' = ', potenciar)
    return potenciar

def raiz (num,raiz):
    numraiz = 1/raiz
    resraiz = float(pow(num,numraiz))
    print('• Raiz: numero: ',num,' raiz: ',raiz, ' = ', resraiz)
    return resraiz

def inverso(num):
    #Redondear numero por si tiene decimales
    numero = round(num)
    #Convertir a texto
    txtnumero = str(numero)
    resinverso = txtnumero[::-1]
    #Convertir texto a numero    
    resinverso = int(resinverso)
    print('• Inverso: ', num,'=', resinverso )
    return resinverso

def seno(num):
    numradianes = math.radians(num)
    resseno = float(math.sin(numradianes))
    nuevoformato = format(resseno,'.6f')
    print('• Seno: sen(',num,'°) = ', nuevoformato)
    return resseno

def coseno(num):
    numradianes = math.radians(num)
    rescoseno = float(math.cos(numradianes))
    nuevoformato = format(rescoseno,'.6f')
    print('• Coseno: cos(',num,'°) = ', nuevoformato)
    return rescoseno


def tangente(num):
    numradianes = math.radians(num)
    restangente = float(math.tan(numradianes))
    nuevoformato = format(restangente,'.6f')
    print('• Tangente: tan(',num,'°) = ', nuevoformato)
    return restangente

def mod(num1, num2):
    newmod = float(num1) + float(num2)
    print('• mod: ',num1,' y ',num2,' = ', newmod)
    return newmod
