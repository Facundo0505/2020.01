class Person:
    # declaramos el metodo __init__
    def __init__(self, name, surname, age, phone):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
    # Devuelve una lista con el nombre y la edad
    # return ["Claudio", 32]

    def get_person(self):
        person = {'name': self.name, 'surname': self.surname, 'age': self.age,
                  'phone': self.phone}
        return person


class Employee(Person):
    def __init__(self, name, surname, age, phone, salary):
        super().__init__(name, surname, age, phone)
        self.salary = salary

    @property
    def name_emp(self):
        return self.name

    @name_emp.setter
    def name_emp(self, nombre_nuevo):
        self.name = nombre_nuevo

    def get_employee(self):
        return[self.name, self.age, self.salary]

    def pay_tax(self):
        if self.salary > 30000 and self.age < 32:
            return "Paga impuestos"
        else:
            return "No paga impuestos"


empleado1 = Employee("Julia", "locamuz", "age", 5555, 10000)
print(empleado1.pay_tax())
