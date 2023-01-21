from Reader import Reader
from Writer import Writer
from Tablero import Tablero



if __name__ == '__main__':
    reader = Reader()
    binary, img = reader.read('./Test1.bmp')
    matrix = reader.discretizacion(img, binary)

    tablero = Tablero(matrix)

    tablero.create_Nodos()

    print(tablero.Grafo.nodes)

    Writer("New_Map.bmp", matrix, img)

    
    