from administration import Administration
from employee import Employee
from parameterized import parameterized
import unittest

class testAdministation(unittest.TestCase):
    @parameterized.expand([
        ('Matias','Robbio',18,2615555555,5000,0),
        ('Bruno','Bonil',19,2616666666,6000,1),
        ('Agustin','Prieto',20,26177777777,7000,2)
    ])
    def test_add_employee(self, name, surname, age, phone,salary, legajo):
        emp = Employee(name,surname,age,phone,salary)
        adm.add_employee(emp)
        self.assertEqual(adm.listEmployee[legajo],emp)

if __name__=='__main__':
    adm= Administration()
    unittest.main()