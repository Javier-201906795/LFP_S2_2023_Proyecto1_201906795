from tkinter import *
from tkinter.ttk import Combobox

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
def listaseleccion():
    print(listaopcionesarchivo.get())

raiz = Tk()
raiz.title('LFP Proyecto 1 | 201906795')
raiz.geometry('900x500')

btnanalizar = Button(raiz,text='Analizar', bg='#313446', fg='#FFFFFF', command=listaseleccion)
btnanalizar.place(x=230,y=10, width=80, height= 35)

btnerrores = Button(raiz,text='Errores', bg='#313446', fg='#FFFFFF')
btnerrores.place(x=370,y=10, width=80, height= 35)

btnreportes = Button(raiz,text='Reportes', bg='#313446', fg='#FFFFFF')
btnreportes.place(x=510,y=10, width=80, height= 35)

opcionesarchivo = ['ARCHIVO','Abrir','Guardar','Guardar como', 'Salir']
listaopcionesarchivo = Combobox(raiz, text='Archivo', values = opcionesarchivo)
listaopcionesarchivo.place(x=50,y=12, width=130, height= 30)
listaopcionesarchivo.current(0)

inputtexto = Entry(raiz)
inputtexto.place(x=80,y=100, width=800, height=350)

raiz.mainloop()
