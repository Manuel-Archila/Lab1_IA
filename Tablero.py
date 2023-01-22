from Casillas import Casilla
import networkx as nx
from Casillas import Casilla

class Tablero():
    def __init__(self,matriz):
        self.Grafo = nx.Graph()
        self.matriz = matriz
        self.length = len(matriz)
        self.inicio = None
        self.goal = []
        self.MatrizNodes=[[0 for x in range(0,self.length)]
                                for y in range(0,self.length)]	
        
    def create_Nodos(self):
        
        for y in range(self.length):
            for x in range(self.length):
                if self.matriz[y][x] == 1 or self.matriz[y][x] == 2 or self.matriz[y][x] == 3:
                    CasillaTemp =  Casilla(x,y,self.matriz[y][x])
                    #print(CasillaTemp)
                    self.MatrizNodes[y][x] = CasillaTemp
                    self.Grafo.add_node(CasillaTemp)
                    
                    if self.matriz[y][x] == 2:
                        CasillaTemp.Padre = CasillaTemp
                        self.inicio = CasillaTemp
                        

                    if self.matriz[y][x] == 3:
                        self.goal.append(CasillaTemp)
                        
                        

        for y in range(self.length):
            for x in range(self.length):
                if self.matriz[y][x] == 1 or self.matriz[y][x] == 2 or self.matriz[y][x] == 3:

                    try:
                        if self.matriz[y-1][x] == 1 and y != 0 or self.matriz[y-1][x] == 3:
                            self.MatrizNodes[y][x].VecinoArriba = self.MatrizNodes[y-1][x]
                            self.Grafo.add_edge(self.MatrizNodes[y][x],self.MatrizNodes[y-1][x])
                            
                    except:
                        pass
                    
                    try:
                        if self.matriz[y+1][x] == 1 or self.matriz[y+1][x] == 3:
                            self.MatrizNodes[y][x].VecinoAbajo = self.MatrizNodes[y+1][x]
                            self.Grafo.add_edge(self.MatrizNodes[y][x],self.MatrizNodes[y+1][x])
                            
                    except:
                        pass
                    
                    try:
                        if self.matriz[y][x-1] == 1 and x !=0 or self.matriz[y][x-1] == 3:
                            self.MatrizNodes[y][x].VecinoIzquierda = self.MatrizNodes[y][x-1]
                            self.Grafo.add_edge(self.MatrizNodes[y][x],self.MatrizNodes[y][x-1])
                            
                    except:
                        pass
                    
                    try:
                        if self.matriz[y][x+1] == 1 or self.matriz[y][x+1] == 3:
                            self.MatrizNodes[y][x].VecinoDerecha = self.MatrizNodes[y][x+1]
                            self.Grafo.add_edge(self.MatrizNodes[y][x],self.MatrizNodes[y][x+1])
                            
                    except:
                        pass
        