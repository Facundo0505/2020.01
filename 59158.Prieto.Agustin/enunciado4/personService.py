from repository import Repository
from person import Person

class PersonService:
    lista = Repository.person

    def get_personList(self):
        return Repository.person

    #Agrega una persona en el dicionario person, definido en Repository
    def add_person(self, person):
        key = len(self.lista)
        self.lista[key] = person
        return
    
    #Actualiza datos de una person del diccionario person
    def update_person(self, key):
        count = 1
        while count != 0:
        
            print('Opciones: ')
            print('1. Modificar edad')
            print('2. Modificar nombre')
            print('3. Modificar apellido')
            opcion = int(input('Elija una opcion:'))
            
            if opcion == 1:
                #modifica la edad
                new_age = {'_age': int(input('Introduzca la nueva edad: '))}
                self.lista[key].update(new_age)
                print(self.lista)
                
            elif opcion == 2:
            
                new_name = {'_name': str(input('Introduzca el nuevo nombre: ').upper())}
                self.lista[key].update(new_name)
                print(self.lista)
                
                #modifica el apellido
            elif opcion == 3:
                new_surname = {'_surname': str(input('Introduzca el nuevo apellido: ').upper())}
                self.lista[key].update(new_surname)
                print(self.lista)
            
            #si la respuesta es si, se volvera a mostrar el menu de modificaciones
            #si la respuesta es "no", vuelve al menu principal
            listo = str(input('Dese continuar modificando?: '))
            if listo == 'no':
                break
            
    #Elimina persona segun key del dic person
    def delete_person(self, key):
        del self.lista[key]
