from employee import Employee, Person

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
   adm.add_employee({'name':"Claudio",'surname':"Pico",'age':30,'phone':155858585})
   adm.add_employee({'name':"Nicolas",'surname':"Pico",'age':30,'phone':155858585})           
   print(adm.listEmployee)     



    #***** Administation *******
#- Imprementar Unitest para Administration, 
 #* Comprobar que listEmployee tiene agregado el Employee en el legajo correspondiente. Utilizando parameterized
  # ej :
   #{
    #0: {'name': 'Claudio', 'surname': 'Pico', 'age': 30, 'phone': 155858585,salary:30000}, 
    #1: {'name': 'Nicolas', 'surname': 'Pico', 'age': 30, 'phone': 155858585},salary:20000
    #}

   #guia:
   #- def test_add_employee(self, name, surname, age, phone, legajo)