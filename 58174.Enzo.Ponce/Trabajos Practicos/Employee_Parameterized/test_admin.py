import unittest
from administrador import Administration
from parameterized import parameterized
from employee2 import Employee,Person




class Test_Administracion(unittest.TestCase):
    @parameterized.expand([("Enzo","Ponce",23,2615691337,{0:{'name':"Enzo",'surname':"Ponce",'age':23,'phone':2615691337}})])   

    def test_admin(self,name,surname,age,phone,legajo):
            
            person= Person(name,surname,age,phone)
            person1 = person.get_person()
            adm = Administration()
            adm.add_employee(person1)
            adm2 = adm.listEmployee
            self.assertEqual(adm2, legajo)
                
            
if __name__=="__main__":
    unittest.main()