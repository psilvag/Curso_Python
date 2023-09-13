
#Ejercicio de encapsulamiento 

class rectangle:
    def __init__(self,length:float,width:float) -> None:
        self.__length=length
        self.__width=width
    def area(self):
        return self.__length*self.__width
    def perimeter(self):
        return (self.__length+self.__width)*2

rect=rectangle(3.6,5.9)
print("AREA",round(rect.area(),2))
print("PERIMETER",round(rect.perimeter(),2))
