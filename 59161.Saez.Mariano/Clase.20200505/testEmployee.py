import unittest
from employee import Employee
from parameterized import parameterized


class TestEmployee(unittest.TestCase):
    @parameterized.expand([
        ('Mariano', 'Saez', 20, 155922296, 32165, {'name' : 'Mariano','surname' : 'Saez', 'age' : 20, 'phone' : 155922296, 'salary' : 32165}),
        ('Jesus', 'DeNazareth', 999, 00000000, 30001, {'name' : 'Jesus','surname' : 'DeNazareth', 'age' : 999, 'phone' : 00000000, 'salary' : 30001}),
        ('Mirtha', 'Legrande', 1000, 10000000, 50000, {'name' : 'Mirtha','surname' : 'Legrande', 'age' : 1000, 'phone' : 10000000, 'salary' : 50000})
    ])
    def test_get_employee(self, name, surname, age, phone, salary, result):
        empleado = Employee(name, surname, age, phone, salary)
        datosEmpleado = empleado.get_employee()
        self.assertEqual(datosEmpleado, result)

    @parameterized.expand([
        ('Mariano', 'Saez', 20, 155922296, 32165),
        ('Jesus', 'DeNazareth', 31, 00000000, 30001),
        ('Mirtha', 'Legrande', 30, 10000000, 50000)
    ])
    def test_tax_pay(self, name, surname, age, phone, salary):
        empleado = Employee(name, surname, age, phone, salary)
        salarioEmpleado = empleado.pay_tax()
        self.assertEqual(salarioEmpleado, "Paga impuestos")

    @parameterized.expand([
        ('Mariano', 'Saez', 20, 155922296, 29999),
        ('Jesus', 'DeNazareth', 999, 00000000, 29999),
        ('Mirtha', 'Legrande', 1000, 10000000, 29999)
    ])
    def test_tax_no_pay(self, name, surname, age, phone, salary):
        empleado = Employee(name, surname, age, phone, salary)
        salarioEmpleado = empleado.pay_tax()
        self.assertEqual(salarioEmpleado, "No paga impuestos")


if __name__ == '__main__':
    unittest.main()
