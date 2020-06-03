import unittest
from employee import Person
from employee import Employee


class Test_Employee (unittest.TestCase):
    def test_get_person (self):
        person = Person("Claudio", 22).get_person()
        self.assertEqual(person, ["Claudio",22])

    def test_get_employee (self):
        employee = Employee("Claudio", 22, 20000).get_employee()
        self.assertEqual(employee, ["Claudio", 22, 20000])

    def test_get_employee_two (self):
        employee = Employee("Claudio", 22, 20000).pay_tax()
        self.assertEqual(employee, "No paga impuestos")

    def test_get_employee_three (self):
        employee = Employee("Juan", 30, 40000).pay_tax()
        self.assertEqual(employee, "Paga impuestos")


if __name__ == '__main__':
    unittest.main()
