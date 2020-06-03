from repository import Repository
from person import Person

class PersonService:

    def get_personList(self):
        print(Repository.dictPerson)

    #Agrega una persona en el diccionario person con una clave
    def add_person(self, person):
        clave = len(Repository.dictPerson)
        Repository.dictPerson[clave] = person.__dict__

    #Actualiza datos de una person del diccionario person
    #key clave diccionario 
    #object Person
    def update_person(self ,clave):
        num = 1
        while num != 0:
            print('Opciones: ')
            print('1. Modificar edad')
            print('2. Modificar nombre')
            print('3. Modificar apellido')
            opcion = int(input('Elija una opcion:'))
            if opcion == 1:
                nuevaEdad = int(input('Introduzca la nueva edad: '))
                Repository.dictPerson[clave]["_age"] = nuevaEdad
                print(Repository.dictPerson)
            elif num == 2:
                nuevoNombre = input('Introduzca el nuevo nombre: ')
                Repository.dictPerson[clave]["_name"] = nuevoNombre
                print(Repository.dictPerson)
            elif num == 3:
                nuevoApellido = input('Introduzca el nuevo apellido: ')
                Repository.dictPerson[clave]["_surname"] = nuevoApellido
                print(Repository.dictPerson)
            terminar = str(input("Terminar operacion: "))
            if terminar == "si":
                break

            
    #Elimina persona segun key del dic person
    def delete_person(self ,clave):
        del Repository.dictPerson[clave]
