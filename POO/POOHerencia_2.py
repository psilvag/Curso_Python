#FUNCION SUPER

class vehicle:
     fullcap=80
     def showDetails(self):
        return self.fullcap

class car (vehicle):
     fullcap=60
     def details(self):
          #print("Details vehicle",super().fullcap) #la palabra super hace ref a la clase padre
          print("Details vehicle",super().showDetails()) #la palabra super hace ref a la clase padre
          print("Details car",self.fullcap)

tesla= car()
tesla.details() 

