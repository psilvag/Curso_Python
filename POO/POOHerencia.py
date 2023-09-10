 #HERENCIA 
class Vehicle:
    def __init__(self,make,color,model):
        self.make=make
        self.color=color
        self.model=model
    def show_car(self):
        print("MAKE:",self.make)
        print("COLOR:",self.color)
        print("MODEL:",self.model)

class car(Vehicle):
    def __init__(self, make, color, model,numdoors):
        super().__init__(make, color, model)
       # Vehicle().__init__(make, color, model) #otra forma de hacerlo
        self.numdoors=numdoors
    
    def printDetails(self):
        self.show_car()
        print("NUM DOORS:",self.numdoors)

tesla=car('Tesla','red',2019,5)
tesla.printDetails()
tesla.show_car()

