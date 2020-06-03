from repositorio import Repositorio
from persona import Persona


class Serviciopersona:
    def get_personList(self):
        print("\n----> \tLista de personas:\n")
        return Repositorio.persona

    # Agrega una persona en el dicionario person, definido en Repository
    def add_person(self, persona):
        print("\n----> \tAgregando persona...")
        key = len(Repositorio.persona)
        while key in Repositorio.persona:
            key = key + 1
        Repositorio.persona[key] = persona.__dict__
        print("\n----> \tAgregado.")

    # Actualiza datos de una person del diccionario person
    # key clave diccionario
    # object Person
    def update_person(self, key):
        if key in Repositorio.persona:
            print("\n----> \tModificando a %s , de key = %d..." % (Repositorio.persona[key], key))
            Repositorio.persona[key]['_nombre'] = input("\n----> \tIngrese el nuevo nombre: ").upper()
            Repositorio.persona[key]['_apellido'] = input("\n----> \tIngrese el nuevo apellido: ").upper()
            Repositorio.persona[key]['_edad'] = input("\n----> \tIngrese la nueva edad: ")
            print("\n----> \tModificado.")
        else:
            print("\n----> \tERROR: La clave no existe.")

    # Elimina persona segun key del dic person
    def delete_person(self, key):
        if key in Repositorio.persona:
            print("\n----> \tEliminando a %s , de key = %d..." % (Repositorio.persona[key], key))
            del Repositorio.persona[key]
            print("\n----> \tEliminado.")
        else:
            print("\n----> \tERROR: La clave no existe.")