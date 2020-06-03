from repository import Repository
from person import Person


class PersonService:
    def __init__(self, repository):
        self.repository = repository

    def get_personList(self,):
        return Repository.person

    # Agrega una persona en el dicionario person, definido en Repository F
    def add_person(self, per=None):
        print("\n   Agregando persona: ")
        if per is None:
            name = input("Ingrese el nombre: ")
            surname = input("Ingrese el surname: ")
            age = int(input("Ingrese la edad: "))
            key = int(input("Ingrese la clave: "))

            per = Person(name, surname, age, key)
        print("\n   Agregando persona: %s " % per.name)

        Repository.person[per.key] = per.__dict__         # Ingreso al
        # respositorio, me paro en el diccionario
        # e ingreso con la variable local y la key
        # a la persona, __dict__ para que muestre el diccionario

    def update_person(self):
        print("\n Updating person")
        key = int(input('Ingrese código de persona a actualizar datos'))
        per = Repository.person[key]
        print("persona %s" % per)
        name = input("Ingrese el nombre: ")
        surname = input("Ingrese el surname: ")
        age = int(input("Ingrese la edad: "))
        person = Person(name, surname, age)
        Repository.person[key] = person.__dict__

    # Elimina persona segun key del dic person F

    def delete_person(self, key):
        print("\n   Eliminando persona")
        key = int(input("Ingrese key de la persona a eliminar"))
        del self.repository.person[key]
