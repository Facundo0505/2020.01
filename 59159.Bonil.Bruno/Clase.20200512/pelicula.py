class Pelicula():
    def __init__(self, key={}, title="", duracion=0, genero="", personajes={}):
        self.key = key
        self.title = title
        self.duracion = duracion
        self.genero = genero
        self.personajes = personajes

    def __str__(self):
        return "%s %d %s %s" % (self.title, self.duracion, self.genero, self.personajes)
    
    def ingresar(self):
        print("Ingresando Pelicula")
        self.title = input("Ingrese Tiutlo: ")
        self.duracion = int(input("Ingrese duracion como número:"))
        self.genero = input("Ingrese género: ")
        self.personajes = {}
