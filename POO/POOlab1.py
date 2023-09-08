

# Ejericio de creacion de objetos
class Student:
    def __init__(self,name,Physics,Chemestry,Biology) -> None:
        self.name=name
        self.Physics=Physics
        self.Chemestry=Chemestry
        self.Biology=Biology

    def total_obtained(self):
        return self.Physics+self.Chemestry+self.Biology
    def percent(self):
        return (self.total_obtained())/300*100
    
student1=Student('pepito',90,67,82)
print(f"{student1.name} obtuvo {student1.total_obtained()} puntos con un{round(student1.percent(),2)}% de rendimiento")
student2=Student('pablito',98,87,70)
print(f"{student2.name} obtuvo {student2.total_obtained()} puntos con un{round(student2.percent(),2)}% de rendimiento")