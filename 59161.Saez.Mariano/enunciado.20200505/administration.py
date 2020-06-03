class Administration:
    _listEmployee = {}

    @property
    def listemployee(self):
        return self._listEmployee

    @listemployee.setter
    def listEmployee(self, obj):
        self._listEmployee = obj

    # Agrega employee en listEmployee incrementando el legajo (key)
    # employee {'name':"Claudio",'surname':"Pico",'age':30,'phone':155858585}
    def add_employee(self, employee):
        legajo = len(self.listEmployee)
        self._listEmployee[legajo] = employee
        return


if __name__ == '__main__':
    adm = Administration()
    adm.add_employee({'name': "Claudio", 'surname': "Pico", 'age': 30, 'phone': 155858585, 'salary': 35000})
    adm.add_employee({'name': "Nicolas", 'surname': "Pico", 'age': 30, 'phone': 155858585, 'salary': 40000})
    print(adm.listEmployee)
