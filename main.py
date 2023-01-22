from Reader import Reader
from Writer import Writer
from Tablero import Tablero
from BFS import BFS



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
        dfs = BFS(tablero.Grafo, tablero.inicio, tablero.goal)
        nodof = (dfs.deep_first()).Padre
        
    
    Writer("Normal_Map.bmp", matrix, img)
    
    while nodof.Padre != nodof:
        matrix[nodof.position[0]][nodof.position[1]] = 4
        nodof = nodof.Padre

    #print(matrix)
    
    Writer("New_Map.bmp", matrix, img)
    
    