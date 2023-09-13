#Clases absctractas
# las clases abstractas exigen a sus clases hijas que tengan los mismos metodos
# pero cada clase hija puede tener sus propios metodos y propiedades
from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self,length) :
        self.length=length
    def area(self):
        return self.length*self.length
             
    def perimeter(self):
        return 4*(self.length)
    
class Triangle(Shape):
    def __init__(self,b,h) :
        self.b=b
        self.h=h
    def area(self):
        return (self.b*self.h)/2
             
    def perimeter(self):
        pass

   

square= Square(4)
print("area square",square.area())
print("perimeter square",square.perimeter())

triangle= Triangle(4,5)
print("area triangle",triangle.area())
print("perimeter triangle",triangle.perimeter())




    
       
        
    