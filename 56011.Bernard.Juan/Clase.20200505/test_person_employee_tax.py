import unittest
from employee import Employee, Person
from parameterized import parameterized


class TestPerson(unittest.TestCase):
    @parameterized.expand([
        ("Juan", 22, "Bernard", 1546894, {'name': "Juan", 'age': 22, 'surname': "Bernard", 'phone': 1546894})
    ])
    def test_get_person(self, name, age, surname, phone, result):
        person = Person(name, age, surname, phone)
        dictPerson = person.get_person()
        self.assertEqual(dictPerson, result)


class TestEmployee(unittest.TestCase):
    @parameterized.expand([
        ("Alicia", 25, "Carrizo", 1567352, 50000, {'name': "Alicia", 'age': 25, 'surname': "Carrizo", 'phone': 1567352, 'salary': 50000})
    ])
    def test_get_employee(self, name, age, surname, phone, salary, result):
        employee = Employee(name, age, surname, phone, salary)
        dictEmployee = employee.get_employee()
        self.assertEqual(dictEmployee, result)

    @parameterized.expand([
        ("Pedro", 31, "Jones", 1524168, 45000, "Paga impuestos"),
        ("María", 35, "Vila", 1523521, 25000, "No paga impuestos")
    ])
    def test_pay_tax_pay(self, name, age, surname, phone, salary, result):
        employee = Employee(name, age, surname, phone, salary)
        tax = employee.pay_tax()
        self.assertEqual(tax, result)


if __name__ == '__main__':
    unittest.main()
