class Person():

    def __init__(self, name="None", surname="None", age=None, key="None"):
        self._name = name.upper()
        self._surname = surname.upper()
        self._age = age
        self._key = key

    def ingresar(self, modificar=False):
        print("\n   Ingresando persona")
        if not modificar:
            self._key = input("Key: ")

        self._name = input("Nombre: ")
        self._surname = input("Surname")
        self.age = input("Age")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name.upper()

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname):
        self._surname = surname.upper()

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        self._key = key
