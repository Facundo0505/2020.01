class Actor():
    def __init__(self, nombre, personajes):
        self.nombre = nombre
        self.personajes = personajes

    def getActor(self):
        print("\n")
        return "Nombre: %s, Personajes: %s" % (
                self.nombre, self.personajes)

    def getDiccActor(self):
        return self.__dict__


if __name__ == "__main__":
    # peli = Pelicula("test", 20, "nada", "")
    # print(peli.getPelicula())
    pass
