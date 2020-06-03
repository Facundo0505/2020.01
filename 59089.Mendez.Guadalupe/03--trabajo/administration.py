from employee import Employee, Person

class Administration:
    listEmployee={}
    
    def add_employee(self,employee):
        legajo=len(self.listEmployee)
        self.listEmployee[legajo]=employee
        return

if __name__ == '__main__':
   adm=Administration()
   adm.add_employee({'name':"Guadalupe",'surname':"Méndez",'age':19,'phone':2615191849})
   adm.add_employee({'name':"Ignacio",'surname':"Méndez",'age':18,'phone':2615191850})            
   print(adm.listEmployee) 