import unittest
from administration import Administration
from employee import Employee
from parameterized import parameterized, param


class TestLegajo(unittest.TestCase):
    
    @parameterized.expand([
        param([                  
        
        {0:{'name': 'Claudio', 'surname': 'Pico', 'age': 30, 'phone': 155858585,'salary':30000}},
        {1:{'name': 'Gabriel', 'surname': 'Sosa', 'age': 22, 'phone': 153242445,'salary':20000}},
        {2:{'name': 'Nicolas', 'surname': 'Pico', 'age': 30, 'phone': 123454552,'salary':25000}} 

        ])
    ])

    def test_legajo(self, empleados):
        adm = Administration()              #Reemplaza el nombre de la funcion para comodidad de tipeo.
       
        for n in range(len(empleados)):
            adm.add_employee(empleados[n])  #Crea la lista con los Legajos generados de cada empleado.
            
        print (empleados)

        NL = [*adm.listEmployee.keys()]     #NL = Numero de Legajo. Separa los Legajos(Claves/Keys) y los guarda en una lista.
        NLR = [n for n in range (len(NL))]  #NLC = Numero de Legajo Registrado.

        self.assertListEqual (NL, NLR)      #Compara ambas listas para comprobar si son iguales.

        print (NL, NLR)                     

if __name__ == '__main__':
    unittest.main()