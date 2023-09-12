#POLIMORFISMO
# estamos sobreescribiendo la funcion getarea

class Shape:
    def __init__(self) -> None:
        self.sides=0
    def get_area():
        pass


class Rectangle(Shape):
    def __init__(self,width=0,heigth=0):
        self.width=width
        self.heigth=heigth
        self.sides=4
    
    def get_area(self):
        return self.width*self.heigth
    
class Circle(Shape):
    def __init__(self,radius) -> None:
        self.radius=radius
    
    def get_area(self):
        return 3.141659*self.radius*self.radius


shapes= [Rectangle(10,10),Circle(5)]

for shape in shapes:
    print(shape.get_area())


