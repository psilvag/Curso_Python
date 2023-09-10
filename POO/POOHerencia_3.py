#TIPOS DE HERENCIA


#-------------HERENCIA MULTINIVEL--------
# herencia en cascada
class Vehicle:
    def max_speed(self,speed):
        self.max_speed=speed
        print("MAX SPEED",self.max_speed)

class Car(Vehicle):
    def open_trunk(self):
        print("open trunk")

class Hibryd(Car):
    def showHibryd(self):
        print("Hibryd")
    

toyota=Hibryd()
toyota.max_speed(90)
toyota.open_trunk()
toyota.showHibryd()

#-------------HERENCIA JERARQUICA--------
# de una clase pueden hereredar carios
class Vehicle:
    def max_speed(self,speed):
        self.max_speed=speed
        print("MAX SPEED",self.max_speed)

class Car(Vehicle):
    def open_trunk(self):
        print("open trunk")

class Truck(Vehicle):
    pass

class Hibryd(Car):
    def showHibryd(self):
        print("Hibryd")
    

toyota=Hibryd()
toyota.max_speed(90)
toyota.open_trunk()
toyota.showHibryd()

nissan=Truck()
nissan.max_speed(40)


#-------------HERENCIA MULTIPLE--------
# una clase hija hereda de dos padres  ( NO SE RECOMIENDA HACERLO)

class electricEngine:
    def setPowerElectric(self,power):
        self.powerEngine=power

class combustionEngine:
    def setPowerCombustion(self,power):
        self.powerCombustion=power

class hibrydMotor(electricEngine,combustionEngine):
      def showPower(self):
          print("HIBRYD MOTOR",self.powerEngine,"and ",self.powerCombustion)


motor=hibrydMotor()
motor.setPowerElectric("23 kW")
motor.setPowerCombustion("56 kW")
motor.showPower()
          