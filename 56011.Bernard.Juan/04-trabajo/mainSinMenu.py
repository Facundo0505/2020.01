from person import Person
from personService import PersonService

if __name__ == '__main__':

    personService = PersonService()

    # Agregamos una persona
    p1 = Person()
    p1.name = 'federico'
    p1.surname = 'gonzalez'
    p1.age = '20'
    personService.add_person(p1)

    # Agregamos una persona
    p1 = Person()
    p1.name = 'claudio'
    p1.surname = 'pico'
    p1.age = '33'
    personService.add_person(p1)

    # Agregamos al hermano
    p1 = Person()
    p1.name = 'nicolas'
    p1.surname = 'pico'
    p1.age = '40'
    personService.add_person(p1)

    print(personService.get_personList())  # {0: {'_name': 'FEDERICO', '_surname': 'GONZALEZ', '_age': '20'}, 1: {'_name': 'CLAUDIO', '_surname': 'PICO', '_age': 33}, 2: {'_name': 'NICOLAS', '_surname': 'PICO', '_age': 40}}

    # Update FEDERICO
    personService.update_person(0)
    print(personService.get_personList())

    # delete person
    personService.delete_person(2)

    print(personService.get_personList())  # {0: {'_name': 'FEDERICO', '_surname': 'GONZALEZ', '_age': '30'}, 1: {'_name': 'CLAUDIO', '_surname': 'PICO', '_age': 33}}
