from employee2 import Employee, Person

class Administration:
    listEmployee={}
    
    # Agrega employee en listEmployee incrementando el legajo (key)
    # employee {'name':"Claudio",'surname':"Pico",'age':30,'phone':155858585}
    def add_employee(self,employee):
        legajo=len(self.listEmployee)
        self.listEmployee[legajo]=employee
        return

if __name__ == '__main__':
   adm=Administration()
   adm.add_employee({'name':"Enzo",'surname':"Ponce",'age':23,'phone':2615691337})
               
   print(adm.listEmployee)