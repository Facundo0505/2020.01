class Person:
    def __init__(self, name, apellido, age, tel):
        self.name=name
        self.apellido=apellido
        self.age=age
        self.tel= tel

 
    def get_person(self):
       person = {'name': self.name, 'apellido': self.apellido, 'edad': self.age, 'tel': self.tel}
       return person
 
 
class Employee(Person):
    def __init__(self, name, apellido, age, tel, salary):
        Person.__init__(self, name, apellido, age, tel)
        self.salary = salary 

    
    def get_employee(self):
       employee = {'name': self.name, 'apellido': self.apellido, 'edad': self.age, 'tel': self.tel, 'salary': self.salary}
       return employee

    
    def pay_tax(self):
        if self.salary > 3000 and self.age < 32:
            return "Paga impuestos"
        else:
            return "No paga impuestos"
