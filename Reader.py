from Color import color
import struct
from math import floor

class Reader:
    def __init__(self, path):
        self.path = path
        self.pixels = []
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (195, 0, 0)
        self.green = (0, 0, 195)
        self.sectores = []
        self.veces = 0
        self.read()

    def VerMatriz(self,m):
        for i in m:
            print(i)

    
    def read(self):
        with open(self.path, 'rb') as image:
            image.seek(10)
            header_size = struct.unpack("=l", image.read(4))[0]
            image.seek(18)
            self.width = struct.unpack("=l", image.read(4))[0]
            self.height = struct.unpack("=l", image.read(4))[0]
            if self.width != self.height:
                print("La imagen no es cuadrada")
                return
            image.seek(header_size)
            for y in range(self.height):
                self.pixels.append([])
                for x in range(self.width):
                    b = ord(image.read(1))
                    g = ord(image.read(1))
                    r = ord(image.read(1))
                    if (r, g, b) == self.black:
                        self.pixels[y].append(
                            0
                        ) 
                    elif (r, g, b) == self.white:
                        self.pixels[y].append(
                            1
                        )
                    elif (r, g, b) >= self.red:
                        self.pixels[y].append(
                            2
                        )
                    elif (r, g, b) >= self.green:
                        self.pixels[y].append(
                            3
                        )
    def write(self, filename, framebuffer):
        f = open(filename, 'bw')
        
        #pixel header
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + self.width * self.height*3))
        f.write(word(0))
        f.write(word(0))
        f.write(dword(14 + 40))
        
        #info header
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.height * self.width * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        
        #pixel data
        for y in range(self.height):
            for x in range(self.width):
                #print(y, x)
                number = framebuffer[y][x]

                if number == 0:
                    f.write(color(0,0,0))

                if number == 1:
                    f.write(color(255,255,255))

                if number == 2:
                    f.write(color(255,0,0))

                if number == 3:
                    f.write(color(255,0,0))


        f.close()

    def get_color_with_intensity(self, tx, ty, intensity):
        x = round(tx * self.width)
        y = round(ty * self.height)

        b = round(self.pixels[y][x][0] * intensity)
        g = round(self.pixels[y][x][1] * intensity)
        r = round(self.pixels[y][x][2] * intensity)

        return color(
            max(min(r, 255), 0),
            max(min(g, 255), 0),
            max(min(b, 255), 0))

    def discretizacion(self):

        porcentaje = 2
        proporcion = floor(self.width * (porcentaje/100))
        self.veces = int(100 / porcentaje)


        for i in range(0, self.width-proporcion, proporcion):
            for j in range(0, self.height-proporcion, proporcion):
                contador = [0,0,0,0]
                for columna in range((i+proporcion)):
                    for fila in range((j+proporcion)):
                        if self.pixels[columna][fila] == 0:
                            contador[0] += 1
                        elif self.pixels[columna][fila] == 1:
                            contador[1] += 1
                        elif self.pixels[columna][fila] == 2:
                            contador[2] += 1
                        elif self.pixels[columna][fila] == 3:
                            contador[3] += 1
                if contador[0]>contador[1]:
                    self.sectores.append(0)
                elif contador[0]==contador[1]:
                    self.sectores.append(0)
                else:
                    self.sectores.append(1)
                contador = [0,0,0,0]
                

        matrizdiscrete = []


        contador = 0
        for fila in range(self.veces):
            matrizdiscrete.append([])
            for columna in range(self.veces):
                for repetido in range(proporcion):
                    matrizdiscrete[fila].append(self.sectores[contador])
                contador += 1

        return matrizdiscrete


            

        
            





        