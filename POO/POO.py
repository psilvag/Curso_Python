

class Employee:
    def __init__(self, id:int, name:str='name', lastname:str='lastname',age=None) -> None:
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


# Variables de clase :son compartidos por todos los objetos de la clase
# Variables de instancia: variables que son propias de la instancia

class Player:
    team="PORTUGAL"
    members=[] # es una variable de clase
    plays=[]
    def __init__(self,name):
        self.name=name
        self.members.append(self.name)

    def players(self,persons):
        self.plays.append(persons)
        

player1=Player("Pablo")
player2=Player("Ema")
print(player1.members)# al ser member una variable de clase comparte la variable
print(player2.members)


player1.players('ana')
player1.players('ema')
player1.players('roxana')
player2.players('Pablo')
player2.players('Silvia')
player2.players('Roger')
print(player1.plays)
print(player2.plays)
# el resultado deberia ser un array distinto por cada instancia pero los datos se suman porque es una variable de clase



class Employee:
    def __init__(self,ID=None,salary:float=None,departament=None):
       self.ID=ID
       self.salary=salary,
       self.departament=departament
    def tax(self):
        return  self.salary*0.2
    def salary_per_day(self):
        return self.salary/24.00
    def demo(self,a,b,c,d=5,e=None):
        print("a =",a)
        print("b =",b)
        print("c =",c)
        print("d =",d)
        print("e =",e)
        
    
    
employee=Employee(220,4300.00,"ENG")
print(employee.salary)
# print("TAX",employee.tax())
# print("SALARY PER DAY",employee.salary_per_day())
       
    
#aqui se hace overloading, recibe distintos parametros y hace distintas cosas
pepe=Employee()
pepe.demo(1,2,3)
pepe.demo(4,5,6,7)
pepe.demo(5,6,7,8,9)