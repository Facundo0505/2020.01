from repository import Repository
from person import Person


class PersonService:
    def get_personList(self):
        print("\n----> \tLista de personas:\n")
        return Repository.person

    # Agrega una persona en el dicionario person, definido en Repository
    def add_person(self, person):
        print("\n----> \tAgregando persona...")
        key = len(Repository.person)
        while key in Repository.person:
            key = key + 1
        Repository.person[key] = person.__dict__
        print("\n----> \tAgregado.")

    # Actualiza datos de una person del diccionario person
    # key clave diccionario
    # object Person
    def update_person(self, key):
        if key in Repository.person:
            print("\n----> \tModificando a %s , de key = %d..." % (Repository.person[key], key))
            Repository.person[key]['_name'] = input("\n----> \tIngrese el nuevo nombre: ").upper()
            Repository.person[key]['_surname'] = input("\n----> \tIngrese el nuevo apellido: ").upper()
            Repository.person[key]['_age'] = input("\n----> \tIngrese la nueva edad: ")
            print("\n----> \tModificado.")
        else:
            print("\n----> \tERROR: La clave no existe.")

    # Elimina persona segun key del dic person
    def delete_person(self, key):
        if key in Repository.person:
            print("\n----> \tEliminando a %s , de key = %d..." % (Repository.person[key], key))
            del Repository.person[key]
            print("\n----> \tEliminado.")
        else:
            print("\n----> \tERROR: La clave no existe.")
