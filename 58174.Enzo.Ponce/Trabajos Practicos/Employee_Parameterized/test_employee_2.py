import unittest
from employee2 import Person, Employee

from parameterized import parameterized



class Test_employee(unittest.TestCase):
    @parameterized.expand([("Enzo", "Ponce", 23, 2615691337, {"phone":2615691337, "age": 23,"surname":"Ponce","name": "Enzo"})])
    
    def test_1_employee(self,phone,age,surname,name,diccionario):
        person = Person(phone,age,surname,name)
        datos = person.get_person()
        self.assertEqual(datos, diccionario)

    @parameterized.expand([("Enzo", "Ponce", 23, 2615691337, 50000, {"salary":50000, "phone":2615691337, "age": 23,"surname":"Ponce","name": "Enzo"})])

    def test_2_employee(self,name,surname,age,phone,salary,diccionario):
        person = Employee(name, surname, age, phone, salary)
        datos = person.get_employee()
        self.assertEqual(datos, diccionario)

    @parameterized.expand([("Enzo","Ponce",23,2615691337,50000)])

    def test_3_employee(self,name,surname,age,phone,salary):
        impuestos = Employee(name,surname,age,phone,salary)
        cobro = impuestos.pay_tax()
        self.assertEqual(cobro,("Paga impuestos"))

    @parameterized.expand([("Enzo","Ponce",35,2615691337,20000)])

    def test_4_employee(self,name,surname,age,phone,salary):
        impuestos = Employee(name,surname,age,phone,salary)
        cobro = impuestos.pay_tax()
        self.assertEqual(cobro,("No paga impuestos"))

    
if __name__=="__main__":
    unittest.main()