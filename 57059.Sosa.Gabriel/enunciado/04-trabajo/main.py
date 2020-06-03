import os
from person import Person
from personService import PersonService

def clear():
    os.system("clear")

clear()

class App():
    def menu(self):
        clear()
        Person.frame()
        print ("\n¡Bienvenido al menu!")
        Person.frame()
        print("\n1. Agregar una Persona")
        print("2. Listar Personas")
        print("3. Modificar una Persona")
        print("4. Borrar una Persona")
        print("5. Prueba por defecto")
        Person.frame()
        return int(input("Ingrese una opcion: "))
        Person.frame()
        clear()
if  __name__ == '__main__':
    app = App()
    personService = PersonService()

    while True:
        opc = app.menu()
        if opc == 1:
            clear()
            personService.add_person()
            continuar = input("\nPresione ENTER para continuar...\n")
        if opc == 2:
            clear()
            print("\n", personService.get_personList())
            Person.frame()
            continuar = input("\nPresione ENTER para continuar...\n")

        if opc == 3:
            clear()
            personService.update_person()
            continuar = input("\nPresione ENTER para continuar...\n")

        if opc == 4:
            clear()
            personService.delete_person()
            continuar = input("\nPresione ENTER para continuar...\n")

        if opc == 5:
            clear()
            # Agregamos a FEDERICO
            p1 = Person('Federico', 'Gonzalez', '20')
            personService.add_person(p1)
            continuar = input("\nPresione ENTER para continuar...\n")
            clear()
            

            # Agregamos a CLAUDIO
            p1 = Person('Claudio', 'Pico', 33)
            personService.add_person(p1)
            continuar = input("\nPresione ENTER para continuar...\n")
            clear()
            

            # Agregamos a NICOLAS 
            p1 = Person('Nicolas', 'Pico', 40)
            personService.add_person(p1)
            continuar = input("\nPresione ENTER para continuar...\n")
            clear()
            

            print(personService.get_personList())
            # {0: {'_name': 'FEDERICO', '_surname': 'GONZALEZ', '_age': '20'},
            #  1: {'_name': 'CLAUDIO', '_surname': 'PICO', '_age': 33},
            #  2: {'_name': 'NICOLAS', '_surname': 'PICO', '_age': 30}}
            Person.frame()

            continuar = input("\nPresione ENTER para continuar...\n")
            clear()
            

            # Moddificar a 0:FEDERICO
            Person.frame()
            print ("\nNota: Se debe modificar la edad de Federico a 30")
            personService.update_person(0)

            # {0: {'_name': 'FEDERICO', '_surname': 'GONZALEZ', '_age': '30'}

            continuar = input("\nPresione ENTER para continuar...\n")
            clear()
           
            print(personService.get_personList())

            # {0: {'_name': 'FEDERICO', '_surname': 'GONZALEZ', '_age': '30'},
            #  1: {'_name': 'CLAUDIO', '_surname': 'PICO', '_age': 33},
            #  2: {'_name': 'NICOLAS', '_surname': 'PICO', '_age': 30}}

            Person.frame()
            continuar = input("\nPresione ENTER para continuar...\n")
            clear()
            
            # Borrar a Persona 2:NICOLAS
            personService.delete_person(2)

            continuar = input("\nPresione ENTER para continuar...\n")
            clear()
            
            print(personService.get_personList())

            # {0: {'_name': 'FEDERICO','_surname': 'GONZALEZ', '_age': '20'},
            #  1: {'_name': 'CLAUDIO', '_surname': 'PICO', '_age': 33}}

            Person.frame()
            continuar = input("\nPresione ENTER para continuar...\n")
            clear()

        if opc < 1 or opc > 5:
            break