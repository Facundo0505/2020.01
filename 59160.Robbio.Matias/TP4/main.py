from person import Person
from personService import PersonService

if __name__ == '__main__':
    personService = PersonService()

    p1 = Person()
    p1.name = 'federico'
    p1.surname = 'gonzalez'
    p1.age = '20'
    personService.add_person(p1)

    p1 = Person()
    p1.name = 'claudio'
    p1.surname = 'pico'
    p1.age = '33'
    personService.add_person(p1)

    p1 = Person()
    p1.name = 'nicolás'
    p1.surname = 'pico'
    p1.age = '30'
    personService.add_person(p1)
    print(personService.get_personList())

    p1 = Person()
    p1.name = 'federico'
    p1.surname = 'gonzalez'
    p1.age = '30'
    personService.update_person(0, p1)
    print(personService.get_personList())

    personService.delete_person(2)
    print(personService.get_personList())
