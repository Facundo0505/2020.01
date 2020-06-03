class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_person(self):
        return[self.name, self.age]


class Employee(Person):
    def __init__(self, name, age, salary):
        Person.__init__(self, name, age)
        self.salary = salary

    def get_employee(self):
        return[self.name, self.age, self.salary]

    def pay_tax(self):
        if self.salary > 30000 and self.age < 32:
            return "Paga impuestos"
        else:
            return "No paga impuestos"
