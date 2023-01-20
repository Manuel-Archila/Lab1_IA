from Reader import Reader
from Writer import Writer



if __name__ == '__main__':
    reader = Reader()
    binary, img = reader.read('./Test1.bmp')
    matrix = reader.discretizacion(img, binary)
    Writer("New_Map.bmp", matrix, img)

    
    