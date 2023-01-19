from math import floor
from WriteUtilities import *
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
        self.matrizdiscrete = []
        self.porcentaje = 4
        self.bandera = True
        self.proporcion =25
        self.read()
        self.Llenar()
        

    def VerMatriz(self,m):
        for i in m:
            print(i)

    def Llenar(self):
        divi = floor(self.width / self.proporcion)
        faltante = self.proporcion*(divi+1) - self.width
        
        print(faltante)
        
        
        
        for i in range(0,faltante):
            self.pixels.append([])
            for j in range(0,self.width+faltante):
                self.pixels[self.width+i].append(5)
        
           
        for i in range(0,self.width):
            for j in range(0,faltante):
                self.pixels[i].append(5)
        
        print(self.pixels[4])
        print(len(self.pixels[4]))
        
        
        self.matrizdiscrete = self.pixels    
        self.write("Prueba.bmp")
        
            
        
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
                    elif (r,g,b) >= self.morado:
                        self.pixels[y].append(
                            5
                        )

                    
        

    
    def write(self, filename):
        f = open(filename, 'bw')
        
        #pixel header
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + (len(self.matrizdiscrete)) * (len(self.matrizdiscrete))*3))
        f.write(word(0))
        f.write(word(0))
        f.write(dword(14 + 40))
        
        #info header
        f.write(dword(40))
        f.write(dword((len(self.matrizdiscrete))))
        f.write(dword((len(self.matrizdiscrete))))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword((len(self.matrizdiscrete)) * (len(self.matrizdiscrete)) * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        
        #pixel data
        for y in range(len(self.matrizdiscrete)):
            for x in range(len(self.matrizdiscrete)):

                number = self.matrizdiscrete[y][x]
                
                if number == 0:
                    f.write(color(0,0,0))

                if number == 1:
                    f.write(color(255,255,255))

                if number == 2:
                    f.write(color(255,0,0))

                if number == 3:
                    f.write(color(0,0,255))

                if number == 5:
                    f.write(color(255,255,0))
                


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

        self.veces = int(len(self.pixels)/self.proporcion)
        
        print("pixeles",len(self.pixels))
        print("pixeles[0]",len(self.pixels[0]))
        
        for i in range(0, self.veces):
            self.sectores.append([])
            for j in range(0, self.veces):
                contador = [0,0,0,0]
                for columna in range(i*self.proporcion,i*self.proporcion+self.proporcion):
                    for fila in range(j*self.proporcion,j*self.proporcion+self.proporcion):
                        try:
                            if self.pixels[columna][fila] == 0:
                                contador[0] += 1
                            elif self.pixels[columna][fila] == 1:
                                contador[1] += 1
                            elif self.pixels[columna][fila] == 2:
                                contador[2] += 1
                            elif self.pixels[columna][fila] == 3:
                                contador[3] += 1
                        except:
                            print(columna,fila)
                if contador[2] != 0 and self.bandera:
                    self.sectores[i].append(2)
                    self.bandera = False
                elif contador[0]>contador[1]:
                    self.sectores[i].append(0)
                elif contador[0]==contador[1]:
                    self.sectores[i].append(0)
                else:
                    self.sectores[i].append(1)
                contador = [0,0,0,0]
        
        
        self.VerMatriz(self.sectores)
        print(len(self.sectores))
        print(len(self.sectores[0]))
        
        
        self.matrizdiscrete=[
            [5 for x in range(0,self.veces*self.proporcion)]
            for y in range(0,self.veces*self.proporcion)]
        
        
        print(len(self.matrizdiscrete),len(self.matrizdiscrete[0]))
        
        
        
        
        #self.VerMatriz(self.sectores)
        
        for i in range(0, self.veces):
            for j in range(0, self.veces):
                for columna in range(i*self.proporcion,i*self.proporcion+self.proporcion):
                    for fila in range(j*self.proporcion,j*self.proporcion+self.proporcion):
                        if self.sectores[i][j] == 0:
                            self.matrizdiscrete[columna][fila]=0
                            
                        elif self.sectores[i][j] == 1:
                            self.matrizdiscrete[columna][fila]=1
                            
                        elif self.sectores[i][j] == 2:
                            self.matrizdiscrete[columna][fila]=2
                            
                        elif self.sectores[i][j] == 3:
                            self.matrizdiscrete[columna][fila]=3
                            
    #def discretizar(self):
        
        
                
                
            
            

        


            

        
            





        