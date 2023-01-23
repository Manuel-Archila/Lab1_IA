import imageio.v3 as iio
import numpy as np

class Writer(object):
    def __init__(self, filename, sectores, img):
        self.proporcion = 25
        self.write(filename, sectores, img)

    def write(self, filename, sectores, img):
        self.proporcion = int(len(img) / 23)

        base_matrix = self.agrandar(img, sectores)


        Dibujo = [[None for x in range(0,len(img))]
                for y in range(0,len(img))]	
                
        Dibujo = np.copy(img)


        negro = np.array([0,0,0], dtype=np.uint8)
        blanco = np.array([255,255,255], dtype=np.uint8)
        rojo = np.array([255,0,0], dtype=np.uint8)
        verde = np.array([0,255,0], dtype=np.uint8)
        morado = np.array([255,0,255], dtype=np.uint8)
        



        for i in range(len(Dibujo)):
            for j in range(len(Dibujo)):
                if base_matrix[i][j]==1:
                    Dibujo[i][j] = blanco
                elif base_matrix[i][j]==0:
                    Dibujo[i][j] = negro
                elif base_matrix[i][j]==2:
                    Dibujo[i][j] = rojo
                elif base_matrix[i][j]==3:
                    Dibujo[i][j] = verde
                elif base_matrix[i][j]==4:
                    Dibujo[i][j] = morado



        # writing:
        iio.imwrite(filename, Dibujo)

    def agrandar(self, img, sectores):

        matrizdiscrete=[
                    [5 for x in range(0,len(img))]
                    for y in range(0,len(img))]	


        veces = int(len(img) / self.proporcion)

        for i in range(0,veces):
                for j in range(0, veces):
                    for columna in range(i*self.proporcion,i*self.proporcion+self.proporcion):
                        for fila in range(j*self.proporcion,j*self.proporcion+self.proporcion):
                            try:
                                if sectores[i][j] == 0:
                                    matrizdiscrete[columna][fila]=0
                                elif sectores[i][j] == 1:
                                    matrizdiscrete[columna][fila]=1
                                    
                                elif sectores[i][j] == 2:
                                    matrizdiscrete[columna][fila]=2
                                    
                                elif sectores[i][j] == 3:
                                    matrizdiscrete[columna][fila]=3
                                    
                                elif sectores[i][j] == 4:
                                    matrizdiscrete[columna][fila]=4
                            except:
                                pass
        return matrizdiscrete