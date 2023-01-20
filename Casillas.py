class Casilla():
    def __init__(self,matriz,x,y,color):
        self.position =[y,x]
        self.VecinoArriba=None
        self.VecinoAbajo=None
        self.VecinoDerecha=None
        self.VecinoIzquierda=None
        self.Padre = None
        self.color=color