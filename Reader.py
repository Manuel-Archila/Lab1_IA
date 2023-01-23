import imageio.v3 as iio
import numpy as np

class Reader(object):
    def __init__(self):
        self.proporcion = 25
        self.sectores = []
        self.info = []


    def VerMatriz(self, m):
        for i in m:
            print(i)

    def discretizacion(self, img, binary_mat):
        self.proporcion = int(len(img) / 23)
        veces = int(len(img) / self.proporcion)
        bandera = True
        color_rojo = self.proporcion * self.proporcion * 0.3
        #print(color_rojo)  
        for i in range(0,veces):
            self.sectores.append([])
            for j in range(0, veces):
                contador = [0,0,0,0]
                for columna in range(i*self.proporcion,i*self.proporcion+self.proporcion):
                    for fila in range(j*self.proporcion,j*self.proporcion+self.proporcion):
                        try:
                            if binary_mat[columna][fila] == 0:
                                contador[0] += 1
                            elif binary_mat[columna][fila] == 1:
                                contador[1] += 1
                            elif binary_mat[columna][fila] == 2:
                                contador[2] += 1
                            elif binary_mat[columna][fila] == 3:
                                contador[3] += 1
                        except:
                            pass
                            #print(columna,fila)
                if contador[2] >= color_rojo and bandera:
                    self.sectores[i].append(2)
                    bandera = False
                elif contador[3]>=175:
                    try:
                        if self.sectores[i][j-1]!=3 and self.sectores[i-1][j]!=3:
                            self.sectores[i].append(3)
                        else:
                            self.sectores[i].append(1)
                    except:
                        self.sectores[i].append(1)
                        
                elif contador[0]>contador[1]:
                    self.sectores[i].append(0)
                elif contador[0]==contador[1]:
                    self.sectores[i].append(0)
                else:
                    self.sectores[i].append(1)
                contador = [0,0,0,0]
        
        return self.sectores

    def agrandar(self, img):

        matrizdiscrete=[
                    [5 for x in range(0,len(img))]
                    for y in range(0,len(img))]	


        veces = int(len(img) / self.proporcion)

        for i in range(0,veces):
                for j in range(0, veces):
                    for columna in range(i*self.proporcion,i*self.proporcion+self.proporcion):
                        for fila in range(j*self.proporcion,j*self.proporcion+self.proporcion):
                            try:
                                if self.sectores[i][j] == 0:
                                    matrizdiscrete[columna][fila]=0
                                elif self.sectores[i][j] == 1:
                                    matrizdiscrete[columna][fila]=1
                                    
                                elif self.sectores[i][j] == 2:
                                    matrizdiscrete[columna][fila]=2
                                    
                                elif self.sectores[i][j] == 3:
                                    matrizdiscrete[columna][fila]=3
                            except:
                                pass

        return matrizdiscrete

    def read(self,filename):

        # reading:
        img = iio.imread(filename)  

        # Base de la matrix de unos y ceros
        binary_mat = np.zeros((len(img), len(img[0])), dtype=np.uint8)

        # Asignar 0, 1, 2, 3 
        for i in range(len(img)):
            for j in range(len(img)):
                if img[i][j][0] >= 250 and img[i][j][1] >= 250 and img[i][j][2] >= 250:
                    binary_mat[i][j] = 1
                elif img[i][j][0] <= 80 and img[i][j][1] <= 80 and img[i][j][2] <= 80:
                    binary_mat[i][j] = 0
                elif img[i][j][0] >= 180 and img[i][j][1] >= 0 and img[i][j][2] >= 0:
                    binary_mat[i][j] = 2
                elif img[i][j][0] >= 0 and img[i][j][1] >= 180 and img[i][j][2] >= 0:
                    binary_mat[i][j] = 3

        return binary_mat, img






