from employee import Employee, Person

class Administrtion:
    listEmployee={}

    def add_employee(self, employee):
        legajo = len(self.listEmployee)
        self.listEmployee[legajo] = employee
        return

if __name__ == '__main__':
    adm = Administrtion()
    adm.add_employee({'name':'Santiago', 'lastname':'Coria', 'age':'19', 'phone':154846570})
    adm.add_employee({'name':'Julio', 'lastname':'Coria', 'age':'52', 'phone':154846570})
    print(adm.listEmployee)