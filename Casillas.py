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
        #return [self.VecinoArriba,self.VecinoAbajo,self.VecinoDerecha,self.VecinoIzquierda]
        #return [self.VecinoIzquierda,self.VecinoAbajo,self.VecinoArriba,self.VecinoDerecha]
        #return [self.VecinoIzquierda,self.VecinoArriba,self.VecinoAbajo,self.VecinoDerecha]
        return [self.VecinoDerecha,self.VecinoArriba,self.VecinoIzquierda,self.VecinoAbajo]
    
    def __repr__(self):
        return (str(self.color)+", "+str(self.position))

    def color(self):
        return self.color