import unittest
from persona import Person, Employee
from admin import Administration
from parameterized import parameterized


class TestAdministration(unittest.TestCase):
  @parameterized.expand([("martin", "ruggeri", 21, 2612445829, 2500),
                         ("juan", "lopez", 30, 2613334444, 3500)])
  def test_get_employee(self, name, apellido, age, tel, salary):
    employee = Employee(name, apellido, age, tel, salary).get_employee()
    adm = Administration()
    adm.add_employee(employee) 
    self.assertEqual(adm.listEmployee[len(adm.listEmployee)-1], employee)


class TestPerson(unittest.TestCase):
  @parameterized.expand([("martin", "ruggeri", 21, 2612445829, {'name': 'martin', 'apellido': 'ruggeri', 'edad': 21, 'tel': 2612445829})])
  def test_get_person(self, name, apellido, age, tel, string):
    person = Person(name, apellido, age, tel).get_person()
    self.assertEqual(person, string) 


class TestEmployee(unittest.TestCase):
  @parameterized.expand([("martin", "ruggeri", 21, 2612445829, 2500, {'name': 'martin', 'apellido': 'ruggeri', 'edad': 21, 'tel': 2612445829, 'salary': 2500}),
                         ("juan", "lopez", 30, 2613334444, 3500, {'name': 'juan', 'apellido': 'lopez', 'edad': 30, 'tel': 2613334444, 'salary': 3500})])
  def test_get_employee(self, name, apellido, age, tel, salary, string):
    employee = Employee(name, apellido, age, tel, salary).get_employee()
    self.assertEqual(employee, string)

  @parameterized.expand([("martin", "ruggeri", 21, 2612445829, 2500, {'name': 'martin', 'apellido': 'ruggeri', 'edad': 21, 'tel': 2612445829, 'salary': 2500}, "No paga impuestos"),
                         ("juan", "lopez", 30, 2613334444, 3500, {'name': 'juan', 'apellido': 'lopez', 'edad': 30, 'tel': 2613334444, 'salary': 3500}, "Paga impuestos")])
  def test_pay_tax(self, name, apellido, age, tel, salary, string, str_impuestos):  
    impuestos = Employee(name, apellido, age, tel, salary).pay_tax()
    self.assertEqual(impuestos, str_impuestos) 


if __name__ == "__main__":
    unittest.main()

