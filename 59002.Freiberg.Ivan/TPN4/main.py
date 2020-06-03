from person import Person
from personService import PersonService
from repository import Repository


class Main():

    def menu_personas(self):
        print("1: Listar personas")
        print("2: Agregar personas")
        print("3: Modificar personas")
        print("4: Eliminar personas")
        print("5: Mostrar ejercicio completo: ")
        return int(input("Elija una opcion: "))

    def menu(self):
        print("Menu personas")


if __name__ == '__main__':
    main = Main()

    personService = PersonService(Repository)

    while True:
        opcionElegida = main.menu_personas()
        print("\n --------------------------------------")

        if opcionElegida == 1:
            print(personService.get_personList())

        if opcionElegida == 2:
            personService.add_person()

        if opcionElegida == 3:
            personService.update_person()

        if opcionElegida == 4:
            personService.delete_person()

        if opcionElegida == 5:


            # Agregamos una persona

            p1 = Person()
            p1.key = 1
            p1.name = 'federico'
            p1.surname = 'gonzalez'
            p1.age = '20'
            personService.add_person(p1)

            # Agregamos una persona
            p2 = Person()
            p2.key = 2
            p2.name = 'claudio'
            p2.surname = 'pico'
            p2.age = '33'
            personService.add_person(p2)

            # Agregamos al hermano **********************

            p3 = Person()
            p3.key = 3
            p3.name = "Nicolás"
            p3.surname = "Pico"
            p3.age = "40"

            personService.add_person(p3)

            print(personService.get_personList())
            # {0: {'_name': 'FEDERICO', '_surname': 'GONZALEZ', '_age': '20'},
            # 1: {'_name': 'NICOLAS', '_surname': 'PICO', '_age': 30},
            # 2: {'_name': 'NICOLAS', '_surname': 'PICO', '_age': 30}}
            # Update fEDERICO
            personService.update_person()
            print(personService.get_personList())


            # delte person
            personService.delete_person(2)

            print(personService.get_personList())
            # {0: {'_name': 'FEDERICO', '_surname': 'GONZALEZ', '_age': '20'},
            # 1: {'_name': 'NICOLAS', '_surname': 'NICOLAS', '_age': 41}}
