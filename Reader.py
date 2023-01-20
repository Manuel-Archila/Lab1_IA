import imageio.v3 as iio
import numpy as np

def VerMatriz(m):
        for i in m:
            print(i)

def discretizacion(matrizdiscrete):
    veces = int(len(img) / proporcion)
    bandera = True
        
    for i in range(0,veces):
        sectores.append([])
        for j in range(0, veces):
            contador = [0,0,0,0]
            for columna in range(i*proporcion,i*proporcion+proporcion):
                for fila in range(j*proporcion,j*proporcion+proporcion):
                    try:
                        if bin[columna][fila] == 0:
                            contador[0] += 1
                        elif bin[columna][fila] == 1:
                            contador[1] += 1
                        elif bin[columna][fila] == 2:
                            contador[2] += 1
                        elif bin[columna][fila] == 3:
                            contador[3] += 1
                    except:
                        pass
                        #print(columna,fila)
            if contador[2] >= 150 and bandera:
                sectores[i].append(2)
                bandera = False
            elif contador[3]>=175:
                try:
                    if sectores[i][j-1]!=3 and sectores[i-1][j]!=3:
                        sectores[i].append(3)
                    else:
                        sectores[i].append(1)
                except:
                    sectores[i].append(1)
                    
            elif contador[0]>contador[1]:
                sectores[i].append(0)
            elif contador[0]==contador[1]:
                sectores[i].append(0)
            else:
                sectores[i].append(1)
            contador = [0,0,0,0]
    
    VerMatriz(sectores)
    
    for i in range(0,veces):
            for j in range(0, veces):
                for columna in range(i*proporcion,i*proporcion+proporcion):
                    for fila in range(j*proporcion,j*proporcion+proporcion):
                        try:
                            if sectores[i][j] == 0:
                                matrizdiscrete[columna][fila]=0
                            elif sectores[i][j] == 1:
                                matrizdiscrete[columna][fila]=1
                                
                            elif sectores[i][j] == 2:
                                matrizdiscrete[columna][fila]=2
                                
                            elif sectores[i][j] == 3:
                                matrizdiscrete[columna][fila]=3
                        except:
                            pass

    return matrizdiscrete


# reading:
img = iio.imread("./Test1.bmp")

#''''''

bin = np.zeros((len(img), len(img[0])), dtype=np.uint8)


for i in range(len(img)):
    for j in range(len(img)):
        if img[i][j][0] >= 250 and img[i][j][1] >= 250 and img[i][j][2] >= 250:
            bin[i][j] = 1
        elif img[i][j][0] <= 80 and img[i][j][1] <= 80 and img[i][j][2] <= 80:
            bin[i][j] = 0
        elif img[i][j][0] >= 180 and img[i][j][1] >= 0 and img[i][j][2] >= 0:
            bin[i][j] = 2
        elif img[i][j][0] >= 0 and img[i][j][1] >= 180 and img[i][j][2] >= 0:
            bin[i][j] = 3

proporcion = 25
sectores = []
matrizdiscrete=[
            [5 for x in range(0,len(img))]
            for y in range(0,len(img))]	
    
penultima = discretizacion(matrizdiscrete)

ultima = [[None for x in range(0,len(img))]
            for y in range(0,len(img))]	
            
ultima = np.copy(img)


negro = np.array([0,0,0], dtype=np.uint8)
blanco = np.array([255,255,255], dtype=np.uint8)
rojo = np.array([255,0,0], dtype=np.uint8)
verde = np.array([0,255,0], dtype=np.uint8)



for i in range(len(penultima)):
    for j in range(len(penultima)):
        if penultima[i][j]==1:
            ultima[i][j] = blanco
        elif penultima[i][j]==0:
            ultima[i][j] = negro
        elif penultima[i][j]==2:
            ultima[i][j] = rojo
        elif penultima[i][j]==3:
            ultima[i][j] = verde


# writing:
iio.imwrite("out_image.bmp", ultima)






