import unittest
from administration import Administration
from employee import Employee, Person
from parameterized import parameterized

class TestAdministration(unittest.TestCase):
    @parameterized.expand([
        ("Nahuel", "Silva", 19, 123456789, 40000, 0, {"name":"Nahuel", "surname":"Silva", "age":19, "phone":123456789, "salary":40000}),
        ("Christian", "Silva", 25, 123456789, 20000, 1, {"name":"Christian", "surname":"Silva", "age":25, "phone":123456789, "salary":20000})
    ])

    def test_add_employee(self, name, surname, age, phone, salary, legajo, result):
        employee = Employee(name, surname, age, phone, salary)
        adm = Administration()
        adm.add_employee(employee.get_employee())
        self.assertEqual(adm.listEmployee[legajo], result)

if __name__ == "__main__":
    unittest.main()