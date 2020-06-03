import unittest
from employee import Person, Employee

class PersonTest (unittest.TestCase):

    def test_get_person (self):
        self.name = "Gabi"
        self.surname= "Sosa"
        self.age = 22
        self.phone = 232323332

        person = Person.get_person(self)
        self.assertEqual(person, {'name':'Gabi', 'surname':'Sosa', 'age':22, 'phone':232323332})

class EmployeeTest (unittest.TestCase):
    def test_get_employee (self):
        self.name = "Gabi"
        self.surname= "Sosa"
        self.age = 22
        self.phone = 232323332
        self.salary = 30001
        employee = Employee.get_employee(self)
        self.assertEqual (employee, {'name':'Gabi', 'surname':'Sosa', 'age':22, 'phone':232323332,'salary':30001})
        
    def test_pay_tax_pay (self):
        self.salary = 40000
        self.age = 22
        taxes = Employee.pay_tax(self)
        self.assertEqual (taxes, "Paga impuestos" )

    def test_pay_tax_no_pay (self):
        self.salary = 20000
        self.age = 22
        taxes = Employee.pay_tax(self)
        self.assertEqual (taxes, "No paga impuestos" )    
        
if __name__ == "__main__":
    unittest.main()