#using @property decorator
class Celsius:
    def __init__(self, temperatura=0):
        self.temperatura = temperatura
    
    def to_fahrenheit(self):
        return (self.temperatura * 1.8) + 32

    #reemplazar getter y setter con @
    #decroradores
    @property #se lo ponemos a funcion como getter, debe tener el mismo nombre que el atributo que vamos a usar
    def temperatura(self):
        print("getting value...")
        return self._temperatura

    #setter(valor al atributo)
    @temperatura.setter
    def temperatura(self, value):
        print("setting value")
        if value < -273.15:
            raise ValueError("temperatura menor a -273 no es posible")
        self._temperatura = value
    
#crear un objeto
human = Celsius(37)
print(human.temperatura)
print(human.to_fahrenheit())

human.temperatura = 41
print(human.temperatura)

#coldest_thing = Celsius(-300)

print(human.__dict__)