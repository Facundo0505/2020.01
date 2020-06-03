import unittest
from punto import Punto, PuntoMejorado
from parameterized import parameterized
class TestPunto(unittest.TestCase):
    def test_str_punto(self, x, y, string):
        punto = Punto(x, y)
        self.assertEqual(punto.__str__(), string)
if __name__ == "__main__":
    unittest.main()
