print(" ")
print(" ")

class Punto2D(): 
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "(%d, %s)" % (self.x, self.y) 

class PuntoMejorado(Punto2D):
    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return 0
        if self.x > 0 and self.y > 0:
            return 1
        if self.x < 0 and self.y > 0:
            return 2
        if self.x > 0 and self.y < 0:
            return 3 
        return 4      

if __name__ == "__main__":

    p1 = PuntoMejorado(5, -6)
    
    print("Posicion: " + str(p1))

    print("Cuadrante: " + str(p1.cuadrante()))
