from tkinter import *
from Operaciones import *
from Archivojson import *

aritmetica.suma(5,6)
aritmetica.resta(3,1)
aritmetica.multiplicacion(5,5)
aritmetica.division(15,5)
aritmetica.potencia(5,2)
aritmetica.raiz(25,2)
aritmetica.inverso(5,3)
aritmetica.seno(45)
aritmetica.coseno(45)
aritmetica.tangente(45)

print("\n------------------------")
########################################################################

diccionrarioJson = Sjson.diccionarioJSON('test.json')
listaOperaciones = diccionrarioJson['operaciones']
print(listaOperaciones[0])
print(listaOperaciones[0]['operacion'])
print(listaOperaciones[0]['valor1'])
print(listaOperaciones[0]['valor2'])


########################################################################
def hola():
    print("hola...")

raiz = Tk()
raiz.title('LFP Proyecto 1 | 201906795')
raiz.geometry('900x500')
lbl = Label(raiz,text='label1')
lbl.pack()
btn = Button(raiz, text='boton1', command= hola)
btn.pack()
raiz.mainloop()
