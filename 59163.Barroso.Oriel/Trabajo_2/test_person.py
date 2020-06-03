<<<<<<< HEAD
import unittest
from classes import Person
from parameterized import parameterized


class test_classes(unittest.TestCase):
    @parameterized.expand([
        ("Oriel", "Barroso", 23, 156250112, {"name" : "Oriel", "surname": "Barroso", "age" : 23, "cellphone" : 156250112})
    ])
    def test_get_person(self, name, surname, age, cellphone, result):
        person = Person(name, surname, age, cellphone)
        persona1 = person.get_person()
        self.assertEqual(persona1, result)


if __name__ == "__main__":
    unittest.main()
=======
import unittest
from classes import Person


class test_classes(unittest.TestCase):
    def test_get_person(self):
        self.name = "Oriel"
        self.age = "23"
        persona1 = Person.get_person(self)
        self.assertEqual(["Oriel", "23"], persona1)


if __name__ == "__main__":
    unittest.main()
>>>>>>> 975d3f3331291a4f958f99df623a3bc8b8147556
