# Manual Tenico

### Librerias utilizadas

* tkinter 
   + Interfa grafica 
* json
   + Leer y crear archivos json
* graphviz
   + Generador de graficas  
<br>


~~~
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import filedialog
from tkinter import messagebox as MessageBox
from graphviz import *
from graphviz import Digraph
import json
~~~

___

<br>

###  Estructura Carpetas

~~~
LFP_S2_2023_Proyecto1_201906795
├── Analizador
│   ├── __init__.py
│   └── analizador.py
├── Archivojson
│   ├── __init__.py
│   └── Sjson.py
├── Grafica
│   ├── __init__.py
│   └── Arbol.py
├── Operaciones
│   ├── __init__.py
│   └── aritmetica.py
├── error.RESULTADOS_201906795.json
├── GraficaArbol
├── GraficaArbol.dot
├── GraficaArbol.png
├── main.py
└── entrada.json
~~~