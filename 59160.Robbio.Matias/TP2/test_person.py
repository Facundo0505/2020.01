import unittest
from employee import Person

class testPerson(unittest.TestCase):
    def test_get_person(self):
        persona = Person("Claudio",19)
        self.assertEqual(Person.get_person(persona),["Claudio",19])

if __name__ == "__main__":
    unittest.main()

