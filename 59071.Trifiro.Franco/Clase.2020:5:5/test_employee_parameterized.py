import unittest 
from employee import Employee
from employee import Person
from parameterized import parameterized

class TestPerson(unittest.TestCase):
     @parameterized.expand([ 
         ("Franco", 20, "Trifiro", 2615870558, {"name":"Franco", "age":20, "surname":"Trifiro", "phone":2615870558})
     ])
     def test_get_person(self, name, surname, age, phone, result):
         person1 = Person(name, surname, age, phone)
         dictPerson = person1.get_person()
         self.assertEqual(dictPerson, result)

class TestEmployee(unittest.TestCase):
     @parameterized.expand ([ 
         ("Franco", 20, "Trifiro", 2615870558, {"name":"Franco", "age":20, "surname":"Trifiro", "phone":2615870558, "salary":50000})
     ])

     def test_get_employee(self, name, age, surname, phone, salary, result):
         employee = Employee(name, age, surname, phone, salary)
         dictEmployee = employee.get_employee()
         self.assertEqual(dictEmployee, result)

     @parameterized.expand([ 
         ("Franco", 20, "Trifiro", 2615870558, 50000, "Paga impuestos"),
         ("Ivan", 20, "Freiberg", 120839432, 20000, "No paga impuestos")
     ])

     def test_pay_tax_pay(self, name, age, surname, phone, salary, result):
         employee = Employee(name, age, surname, phone, salary)
         tax = employee.pay_tax()
         self.assertEqual(tax, result)


if __name__ == "__main__":
     unittest.main()