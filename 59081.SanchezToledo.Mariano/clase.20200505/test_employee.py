import unittest
from employee import Person, Employee
from parameterized import parameterized

class TestPerson (unittest.TestCase):
    @parameterized.expand([
        ("Claudio","Pico", 30, 155858585, {'name':"Claudio",'surname':"Pico",'age':30,'phone':155858585}),
        ("Mariano","Sanchez",20,2323, {'name':"Mariano",'surname':"Sanchez",'age':20,'phone':2323})
        ])

    def test_get_person (self, name, surname, age, phone, result):
        person = Person(name, surname, age, phone)
        personlist = person.get_person()
        self.assertEqual(personlist, result)

    @parameterized.expand([
            ("Claudio","Pico",30,155858585,30000, {'name':"Claudio",'surname':"Pico",'age':30,'phone':155858585,'salary':30000}),
            ("Mariano","Sanchez",20,2323,20000, {'name':"Mariano",'surname':"Sanchez",'age':20,'phone':2323,'salary':20000})
             ])

    def test_get_employee (self, name, surname, age, phone, salary, result):
        employeelist = Employee(name, surname, age, phone, salary).get_employee()
        self.assertEqual(employeelist, result)

    @parameterized.expand([
            ("Claudio","Pico",30,155858585,30000, "No paga impuestos"),
            ("Jose","Gimenez",25,265874,50000, "Paga impuestos")

    ])
    def test_pay_tax (self, name, surname, age, phone, salary, result):
        paytax = Employee(name, surname, age, phone, salary).pay_tax()
        self.assertEqual(paytax, result)



if __name__ == "__main__":
    unittest.main()
