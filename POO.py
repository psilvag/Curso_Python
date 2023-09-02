

class Employee:
    def __init__(self, id, name:str='name', lastname:str='lastname',age=None) -> None:
        self.id=id
        self.name=name
        self.lastname=lastname
        self.age=age
        
employee = Employee('5342g4645yerghrfhy4','Robert','Pinedo',34)
employee2=Employee('gdfgdg55dgdgfgsdgzx0','Martha','Pinedo')
employee3=Employee('fdgfdn89489nchfpqwlf','Pedro',43)
print(f'{employee.name} {employee.lastname} con el ID {employee.id} tiene {employee.age} años')
print(f'{employee2.name} {employee2.lastname} con el ID {employee2.id} tiene {employee2.age} años')
print(f'{employee3.name} {employee3.lastname} con el ID {employee3.id} tiene {employee3.age} años')