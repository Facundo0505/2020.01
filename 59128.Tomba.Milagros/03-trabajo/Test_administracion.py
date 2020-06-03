import unittest
from Employee import Person, Employee
from Administracion import Administracion
from parameterized import parameterized

class  Test_Administracion(unittest.TestCase):
    @parameterized.expand([
        ("Milagros", "Tomba", 19, 2615080491, 30000, 0, {"name":"Milagros", "Surname":"Tomba", "age":19, "Phone":2615080491, "salary":30000}),
        ("Agustina", "Tomba", 24, 2611111111, 20000, 1, {"name":"Agustina", "Surname":"Tomba", "age":24, "Phone":2611111111, "salary":20000})
    ])

    def test_add_employee(self, name, surname, age, phone, salary, legajo, result):
        employee = Employee(name, surname, age, phone, salary)
        adm = Administracion()      
        adm.add_employee(employee.get_employee())        
        self.assertEqual(adm.listEmployee[legajo], result) 
      

if __name__ == '__main__':
  unittest.main()