import unittest
from Employeee import Person
from Employeee import Employee
from parameterized import parameterized

class Test_person(unittest.TestCase):
    @parameterized.expand([
        ("Milagros", 19, ["Milagros", 19])
    ])

    def test_get_person(self, name, age, result):
        persona1 = Person(name, age)
        listPerson = persona1.get_person()
        self.assertEqual(listPerson, result)

class  Test_employee(unittest.TestCase):
    @parameterized.expand([
        ("Milagros", 19, 30000, ["Milagros", 19, 30000])
    ])

    def test_get_employee(self,name, age, salary, result):
        employee1 = Employee(name, age, salary)
        listEmployee = employee1.get_employee()
        self.assertEqual(listEmployee, result)
    @parameterized.expand([
        ("Milagros", 19, 30000, "No paga impuesto"),
        ("Milagros", 19, 40000, "Paga impuestos")
    ])

    def Test_pay_tax_pay(self,name, age, salary, result):
        employee1 = Employee(name, age, salary)
        tax = employee1.pay_tax()
        self.assertEqual(tax, result)
   

if __name__ == '__main__':
  unittest.main()