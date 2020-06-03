from repository import Repository
from person import Person

class PersonService:

    def get_personList(self):
        print("\n--Listando Personas--\n")
        return Repository.diccionarioPerson

    def crearPersona(self):
        name = input("Ingrese un nombre: ")
        surname = input("Ingrese un apellido: ")
        age = int(input("Ingrese una edad: "))
        return Person(name, surname, age)

    def add_person(self, person=None):
        print("\n--Agregar Personas--\n")
        if person is None:
            person = self.crearPersona()
        key = len(Repository.diccionarioPerson)
        Repository.diccionarioPerson[key] = person.__dict__

    def update_person(self, key=None, person=None):
        print("\n--Modificar Personas--\n")
        if key is None:
            key = int(input("Ingrese una llave: "))
        if person is None:
            person = self.crearPersona()
        Repository.diccionarioPerson[key] = person.__dict__

    def delete_person(self, key=None):
        print("\n--Eliminar Personas--\n")
        if key is None:
            key = int(input("Ingrese una llave: "))
            del Repository.diccionarioPerson[key]
            