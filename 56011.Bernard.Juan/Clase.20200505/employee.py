class Person:
    def __init__(self, name, age, surname, phone):
        self.name = name
        self.age = age
        self.surname = surname
        self.phone = phone

    def get_person(self):
        return self.__dict__


class Employee(Person):
    def __init__(self, name, age, surname, phone, salary):
        Person.__init__(self, name, age, surname, phone)
        self.salary = salary

    def get_employee(self):
        return self.__dict__

    def pay_tax(self):
        if self.salary > 30000 and self.age < 32:
            return "Paga impuestos"
        else:
            return "No paga impuestos"


if __name__ == '__main__':
    persona1 = Person("Javier", 28, "Perez", 1546327)
    print(persona1.get_person())

    empleado1 = Employee("Viviana", 32, "Marquez", 1679366, 60000)
    print(empleado1.get_employee())
