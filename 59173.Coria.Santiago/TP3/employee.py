class Person:
    def __init__(self, name, lastname, age, phone):
        self.name = name 
        self.lastname = lastname
        self.age = age
        self.phone = phone
    def get_person(self):
        return self.__dict__


class Employee(Person):
    def __init__(self, name, lastname, age, phone, salary):
        super().__init__(name, lastname, age, phone)
        self.salary = salary

    def get_employee(self):
        return self.__dict__

    def pay_taxes(self):
        if self.salary > 30000 and self.age < 32:
            return "Paga Impuestos" 
        else:
            return "No paga impuestos"
