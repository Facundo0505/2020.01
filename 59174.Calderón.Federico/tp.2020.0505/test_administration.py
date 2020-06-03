import unittest
from administration import Administration
from employee import Employee
from parameterized import parameterized

class Test_administration(unittest.TestCase):
    @parameterized.expand([

    ("Claudio","Pico",30, 155858585, 45000,0),
    
    ("Federico","Calderon",20,1234,25000,1)
    
    ])
    def test_administration(self,name,surname,age,phone,salary, key):
        for i in range(len(list(Administration().listEmployee))):
            empleado = Employee(name,surname,age,phone,salary).get_employee()
            administ = Administration().add_employee(empleado)
            asertEqual(administ[i],i)
        
        
        
         
if __name__ == '__main__':
    unittest.main()
