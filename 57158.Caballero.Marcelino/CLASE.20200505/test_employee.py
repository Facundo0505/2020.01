import unittest
from employee import Person, Employee
from parameterized import parameterized



class TestPerson(unittest.TestCase):
    @parameterized.expand([
        ("Marcelino", 25, "Caballero", 498284154678, {'name':"Marcelino", 'age':25, 'apellido':"Caballero", 'telefono':498284154678})
    ])

    def test_get_person(self, name, age, apellido, telefono, result):
        person = Person(name, age, apellido, telefono)
        dictPerson = person.get_person()
        self.assertEqual(dictPerson, result)


class TestEmployee(unittest.TestCase):
    @parameterized.expand([
        ("Marcelino", 25, "Caballero", 498284154678,50000, {'name':"Marcelino", 'age':25, 'apellido':"Caballero", 'telefono':498284154678, 'salary':50000})
    ])

    def test_get_employee(self, name, age, apellido, telefono, salary, result):
        employee = Employee(name, age, apellido, telefono, salary)
        dictEmployee = employee.get_employee()
        self.assertEqual(dictEmployee, result)

    @parameterized.expand([
        ("Jorge", 31, "Perez", 488181845678, 35000, "Paga impuestos"),
        ("Rafael", 25, "Dominguez", 498053216791, 25000, "No paga impuestos")
    ])

    def test_pay_tax_pay(self, name, age, apellido, telefono, salary, result):
        employee = Employee( name, age, apellido, telefono, salary)
        dict_pay_tax = employee.pay_tax()
        self.assertEqual(dict_pay_tax, result)

    


if __name__ == "__main__":
    unittest.main()