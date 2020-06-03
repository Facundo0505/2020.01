import unittest
from diagnostico import CompuTools
from parameterized import parameterized
class TestDiagnostico(unittest.TestCase):
    @parameterized.expand([
                           ([[1, 2, 3, 4]]),
                           ([[5, 6, 7, 8, 10]]),
                           ([[1, 3, 5, 7, 9, 11]]),
                           ([[5, 6, 7, 8, 9, 10, 11, 12]]),
                          ])
    def test_is_sorted(self, list, result):
        compu = CompuTools()
        self.assertEqual(compu.is_sorted(list), result)
    @parameterized.expand([
                           ([[4, 2, 3, 1]]),
                           ([[5, 6, 17, 8, 10]]),
                           ([[1, 3, 5, 17, 9, 11]]),
                           ([[5, 6, 7, 18, 9, 10, 11, 12]]),
                          ])
    def test_is_not_sorted(self, list, result):
        compu = CompuTools()
        self.assertFalse(compu.is_sorted(list), result)

if __name__ == "__main__":
    unittest.main()
