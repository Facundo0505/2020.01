class Person():

    def __init__(self, nombre, apellido, edad, mail):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.mail = mail
    
    def get_persona(self):
        return self.__dict__

class Empleado (Person):

    def __init__(self, nombre, apellido, edad, mail, salario):
        Person.__init__(self, nombre, apellido, edad, mail)
        self.salario = salario

    def get_empleado(self):
        return self.__dict__

    def paga_impuesto(self):
        if self.edad < 32 and self.salario > 3000:
            return "Paga impuestos"
        else:
            return "No paga impuestos"

class Administracion(Empleado):
    diccionarioEmployee = {}
    def __init__(self, nombre, apellido, edad, mail, salario):
        Person.__init__(self, nombre, apellido, edad, mail)
        self.salario = salario
        
    def crearDiccionario(self):
        return self.__dict__

    def add_employee(self):
        emple = {"nombre":self.nombre, "apellido":self.apellido, "edad":self.edad, "mail":self.mail, "salario": self.salario}
        legajo=len(self.diccionarioEmployee)
        self.diccionarioEmployee[legajo] = emple
        return self.diccionarioEmployee
