import unittest
from Employeee import Person
from Employeee import Employee

class Test_person(unittest.TestCase):
    def test_get_person(self):
        persona1 = Person("Milagros", 19).get_person()
        self.assertEqual(persona1, (["Milagros", 19]))
    
class  Test_employee(unittest.TestCase):
    def test_get_employee(self):
        employee1 = Employee("Milagros", 19, 30000).get_employee()
        self.assertEqual(employee1, (["Milagros", 19, 30000]))

    def Test_pay_tax_pay(self):
        taxes = Employee("Milagros", 19, 40000).pay_tax()
        self.assertEqual(taxes, "Paga impuestos")

    def Test_pay_tax_no_pay(self):
        taxes2 = Employee("Milagros", 19, 30000,"Tomba").pay_tax()
        self.assertEqual(taxes2, "No paga impuestos")
    
       

if __name__ == '__main__':
  unittest.main()
 