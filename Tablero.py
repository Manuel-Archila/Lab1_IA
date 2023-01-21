from Casillas import Casilla
import networkx as nx
from Casillas import Casilla

class Tablero():
    def __init__(self,matriz):
        self.Grafo = nx.Graph()
        self.matriz = matriz
        self.length = len(matriz)
        self.inicio = None
        self.MatrizNodes=[[0 for x in range(0,self.length)]
                                for y in range(0,self.length)]	
        
    def create_Nodos(self):
        
        for y in range(self.length):
            for x in range(self.length):
                if self.matriz[y][x] == 1 or self.matriz[y][x] == 2 or self.matriz[y][x] == 3:
                    CasillaTemp =  Casilla(self.matriz,x,y,self.matriz[y][x])
                    self.MatrizNodes[y][x] = CasillaTemp
                    self.Grafo.add_node(CasillaTemp)
                    
                    if self.matriz[y][x] == 2:
                        self.inicio = CasillaTemp

        for y in range(self.length):
            for x in range(self.length):
                if self.matriz[y][x] == 1 or self.matriz[y][x] == 2 or self.matriz[y][x] == 3:
                    
                    if self.matriz[y-1][x] == 1:
                        self.MatrizNodes[y][x].VecinoArriba = self.MatrizNodes[y-1][x]
                        self.Grafo.add_edge(self.MatrizNodes[y][x],self.MatrizNodes[y-1][x])
                        self.MatrizNodes[y-1][x].Padre = self.MatrizNodes[y][x]
                        
                    if self.matriz[y+1][x] == 1:
                        self.MatrizNodes[y][x].VecinoAbajo = self.MatrizNodes[y+1][x]
                        self.Grafo.add_edge(self.MatrizNodes[y][x],self.MatrizNodes[y+1][x])
                        self.MatrizNodes[y+1][x].Padre = self.MatrizNodes[y][x]
                        
                    if self.matriz[y][x-1] == 1:
                        self.MatrizNodes[y][x].VecinoIzquierda = self.MatrizNodes[y][x-1]
                        self.Grafo.add_edge(self.MatrizNodes[y][x],self.MatrizNodes[y][x-1])
                        self.MatrizNodes[y][x-1].Padre = self.MatrizNodes[y][x]
                        
                    if self.matriz[y][x+1] == 1:
                        self.MatrizNodes[y][x].VecinoDerecha = self.MatrizNodes[y][x+1]
                        self.Grafo.add_edge(self.MatrizNodes[y][x],self.MatrizNodes[y][x+1])
                        self.MatrizNodes[y][x+1].Padre = self.MatrizNodes[y][x]
        