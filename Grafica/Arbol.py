from graphviz import *
from graphviz import Digraph


dot = None
cont = 0




def generagraficaarbol():
    global dot
    dot = Digraph('Grafica',filename='Grafica1', format='png')
    #dot.attr(rankdir='LR', size='8,5')

def configuraciones(configuraciones):
    global dot
    #dot.attr('node', shape='circle')
    dot.attr(
            "node",
            style="filled",
            fillcolor=configuraciones['fondo'],
            fontcolor=configuraciones['fuente'],
            shape=configuraciones['forma'],
        )

def agregarnodo(label):
    global dot, cont
    cont += 1
    nodonombre = 'x' + str(cont) 
    dot.node(nodonombre,str(label))
    return nodonombre

def conectarnodo(nodo1,nodo2):
    global dot
    dot.edge(str(nodo1),str(nodo2))

def render():
    global dot
    dot.render('Graficapng', view=True)