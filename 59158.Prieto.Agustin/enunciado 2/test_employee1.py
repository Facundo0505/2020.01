import unittest
from employee import Employee
from parameterized import parameterized


class TestEmployee(unittest.TestCase):
    @parameterized.expand([
        ('Agustin', 'Prieto', 19, 1234, 40000, 
        {'name': 'Agustin', 'surname': 'Prieto', 'age': 19, 'cellphone': 1234, 'salary': 40000})

    ])
    def test_get_employee(self, name, surname, age, cellphone, salary, result):
        persona1 = Employee(name, surname, age, cellphone, salary)
        self.assertEqual(persona1.get_employee(), result)

    @parameterized.expand([
        ('Agustin', 'Prieto', 19, 1234, 40000, 'Paga impuestos')
    ])
    def test_pay_tax_pay(self, name, surname, age, cellphone, salary, result):
        person1 = Employee(name, surname, age, cellphone, salary)
        self.assertEqual(person1.pay_tax(), 'Paga impuestos')
    
    @parameterized.expand([
        ('Agustin', 'Prieto', 38, 1234, 10000, 'No paga impuestos')
    ])
    def test_pay_tax_no_pay(self, name, surname, age, cellphone, salary, result):
        person1 = Employee(name, surname, age, cellphone, salary)
        self.assertEqual(person1.pay_tax(), result)


if __name__ == '__main__':
    unittest.main()
