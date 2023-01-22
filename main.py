from Reader import Reader
from Writer import Writer
from Tablero import Tablero
from BFS import BFS



if __name__ == '__main__':
    reader = Reader()
    binary, img = reader.read('./Test2.bmp')
    matrix = reader.discretizacion(img, binary)

    tablero = Tablero(matrix)

    tablero.create_Nodos()

    bfs = BFS(tablero.Grafo, tablero.inicio, tablero.goal)
    
    nodof = (bfs.breadth_first()).Padre
    
    while nodof.Padre != nodof:
        matrix[nodof.position[0]][nodof.position[1]] = 4
        nodof = nodof.Padre

    #print(matrix)
    
    Writer("New_Map.bmp", matrix, img)
    
    