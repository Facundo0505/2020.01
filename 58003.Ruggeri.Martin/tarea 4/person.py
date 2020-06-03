class Person():
    def __init__(self, key="", nombre="", apellido="", edad=0):
        self.key = key
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        return "%s %s %s %d" % (self.key, self.nombre, self.apellido,
                                 self.edad)

    def ingresar(self):
        print("Ingresando Person")
        self.key = input("Key: ")
        self.nombre = input("Ingrese nombre: ").upper()
        self.apellido = input("Ingrese apellido : ").upper()
        self.edad = int(input("Ingrese edad: "))
        
    def modificar(self, modificar):
        print("modificando Person")
        if modificar == 1:
            self.nombre = input("Ingrese nombre: ").upper()
        elif modificar == 2:
            self.apellido = input("Ingrese apellido : ").upper()
        elif modificar == 3:
            self.edad = int(input("Ingrese edad: "))
