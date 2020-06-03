import unittest
from Diagnostico import CompuTools

class TestDiagnostico(unittest.TestCase):
    def test_is_sorted(self):
        compu = CompuTools()
        self.assertTrue(compu.is_sorted([1, 2, 3, 4]))

    def test_is_not_sorted(self):
        compu = CompuTools()
        self.assertFalse(compu.is_sorted([1, 3, 2, 4]))
        
if __name__ == "__main__":
    unittest.main()