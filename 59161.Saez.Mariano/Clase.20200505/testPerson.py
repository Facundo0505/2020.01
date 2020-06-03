import unittest
from employee import Person
from parameterized import parameterized


class TestPerson(unittest.TestCase):
    @parameterized.expand([
        ('Mariano', 'Saez', 20, 155922296, {'name' : 'Mariano','surname' : 'Saez', 'age' : 20, 'phone' : 155922296}),
        ('Jesus', 'DeNazareth', 999, 00000000, {'name' : 'Jesus','surname' : 'DeNazareth', 'age' : 999, 'phone' : 00000000}),
        ('Mirtha', 'Legrande', 1000, 10000000, {'name' : 'Mirtha','surname' : 'Legrande', 'age' : 1000, 'phone' : 10000000})
    ])
    def test_get_person(self, name, surname, age, phone, result):
        persona = Person(name, surname, age, phone)
        datosPersona = persona.get_person()
        self.assertEqual(datosPersona, result)


if __name__ == '__main__':
    unittest.main()
