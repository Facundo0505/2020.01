import unittest
from classes import Employee, Person

class test_classes(unittest.TestCase):
    def test_get_employee(self):
        self.nombre = "Oriel"
        self.age = 23
        self.salary = 32000
        emp1 = Employee.get_employee(self)
        self.assertEqual(emp1, ["Oriel", 23, 32000])

    def test_pay_taxes(self):
        self.age = 48
        self.salary = 50000
        imp1 = Employee(self)
        self.assertEqual(imp1.pay_tax, "Paga impuestos")

    def test_no_pay_taxes(self):
        self.age = 23
        self.salary = 31999
        imp2 = Employee(self)
        self.assertEqual(imp2.pay_tax, "No paga impuestos")


if __name__ == "__main__":
    unittest.main()
