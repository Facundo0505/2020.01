from persona import Persona
from serviciopersona import Serviciopersona

class App:
    def menu_persona(self):
        print("\n\n\tMENU - Persona")
        print("\n1.\tListar personas")
        print("2.\tAgregar una persona")
        print("3.\tModificar una persona")
        print("4.\tEliminar una persona")
        print("  \tSalir (otra tecla)")
        return int(input("\n\tElija una opción: "))

if __name__ == '__main__':
    serviciopersona = Serviciopersona()

    # Agregamos una persona
    p1 = Persona()
    p1.nombre = 'federico'
    p1.apellido = 'gonzalez'
    p1.edad = '20'
    serviciopersona.add_person(p1)

    # Agregamos una persona
    p1 = Persona()
    p1.nombre = 'claudio'
    p1.apellido = 'pico'
    p1.edad = '33'
    serviciopersona.add_person(p1)

    # Agregamos al hermano
    p1 = Persona()
    p1.nombre = 'nicolas'
    p1.apellido = 'pico'
    p1.edad = '40'
    serviciopersona.add_person(p1)

    print(serviciopersona.get_personList())  # {0: {'_name': 'FEDERICO', '_surname': 'GONZALEZ', '_age': '20'}, 1: {'_name': 'CLAUDIO', '_surname': 'PICO', '_age': 33}, 2: {'_name': 'NICOLAS', '_surname': 'PICO', '_age': 40}}

    # Actualizacion de FEDERICO
    serviciopersona.update_person(0)
    print(serviciopersona.get_personList())

    # borrar persona
    serviciopersona.delete_person(2)

    print(serviciopersona.get_personList())  # {0: {'_name': 'FEDERICO', '_surname': 'GONZALEZ', '_age': '30'}, 1: {'_name': 'CLAUDIO', '_surname': 'PICO', '_age': 33}}

    # menú
    app = App()
    while True:
        opcion_persona = app.menu_persona()
        if opcion_persona == 1:
            print(serviciopersona.get_personList())
        if opcion_persona == 2:
            _nombre = input("\n----> \tIngrese el nombre de la persona: ").upper()
            _apellido = input("\n----> \tIngrese el apellido de la persona: ").upper()
            _edad = input("\n----> \tIngrese la edad de la persona: ")
            px = Persona(_nombre, _apellido, _edad)
            serviciopersona.add_person(px)
        if opcion_persona == 3:
            key = int(input("\n----> \tIngrese la key de la persona que quiere modificar: "))
            serviciopersona.update_person(key)
        if opcion_persona == 4:
            key = int(input("\n----> \tIngrese la key de la persona que quiera eliminar: "))
            serviciopersona.delete_person(key)
        if opcion_persona < 1 or opcion_persona > 4:
            break