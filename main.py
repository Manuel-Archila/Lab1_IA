from Reader import Reader
from Writer import Writer
from Tablero import Tablero
from BFS import BFS
from DFS import DFS
from AStarUno import AStarUno




if __name__ == '__main__':
    reader = Reader()
    binary, img = reader.read('./Test1.bmp')
    matrix = reader.discretizacion(img, binary)

    tablero = Tablero(matrix)

    tablero.create_Nodos()
    nodof=None
    print(" 1. BFS \n 2. DFS \n 3. A*") 
    opcion = input("Ingrese la opción a utilizar: ")
    if opcion == "1":
        bfs = BFS(tablero.Grafo, tablero.inicio, tablero.goal)
        nodof = (bfs.breadth_first()).Padre
        
    elif opcion == "2":
        dfs = DFS(tablero.Grafo, tablero.inicio, tablero.goal)
        visited = []
        nodof = (dfs.deep_first(tablero.inicio, visited)).Padre
        
    elif opcion == "3":
        A = AStarUno(tablero.matriz, tablero.inicio, tablero.goal)
        visited = []
        nodof = (A.astar(tablero.inicio, visited)).Padre
        
        
    
    Writer("Normal_Map.bmp", matrix, img)
    
    while nodof.Padre != nodof:
        matrix[nodof.position[0]][nodof.position[1]] = 4
        nodof = nodof.Padre

    #print(matrix)
    
    Writer("New_Map.bmp", matrix, img)
    
    