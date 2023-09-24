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

##  Estructura Carpetas

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

**Directorio raiz**

* **main.py**
   - contiene la interfaz grafica y llama a las funciones necesias de analizado, sjson .arbol y arimetica

* **error.RESULTADOS_201906795.json**
   - archivo json con un listado de errores

* **Grafica**
  * **GraficaArbol**
     - archivo temporal para la creacion de la grafica
  * **GraficaArbol.dot**
     - archivo para la creacion de la grafica con  graphviz 
  * **GraficaArbol.png**
     - imagen creada para mostrar la grafica

**Carpetas**
~~~
├── Analizador
│   ├── __init__.py
│   └── analizador.py
~~~
* **analizador.py**
    - codigo para el analizador lexico

~~~
├── Archivojson
│   ├── __init__.py
│   └── Sjson.py
~~~
* **Sjson.py**
   - codigo para leer archivo json

~~~
├── Grafica
│   ├── __init__.py
│   └── Arbol.py
~~~
* **Arbol.py**
    - codigo para crear graficas usando graphviz

~~~
├── Operaciones
│   ├── __init__.py
│   └── aritmetica.py
~~~
* **aritmetica.py**
    - codigo para operaciones aritmeticas (suma, resta, seno ... etc)
<br>
<br><br><br>
.
---

# main.py

~~~
from Operaciones import *
from Archivojson import *
from Analizador import *
~~~