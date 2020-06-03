
import unittest
from employee import Employee,Person 
from parameterized import parameterized

class TestPerson_parameterized(unittest.TestCase):
    @parameterized.expand([
        ("Federico", "Calderon", 20, 1234, {'name ': "Federico",'surname ': "Calderon",'age ': 20,'phone ': 1234})
    ])
    def test_get_person_parameterized(self, name, surname, age, phone,result):
        person = Person(name, surname, age, phone).get_person()
        self.assertEqual(person,result)
    
    @parameterized.expand([
        ("Federico", "Calderon", 20, 1234,30000 , {'name ': "Federico",'surname ': "Calderon",'age ': 20,'phone ': 1234, 'salary': 30000})
    ])
    def test_get_employee_parameterized(self, name, surname, age, phone, salary, result):
        employee = Employee(name, surname, age, phone,salary).get_employee()
        self.assertEqual(employee,result)
    
    @parameterized.expand([
        ("Federico", "Calderon", 20, 1234,45000 ,'Paga impuestos')
    ])
    def test_get_pay_tax_parameterized(self, name, surname, age, phone, salary, result):
        employee =Employee(name, surname, age, phone,salary).get_pay_tax()
        self.assertEqual(employee,result)

    @parameterized.expand([
        ("Federico", "Calderon", 20, 1234,25000 ,'No paga impuestos')    
    ])
    def test_get_no_pay_tax_parameterized(self, name, surname, age, phone, salary, result):
        employee =Employee(name, surname, age, phone,salary).get_pay_tax()
        self.assertEqual(employee,result)
        

if __name__ == "__main__":
    unittest.main()

