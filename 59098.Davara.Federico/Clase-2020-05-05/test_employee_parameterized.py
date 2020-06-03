import unittest 
from employee import Employee, Person
from parameterized import parameterized

class TestPerson(unittest.TestCase):
    @parameterized.expand([
        ("Federico", "Davara", 19, 2612427136, {"name":"Federico", "surname":"Davara", "age":19, "phone":2612427136})
    ])
    def test_get_person(self, name, surname, age, phone, result):
        person = Person(name, surname, age, phone)
        listPerson = person.get_person()
        self.assertEqual(listPerson, result)
class TestEmployee(unittest.TestCase):
    @parameterized.expand([
        ("Federico", "Davara", 19, 2612427136, 50000, {"name":"Federico", "surname":"Davara", "age":19, "phone":2612427136, "salary":50000})
    ])
    def test_get_employee(self, name, surname, age, phone, salary, result):
        employee = Employee(name, surname, age, phone, salary)
        listEmployee = employee.get_employee()
        self.assertEqual(listEmployee, result)

if __name__ == "__main__":
    unittest.main()