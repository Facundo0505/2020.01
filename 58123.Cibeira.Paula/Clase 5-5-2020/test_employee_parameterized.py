import unittest
from emp import Person
from emp import Employee
from parameterized import parameterized

class Test_person(unittest.TestCase):
    @parameterized.expand([
        ("Paula", 20, "Cibeira", 424242, {"name":"Paula", "age":20, "surname":"Cibeira", "phone":424242})
    ])

    def test_get_person(self, name, age, surname, phone, result):
        person = Person(name, age, surname, phone)
        listPerson = person.get_person()
        self.assertEqual(listPerson, result)

class Test_employee(unittest.TestCase):
    @parameterized.expand([
        ("Paula", 20, "Cibeira", 424242, 20000, {"name":"Paula", "age":20, "surname":"Cibeira", "phone":424242, "salary":20000})
    ])
    
    def test_get_employee(self, name, age, surname, phone, salary, result):
        employee1 = Employee(name, age, surname, phone, salary)
        listEmployee = employee1.get_employee()
        self.assertEqual(listEmployee, result)

if __name__ == "__main__":
    unittest.main()