import unittest
from employee import Employee
from administration import Administration
from parameterized import parameterized


class TestAdminitration(unittest.TestCase):
    @parameterized.expand([
        ('Mariano', 'Saez', 20, 2995922296, 30000, 0),
        ('Agustin', 'Prieto', 20, 261756890, 29999, 1),
        ('Matias', 'Robbio', 19, 2613424565, 90000, 2),
        ('Bruno', 'Bonil', 19, 261890098, 100000, 3)
        ])
    def test_add_employee(self, name, surname, age, phone, salary, legajo):
        # Creamos una instancia de employee llamada empleado
        empleado = Employee(name, surname, age, phone, salary)
        # Agregamos a empleado a la lista de empleados de la instancia de
        # Administration que se crea en el main
        adm.add_employee(empleado)
        # Dado que conocemos el legajo que se asignara a empleado podemos
        # comparar si el elemento almacenado en
        # la key = legajo es igual a empleado (deberia ser el mismo)
        self.assertEqual(adm.listemployee[legajo], empleado)


if __name__ == '__main__':
    # Instanciamos Administration
    adm = Administration()
    unittest.main()
