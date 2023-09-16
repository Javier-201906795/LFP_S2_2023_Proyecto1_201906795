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
# lbl = Label(raiz,text='label1')
# lbl.pack()
# btn = Button(raiz, text='boton1', command= hola)
# btn.pack()

btnanalizar = Button(raiz,text='Analizar', bg='#313446', fg='#FFFFFF')
btnanalizar.place(x=200,y=10, width=80, height= 35)

btnerrores = Button(raiz,text='Errores', bg='#313446', fg='#FFFFFF')
btnerrores.place(x=340,y=10, width=80, height= 35)

btnreportes = Button(raiz,text='Reportes', bg='#313446', fg='#FFFFFF')
btnreportes.place(x=480,y=10, width=80, height= 35)

raiz.mainloop()
