from tkinter import *
from tkinter.ttk import Combobox
from tkinter import filedialog
from tkinter import messagebox as MessageBox


from Operaciones import *
from Archivojson import *
from Analizador import *





#######################################################################
VArchivo ={'ruta':''}



#######################################################################
def Abrir():
    print('abrir')
    rutaarchivo = filedialog.askopenfilename()
    print(rutaarchivo)
    textoarchivo = Sjson.jsonabrirarchivo(rutaarchivo)
    #añadir texto a input
    inputtexto.insert('1.0', str(textoarchivo))
    #Guardar en variable
    VArchivo['ruta'] = rutaarchivo
    
    

def Guardar():
    print('Guardar')
    print('Ruta: ',VArchivo['ruta'])
    ruta = VArchivo['ruta']
    #Obtener texto de input
    texto = str(inputtexto.get("1.0",END))
    #Guardar
    archivo = open(ruta,'w')
    archivo.write(texto)
    archivo.close()
    print('Archivo guardado.')

def Guardarcomo():
    print('Guardarcomo')
    rutaarchivo = filedialog.asksaveasfile(defaultextension=".json", filetypes=[("All Files","*.json")])
    rutaarchivo = rutaarchivo.name
    #Obtener texto de input
    texto = str(inputtexto.get("1.0",END))
    #Guardar
    archivo = open(rutaarchivo,'w')
    archivo.write(texto)
    archivo.close()
    print('Archivo guardado.')
    
    

def Salir():
    print('Salir')
    raiz.destroy()




def Analizar():
    print('analizar')
    #Obtener texto input
    texto = str(inputtexto.get("1.0",END))
    #Enviar texto al analizador lexico
    analizador.lexico(texto)

    

def Errores():
    print('errores')
    MessageBox.showinfo("Hola!", "Hola mundo")

def Reporte():
    print('reporte')





# ########################################################################
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

# print("\n------------------------")
########################################################################

# diccionrarioJson = Sjson.diccionarioJSON('test.json')
# listaOperaciones = diccionrarioJson['operaciones']
# print(listaOperaciones[0])
# print(listaOperaciones[0]['operacion'])
# print(listaOperaciones[0]['valor1'])
# print(listaOperaciones[0]['valor2'])


########################################################################
def listaseleccion():
    print(listaopcionesarchivo.get())

raiz = Tk()
raiz.title('LFP Proyecto 1 | 201906795')
raiz.geometry('900x500')

btnanalizar = Button(raiz,text='Analizar', bg='#313446', fg='#FFFFFF', command=Analizar)
btnanalizar.place(x=230,y=10, width=80, height= 35)

btnerrores = Button(raiz,text='Errores', bg='#313446', fg='#FFFFFF', command=Errores)
btnerrores.place(x=370,y=10, width=80, height= 35)

btnreportes = Button(raiz,text='Reportes', bg='#313446', fg='#FFFFFF', command=Reporte)
btnreportes.place(x=510,y=10, width=80, height= 35)

opcionesarchivo = ['ARCHIVO','Abrir','Guardar','Guardar como', 'Salir']
listaopcionesarchivo = Combobox(raiz, text='Archivo', values = opcionesarchivo)
listaopcionesarchivo.place(x=50,y=12, width=130, height= 30)
listaopcionesarchivo.current(0)

#Switch case
def seleccion(event):
    print('Seleccionando ->', listaopcionesarchivo.get())
    sel = listaopcionesarchivo.get()
    if sel == 'Abrir':
        Abrir()
    elif sel == 'Guardar':
        Guardar()
    elif sel == 'Guardar como':
        Guardarcomo()
    elif sel == 'Salir':
        Salir()

#Ejecuta la opcion cuando cambia de seleccion
listaopcionesarchivo.bind('<<ComboboxSelected>>',seleccion)


inputtexto = Text(raiz,padx=40)
inputtexto.place(x=80,y=100, width=800, height=350)

labelnumeracion = Label(raiz, pady=0,text=' 1.\n 2.\n 3.\n 4.\n 5.', font=("Consolas",10), bg="#FFFFFF").place(x=85,y=102)
labelnumeracion = Label(raiz, pady=0,text=' 6.\n 7.\n 8.', font=("Consolas",10), bg="#FFFFFF").place(x=85,y=180)
labelnumeracion = Label(raiz, pady=0,text=' 9.\n10.\n11.', font=("Consolas",10), bg="#FFFFFF").place(x=85,y=230)
labelnumeracion = Label(raiz, pady=0,text='12.\n13.\n14.', font=("Consolas",10), bg="#FFFFFF").place(x=85,y=278)
labelnumeracion = Label(raiz, pady=0,text='15.\n16.\n17.', font=("Consolas",10), bg="#FFFFFF").place(x=85,y=325)
labelnumeracion = Label(raiz, pady=0,text='18.\n19.\n20.\n21.', font=("Consolas",10), bg="#FFFFFF").place(x=85,y=375)



raiz.mainloop()
