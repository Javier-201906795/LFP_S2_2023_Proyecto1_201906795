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
<br><br><br><br><br><br><br>
.
---

# main.py

La interfaz gráfica, provista de botones, invoca las funciones correspondientes para operar con Graphviz y realizar operaciones aritméticas con el fin de resolver problemas, en colaboración con el analizador léxico.
<br>

importaciones librerias
~~~
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import filedialog
from tkinter import messagebox as MessageBox
~~~

importaciones codigo
~~~
from Operaciones import *
from Archivojson import *
from Analizador import *
~~~

### Funciones
**Estructura funciones**
~~~
main.py
├── Abrir()
│   └── SJson.jsonabrirarchivo(rutaarchivo)
├── Guardar()
├── Guardarcomo()
├── Salir()
├── Analizar()
│   └── analizador.lexico(texto)
├── Errores()
│   └── analizador.erroresjson()
├── Reporte()
│   └── analizador.reporte()
├── {
        Codigo tkinter 
    }
~~~
<br><br><br><br><br><br><br>
.
---

# aritmetica.py
Estructura carpeta
~~~
LFP_S2_2023_Proyecto1_201906795
├── Operaciones
│   ├── __init__.py
│   └── aritmetica.py
~~~
---
**Estructura funciones**
~~~
aritmetica.py
├── suma(num1,num2)
├── resta(num1,num2)
├── multiplicacion(num1,num2)
├── division(num1,num2)
├── potencia(num,numpotencia)
├── raiz(num,raiz)
├── inverso(num)
├── seno(num)
├── coseno(num)
├── tangente(num)
└── mod(num)
~~~
<br><br><br><br><br><br><br><br>
.
---

# Sjson.py
~~~
Sjson.py
└── jsonabrirarchivo(ruta)
~~~
<br><br><br><br><br><br><br><br>
.
---
# Arbol.py
~~~
aritmetica.py
├── reiniciarvalores()
├── generagraficaarbol()
├── configuraciones(configuraciones)
├── agregarnodo(label)
├── conectarnodo(nodo1,nodo2)
└── render()
~~~
<br><br><br><br><br><br><br><br>
.
# analizador.py
~~~
analizador.py
├── obtenertexto(text,a)
├── obtenernumero(text,a)
├── obtenertokens(texto)
├── obtener_instruccion()
├── formar_instrucciones()
│   └── obtener_instruccion(texto)
├── esunnumero(posiblenumero)
├── evaluar_tipo_operacion(operacion, valor1, valor2)
├── interpretar_instruccion(operacion,valor1,valor2)
│    ├── esunumero(posiblenumero)
│    ├── interpretar_instruccion(operacion,valor1,valor2)
│    └── evaluar_tipo_operacion(operacion,valor1,valor2)
├── realizar_instruccion()
│   └── interpretar_instruccion(operacion,valor1,valor2)
├── lexico(texto)
│    ├── Arbol.generagraficaarbol()
│    ├── obtenertokens(texto)
│    ├── formar_instrucciones()
│    ├── Arbol.configuraciones(configuraciones)
│    └── realizar_instruccion()
├── reporte()
│    ├── Arbol.render()
│    └── Arbol.reiniciarvalores()
├── erroresjson()
~~~