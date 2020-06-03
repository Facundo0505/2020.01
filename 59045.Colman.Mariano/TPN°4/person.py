class Person:

    def __init__(self, name=None, surname=None, age=None, key=None):
        self._name = name
        self._surname = surname
        self._age = age
        self._key = key

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
    def surname(self, surname):
        self._surname = surname

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

    def agregarPersona(self):
        print("\n Agreganddo persona")
        self._name = str(input("\nIngrese el nombre: "))
        self._surname = str(input("Ingrese el apellido: "))
        self._age = str(input("Ingrese la edad: "))
        self._key = int(input("Ingrese la clave que quiere asignarle: "))

    def updatearPersona(self, resultado=False):
        print("\nActualizando persona")
        if resultado == False:
            self._key = int(input("\nIngrese la clave de la persona que quiere modificar: "))
        elif resultado == True:
            self._name = str(input("Ingrese el nombre: "))
            self._surname = str(input("Ingrese el apellido: "))
            self._age = str(input("Ingrese la edad: "))
    
    def eliminarPersona(self, resultado=False):
        self._key = int(input("\nIngrese la clave de la persona que quiere eliminar: "))
