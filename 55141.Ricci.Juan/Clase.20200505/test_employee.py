import unittest
from employee import Person, Employee
from parameterized import parameterized

class TestEmployee(unittest.TestCase):
    @parameterized.expand([
            ("Juan", 23, "Ricci", 2610000000, {"name":"Juan", "age":23, "surname":"Ricci", "phone":2610000000})
        ])
    def test_get_persona(self, name, age, surname, phone, resultado):
        person = Person(name, age, surname, phone)
        listaPerson = person.get_person()
        self.assertEqual(listaPerson, resultado)

    @parameterized.expand([
            ("Juan", 23, "Ricci", 2610000000, 30000, {"name":"Juan", "age":23, "surname":"Ricci", "phone":2610000000, "salary":30000})
        ])
    def test_employee(self, name, age, surname, phone, salary, resultado):
        person = Employee(name, age, surname, phone, salary)
        listaPerson = person.get_employee()
        self.assertEqual(listaPerson, resultado)
    
    @parameterized.expand([
            ("Juan", 23, "Ricci", 2610000000, 30001, {"name":"Juan", "age":23, "surname":"Ricci", "phone":2610000000, "salary":30000})
        ])
    def test_tax_pay(self, name, age, surname, phone, salary, resultado):
        taxes =  Employee(name, age, surname, phone, salary).pay_tax()
        self.assertEqual("Paga impuestos", taxes)

    @parameterized.expand([
            ("Juan", 32, "Ricci", 2610000000, 29999, {"name":"Juan", "age":23, "surname":"Ricci", "phone":2610000000, "salary":30000})
        ])
    def test_tax_no_pay(self, name, age, surname, phone, salary, resultado):
        taxes =  Employee(name, age, surname, phone, salary).pay_tax()
        self.assertEqual("No paga impuestos", taxes)

if __name__ == "__main__":
    unittest.main()