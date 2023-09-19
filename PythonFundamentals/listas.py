

milista=["rojo","verde",4.5,3,"cafe",[1,2,3,4,5]] #las listas son mutables
milista[2]=9.0
print(milista)
print(milista[5][0])

valores= range(1,20,2)# creamos un rango de numeros del 1 al 19 y de 2 en 2
print(list(valores)) #convertimos ese rango en una lista o un array

lista1=[1,2,4,5,6,7,8]
lista2=[0,4,5,6,76]
#print(lista1+lista2) # solo lo concatena
lista1.extend(lista2)
print(lista1)

#OPERACIONES CON LISTAS
#------APPEND--------
lista=[4,5,6,7,8,9]
lista.append(0)
print(lista)
#-------INSERT-------
lista.insert(4,-1) #en el indice  4 coloca -1
print(lista)
#-------POP-------
lista.pop() #elimina el ultimo valor
print(lista)
#-------REMOVE-------
lista.remove(6) #elimina solo el  primer elemento 6 de la lista, si hay mas los deja
print(lista)
#-------REVERSE-------
lista.reverse() #lista al reves
print(lista)
#-------SEARCH-------
frutas=['manzana','piña','coco']
#
print(frutas.index('manzana'))# devuelve el valor del indice
print('piña' in frutas) # pregunta si ese elemento esta en el array
# SORT
numeros =[12,4,5,100,1,5]
numeros.sort() # de menor a mayor
numeros.sort(reverse=True) #mayor a menor
print(numeros)
