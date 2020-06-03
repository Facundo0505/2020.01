import unittest
from administration import Administrtion
from employee import Employee
from parameterized import parameterized, param

class TestAdm(unittest.TestCase):
    def setUp(self):
        self.adm = Administrtion()

    def tearDown(self):
        self.adm = None

    @parameterized.expand([
        param([
            Employee("Santiago","Coria",19,1234,20000).get_employee(),
            Employee("Pepe","Rodriguez",40,1234,35000).get_employee(),
        ])
    ])

    def test_legajo(self,employee_arr):
        for i in range(len(employee_arr)):
            self.adm.add_employee(employee_arr[i])
        key_list = [*self.adm.listEmployee.keys()]
        self.assertListEqual(key_list,[i for i in range(len(key_list))])

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAdm)
    unittest.TextTestRunner().run(suite)
