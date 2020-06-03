import unittest 
from employee import Employee
from employee import Person
from parameterized import parameterized

class TestPerson(unittest.TestCase):
    @parameterized.expand([ 
        ("Guadalupe", 19, "Méndez", 2615191849, {"name":"Guadalupe", "age":19, "surname":"Méndez", "phone":2615191849})
    ])

    def test_get_person(self, name, surname, age, phone, result):
        person1 = Person(name, surname, age, phone)
        dictPerson = person1.get_person()
        self.assertEqual(dictPerson, result)

class TestEmployee(unittest.TestCase):
    @parameterized.expand ([ 
        ("Guadalupe", 19, "Méndez", 2615191849, 40000, {"name":"Guadalupe", "age": 19, "surname": "Méndez", "phone":2615191849, "salary":40000})
    ])

    def test_get_employee(self, name, age, surname, phone, salary, result):
        employee = Employee(name, age, surname, phone, salary)
        dictEmployee = employee.get_employee()
        self.assertEqual(dictEmployee, result)

    @parameterized.expand([ 
        ("Guadalupe", 19, "Méndez", 2615191849, 50000, "Paga impuestos"),
        ("Ignacio", 18, "Méndez", 2615191850, 20000, "No paga impuestos")
    ])

    def test_pay_tax_pay(self, name, age, surname, phone, salary, result):
        employee = Employee(name, age, surname, phone, salary)
        tax = employee.pay_tax()
        self.assertEqual(tax, result)


if __name__ == "__main__":
    unittest.main()