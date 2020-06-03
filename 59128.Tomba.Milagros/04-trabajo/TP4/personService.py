from repository import Repository
from person import Person


class PersonService():

    def get_personList(self):
        print("LISTAR PERSONAS")
        print(Repository.personDict)

    def crearPesona(self):
        name = input("Ingrese un nombre: ")
        surname = input("Ingrese un apellido: ")
        age = int(input("Ingrese un edad: "))
        return Person(name, surname, age)

    '#Agrega una persona en el dicionario person, definido en Repository'
    def add_person(self, person):
        print("\n----AGREGAR PERSONA")
        if person is None:
            person = self.crearPesona()
        key = len(Repository.personDict)
        Repository.personDict[key] = person.__dict__

    '#Actualiza datos de una person del diccionario person'
    '#key clave diccionario '
    '#object Person'
    def update_person(self, key, person):

        print("\n----MODIFICAR PERSONA")
        if key is None:
            key = int(input("Ingrese una llave: "))
        if person is None:
            person = self.crearPesona()
        Repository.personDict[key] = person.__dict__

    '#Elimina persona segun key del dic person'
    def delete_person(self, key):
        print("\n----ELIMINAR PERSONA")
        if key is None:
            key = int(input("Ingrese una llave: "))
        del Repository.personDict[key]
