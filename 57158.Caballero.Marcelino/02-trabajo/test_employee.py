import unittest
from employee import Person, Employee


class TestPerson(unittest.TestCase):
    def test_get_person(self):
        person = Person("Marcelino",25,"Caballero", 4982841).get_person()
        self.assertEqual(person, ["Marcelino", 25])


class TestEmployee(unittest.TestCase):
    def test_get_employee(self):
        employee = Employee("Marcelino", 25, "Caballero",4982841, 25000).get_employee()
        self.assertEqual(employee, ["Marcelino", 25, 25000])

class TestPayTax(unittest.TestCase):    
    def test_pay_tax_pay(self):
        employee_two = Employee("Jorge", 31, "Perez", 4881818, 35000).pay_tax()
        self.assertEqual(employee_two, "Paga impuestos")

    def test_pay_tax_no_pay(self):
        employee = Employee("Marcelino", 25, "Caballero", 4982841, 25000).pay_tax()
        self.assertEqual(employee, "No paga impuestos")


if __name__ == "__main__":
    unittest.main()
