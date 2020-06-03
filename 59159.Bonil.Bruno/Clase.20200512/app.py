from pelicula_repository import PeliculaRepository
from pelicula_service import PeliculaService

class App():
    def __init__(self):
        self.repository = PeliculaRepository()
    def menu(self):
        print("1. Agregar pelicula")
        print("2. Listar pelicula")
        print("3. Modificar pelicula")
        print("4. Eliminar pelicula")
        return int(input("Elija una opción: "))

if __name__ == '__main__':
    app = App()
    opcion = app.menu()
    if opcion == 1:
        service = PeliculaService(app.repository)
        service.agregar_pelicula()
        service = None
    if opcion == 2:
        service = PeliculaService(app.repository)
        service.listar()
        service = None
    if opcion == 3:
        pass
    if opcion == 4:
        pass
    
    if (opcion < 1 or opcion > 4):
        pass
  