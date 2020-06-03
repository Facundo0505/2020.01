import unittest
from administracion import Administracion 
from parameterized import parameterized
from employee import Person

class TestAdministracion(unittest.TestCase):
    @parameterized.expand([
        ("Marcelino","Caballero", 30, 155858585,0),
        ("Marcelino","Caballero", 30, 155858585,1),
        ("Marcelino","Caballero", 30, 155858585,2)
    ])

    def test_add_employee(self, name, surname, age, phone, legajo):
        person = Person(name, surname, age, phone)
        personDict = person.get_person()

        administracion = Administracion()
        administracion.add_employee(personDict)

        self.assertDictEqual(administracion.listEmployee[legajo], personDict)  
 
if __name__ == '__main__':
    unittest.main()          