from Employee import Employee, Person

class Administracion:
    listEmployee={}

    def add_employee(self,employee):
        legajo=len(self.listEmployee)
        self.listEmployee[legajo]=employee
        return

if __name__ == "__main__":
    adm = Administracion()
    adm.add_employee({"name": "Milagros", "Surname": "Tomba", "age": 19, "Phone": 2615080491, "salary": 30000})
    adm.add_employee({"name": "Agustina", "apellido": "Tomba","age": 24, "telefono": 2611111111, "salary": 20000})
    print(adm.listEmployee)
    