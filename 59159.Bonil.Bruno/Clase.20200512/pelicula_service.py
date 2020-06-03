from pelicula_repository import PeliculaRepository
from pelicula import Pelicula

class PeliculaService():
    def __init__(self, repository):
        self.repository = repository
    def listar(self):
        print("Listar")
        self.repository = PeliculaRepository()
        if self.repository.peliculas is not None:
            for key in self.repository.peliculas:
                print ("Listar %s %s" % (key, self.repository.peliculas[key]))
        
    def agregar_pelicula(self):
        print("Agregar: ")
        pelicula = Pelicula()
        pelicula.ingresar()
        self.repository.peliculas[pelicula.key] = pelicula

    def eliminar(self):
       