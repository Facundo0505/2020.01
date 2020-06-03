# declaramos la clase persona
class Person:
    # declaramos el metodo __init__ 
    def __init__(self, name, age, apellido, telefono):
        self.name=name
        self.age=age
        self.apellido=apellido
        self.telefono=telefono 
    #Devuelve una lista con el nombre y la edad
    #return ["Claudio", 32]
    def get_person(self):
        Person = {'name':self.name, 'age':self.age, 'apellido':self.apellido, 'telefono':self.telefono}
        return Person
 
# declaramos la clase Employee
# la clase empleado hereda los atributos y metodos de la clase Persona
class Employee(Person):
    # declaramos el metodo __init__ para Employee
    def __init__(self, name, age, apellido, telefono, salary):
        # llamamos al metodo init de la clase padre
        Person.__init__(self, name, age, apellido,telefono)
        #ingresamos salary para employee
        self.salary=salary 


    #Devuelve una lista con los atributos
    #return ["Claudio", 32, 30000]
    def get_employee(self):
        Employee = {'name':self.name, 'age':self.age, 'apellido':self.apellido, 'telefono':self.telefono, 'salary':self.salary}
        return Employee

    # declaramos el metodo pagar_impuestos
    # comprobara si el empleado debe pagar o no
    # return "Paga impuestos" or "No paga impuestos"
    def pay_tax(self):
        if self.salary > 30000 and self.age < 32:
            return "Paga impuestos"
        else:
            return "No paga impuestos"

    if __name__ == "__main__":
        p = Person("Marcelino", 25 , "Caballero", 498284154678)   
        persondic = p.get_person
        print(p.get_person())
        #muestra los atributos de persona a traves del diccionario
    
        e = Employee("Marcelino", 25 , "Caballero", 498284154678, 50000)
        employeedic = e.get_employee
        print(e.get_employee())
        #muestra los atributos de empleado a traves del diccionario
    
