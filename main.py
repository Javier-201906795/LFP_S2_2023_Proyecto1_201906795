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
    #Limpiar input
    inputtexto.delete('1.0', 'end')
    print('abrriendo archivo y cargandolo en input')
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
    MessageBox.showinfo('Guardar','Archivo guardado con exito.')

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
    MessageBox.showinfo('Guardar como','Archivo guardado con exito.')
    
    

def Salir():
    print('Salir')
    salir = MessageBox.askokcancel(message="¿Desea continuar?", title="Salir")
    if salir:
        raiz.destroy()




def Analizar():
    print('analizar')
    #Obtener texto input
    texto = str(inputtexto.get("1.0",END))
    #Enviar texto al analizador lexico y obtiene tokens
    analizador.lexico(texto)

    
    

    

def Errores():
    print('errores')
    contenidojson = analizador.erroresjson()
    if contenidojson == None:
        MessageBox.showinfo('Advertencia','No hay errores que evaluar')
    else:
         #Guardar
        archivo = open('error.RESULTADOS_201906795.json','w')
        archivo.write(contenidojson)
        archivo.close()
        MessageBox.showinfo('Advertencia','Se creo el archivo "error.RESULTADOS_201906795.json"')
        print(contenidojson)

def Reporte():
    print('reporte')
    analizador.reporte()






########################################################################
raiz = Tk()
raiz.title('LFP Proyecto 1 | 201906795')
raiz.geometry('900x500')

btnanalizar = Button(raiz,text='Analizar', bg='#313446', fg='#FFFFFF', command=Analizar)
btnanalizar.place(x=230,y=10, width=80, height= 35)

btnerrores = Button(raiz,text='Errores', bg='#313446', fg='#FFFFFF', command=Errores)
btnerrores.place(x=370,y=10, width=80, height= 35)

btnreportes = Button(raiz,text='Reporte', bg='#313446', fg='#FFFFFF', command=Reporte)
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
