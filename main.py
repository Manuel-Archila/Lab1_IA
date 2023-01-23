from Reader import Reader
from Writer import Writer
from Tablero import Tablero
from BFS import BFS
from DFS import DFS
from AStarUno import AStarUno
from AStarDos import AStarDos





if __name__ == '__main__':
    reader = Reader()
    binary, img = reader.read('./Test7.bmp')
    matrix = reader.discretizacion(img, binary)

    tablero = Tablero(matrix)
    name=""
    nodof=None
    print(" 1. BFS \n 2. DFS \n 3. A*(1) \n 4. A*(2)") 
    tablero.create_Nodos()
    
    opcion = input("Ingrese la opción a utilizar: ")
    if opcion == "1":
        bfs = BFS(tablero.Grafo, tablero.inicio, tablero.goal)
        nodof = (bfs.breadth_first()).Padre
        name="BFS"
        
    elif opcion == "2":
        dfs = DFS(tablero.Grafo, tablero.inicio, tablero.goal)
        visited = []
        nodof = (dfs.deep_first(tablero.inicio, visited)).Padre
        name="DFS"
        
    elif opcion == "3":
        A = AStarUno(tablero.matriz, tablero.inicio, tablero.goal)
        visited = []
        nodof = (A.astar(tablero.inicio, visited)).Padre
        name="A-star(1)"

    elif opcion == "4":
        A = AStarDos(tablero.matriz, tablero.inicio, tablero.goal)
        visited = []
        nodof = (A.astar(tablero.inicio, visited)).Padre
        name="A-star(2)"
        
        
    
    Writer("Normal_Map.bmp", matrix, img)
    
    while nodof.Padre != nodof:
        matrix[nodof.position[0]][nodof.position[1]] = 4
        nodof = nodof.Padre

    #print(matrix)
    
    Writer("./Soluciones/"+name+"_New_Map.bmp", matrix, img)
    
    