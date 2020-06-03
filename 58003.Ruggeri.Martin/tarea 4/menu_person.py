from person_service import PersonService
from person_repository import PersonRepository


class App():
    def __init__(self):
        self.persons_db = PersonRepository({})

    def menu_person(self):
        print("\n\n1. Listar persons")
        print("2. Agregar person")
        print("3. Modificar person")
        print("4. Eliminar person")
        print("5. Salir\n")
        return int(input("Elija una opción: "))

    def menu_modificar(self):
        print("\n1. cambiar nombre")
        print("2. cambiar apellido")
        print("3. cambiar edad")
        print("4. retroceder\n")
        return int(input("Elija una opción: "))


if __name__ == '__main__':
    app = App()
    while True:
        opcion_person = app.menu_person()
        service = PersonService(app.persons_db)
        if opcion_person == 1:
            service.listar()
        if opcion_person == 2:
            service.agregar_person()
        if opcion_person == 3:
            modificar = app.menu_modificar()
            if modificar > 0 and modificar < 4:
                service.modificar(modificar)
            else:
                break
        if opcion_person == 4:
            service.eliminar()
        if opcion_person < 1 or opcion_person > 4:
            break
        