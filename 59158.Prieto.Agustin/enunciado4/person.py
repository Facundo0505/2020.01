class Person:

    def __init__(self, name=None, surname=None, age=None):
        self._name = name
        self._surname = surname
        self._age = age

    def get_person(self):
        #upper() pone a los atributos en mayusculas.
        return {'_name': self._name.upper(), '_surname': self._surname.upper(), '_age': self._age}
    
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def name(self, surname):
        self._surname = surname
    
    @property
    def age(self):
        return self._age

    @surname.setter
    def name(self, age):
        self._age = age
