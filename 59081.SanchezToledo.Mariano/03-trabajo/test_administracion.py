import unittest
from parameterized import parameterized, param
from employee import Employee
from administration import Administration

class Test_Legajo (unittest.TestCase):
    @parameterized.expand([
        param([

        {0:{'name': 'Claudio', 'surname': 'Pico', 'age': 30, 'phone': 155858585,'salary':30000}},
        {1:{'name': 'Gabriel', 'surname': 'Sosa', 'age': 22, 'phone': 153242445,'salary':20000}},
        {2:{'name': 'Mariano', 'surname': 'Sanchez Toledo','age': 20,'phone':153334355,'salary':40000}}

        ])
    ])
    
    def testing_legajo (self, employee):
        for n in range (len(employee)):
            Administration().add_employee(employee[n])
        
        NumLeg = [*Administration().listEmployee.keys()]
        NumLegRange = [n for n in range (len(NumLeg))]

        self.assertEqual(NumLeg, NumLegRange)


if __name__ == '__main__':
    unittest.main()
        