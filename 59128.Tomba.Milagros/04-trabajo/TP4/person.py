class Person():

    def _init_(self, name=None, surname=None, age=0):
        self._name = name.upper()
        self._surname = surname.upper()
        self._age = age
    '#get y set'
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
