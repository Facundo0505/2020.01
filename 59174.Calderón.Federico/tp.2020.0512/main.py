from person import Person
from personService import PersonService


if __name__ == '__main__':
        
    personService = PersonService()

    #Agregamos una persona
    p1 = Person()
    p1.name ='federico'
    p1.surname = 'gonzalez'
    p1.age = '20'
    personService.add_person(p1)

    #Agregamos una persona
    p2 = Person()
    p2.name ='claudio'
    p2.surname = 'pico'
    p2.age = '33'
    personService.add_person(p2)

    #Agregamos al hermano **********************
    p3 = Person()
    p3.name = 'niclas'
    p3.surname = 'pico'
    p3.age = 40
    personService.add_person(p3)

    print (personService.get_personList()) # {0: {'_name': 'FEDERICO', '_surname': 'GONZALEZ', '_age': '20'}, 1: {'_name': 'NICOLAS', '_surname': 'PICO', '_age': 33}, 2: {'_name': 'NICOLAS', '_surname': 'PICO', '_age': 40}}

    #Update fEDERICO
    p4 = Person()
    p4.name ='federico'
    p4.surname = 'gonzalez'
    p4.age = '30'
    personService.update_person(0,p4)

    
    print (personService.get_personList()) #{0: {'_name': 'FEDERICO', '_surname': 'GONZALEZ', '_age': '30'}, 1: {'_name': 'NICOLAS', '_surname': 'PICO', '_age': 33}, 2: {'_name': 'NICOLAS', '_surname': 'PICO', '_age': 40}}


    #delte person
    #Elimina persona segun key del dic person
    personService.delete_person(2)
    

    print (personService.get_personList()) #{0: {'_name': 'FEDERICO', '_surname': 'GONZALEZ', '_age': '20'}, 1: {'_name': 'NICOLAS', '_surname': 'NICOLAS', '_age': 41}}
    
    