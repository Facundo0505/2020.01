import unittest
from employee import Person, Employee

class TestEmployee(unittest.TestCase):
    def test_persona(self):
        name = "Claudio"
        age = 32
        person = Person(name, age)
        self.assertEqual("Claudio", person.name)
        self.assertEqual(32, person.age)

    def test_employee(self):
        name = "Claudio"
        age = 32
        salary = 30000
        person = Employee(name, age, salary)
        self.assertEqual(30000, person.salary)
    
    def test_tax_pay(self):
        name = "Claudio"
        age = 31
        salary = 30001
        taxes = Employee(name, age, salary).pay_tax()
        self.assertEqual("Paga impuestos", taxes)

    def test_tax_no_pay(self):
        name = "Claudio"
        age = 32
        salary = 30000
        taxes = Employee(name, age, salary).pay_tax()
        self.assertEqual("No paga impuestos", taxes)

if __name__ == "__main__":
    unittest.main()