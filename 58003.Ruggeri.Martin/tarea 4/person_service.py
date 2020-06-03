from person import Person
       

class PersonService():
    
    def __init__(self, repository):
        self.repository = repository

    def listar(self):
        print("\n     Listando")
        for key in self.repository.person:
            print("-> %s" % (self.repository.person[key]))

    def agregar_person(self):
        print("\n     Agregando")
        person = Person()
        person.ingresar()
        self.repository.person[person.key] = person

    def eliminar(self):
        print("\n     Eliminando")
        key = input("Ingrese código a Eliminar: ")
        del self.repository.person[key]

    def modificar(self, modificar):
        print("\n     Modificando")
        key = input("Ingrese código a Modificar: ")
        person = self.repository.person[key]
        print("Person %s " % person)
        person.modificar(modificar)
        self.repository.person[key] = person