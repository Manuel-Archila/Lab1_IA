class Casilla():
    def __init__(self,x,y,color):
        self.position =[y,x]
        self.VecinoArriba=None
        self.VecinoAbajo=None
        self.VecinoDerecha=None
        self.VecinoIzquierda=None
        self.Padre = None
        self.color=color
        
    def identificador(self):
        return [self.color,self.position[0],self.position[1]]
    def Movments(self):
        return [self.VecinoArriba,self.VecinoAbajo,self.VecinoDerecha,self.VecinoIzquierda]
    
    def __repr__(self):
        return (str(self.color)+", "+str(self.position))

    def color(self):
        return self.color