from person import Person
from personService import PersonService


if __name__ == '__main__':
    personService = PersonService()

    # creamos un menu
    counter = 1
    while counter != 0:
      counter += 1
      print('Opciones: ')
      print('1. Agregar una persona')
      print('2. Actualizar datos de una persona')
      print('3. Borrar persona')
      print('4. Mostrar lista')
      opcion = int(input('Elija una opcion: '))

      # agregamos una persona
      if opcion == 1:
        p1 = Person()
        p1._name = str(input('Nombre: '))
        p1._surname = str(input('Apellido: '))
        p1._age = int(input('Edad: '))
        p1 = Person.get_person(p1)
        personService.add_person(p1)

      # actualizamos datos de una persona
      if opcion == 2:
        key = int(input('Elija la key de la persona que desea modificar: '))
        personService.update_person(key)

      # eliminamos una persona del diccionario
      if opcion == 3:
        key_delete = int(input('Ingrese la key de la persona que desea borrar: '))
        personService.delete_person(key_delete)
        print(personService.lista)
      

      
      # mostramos la lista
      if opcion == 4: 
        print(personService.get_personList())
        