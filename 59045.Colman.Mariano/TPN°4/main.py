from personService import PersonService


class Menu():
    def __init__(self):
        pass

    def menuPersona(self):
        print("\n  Menu de persona")
        print("\n--> 1 - Listar personas")
        print("--> 2 - Agregar persona")
        print("--> 3 - Modificar persona")
        print("--> 4 - Eliminar persona")
        print("--> 5 - Finalizar")
        return int(input("\n Ingrese un numero para seleccionar una opcion: "))


if __name__ == '__main__':
    menu = Menu()
    bucle = True
    while bucle == True:
        opcion = menu.menuPersona()
        if opcion == 1:
            servicePersona = PersonService()
            servicePersona.get_personList()
            servicePersona = None
        if opcion == 2:
            servicePersona = PersonService()
            servicePersona.add_person()
            servicePersona = None
        if opcion == 3:
            servicePersona = PersonService()
            servicePersona.update_person()
            servicePersona = None
        if opcion == 4:
            servicePersona = PersonService()
            servicePersona.delete_person()
            servicePersona = None
        if opcion == 5:
            bucle = False
