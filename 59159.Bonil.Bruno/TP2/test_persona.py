import unittest
import employee
from parameterized import parameterized
from employee import Person

class TestPersona(unittest.TestCase):

    @parameterized.expand ([
        ("Bruno", "Bonil", 19, 2612502686, {'name': "Bruno", 'surname': "Bonil", 'age': 19, 'num': 2612502686})
    ])
    
    def test_get_person(self, name, surname, age, num, dic):
        persona = Person(name, surname, age, num)
        dict_persona = persona.get_person()
        self.assertEqual(dict_persona, dic)
        


if __name__ == '__main__':
    unittest.main()