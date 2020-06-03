from employee import Employee, Person

class Administration:
    listEmployee={}
    
    # Agrega employee en listEmployee incrementando el legajo (key)
    # employee {'name':"Claudio",'surname':"Pico",'age':30,'phone':155858585, 'salary':30000}
    def add_employee(self,employee):
        legajo=len(self.listEmployee)
        self.listEmployee[legajo]=employee
        return self.listEmployee[legajo]

if __name__ == '__main__':
   adm=Administration()
   adm.add_employee({'name':"Claudio",'surname':"Pico",'age':30,'phone':155858585, 'salary':45000})
   adm.add_employee({'name':"Federico",'surname':"Calderon",'age':20,'phone':1234, 'salary':25000})            
   print(adm.listEmployee)   
   print("")
   print(list(Administration().listEmployee))
   

   
   