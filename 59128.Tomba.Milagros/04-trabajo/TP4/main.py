from person import Person
from personService import PersonService


class Menu():
    def menu_personas(self):
        print("1. Agregar persona")
        print("2. Listar persona")
        print("3. Modificar persona")
        print("4. Borrar persona")
        print("5. Ejercicio TP")
        return int(input("Ingresar opcion: "))


if __name__ == '__main__':
    menu = Menu()
    personService = PersonService()

    while True:
        opcionElegida = menu.menu_personas()
        if opcionElegida == 1:
            personService.add_person()
        if opcionElegida == 2:
            print(personService.get_personList())
        if opcionElegida == 3:
            personService.update_person()
        if opcionElegida == 4:
            personService.delete_person()
        if opcionElegida == 5:
            '#Agregamos una persona'
            p1 = Person()
            p1.name = 'federico'
            p1.surname = 'gonzalez'
            p1.age = '20'
            personService.add_person(p1)

            '#Agregamos una persona'
            p1 = Person()
            p1.name = 'claudio'
            p1.surname = 'pico'
            p1.age = '33'
            personService.add_person(p1)

            '# #Agregamos al hermano **********************'
            p1 = Person()
            p1.name = 'Nicolas'
            p1.surname = 'pico'
            p1.age = '40'
            personService.add_person(p1)
            print(personService.get_personList())
            '# #Update fEDERICO'
            p1 = Person()
            p1.name = 'federico'
            p1.surname = 'gonzalez'
            p1.age = '12'
            personService.update_person(0, p1)
            print(personService.get_personList())
            '# #delte person'
            personService.delete_person(2)
            print(personService.get_personList())
