import unittest
from unittest import TestCase
from administration import Administration
from class1 import Person, Employee
from parameterized import parameterized

class testAdministration (unittest.TestCase):
    @parameterized.expand([
                           {"name":"Oriel", "surname": "Barroso", "age":23, "phone":155, "salary":25000, "legajo":0},
                            {"name":"Nicolas", "surname":"Barroso", "age":32, "phone":156, "salary":32000, "legajo":1}
                        ])
    
    def test_add_employee(self, name, surname, age, phone, salary, legajo):
        emp = Employee("Oriel", "Barroso", 23, 155, 23000, 0).get_employee()
        emp2 = Employee("Nicolas", "Barroso", 32, 156, 32000, 1).get_employee()
        adm = Administration()
        adm.add_employee(emp)
        adm.add_employee(emp2)
        self.assertTrue(adm.listEmployee)

if __name__ == "__main__":
    unittest.main()