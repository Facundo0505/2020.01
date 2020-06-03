import unittest
from Employee import Person
from Employee import Employee
from parameterized import parameterized

class Test_person(unittest.TestCase):
    @parameterized.expand([
        ("Milagros", 19, "Tomba", 2615080491, {"name":"Milagros", "age":19, "apellido":"Tomba", "telefono": 2615080491})
    ])

    def test_get_person(self, name, age, apellido, telefono, result):
        persona1 = Person(name, age, apellido, telefono)
        listPerson = persona1.get_person()
        self.assertEqual(listPerson, result)
class  Test_employee(unittest.TestCase):
    @parameterized.expand([
        ("Milagros", 19, 30000, "Tomba", 2615080491, {"name":"Milagros", "age":19,"salary":30000, "apellido":"Tomba", "telefono": 2615080491})
    ])

    def test_get_employee(self,name, age, salary, apellido, telefono, result):
        employee1 = Employee(name, age, salary, apellido, telefono)
        listEmployee = employee1.get_employee()
        self.assertEqual(listEmployee, result)


if __name__ == '__main__':
  unittest.main()