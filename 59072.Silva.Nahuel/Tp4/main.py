from person import Person
from personService import PersonService

#menu
class Menu():

    def menu_inicio(self):
        print("\n\n1. Entrar al menu")
        print("2. No entrar al menu")
        return int(input("Elija una opción: "))

    def menu_person(self):
        print("\n\n1. Agregar personas")
        print("2. Modificar datos de la persona")
        print("3. Eliminar persona")
        print("4. Listar personas")
        return int(input("Elija una opción: "))

if __name__ == '__main__':
    personService = PersonService()
    menu = Menu()
    opcion = Menu.menu_inicio({})
    while True:
        if opcion == 1:
            numero = Menu.menu_person({})
            if numero == 1:
                #Agregar personas
                p1 = Person()
                p1.name = str(input("Ingrese un nombre: "))
                p1.surname = str(input("Ingrese un Apellido: "))
                p1.age = int(input("Ingrese una edad: "))
                personService.add_person(p1)
            #Modificar alguna persona
            if numero == 2:
                clave = int(input('Elija la clave de la persona que desea modificar: '))
                personService.update_person(clave)
            #Eliminar alguna persona
            if numero == 3:
                clave = int(input('Elija la clave de la persona que desea eliminar: '))
                personService.delete_person(clave)
            #Listar personas
            if numero == 4:
                personService.get_personList()  
        if opcion == 2:
            print ("Chau...")