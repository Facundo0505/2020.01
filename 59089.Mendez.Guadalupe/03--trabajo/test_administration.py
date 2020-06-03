import unittest
from administration import Administration
from employee import Employee, Person
from parameterized import parameterized

class TestAdministration(unittest.TestCase):
    @parameterized.expand([
        ("Guadalupe", "Méndez", 19, 2615191849, 40000, 0, {"name":"Guadalupe", "surname":"Méndez", "age":19, "phone":2615191849, "salary":40000}),
        ("Ignacio", "Méndez", 18, 2615191850, 20000, 1, {"name":"Ignacio", "surname":"Méndez", "age":18, "phone":2615191850, "salary":20000})
    ])

    def test_add_employee(self, name, surname, age, phone, salary, legajo, result):
        employee = Employee(name, surname, age, phone, salary)
        adm = Administration()
        adm.add_employee(employee.get_employee())
        self.assertEqual(adm.listEmployee[legajo], result)

if __name__== "__main__":
    unittest.main()