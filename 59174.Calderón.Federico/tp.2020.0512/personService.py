from repository import Repository
from person import Person
class PersonService:

    def get_personList(self):
        return Repository().person

    #Agrega una persona en el dicionario person, definido en Repository
    def add_person(self, person_parameter):
        key = len(Repository.person)
        Repository.person[key] = person_parameter.get_person()
        
    def update_person(self, key, person_parameter):
        Repository.person[key] = person_parameter.get_person()
    
    def delete_person(self,key):
        del(Repository.person[key])