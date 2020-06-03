class Person():

    def __init__(self, name, surname, age, phone):
        self.name=name
        self.surname=surname 
        self.age=age
        self.phone=phone

    def get_person(self):
        person = {'name':self.name,'surname':self.surname,'age':self.age, 'phone':self.phone}
        return person
 

class Employee(Person):

    def __init__(self, name, surname, age, phone, salary):

        super().__init__(name, surname, age, phone)
        self.salary=salary


    def get_employee(self):
        Employee = {"name": self.name, "surname": self.surname, "age": self.age, "phone": self.phone, "salary":self.salary}
        return Employee


    def pay_tax(self):
        if self.salary > 30000 and self.age < 32:
            return "Paga impuestos"
        else:
            return "No paga impuestos"