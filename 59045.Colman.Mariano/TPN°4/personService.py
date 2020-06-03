from repository import Repository
from person import Person


class PersonService:
    def __init__(self):
        pass

    def get_personList(self):
        print("\nLista de personas:")
        print(Repository.person)

    def add_person(self):
        print("\n Agregar persona")
        persona = Person()
        persona.agregarPersona()
        key = persona.key
        per = {"Nombre": persona.name.upper(), "Apellido": persona.surname.upper(), "Edad": persona.age}
        Repository.person[key] = per

    def update_person(self):
        print("\n Update persona")
        persona = Person()
        print("\n La lista de personas es: ")
        print(Repository.person)
        persona.updatearPersona()
        clave = persona.key
        print("\n La persona a actualizar es:")
        print(Repository.person[clave])
        respuesta = str(input("\nEsta seguro que quiere modificar esta persona? (S/N): "))
        if respuesta.upper() == "S":
            persona.updatearPersona(True)
            per = {"Nombre": persona.name.upper(), "Apellido": persona.surname.upper(), "Edad": persona.age}
            Repository.person[clave] = per
        elif respuesta.upper() == "N":
            pass

    # Elimina persona segun key del dic person
    def delete_person(self):
        print("\n Eliminar persona")
        persona = Person()
        print("\n La lista de personas es: ")
        print(Repository.person)
        persona.eliminarPersona()
        clave = persona.key
        print("\nLa persona a eliminar es: ")
        print(Repository.person[clave])
        respuesta = str(input("\nEsta seguro que quiere eliminar esta persona? (S/N): "))
        if respuesta.upper() == "S":
            del Repository.person[clave]
        elif respuesta.upper() == "N":
            pass
