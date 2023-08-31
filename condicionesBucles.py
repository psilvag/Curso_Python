

# #--------------------CONDICIONALES  if--elif-else--------------------------
# #en python se puede usar BREAK, CONTINUE y PASS: PASS DICE NO HACER NADA
num=12
if num==5:
    print('el numero es menor que',num)
else:
    print('el numero es',num)

if num%3==0 and num%4==0 and num%6==0:
    print(f'los numeros 3,4,6 son multiplos de',num)

if num%3==0 or num%4==0 or num%6==0:
    print(f'si hay un multiplo de ',num)
else:
    print(f'no hay ningun numero multiplo de',num)

# #----------------------FOR------------------------
lista=[3,4,5,6,7,8,9]
for i in lista:
    print(i)

nums= list(range(1,31,3)) # no toma el ultimo valor por eso hasta el 21, si quiero que vaya hasta el 20, el ultimo parametro es la cantidad que salatara es decir de 2 en 2

for element in range(1,21,2):
    print(element)

for elem in nums:
    print(elem)

#------------------------------WHILE----------------------------

n=2
power=0
val=n
while(val<100):
    power+=1
    val*=2
print('ya termino')

while True:
     print('hola')
