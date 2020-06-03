class Person:                                       # declaramos la clase persona
    def __init__(self, name, surname, age, phone):                  # declaramos el metodo __init__ 
        self.name=name
        self.surname=surname
        self.age=age
        self.phone=phone


    def get_person(self):                           #Devuelve una lista con el nombre y la edad
       person = {'name':self.name, 'surname':self.surname, 'age':self.age, 'phone':self.phone} 
       return person         #return ["Claudio", 32]
 

        # la clase empleado hereda los atributos y metodos de la clase Persona
class Employee(Person):                             # declaramos la clase Employee
    def __init__(self, name, age, salary):          # declaramos el metodo __init__ para Employee
        Person.__init__(self, name, age)            # llamamos al metodo init de la clase padre
        self.salary=salary                          #ingresamos salary para employee

    def get_employee(self):                         #Devuelve una lista con los atributos
       employee = {'name':self.name, 'surname':self.surname, 'age':self.age, 'phone':self.phone, 'salary':self.salary}
       return employee   #return ["Claudio", 32, 30000]
                                            
    def pay_tax(self):                              # declaramos el metodo pagar_impuestos
        if self.salary > 30000 and self.age < 32:   # comprobara si el empleado debe pagar o no  
            return "Paga impuestos"                 # return "Paga impuestos" or "No paga impuestos"
        else:
            return "No paga impuestos"