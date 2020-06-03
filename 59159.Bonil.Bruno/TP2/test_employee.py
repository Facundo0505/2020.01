import unittest
import employee
from parameterized import parameterized
from employee import Employee

class TestEmployee(unittest.TestCase):
    @parameterized.expand ([
        ("Bruno", "Bonil", 19, 2612502686, 15000, {'name': "Bruno", 'surname': "Bonil", 'age': 19, 'num': 2612502686, 'salary': 15000})
        ])
    def test_get_employee(self, name, surname, age, num, salary, dic):
        empleado = Employee(name, surname,age, num ,salary)
        self.assertEqual(empleado.get_employee(), dic)
    @parameterized.expand ([
        ("Lucas", "Perez", 25, 2616584938, 70000, "Paga impuestos"),
        ("Juan", "Martinez", 34, 261783421, 15000, "No paga impuestos")
    ])
    def test_pay_tax_pay(self, name, surname, age, num, salary, tax):
        empleado1 = Employee(name, surname, age, num, salary)
        self.assertEqual(empleado1.pay_tax(), tax)
 
if __name__ == '__main__':
    unittest.main()
