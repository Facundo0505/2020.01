import unittest
from employee import Person, Employee
from administration import Administration
from parameterized import parameterized

class TestAdminitration(unittest.TestCase):
    @parameterized.expand([
        ('Claudio', 'Pico', 30, 155858585, 30000, 0),
        ('Nicolas', 'Pico', 30, 155858585, 30000, 1),
        ])
    def test_add_employee(self, name, surname, age, phone, salary, legajo):
        employee = Employee(name, surname, age, phone, salary)
        adm.add_employee(employee)
        self.assertEqual(adm.listEmployee[legajo], employee)


if __name__ == '__main__':
    adm = Administration()
    unittest.main()