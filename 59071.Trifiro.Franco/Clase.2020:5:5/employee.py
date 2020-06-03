class Person:

    def __init__(self, name, age, surname, phone):
        self.name=name
        self.age=age
        self.surname=surname
        self.phone=phone

    #agrego diccionario a person
    def get_person(self):
        Person = {"name": self.name, "age": self.age, "surname": self.surname, "phone": self.phone}
        return Person
        #manera optima de hacerlo retun self.__dict_-


class Employee(Person):

    def __init__(self, name, age, surname, phone, salary):
        Person.__init__(self, name, age, surname, phone)
        self.salary=salary
    
    def get_employee(self):
        Employee = {"name": self.name, "surname": self.surname, "age": self.age, "phone": self.phone, "salary":self.salary}
        return Employee
    
    def pay_tax(self):
        if self.salary > 3000 and self.age < 32:
            return "Paga imouestos"
        else:
            return "No paga impuestos"

if __name__ == "__main__":
    p= Person ("Franco", "Trifiro", 20, 2615870558)
    personlist = p.get_person()
    print(p.get_person())
    #me tira un atributo del diccionario
    #print(personDic["name"])

    e = Employee ("Franco", "Trifiro", 20, 2615870558, 50000)
    employelist = e.get_employee()
