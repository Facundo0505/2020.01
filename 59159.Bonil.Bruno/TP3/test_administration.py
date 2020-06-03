import unittest
from parameterized import parameterized
from administration import Administration
from employee import Person, Employee

class test_administration(unittest.TestCase):
    @parameterized.expand ([
        ("Bruno", "Bonil", 19, 152502686, 30000, 0),
        ("Emiliano", "Bonil", 14, 155858585, 20000, 1)
    ])

    def test_add_employee(self, name, surname, age, phone, salary, legajo):
        empleado = Employee(name, surname, age, phone, salary)
        admin = Administration()
        admin.add_employee(empleado)
        self.assertEqual(Administration.listEmployee[legajo], empleado)
    

if __name__ == '__main__':
    unittest.main()