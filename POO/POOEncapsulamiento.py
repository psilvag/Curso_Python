# ENCAPSULAMIENTO

class Person:
    def __init__(self,name,age) :
        self.__secret="·%·gdg·$g560%/·%&&g" ## colocar doble guion bajo __name hace referencia a una propiedad oculta
        self.name=name
        self.age=age
    def showSecret(self):
        return self.__secret
pablo= Person("pablo",30)
print(pablo.name)
#print(pablo.__secret)
print(pablo.showSecret())


class BankAcount:
    def __init__(self,balance=0):
        self.__balance=0

    def __allow_withdrawal(self):
        if self.__balance<1:
            return False
        return True
    
    def deposit(self,amount):
        self.__balance=+amount

    def wihtdraw(self,amount):
        allow=self.__allow_withdrawal()
        if allow:
            if(self.__balance>=amount):
                self.__balance-=amount
            else:
                print("Tu saldo es insuficiente")
        else:
            print("SALDO: 0.00")
            
    def get_balance(self):
        return self.__balance
        
bisa=BankAcount()
bisa.deposit(3000)
bisa.wihtdraw(2000)
print(bisa.get_balance())
bisa.wihtdraw(500)
print(bisa.get_balance())
bisa.wihtdraw(500)
print(bisa.get_balance())
bisa.wihtdraw(50)

# GETTERS Y SETTERS

# class User:
#     def __init__(self,username=None) -> None:
#         self.__username=username
#     def getusername(self):
#         return self.__username
#     def setusername(self,username):
#         self.__username=username

# user1=User('Pablo')
# print("antes de setter:",user1.getusername())
# user1.setusername('Chanchito feliz')
# print("Despues de getter:",user1.getusername())
        
#-------------OTRA FORMA DE HACERLO ES USARLO DECORADORES

class User:
    def __init__(self,username=None) -> None:
        self.__username=username
    @property   #este estaria actuando como el getter
    def username(self):
        return self.__username
    
    @username.setter
    def username(self,username):
        self.__username=username

user2=User('Pablo')
print("antes de setter:",user2.username)
user2.username='Chanchito'
print("Despues de setter:",user2.username)  
