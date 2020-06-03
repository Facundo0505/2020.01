import unittest
from parameterized import parameterized
from admin import Administration
from employee import Employee


class TestAdmin(unittest.TestCase):

    @parameterized.expand([
        ('Agustin', 'Prieto', 29, 1243, 341234, 0),
        ('Matias', 'Robbio', 19, 4321, 20000, 1),
        ('Agustin', 'Bonil', 19, 1224, 33333, 2),
        ('Bruno', 'Diaz', 19, 1154, 3344444, 3)
    ])
    def test_add_employee(self, name, surname, age, phone, salary, legajo):
        emp1 = Employee(name, surname, age, phone, salary)
        adm=Administration()
        adm.add_employee(emp1)
        self.assertEqual(emp1, adm.listEmployee[legajo])
        


if __name__ == '__main__':
    unittest.main()
