class Person:

    def _init_(self, name, age, surname, phone):
        self.name=name
        self.age=age
        self.surname=surname
        self.phone=phone

    #agrego diccionario a person
    def get_person(self):
        Person = {"name": self.name, "age": self.age, "surname": self.surname, "phone": self.phone}
        return Person
        #manera optima de hacerlo return self._dict_

 
class Employee(Person):

    def _init_(self, name, age, surname, phone, salary):
        Person._init_(self, name, age, surname, phone)
        self.salary=salary 

    def get_employee(self):
        Employee = {"name": self.name,  "surname": self.surname, "age": self.age, "phone": self.phone, "salary":self.salary}
        return Employee

    def pay_tax(self):
        if self.salary > 30000 and self.age < 32:
            return "Paga impuestos"
        else:
            return "No paga impuestos"

if __name__ == "__main__":
    p = Person ("Guadalupe", "Méndez", 19, 2615191849)
    personlist = p.get_person()
    print(p.get_person())
    #me tira un atrbuto del diccionario
    #print(personDic["name"])

    e = Employee ("Guadalupe", "Méndez", 19, 2615191849, 40000)
    employeelist = e.get_employee()