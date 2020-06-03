from employee import Employee, Person

class Administracion:
    listEmployee={}
    
    # Agrega employee en listEmployee incrementando el legajo (key)
    # employee {'name':"Claudio",'surname':"Pico",'age':30,'phone':155858585}
    def add_employee(self,employee):
        legajo=len(self.listEmployee)
        self.listEmployee[legajo]=employee
        return

if __name__ == '__main__':
   adm=Administracion()
   adm.add_employee({'name':"Marcelino",'surname':"Caballero",'age':25,'phone':155858585})
   adm.add_employee({'name':"Nicolas",'surname':"Caballero",'age':225,'phone':155858585})            
   print(adm.listEmployee)     