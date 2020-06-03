import unittest 
from administration import Administration
from employee import Employee
from parameterized import parameterized


class Test_administration(unittest.TestCase):
    @parameterized.expand([
                            ("Claudio","Pico",30, 155858585, 45000,0),   
                            ("Federico","Davara",19,2612427136,30000,1)  
    ])

    def test_administration(self,name,surname,age,phone,salary, key):
        empleado1 = Employee(name,surname,age,phone,salary)
        admin=Administration()
        admin.add_employee(empleado1)
        self.assertEqual(empleado1, admin.listEmployee[key])

if __name__ == '__main__':
    unittest.main()