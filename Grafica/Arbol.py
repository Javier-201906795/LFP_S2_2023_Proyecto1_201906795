from graphviz import *
from graphviz import Digraph


dot = None

def hola():
    print('hola')


def generagraficaarbol():
    global dot
    dot = Digraph('Grafica',filename='Grafica1', format='png')
    dot.attr(rankdir='LR', size='8,5')

def configuraciones():
    global dot
    dot.attr('node', shape='circle')

def agregarnodo():
    global dot
    dot.node('x1','10')
    dot.node('x2','25')
    dot.node('x3','suma\n35')

def conectarnodo():
    global dot
    dot.edge('x3','x1')
    dot.edge('x3','x2')

def render():
    global dot
    dot.render('Graficapng', view=True)