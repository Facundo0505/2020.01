from persona import Person, Empleado

class Administration:
    diccionarioEmployee={}
    
    # Agrega employee en listEmployee incrementando el legajo (key)
    # employee {'name':"Claudio",'surname':"Pico",'age':30,'phone':155858585}
    def add_employee(self,employee):
        legajo=len(self.diccionarioEmployee)
        self.diccionarioEmployee[legajo]=employee
        print(employee)
        return

if __name__ == '__main__':
   adm=Administration()
   adm.add_employee({'nombre':"Mariano",'apellido':"Colman",'edad':21,'telefono':2614312380})
   # adm.add_employee({'nombre':"Nicolas",'apellido':"Pico",'edad':30,'telefono':155858585})            
   print(adm.diccionarioEmployee)
