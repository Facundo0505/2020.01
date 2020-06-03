from repository import Repository
from person import Person

class PersonService():
    def get_personList(self):
        Person.frame()
        print("\nLista de Personas")
        Person.frame()
        return Repository.person

    def createPerson(self):
        name = input("\nIngrese el nombre de la Persona: ")
        surname = input("Ingrese el apellido de la Persona: ")
        age = int(input("Ingrese la edad de la Persona: "))
        person = Person(name, surname, age)
        return person

    # Agrega una persona en el dicionario person, definido en Repository
    def add_person(self, person=None):
        Person.frame()
        print("\nAgregar Persona")
        Person.frame()

        if person is None:
            person = self.createPerson()
        key = len(Repository.person)
        Repository.person[key] = person.__dict__

        Person.frame()
        print("\n¡%s %s añadido exitosamente!" % (person.name, person.surname))
        Person.frame()

    # Actualiza datos de una person del diccionario person
    # Key clave diccionario
    # Object Person
    def update_person(self, key=None, opc=None):
        Person.frame()
        print("\nActualizar Persona")
        Person.frame()

        if key is None:
            key = int(input("\nIngrese el codigo de la persona: "))
        person = Repository.person[key]
        print("\nEsta es la persona: %s" % person)
        Person.frame()
        print("\n1. Nombre")
        print("2. Apellido")
        print("3. Edad")
        Person.frame()
        if opc is None:
            opc = int(input("\nIngrese el atributo que desea modificar: "))
        modify = input("\nIngrese el nuevo valor: ")
        if opc == 1:
            person['_name'] = modify.upper()
        if opc == 2:
            person['_surname'] = modify.upper()
        if opc == 3:
            person['_age'] = int(modify)
        
        Person.frame()
        print("\n¡Modificacion exitosa!\n%s" % person)
        Person.frame()

    # Elimina persona segun key del dic person
    def delete_person(self, key=None):
        Person.frame()
        print("\nEliminar Persona")
        Person.frame()
        if key is None:
            key = int(input("\nIngrese el codigo de la persona: "))
        opc = input("\n¿Seguro quiere borrar a %s %s del diccionario? Y/N\n"
                    % (Repository.person[key]['_name'],Repository.person[key]['_surname']))
        if opc.upper() == "Y":
            del Repository.person[key]
            Person.frame()
            print("\n¡Se elimino del diccionario correctamente!\n")
            Person.frame()
