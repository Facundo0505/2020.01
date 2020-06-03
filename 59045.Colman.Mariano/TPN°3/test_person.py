import unittest
from persona import Person, Empleado, Administracion
from parameterized import parameterized

class TestPerson(unittest.TestCase):
    @parameterized.expand([
        ("Mariano", "Colman", 21, "marianocolman@gmail.com", {"nombre": "Mariano", "apellido": "Colman", "edad": 21, "mail": "marianocolman@gmail.com"})
    ])
    def test_get_person(self, nombre, apellido, edad, mail, diccionario):
        persona = Person(nombre, apellido, edad, mail)
        dicPersona = persona.get_persona()
        self.assertEqual(dicPersona ,diccionario)

class TestEmployee(unittest.TestCase):
    @parameterized.expand([
        ("Mariano", "Colman", 21, "marianocolman@gmail.com", 3500, {"nombre": "Mariano", "apellido": "Colman", "edad": 21, "mail": "marianocolman@gmail.com", "salario": 3500})
    ])
    def test_get_empleado(self, nombre, apellido, edad, mail, salario, diccionario):
        empleado = Empleado(nombre, apellido, edad, mail, salario)
        dicEmpleado = empleado.get_empleado()
        self.assertEqual(dicEmpleado, diccionario)

class TestPagaImpuesto(unittest.TestCase):
    @parameterized.expand([
        ("Mariano", "Colman", 21, "marianocolman@gmail.com", 3500, "Paga impuestos")
    ])

    def test_paga_impuesto(self, nombre, apellido, edad, mail, salario, resultado):
        empleado2 = Empleado(nombre, apellido, edad, mail, salario)
        dicEmpleado2 = empleado2.get_empleado()
        self.assertEqual(resultado, empleado2.paga_impuesto())

class TestNoPagaImpuesto(unittest.TestCase):
    @parameterized.expand([
        ("Mariano", "Colman", 21, "marianocolman@gmail.com", 2000, "No paga impuestos")
    ])
    def test_no_paga_impuesto(self, nombre, apellido, edad, mail, salario, resultado):
        emp3 = Empleado(nombre, apellido, edad, mail, salario)
        dicEmpleado3 = emp3.get_empleado()
        self.assertEqual(resultado, emp3.paga_impuesto())

class TestAdministracion(unittest.TestCase):
    @parameterized.expand([
        ("Mariano", "Colman", 21, 2614312380, 3500, 0),
        ("Octavio", "Colman", 24, 2614312381, 2500, 1),
        ("Jose", "Colman", 20, 2614312382, 1500, 2)
    ])

    def test_add_employee(self, nombre, apellido, edad, mail, salario, legajo):
        admin = Administracion(nombre, apellido, edad, mail, salario)
        empleado = admin.crearDiccionario()
        dicAdmin = admin.add_employee()
        self.assertEqual(dicAdmin[legajo], empleado)


if __name__ == "__main__":
    unittest.main()

