class Person:
    def __init__(self,name,surname,age,phone):
        self.name = name 
        self.surname = surname
        self.age = age 
        self.phone = phone
    
    def get_person(self):
        person = {'name ':self.name,'surname ':self.surname,'age ':self.age,'phone ':self.phone}
        return person
    
class Employee: 
    def __init__(self,name,surname,age,phone,salary):
        Person.__init__(self,name,surname,age,phone)
        self.salary = salary 

    def get_employee(self):     
        lib = {'name ':self.name,'surname ':self.surname,'age ':self.age,'phone ':self.phone, 'salary':self.salary}
        return lib
    
    def get_pay_tax(self):
        if ((self.age) < 32) and ((self.salary) > 30000):
            return 'Paga impuestos'
        else:
            return 'No paga impuestos'


