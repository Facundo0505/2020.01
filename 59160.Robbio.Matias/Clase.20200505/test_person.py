import unittest
from employee import Person

class testPerson(unittest.TestCase):
    def test_get_person(self):
        my_dict = {'name':"Claudio", 'age':32, 'surname':"Pico", 'phone':233}
        persona = Person("Claudio",32,"Pico",233)
        self.assertEqual(Person.get_person(persona),my_dict)

if __name__ == "__main__":
    unittest.main()

